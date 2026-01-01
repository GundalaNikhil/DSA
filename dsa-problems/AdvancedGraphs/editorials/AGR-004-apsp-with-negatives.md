---
problem_id: AGR_APSP_WITH_NEGATIVES__6027
display_id: AGR-004
slug: apsp-with-negatives
title: "All-Pairs Shortest Path With Negative Edges"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - APSP
  - Johnson
tags:
  - advanced-graphs
  - apsp
  - johnson
  - medium
premium: true
subscription_tier: basic
---

# AGR-004: All-Pairs Shortest Path With Negative Edges

## 📋 Problem Summary

Compute the shortest path distance between **every pair of nodes** in a graph that may contain **negative edge weights** (but no negative cycles).

## 🌍 Real-World Scenario

**Scenario Title:** Terrain Hiking with Energy

Imagine hiking on a terrain.
-   **Positive Edge:** Walking uphill consumes energy (cost > 0).
-   **Negative Edge:** Walking downhill recovers energy (cost < 0, or "gain").
-   **Goal:** Find the minimum energy required to get from any point A to any point B.
-   **Challenge:** Since "downhill" edges exist, standard Dijkstra doesn't work. Since the map is huge (2000 points), Floyd-Warshall is too slow. We need a smarter approach.

![Real-World Application](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187674/dsa-problems/AGR-004/editorial/ef9p51em1cfs5p9akfvq.jpg)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (2)
  A --------> B
  |           |
  | (4)       | (-5)
  v           v
  C <-------- D
      (1)
```
**Reweighting (Johnson's Idea):**
We want to transform edge weights to be non-negative so we can use Dijkstra.
-   Assign a "potential" `h[u]` to each node.
-   New weight `w'(u, v) = w(u, v) + h[u] - h[v]`.
-   Telescoping sum: Path cost `A -> ... -> Z` becomes `OriginalCost + h[A] - h[Z]`.
-   If we pick `h` correctly (using Bellman-Ford), all `w'(u, v) >= 0`.

### Algorithm: Johnson's Algorithm

1.  **Add Virtual Source:** Add node `S` with edges `S -> u` (weight 0) for all `u`.
2.  **Compute Potentials:** Run **Bellman-Ford** from `S`. The shortest path distance to `u` becomes `h[u]`.
    -   If Bellman-Ford detects a negative cycle, stop (though problem says none exist).
3.  **Reweight Edges:** `w_new(u, v) = w_old(u, v) + h[u] - h[v]`.
    -   Property: `w_new` is always >= 0.
4.  **Run Dijkstra:** For every node `u`, run Dijkstra using `w_new` to find distances to all `v`.
5.  **Adjust Distances:** `TrueDist(u, v) = DijkstraDist(u, v) - h[u] + h[v]`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **INF:** Use a large number (e.g., `1e18`) for unreachable nodes.
-   **Output:** Print "INF" string for infinity.
-   **Constraints:** N=2000. Floyd-Warshall (O(N^3)) is too slow. Johnson's (O(NM log N)) is required.

## Naive Approach

### Intuition

Run Bellman-Ford from every node.

### Time Complexity

-   **O(N * N * M)**: `2000 * 2000 * 5000` is huge. TLE.

## Optimal Approach (Johnson's Algorithm)

### Time Complexity

-   **O(N * M log N)**: Bellman-Ford takes O(NM). N Dijkstras take O(N * M log N). Total fits in 2s.

### Space Complexity

-   **O(N + M)**: Adjacency list.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1 2
1 2 -1
0 2 4
```
**Bellman-Ford (Potentials h):**
-   Init `h = [0, 0, 0]`.
-   Iter 1:
    -   `0->1 (2)`: `h[1] = min(0, 0+2) = 0`.
    -   `1->2 (-1)`: `h[2] = min(0, 0-1) = -1`.
    -   `0->2 (4)`: `h[2] = min(-1, 0+4) = -1`.
-   `h = [0, 0, -1]`.
-   Iter 2: No changes.

**Reweighted Edges:**
-   `0->1`: `2 + h[0] - h[1] = 2 + 0 - 0 = 2`.
-   `1->2`: `-1 + h[1] - h[2] = -1 + 0 - (-1) = 0`.
-   `0->2`: `4 + h[0] - h[2] = 4 + 0 - (-1) = 5`.

**Dijkstra from 0:**
-   `d[0]=0`.
-   `0->1` (w'=2): `d[1]=2`.
-   `0->2` (w'=5): `d[2]=5`.
-   `1->2` (w'=0): `d[2] = min(5, 2+0) = 2`.
-   Final `d`: `[0, 2, 2]`.
-   Real Dist:
    -   `0->0`: `0 - 0 + 0 = 0`.
    -   `0->1`: `2 - 0 + 0 = 2`.
    -   `0->2`: `2 - 0 + (-1) = 1`.
-   Row 0: `0 2 1`. (Matches example)

## ✅ Proof of Correctness

Johnson's algorithm uses the potential function `h` to reweight edges such that `w'(u,v) >= 0` while preserving shortest paths. `dist'(u,v) = dist(u,v) + h[u] - h[v]`. Since `h` values are fixed, minimizing `dist'` minimizes `dist`. The non-negative weights allow Dijkstra, ensuring efficiency.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Detect Negative Cycle:** If Bellman-Ford step finds a change in the N-th iteration, a negative cycle exists.
-   **SPFA:** Shortest Path Faster Algorithm (queue-based Bellman-Ford) can be used instead of Dijkstra if graph is sparse, but worst case is exponential.
-   **Parallelization:** The N Dijkstra runs are independent and can be parallelized.

### Common Mistakes to Avoid

1.  **INF Value:** Use a large number but not `LLONG_MAX` to avoid overflow when adding weights.
2.  **Bellman-Ford Init:** Initialize `h` to 0 (equivalent to virtual source edges).
3.  **Output Format:** Problem asks for "INF" string, not the number.
