"""Read-only architecture measurements. Stdout JSON; no writes or model calls.

Text similarity and references are candidates, never authority/dependency proof.
"""
import argparse
import difflib
import hashlib
import itertools
import json
import re
import subprocess
from pathlib import Path


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest().upper()


def blocks(text):
    result = []
    pos = 0
    for part in re.split(r"\n\s*\n", text):
        start = text.find(part, pos)
        pos = start + len(part)
        normalized = re.sub(r"\s+", " ", part).strip()
        if len(normalized) >= 120 and not normalized.startswith("#"):
            result.append((text[:start].count("\n") + 1, normalized))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    root = args.project.resolve(strict=True)
    excluded_output = Path(__file__).resolve().parent
    files = sorted(p for p in root.rglob("*") if p.is_file() and
                   excluded_output not in p.parents and ".git" not in p.parts)
    inventory = []
    texts = {}
    for p in files:
        rel = p.relative_to(root).as_posix()
        entry = {"path": rel, "bytes": p.stat().st_size, "sha256": digest(p)}
        if p.suffix in (".md", ".ps1"):
            t = p.read_text(encoding="utf-8-sig")
            texts[rel] = t
            lines = t.splitlines()
            entry.update(lines=len(lines), headings=sum(bool(re.match(r"^#{1,6}\s", s)) for s in lines),
                         unknown_lines=sum(bool(re.search(r"\b(?:UNKNOWN|NOT ESTABLISHED)\b", s)) for s in lines),
                         issue_ids=len(set(re.findall(r"\bAF-(?:OPEN|ML|AV|CX)-\d+\b", t))),
                         md_reference_mentions=len(re.findall(r"[^\s`]+\.md\b", t)))
        inventory.append(entry)
    current = {n: t for n, t in texts.items() if "/" not in n and re.match(r"[1-8]0_.*_CURRENT\.md$", n)}
    controls = {n: t for n, t in texts.items() if n.startswith("Anti-Drift Source/") and n.count("/") == 1}
    controls["AetherFire CI/AetherFire_CI_version_v2.6.md"] = texts["AetherFire CI/AetherFire_CI_version_v2.6.md"]
    pairs = []
    for category, group in (("current", current), ("control", controls)):
        for (an, a), (bn, b) in itertools.combinations(group.items(), 2):
            common = sorted(set(a.splitlines()) & set(b.splitlines()))
            common = [s for s in common if len(s.strip()) >= 40 and not s.startswith("#")]
            # Consecutive exact-line blocks preserve location and avoid treating shared words as copies.
            exact = []
            for m in difflib.SequenceMatcher(None, a.splitlines(), b.splitlines(), autojunk=False).get_matching_blocks():
                fragment = "\n".join(a.splitlines()[m.a:m.a+m.size])
                if m.size >= 3 and len(fragment.strip()) >= 120:
                    exact.append({"a_line": m.a+1, "b_line": m.b+1, "lines": m.size, "chars": len(fragment), "excerpt": fragment[:350]})
            near = []
            bblocks = blocks(b)
            for al, ab in blocks(a):
                for bl, bb in bblocks:
                    if ab == bb or abs(len(ab)-len(bb)) / max(len(ab), len(bb)) > .20:
                        continue
                    # Cheap lexical overlap before exact character similarity.
                    wa, wb = set(ab.split()), set(bb.split())
                    if len(wa & wb) / max(1, len(wa | wb)) < .65:
                        continue
                    ratio = difflib.SequenceMatcher(None, ab, bb, autojunk=False).ratio()
                    if ratio >= .85:
                        near.append({"a_line": al, "b_line": bl, "ratio": round(ratio, 4), "a_excerpt": ab[:240], "b_excerpt": bb[:240]})
            if common or exact or near:
                pairs.append({"category": category, "a": an, "b": bn, "shared_unique_substantive_lines": len(common),
                              "shared_chars": sum(map(len, common)), "exact_blocks": exact, "near_blocks": near})
    manifest = texts["MANIFEST.md"]
    generated, archived = manifest.split("## Archived source snapshot", 1)
    rows = lambda t: re.findall(r"^\| `([^`]+)` \| `([A-Fa-f0-9]{64})` \|$", t, re.M)
    manifest_checks = []
    for category, section, base in (("generated", generated, root), ("archive", archived, root/"Source_Archive")):
        for name, sha in rows(section):
            p = base/name
            manifest_checks.append({"kind": category, "path": p.relative_to(root).as_posix(),
                                    "status": "MISSING" if not p.is_file() else "MATCH" if digest(p) == sha.upper() else "MISMATCH"})
    archive_listed = set(n for n, _ in rows(archived))
    archive_actual = {p.name for p in (root/"Source_Archive").glob("*.md")}
    literal_refs = []
    basenames = {}
    for p in files:
        basenames.setdefault(p.name, []).append(p.relative_to(root).as_posix())
    examined = {n:t for n,t in texts.items() if n in current or n in controls or n in ("00_AETHERFIRE_CONSOLIDATION_INDEX.md", "92_OPEN_ISSUES_CURRENT.md", "91_RECONCILIATION_RECORD.md")}
    for name, t in examined.items():
        for ln, line in enumerate(t.splitlines(), 1):
            for ref in re.findall(r"`([^`\n]+\.md)`", line):
                exact = root / ref
                matches = basenames.get(Path(ref).name, [])
                literal_refs.append({"from": name, "line": ln, "reference": ref,
                                     "candidates": [exact.relative_to(root).as_posix()] if exact.is_file() else matches,
                                     "classification": "EXACT_ROOT_PATH" if exact.is_file() else "BASENAME_ONLY" if matches else "UNRESOLVED_CANDIDATE"})
    changes = []
    for n in sorted(current):
        result = subprocess.run(["git", "log", "--format=%H", "HEAD", "--", n], cwd=root, capture_output=True, text=True)
        changes.append({"path": n, "commits_reachable_from_HEAD_touching_path": len(result.stdout.splitlines()) if result.returncode == 0 else None,
                        "window": "all reachable HEAD history; no rename following; not workload"})
    proposal_manifest = json.loads((root/"AetherFire_Architecture_Revamp_Package/PACKAGE_MANIFEST.json").read_text(encoding="utf-8-sig"))
    proposal_lengths = [{"name": r["name"], "match": (root/"AetherFire_Architecture_Revamp_Package"/r["name"]).stat().st_size == r["bytes"]} for r in proposal_manifest["files"]]
    print(json.dumps({"status": "OBSERVED_STATIC_ONLY", "method": {"headings": "regex including fenced examples", "unknown": "uppercase token lines, not semantic coverage", "near": "paragraphs >=120 chars; Jaccard >=.65; character ratio >=.85", "references": "backtick .md mentions only, not exhaustive dependencies"},
                      "inventory": inventory, "duplication_candidates": pairs, "manifest_checks": manifest_checks,
                      "archive_unlisted": sorted(archive_actual-archive_listed), "archive_missing": sorted(archive_listed-archive_actual),
                      "literal_reference_candidates": literal_refs, "git_change_counts": changes, "proposal_manifest_lengths": proposal_lengths}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
