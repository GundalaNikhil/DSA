---
problem_id: AGR_DINIC_WITH_SCALING__5083
display_id: AGR-011
slug: dinic-with-scaling
title: "Dinic With Scaling"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Max Flow
  - Scaling
tags:
  - advanced-graphs
  - max-flow
  - dinic
  - medium
premium: true
subscription_tier: basic
---

# AGR-011: Dinic With Scaling

## 📋 Problem Summary

Compute the maximum flow in a directed graph using **Dinic's Algorithm with Capacity Scaling**. This optimization helps when edge capacities are very large.

## 🌍 Real-World Scenario

**Scenario Title:** High-Volume Data Pipeline

Imagine a data center network transferring petabytes of data.
-   **Capacities:** Links have massive bandwidths (e.g., 100 Gbps, 10 Gbps).
-   **Challenge:** Standard augmenting path algorithms can waste time finding tiny flows (1 bit) when huge pipes are available.
-   **Scaling:** First, route traffic only through the "thickest" pipes (e.g., > 64 Gbps). Once saturated, use the > 32 Gbps pipes, and so on. This ensures we make significant progress quickly.

![Real-World Application](../images/AGR-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (100)
  S ---------> A
  |            |
  | (1)        | (100)
  v            v
  B ---------> T
      (100)
```
-   **Without Scaling:** Can find path `S->B->T` (100) then `S->A->T` (100).
-   **With Scaling (Delta=64):**
    -   Edges `S->A` (100), `A->T` (100), `S->B` (1), `B->T` (100).
    -   Only consider edges with cap >= 64.
    -   Path `S->A->T` is valid. Push 100.
    -   Path `S->B->T` invalid (`S->B` cap 1 < 64).
-   **Delta=32...1:**
    -   Eventually consider `S->B`.

### Algorithm: Capacity Scaling

1.  **Initialize Delta:** Let `U` be the max capacity. Set `delta` to the largest power of 2 less than or equal to `U`.
2.  **Iterate:** While `delta >= 1`:
    -   Run Dinic's Algorithm (BFS levels + DFS blocking flow), but **ignore edges** where `residual_capacity < delta`.
    -   `delta /= 2`.
3.  **Result:** Sum of all flows pushed.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Large Capacities:** Up to `10^9`. Scaling is effective here.
-   **Flow:** Use `long` (64-bit).
-   **Complexity:** Scaling adds a `log(MaxCap)` factor but reduces the dependence on E in practice for some cases, or ensures polynomial time `O(E^2 log C)` independent of flow value.

## Naive Approach

### Intuition

Standard Edmonds-Karp (BFS).

### Time Complexity

-   **O(V * E^2)**: Theoretically fine for small graphs, but slow if flow is large and many augmentations needed.

## Optimal Approach (Dinic + Scaling)

### Time Complexity

-   **O(E^2 log C)**: The number of scaling phases is `log C`. In each phase, we do at most `2E` augmentations (roughly).

### Space Complexity

-   **O(V + E)**: Graph storage.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4 0 3
0 1 10
0 2 5
1 3 7
2 3 8
```
-   Max Cap = 10. `delta` starts at 8.
-   **Delta = 8:**
    -   Edges >= 8: `0->1` (10), `2->3` (8).
    -   BFS: `0->1`. `1->3` (7 < 8) ignored. `0->2` (5 < 8) ignored.
    -   No path to 3.
-   **Delta = 4:**
    -   Edges >= 4: All.
    -   BFS: `0->1->3` (10, 7), `0->2->3` (5, 8).
    -   DFS `0->1->3`: Push `min(10, 7) = 7`. Flow=7.
    -   DFS `0->2->3`: Push `min(5, 8) = 5`. Flow=12.
    -   Total Flow = 12.
-   **Delta = 2, 1:**
    -   Residuals: `0->1` (3), `1->3` (0), `0->2` (0), `2->3` (3).
    -   No path.

**Result:** 12. Correct.

## ✅ Proof of Correctness

-   **Scaling:** In each phase `delta`, we push flow along paths with bottleneck >= `delta`.
-   **Termination:** When `delta=1`, we consider all edges with residual capacity >= 1. Since capacities are integers, this finds the exact max flow.
-   **Complexity:** The scaling ensures we don't "nibble" at the flow with small augmentations when large ones are possible.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Why Scaling?** Standard Dinic is `O(V^2 E)`. On a graph with `V=2`, `E=2`, caps `10^9`, Dinic is fast (1 step). But on specific "bad" graphs, scaling guarantees polynomial time in `log C`.
-   **Edmonds-Karp:** Scaling can also be applied to Edmonds-Karp (BFS), making it `O(E^2 log C)`.
-   **Real-valued Capacities:** Scaling doesn't work directly; requires integer capacities.

### Common Mistakes to Avoid

1.  **Delta Initialization:** Start with largest power of 2 <= max_cap.
2.  **Loop Condition:** `delta >= 1`.
3.  **Residual Check:** `cap - flow >= delta`.
