---
problem_id: AGR_DIRECTED_CYCLE_BASIS__8240
display_id: AGR-015
slug: directed-cycle-basis
title: "Directed Cycle Basis"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Cycle Basis
  - Spanning Forest
tags:
  - advanced-graphs
  - cycle-basis
  - directed
  - hard
premium: true
subscription_tier: basic
---

# AGR-015: Directed Cycle Basis

## 📋 Problem Summary

Find a **Cycle Basis** of a directed graph consisting of `m - n + c` simple directed cycles, where `m` is edges, `n` is vertices, and `c` is connected components (in the underlying undirected sense).

## 🌍 Real-World Scenario

**Scenario Title:** Circuit Analysis (Kirchhoff's Laws)

In electrical circuits (or hydraulic networks), we analyze loops to apply Kirchhoff's Voltage Law (KVL).
-   **Mesh Analysis:** We need a set of independent loops (cycles) to write equations.
-   **Basis:** The fundamental cycles form a basis. Any other closed loop can be represented as a combination of these basis loops.
-   **Directed:** Current flows in a specific direction, so loops must be directed.

![Real-World Application](../images/AGR-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    0 --> 1
    ^     |
    |     v
    3 <-- 2
```
-   Edges: `0->1`, `1->2`, `2->3`, `3->0`.
-   Cycle: `0-1-2-3-0`.
-   `m=4, n=4, c=1`. Basis size `4-4+1 = 1`.
-   Output: `4 0 1 2 3 0`.

**Two Cycles:**
```
   0 -> 1 -> 0
   1 -> 2 -> 1
```
-   `m=4, n=3, c=1`. Basis size `4-3+1 = 2`.
-   Cycles: `0-1-0` and `1-2-1`.

### Algorithm: Horton's Algorithm (Simplified) or Gaussian Elimination

To find a basis of size `D = m - n + c`:
1.  **Candidate Cycles:** For every edge `u -> v`, find the shortest path from `v` to `u` (using BFS). If a path exists, `u -> v` + `path` forms a directed cycle.
2.  **Independence:** We need `D` linearly independent cycles.
    -   Represent each cycle as a vector in `GF(2)^m` (1 if edge is present, 0 otherwise).
    -   Use **Gaussian Elimination** to maintain a basis.
    -   Iterate through edges. For each edge, find the shortest cycle containing it. Try to add to basis.
    -   Stop when we have `D` cycles.

**Why Gaussian Elimination?**
-   Ensures linear independence.
-   With `M=2000`, `M^3` operations with bitsets is feasible.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Basis Size:** Strictly `m - n + c`. If the graph doesn't support this many directed cycles, the problem constraints/type usually ensure it (e.g., strongly connected components or specific structure).
-   **Output Format:** First line `b` (number of cycles). Then each cycle.
-   **Cycle Format:** `k v1 v2 ... vk` where `v1 == vk`.

## Naive Approach

### Intuition

DFS to find back-edges.

### Failure Case

DFS tree back-edges form a basis only for the cycle space of the *underlying undirected graph* if we treat them as undirected. In directed graphs, cross-edges can also form cycles. A simple DFS can miss some or pick dependent ones.

## Optimal Approach (Shortest Cycles + Gaussian Elimination)

### Time Complexity

-   **O(M * (N + M) + M^3 / 64)**:
    -   `M` BFS runs: `O(M * (N + M))`.
    -   Gaussian Elimination: `O(M * BasisSize * M / 64)`. Since BasisSize <= M, `O(M^3 / 64)`.
    -   For `M=2000`, `2000^3 / 64` is approx `1.25 * 10^8`, feasible.

### Space Complexity

-   **O(M^2 / 64)**: To store basis vectors.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 5
0 1
1 2
2 0
1 3
3 1
```
-   `m=5, n=4, c=1`. D = 2.
-   Edges: `0:0->1, 1:1->2, 2:2->0, 3:1->3, 4:3->1`.
-   **Iterate:**
    -   `i=0 (0->1)`: Path `1->2->0`. Cycle `0-1-2-0`. Vec `11100`. Inserted.
    -   `i=1 (1->2)`: Path `2->0->1`. Cycle `1-2-0-1`. Vec `11100`. Dependent (XOR with basis[0] -> 0). Skip.
    -   `i=2 (2->0)`: Path `0->1->2`. Cycle `2-0-1-2`. Dependent.
    -   `i=3 (1->3)`: Path `3->1`. Cycle `1-3-1`. Vec `00011`. Inserted.
    -   Count = 2. Break.
-   **Output:** 2 cycles. Correct.

## ✅ Proof of Correctness

-   **Basis Size:** The dimension of the cycle space is `m - n + c`.
-   **Independence:** Gaussian Elimination ensures all selected cycles are linearly independent.
-   **Validity:** Each cycle is a valid directed cycle.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Minimum Cycle Basis:** Sort edges by weight? No, iterate all pairs `(u, v)`, find shortest path, form cycle, sort cycles by length, then insert. This gives the Minimum Cycle Basis (Horton's Algorithm).
-   **Undirected:** Same logic applies for undirected graphs (using GF(2)).

### Common Mistakes to Avoid

1.  **Bitset Size:** Ensure it covers `M`.
2.  **Independence Check:** Don't just check if cycle is unique; check linear independence.
3.  **Path Direction:** BFS from `v` to `u` for edge `u->v`.
