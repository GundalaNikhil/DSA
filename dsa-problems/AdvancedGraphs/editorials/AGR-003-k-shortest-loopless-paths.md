---
problem_id: AGR_K_SHORTEST_LOOPLESS_PATHS__2749
display_id: AGR-003
slug: k-shortest-loopless-paths
title: "K Shortest Paths (Loopless)"
difficulty: Medium
difficulty_score: 62
topics:
  - Graphs
  - Shortest Path
  - Yen Algorithm
tags:
  - advanced-graphs
  - k-shortest
  - yen
  - medium
premium: true
subscription_tier: basic
---

# AGR-003: K Shortest Paths (Loopless)

## 📋 Problem Summary

Find the `K` shortest **simple** paths (paths without repeated vertices) from a source `s` to a target `t`. Output their lengths in ascending order.

## 🌍 Real-World Scenario

**Scenario Title:** GPS Route Alternatives

When you use Google Maps, it doesn't just show the single fastest route. It often suggests "Route 1 (20 mins)", "Route 2 (22 mins)", etc.
-   **Constraint:** Drivers don't want to drive in circles (loops).
-   **Goal:** Provide the top `K` distinct, loop-free options so the user can choose based on preference (e.g., avoiding highways).

![Real-World Application](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187131/dsa-problems/AGR-003/editorial/dvh4j3ysmd1vuvbljasr.jpg)

## Detailed Explanation

### Concept Visualization

![Concept Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187134/dsa-problems/AGR-003/editorial/kdxt0pi3lxeduzprntah.jpg)

**Paths from A to C:**
1.  `A -> B -> C`: Cost `1 + 1 = 2`. (Shortest)
2.  `A -> C`: Cost `3`. (2nd Shortest)

**Yen's Algorithm Logic:**
-   Find 1st shortest: `P1 = [A, B, C]`.
-   **Deviate from A:** Ban edge `A->B`. Find shortest `A->...->C`. Result: `A->C` (cost 3).
-   **Deviate from B:** Ban edge `B->C`. Find shortest `B->...->C`. No other path.
-   Candidate: `A->C`. Add to results.

### Algorithm: Yen's Algorithm

Yen's algorithm finds the `k`-th shortest path by exploring deviations from the `(k-1)`-th shortest path.

1.  **Initialization:** Find the 1st shortest path `A[0]` using Dijkstra. Add to `result`.
2.  **Iterate k from 1 to K-1:**
    -   Let `prevPath = A[k-1]`.
    -   For each node `spurNode` in `prevPath` (except the last one):
        -   **Root Path:** The sub-path from `source` to `spurNode`.
        -   **Spur Path:** Find the shortest path from `spurNode` to `target` in the graph, subject to:
            -   **Edge Constraints:** Remove edges that were part of previous shortest paths starting with the same Root Path (to force a new route).
            -   **Node Constraints:** Remove nodes in Root Path (to ensure the path is simple/loopless).
        -   **Total Path:** Root Path + Spur Path. Add to `candidates` heap.
    -   Extract the shortest path from `candidates`. This is `A[k]`.
    -   Add `A[k]` to `result`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Simple Paths:** Crucial. Standard Eppstein’s algorithm finds paths with loops. Yen's handles simple paths if we explicitly block Root Path nodes.
-   **Output:** Only lengths. If fewer than K exist, output as many as found.
-   **Constraints:** N=500, K=50. Yen's is `O(K * N * (M + N log N))`. With N=500, this is roughly `50 * 500 * 5000` ops, which is heavy but passable in 2s.

## Naive Approach

### Intuition

DFS to find ALL paths, sort them, pick top K.

### Time Complexity

-   **Exponential**: Number of simple paths can be `N!`. Impossible for N=500.

## Optimal Approach (Yen's Algorithm)

### Time Complexity

-   **O(K * N * (M + N log N))**: In each of K iterations, we run Dijkstra up to N times (once for each spur node).

### Space Complexity

-   **O(N^2 + K * N)**: Storing graph and K paths.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3 0 2 2
0 1 1
1 2 1
0 2 3
```
**Initialization:**
-   Shortest path `p0`: `0->1->2` (cost 2). `A = [p0]`.

**Iteration k=1:**
-   `prevPath = 0->1->2`.
-   **Spur Node 0:**
    -   Root Path: `[0]`. Root Cost: 0.
    -   Forbidden Edges: `(0,1)` (from p0).
    -   Shortest path `0->2` avoiding `(0,1)`: `0->2` (cost 3).
    -   Total: `0->2` (cost 3). Add to B.
-   **Spur Node 1:**
    -   Root Path: `[0, 1]`. Root Cost: 1.
    -   Forbidden Edges: `(1,2)` (from p0).
    -   Forbidden Nodes: `0`.
    -   Shortest path `1->2` avoiding `(1,2)`: None.
-   **Best from B:** `0->2` (cost 3). `A = [p0, p1]`.

**Result:** 2 paths, costs 2 and 3.

![Walkthrough Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187137/dsa-problems/AGR-003/editorial/sp2k7ifnx2i3peebnk0o.jpg)

## ✅ Proof of Correctness

Yen's algorithm partitions the set of all simple paths. By systematically deviating from every node of every previously found shortest path, it ensures that no path is missed. The use of a heap guarantees we always pick the next smallest cost.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Eppstein's Algorithm:** Finds K shortest paths *allowing loops* in `O(M + N log N + K)`. Much faster but harder to implement.
-   **A* Search:** Use A* with Yen's for faster spur path finding if coordinates are available.

### Common Mistakes to Avoid

1.  **Loopless Constraint:** Yen's naturally handles loops if you don't block root path nodes. For *simple* paths, you MUST block nodes in `rootPath` (except `spurNode`).
2.  **Duplicate Paths:** Different spur nodes can generate the same path. Use a Set or check before adding to heap.
3.  **Edge Removal:** Only remove the specific edge `u->v`, not all edges between `u` and `v` (if multigraph).
