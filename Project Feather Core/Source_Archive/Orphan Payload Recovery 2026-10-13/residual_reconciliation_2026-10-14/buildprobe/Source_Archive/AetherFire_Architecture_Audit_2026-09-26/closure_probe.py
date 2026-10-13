"""Synthetic graph probe, not a production Router or semantic completeness test."""
import json
import time
from collections import defaultdict, deque


def closure(graph, seeds):
    seen = set()
    pending = deque(seeds)
    traversed = 0
    while pending:
        node = pending.popleft()
        if node in seen:
            continue
        if node not in graph:
            raise ValueError("MISSING_NODE:" + node)
        seen.add(node)
        for edge in graph[node]:
            traversed += 1
            pending.append(edge)
    return seen, traversed


def reverse(graph):
    result = {n: [] for n in graph}
    for n, targets in graph.items():
        for target in targets:
            if target not in result:
                raise ValueError("MISSING_NODE:" + target)
            result[target].append(n)
    return result


results = []
for modules in (8, 80):
    # 100 synthetic nodes per module is an experimental input, not a repo measurement.
    graph = {f"M{m}:N{n}": [] if n == 0 else [f"M{m}:N{n-1}"] for m in range(modules) for n in range(100)}
    start = time.perf_counter()
    inv = reverse(graph)
    loaded, traversed = closure(graph, ["M0:N9"])
    impacted, rev_edges = closure(inv, ["M0:N0"])
    elapsed = time.perf_counter() - start
    assert len(loaded) == 10 and len(impacted) == 100
    results.append({"scenario": "sparse_local", "modules": modules, "nodes": len(graph), "edges": sum(map(len, graph.values())), "read_closure": len(loaded), "read_edges": traversed, "reverse_impact": len(impacted), "seconds_including_reverse_index": elapsed})
graph = {"shared": []} | {f"C{i}": ["shared"] for i in range(8000)}
impact, traversed = closure(reverse(graph), ["shared"])
assert len(impact) == 8001
results.append({"scenario": "high_fanout", "impact": len(impact), "edges": traversed, "expected_policy": "NO_SILENT_TRUNCATION; FULL_AFFECTED_AUDIT_OR_BLOCK"})
graph = {f"M{i}": [f"M{j}" for j in range(80) if i != j] for i in range(80)}
loaded, traversed = closure(graph, ["M0"])
assert len(loaded) == 80 and traversed == 6320
results.append({"scenario": "dense_mutual_read", "closure": len(loaded), "edges": traversed})
assert closure({"a": ["b"], "b": ["a"]}, ["a"])[0] == {"a", "b"}
results.append({"scenario": "read_cycle_terminates", "status": "PASS", "limitation": "Does not authorize a derivation/supersession cycle"})
try:
    closure({"a": ["missing"]}, ["a"])
except ValueError as exc:
    results.append({"scenario": "missing_dependency", "status": "PASS", "error": str(exc)})
else:
    raise AssertionError("Missing dependency was silently dropped")
print(json.dumps({"status": "SYNTHETIC_PROTOTYPE_ONLY", "results": results, "not_tested": ["LLM evidence selection", "semantic edge completeness", "actual node router", "concurrent publisher", "JSON Schema implementation"]}, indent=2))
