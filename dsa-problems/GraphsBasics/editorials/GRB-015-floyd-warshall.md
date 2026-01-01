---
problem_id: GRB_FLOYD_WARSHALL__9386
display_id: GRB-015
slug: floyd-warshall
title: "Floyd-Warshall All-Pairs"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Floyd-Warshall
  - Shortest Path
tags:
  - graphs-basics
  - floyd-warshall
  - shortest-path
  - medium
premium: true
subscription_tier: basic
---

# GRB-015: Floyd-Warshall All-Pairs

## 📋 Problem Summary

Given a directed weighted graph (represented as an adjacency matrix), compute the shortest path distance between **every pair of nodes**.
-   If a **negative cycle** exists, output `NEGATIVE CYCLE`.
-   Otherwise, output the `N x N` distance matrix.

## 🌍 Real-World Scenario

**Scenario Title:** Airline Routing

Imagine you are building a flight booking system.
-   **Nodes** are airports.
-   **Edges** are direct flights with costs.
-   **Goal:** A user might want to fly from *any* airport A to *any* airport B. You need a pre-computed table of the cheapest possible routes between all pairs of cities.
-   Floyd-Warshall computes this entire table in one go, allowing instant lookups for "Cheapest flight from NYC to London".

![Real-World Application](../images/GRB-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (4)
  0 ------> 1
  ^         |
  | (-2)    | (3)
  |         v
  2 <------ 2
```
Let's assume: `0->1 (4)`, `1->2 (-2)`, `2->0 (3)`.

**Initial Matrix:**
```
   0  1  2
0  0  4 -1
1 -1  0 -2
2  3 -1  0
```
(-1 means infinity)

**Iteration k=0 (Via Node 0):**
-   Can we improve `2->1` using `2->0->1`?
-   `dist[2][1] = min(inf, dist[2][0] + dist[0][1])`
-   `dist[2][1] = min(inf, 3 + 4) = 7`.
-   Updated Matrix.

**Iteration k=1 (Via Node 1):**
-   Can we improve `0->2` using `0->1->2`?
-   `dist[0][2] = min(inf, 4 + (-2)) = 2`.

**Iteration k=2 (Via Node 2):**
-   Can we improve `1->0` using `1->2->0`?
-   `dist[1][0] = min(inf, -2 + 3) = 1`.

**Final Matrix:**
```
   0  1  2
0  0  4  2
1  1  0 -2
2  3  7  0
```

### Algorithm Steps

1.  **Initialize:** `dist[i][j]` is the weight of edge `i->j`, or infinity if no edge. `dist[i][i] = 0`.
2.  **Triple Loop:**
    -   `for k from 0 to n-1`: (Intermediate node)
        -   `for i from 0 to n-1`: (Source)
            -   `for j from 0 to n-1`: (Destination)
                -   `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
3.  **Negative Cycle Check:**
    -   After the loops, check if any `dist[i][i] < 0`. If so, a negative cycle exists.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Input Format:** `-1` represents infinity (no edge). Convert this to a large constant (e.g., `1e15`) internally.
-   **Output Format:** Convert large constants back to `-1`.
-   **Constraints:** N <= 500. O(N^3) is ~1.25 * 10^8 operations, which fits within 2 seconds in C++/Java. Python might be tight but usually passes if optimized (PyPy).

## Naive Approach

### Intuition

Run Bellman-Ford from every node.

### Time Complexity

-   **O(N^2 * M)**: Since M can be N^2, this is O(N^4). Too slow.

## Optimal Approach (Floyd-Warshall)

Dynamic Programming approach. `dp[k][i][j]` = shortest path from `i` to `j` using only nodes `0..k` as intermediates. We optimize space to `dp[i][j]`.

### Time Complexity

-   **O(N^3)**: Three nested loops.

### Space Complexity

-   **O(N^2)**: Distance matrix.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
0 1 4
-1 0 2
-1 -1 0
```
**Matrix:**
```
0  1  4
∞  0  2
∞  ∞  0
```
**k=0:** No changes (Row 0 and Col 0 are mostly ∞).
**k=1:**
-   `dist[0][2] = min(4, dist[0][1] + dist[1][2])`
-   `dist[0][2] = min(4, 1 + 2) = 3`.
-   Matrix:
    ```
    0  1  3
    ∞  0  2
    ∞  ∞  0
    ```
**k=2:** No changes.

**Result:** Matches example output.

## ✅ Proof of Correctness

Floyd-Warshall is based on the recurrence:
`dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])`.
This considers all paths from `i` to `j` using intermediate nodes `{0...k}`. By the time `k=N-1`, we consider all possible intermediate nodes, thus finding the shortest path.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Path Reconstruction:** Store `next[i][j] = k` whenever you update `dist[i][j]`. This allows reconstructing the actual path.
-   **Transitive Closure:** Use boolean OR/AND instead of min/sum to find reachability (Warshall's Algorithm).
-   **Minimax Path:** Minimize the maximum edge weight on the path (modify relaxation logic).

### Common Mistakes to Avoid

1.  **Loop Order:** The loop order MUST be `k` (intermediate), then `i` (source), then `j` (dest). Swapping them breaks the DP state dependency.
2.  **Overflow:** Adding two `INF` values can overflow if not careful. Use `long long` and check for `INF` before adding.
3.  **Negative Cycle Detection:** Simply checking `dist[i][i] < 0` works, but only if you don't care *which* cycle.
