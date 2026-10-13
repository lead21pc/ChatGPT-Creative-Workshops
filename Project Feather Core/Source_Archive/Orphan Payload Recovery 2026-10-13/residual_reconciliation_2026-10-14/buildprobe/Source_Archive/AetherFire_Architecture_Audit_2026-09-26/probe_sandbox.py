"""Prototype: inject faults ONLY into disposable copies under the OS temp root.

Reads the real project; prints observations; never updates real source/control.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


root = Path(sys.argv[1]).resolve(strict=True)
pwsh = shutil.which("pwsh")
assert pwsh
generated = sorted(root.glob("[0-9][0-9]_*.md"))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run(script, *args):
    p = subprocess.run([pwsh, "-NoProfile", "-File", str(script), *args], capture_output=True, text=True, encoding="utf-8")
    return {"exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def clone(base, name):
    out = base/name
    out.mkdir()
    shutil.copytree(root/"Source_Archive", out/"Source_Archive")
    for p in [*generated, root/"MANIFEST.md", root/"build_consolidation.ps1"]:
        shutil.copy2(p, out/p.name)
    return out


results = {"scope": "TEMP_COPIES_ONLY", "probes": {}}
with tempfile.TemporaryDirectory(prefix="af-architecture-probes-") as tmp:
    base = Path(tmp).resolve()
    assert base.is_relative_to(Path(tempfile.gettempdir()).resolve()) and base != root and not root.is_relative_to(base)
    clean = clone(base, "baseline")
    r = run(clean/"build_consolidation.ps1")
    results["probes"]["isolated_baseline"] = {**r, "generated_matches": {p.name: sha(p) == sha(clean/p.name) for p in generated}, "manifest_matches": sha(root/"MANIFEST.md") == sha(clean/"MANIFEST.md")}
    # Mimic distinct previous generation, then fail after the first five writes.
    partial = clone(base, "partial")
    for p in generated:
        (partial/p.name).write_text("AUDIT_PREVIOUS_GENERATION\n", encoding="utf-8")
    p = partial/"Source_Archive/aetherfire_anti_drift_sex_worker_consent_mobility_white.md"
    t = p.read_text(encoding="utf-8")
    assert "# 1. ĐỊNH HƯỚNG CHUNG" in t
    p.write_text(t.replace("# 1. ĐỊNH HƯỚNG CHUNG", "# AUDIT_MISSING_ANCHOR"), encoding="utf-8")
    r = run(partial/"build_consolidation.ps1")
    results["probes"]["partial_write_failure"] = {**r, "rewritten": [p.name for p in generated if (partial/p.name).read_text(encoding="utf-8") != "AUDIT_PREVIOUS_GENERATION\n"], "still_previous": [p.name for p in generated if (partial/p.name).read_text(encoding="utf-8") == "AUDIT_PREVIOUS_GENERATION\n"]}
    # A phrase changed only by a silent String.Replace no longer matches.
    silent = clone(base, "silent")
    p = silent/"Source_Archive/aetherfire_stable_aviation_rf_airspace_control_canon_delta_2026-09-16.md"
    t = p.read_text(encoding="utf-8")
    old = "hàng nghìn hoặc hàng vạn chuyến bay diễn ra như một utility"
    assert old in t
    p.write_text(t.replace(old, "AUDIT_UNRECONCILED_SENTINEL"), encoding="utf-8")
    r = run(silent/"build_consolidation.ps1")
    results["probes"]["silent_replacement_miss"] = {**r, "unreconciled_sentinel_reaches_output": "AUDIT_UNRECONCILED_SENTINEL" in (silent/"80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md").read_text(encoding="utf-8")}
    # Regex heading shifter cannot distinguish a heading from code content.
    script = base/"helper_probe.ps1"
    helper = (root/"build_consolidation.ps1").read_text(encoding="utf-8")
    start = helper.index("function Shift-MarkdownHeadings")
    end = helper.index("function Write-MarkdownOutput")
    script.write_text(helper[start:end] + "\nShift-MarkdownHeadings -Text @'\n```text\n# literal\n```\n'@\n", encoding="utf-8")
    results["probes"]["heading_in_fence"] = run(script)
    # Independent sandbox repository to avoid git status reading the real worktree.
    repo = base/"runner_repo"
    project = repo/"AetherFire Project"
    project.mkdir(parents=True)
    for d in ("AetherFire CI", "Anti-Drift Source", "tests"):
        shutil.copytree(root/d, project/d)
    for p in (root/"00_AETHERFIRE_CONSOLIDATION_INDEX.md", root/"91_RECONCILIATION_RECORD.md", root/"92_OPEN_ISSUES_CURRENT.md", root/"MANIFEST.md", root/"build_consolidation.ps1"):
        shutil.copy2(p, project/p.name)
    (project/"Source_Archive").mkdir()
    (repo/"ChatGPT Plus+ Era").mkdir()
    shutil.copy2(root.parent/"ChatGPT Plus+ Era/chatgpt v8.5.txt", repo/"ChatGPT Plus+ Era/chatgpt v8.5.txt")
    subprocess.run(["git", "init", "-q", str(repo)], check=True, capture_output=True)
    (project/"AetherFire CI/AetherFire_CI_version_v2.99.md").write_text("# AetherFire CI v2.99 — ChatGPT v8.5 base\n\n> Status: DRAFT\n", encoding="utf-8")
    r = run(project/"tests/control-regressions/run.ps1")
    try:
        payload = json.loads(r["stdout"])
        results["probes"]["runner_draft_version"] = {"exit": r["exit"], "effective_control": payload["effective_control"], "overall": payload["overall"], "model_executed": payload["model_executed"]}
    except json.JSONDecodeError:
        results["probes"]["runner_draft_version"] = r

print(json.dumps(results, ensure_ascii=False, indent=2))
