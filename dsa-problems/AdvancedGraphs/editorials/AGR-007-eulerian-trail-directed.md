---
problem_id: AGR_EULERIAN_TRAIL_DIRECTED__4836
display_id: AGR-007
slug: eulerian-trail-directed
title: "Eulerian Trail With Directed Edges"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Eulerian Path
  - DFS
tags:
  - advanced-graphs
  - eulerian
  - hierholzer
  - medium
premium: true
subscription_tier: basic
---

# AGR-007: Eulerian Trail With Directed Edges

## 📋 Problem Summary

Find a path in a directed graph that visits every edge exactly once. If the path starts and ends at the same vertex, it's an **Eulerian Circuit**. If they are different, it's an **Eulerian Trail**.

## 🌍 Real-World Scenario

**Scenario Title:** The Efficient Mail Carrier

A mail carrier must deliver mail to houses along one-way streets.
-   **Goal:** Traverse every street (edge) exactly once to minimize wasted time.
-   **Constraint:** Streets are one-way.
-   **Problem:** Can they plan such a route? If so, where must they start?

![Real-World Application](../images/AGR-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    (0) --> (1)
     ^       |
     |       v
    (3) <-- (2) --> (4)
```
-   **Degrees:**
    -   0: in=1, out=1
    -   1: in=1, out=1
    -   2: in=1, out=2 (Start candidate? out > in)
    -   3: in=1, out=1
    -   4: in=1, out=0 (End candidate? in > out)
-   **Trail:** `2 -> 4` (stuck).
-   **Example Trail:** `2->0->1->2->4`.
-   **Start Node:** 2 (`out = in + 1`).
-   **End Node:** 4 (`in = out + 1`).

### Algorithm: Hierholzer's Algorithm

1.  **Check Existence:**
    -   Calculate `in` and `out` degrees for all nodes.
    -   Count nodes where `out != in`.
    -   **Case 1 (Circuit):** All `out == in`. Start anywhere (with edges).
    -   **Case 2 (Trail):** Exactly one node `S` has `out = in + 1`, exactly one node `E` has `in = out + 1`, all others `out == in`. Start at `S`.
    -   **Case 3 (Impossible):** Any other degree configuration.
2.  **Check Connectivity:** The graph (ignoring isolated vertices) must be weakly connected. Hierholzer's naturally checks this: if the resulting path length != M+1, it's disconnected.
3.  **Construct Path:**
    -   Start DFS from `S`.
    -   Follow edges, marking them as used (or removing from adjacency list).
    -   When stuck (no outgoing edges), add node to `path`.
    -   Backtrack.
    -   Result is `path` reversed.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **M=0:** A graph with no edges has an Eulerian trail of length 1 (just the node). Output `YES` and any node.
-   **Output Format:** `YES` followed by the sequence of nodes.
-   **Edge Removal:** Efficiently remove edges. `adj[u].pop()` is O(1). Using an index pointer `ptr[u]` is cleaner.

## Naive Approach

### Intuition

Backtracking (Try all paths).

### Time Complexity

-   **Exponential**: `O(N!)`. Impossible for N=100,000.

## Optimal Approach (Hierholzer's)

### Time Complexity

-   **O(N + M)**: Each edge visited once.

### Space Complexity

-   **O(N + M)**: Adjacency list and recursion stack.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1
1 2
2 0
```
**Degree Check:**
-   0: in=1, out=1
-   1: in=1, out=1
-   2: in=1, out=1
-   All equal. Circuit. Start at 0.

**Hierholzer:**
1.  Stack: `[0]`.
2.  Top 0. Has edge `0->1`. Pop. Stack: `[0, 1]`.
3.  Top 1. Has edge `1->2`. Pop. Stack: `[0, 1, 2]`.
4.  Top 2. Has edge `2->0`. Pop. Stack: `[0, 1, 2, 0]`.
5.  Top 0. No edges. Pop 0. Trail: `[0]`.
6.  Top 2. No edges. Pop 2. Trail: `[0, 2]`.
7.  Top 1. No edges. Pop 1. Trail: `[0, 2, 1]`.
8.  Top 0. No edges. Pop 0. Trail: `[0, 2, 1, 0]`.

**Result:** Reverse trail -> `0 1 2 0`. Correct.

## ✅ Proof of Correctness

-   **Degrees:** Euler proved that a connected graph has an Eulerian trail iff the degree conditions are met.
-   **Hierholzer:** By greedily following edges and backtracking only when stuck, we essentially find a main cycle and splice in sub-cycles. Since the graph is connected, we eventually visit all edges.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Undirected Graph:** Conditions change (all degrees even, or exactly two odd). Algorithm is similar but must handle back-edges (remove `u->v` and `v->u`).
-   **Chinese Postman Problem:** Find shortest path visiting all edges (allows repeating). If Eulerian, it's just total weight. If not, add edges to make it Eulerian.

### Common Mistakes to Avoid

1.  **Connectivity:** Degree check passes, but graph has two disjoint components with edges. Check `trail.length == m + 1`.
2.  **Recursion Depth:** Python/Java recursion limit is low. Use `sys.setrecursionlimit` or iterative stack.
3.  **Edge Removal:** Removing from middle of list is O(N). Use `pop()` from end or an index pointer.
