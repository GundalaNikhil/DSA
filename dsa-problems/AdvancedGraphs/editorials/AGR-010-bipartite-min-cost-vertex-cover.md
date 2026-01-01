---
problem_id: AGR_BIPARTITE_MIN_COST_VERTEX_COVER__3406
display_id: AGR-010
slug: bipartite-min-cost-vertex-cover
title: "Minimum Cost Vertex Cover in Bipartite Graph"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Vertex Cover
  - Min Cut
tags:
  - advanced-graphs
  - vertex-cover
  - min-cut
  - medium
premium: true
subscription_tier: basic
---

# AGR-010: Minimum Cost Vertex Cover in Bipartite Graph

## 📋 Problem Summary

Given a bipartite graph where each node has a weight, find a subset of vertices with the minimum total weight such that every edge is incident to at least one vertex in the subset.

## 🌍 Real-World Scenario

**Scenario Title:** Security Camera Placement

Imagine a museum with two rows of rooms (Left and Right).
-   **Edges:** Corridors connecting a room on the Left to a room on the Right.
-   **Goal:** Place security guards to monitor all corridors.
-   **Constraint:** A guard placed in a room can monitor all connected corridors.
-   **Cost:** Hiring a guard for room `i` costs `W[i]`.
-   **Objective:** Minimize the total hiring cost while ensuring every corridor is watched by at least one guard.

![Real-World Application](../images/AGR-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph Construction:**
```
      (wU[0])        (INF)        (wV[0])
  S ------------> U0 -------> V0 ------------> T
                  |
                  | (INF)
                  v
                  V1 ------------> T
                               (wV[1])
```
-   **Source (S):** Connects to all `U` nodes. Capacity `S -> U_i` is `wU[i]`.
-   **Sink (T):** All `V` nodes connect to `T`. Capacity `V_j -> T` is `wV[j]`.
-   **Middle:** Edges `U_i -> V_j` have capacity **Infinity**.

**Min-Cut Interpretation:**
-   A cut partitions nodes into `S-set` (reachable from S) and `T-set` (not reachable).
-   **Cut `S->U_i`:** `U_i` is in `T-set`. Cost `wU[i]`. Represents selecting `U_i`.
-   **Cut `V_j->T`:** `V_j` is in `S-set`. Cost `wV[j]`. Represents selecting `V_j`.
-   **Cut `U_i->V_j`:** Impossible (cost INF). This forces that if `U_i` is in `S-set` (not selected), `V_j` MUST be in `S-set` (selected).
-   **Logic:** For edge `(u, v)`, we cannot leave both `u` unselected (`S-set`) and `v` unselected (`T-set`? No, `V` unselected is `T-set`).
    -   `S->U` cut => `U` in T-side => Selected.
    -   `V->T` cut => `V` in S-side => Selected.
    -   Path `S -> U -> V -> T`.
    -   To break path, must cut `S->U` (select U) OR `V->T` (select V).
    -   Cannot cut `U->V` (INF).
    -   So every edge is covered.

### Algorithm: Min-Cut (Max-Flow)

1.  **Construct Network:**
    -   Source `S`, Sink `T`.
    -   `S -> U_i` with capacity `wU[i]`.
    -   `V_j -> T` with capacity `wV[j]`.
    -   `U_i -> V_j` with capacity `INF` for each graph edge.
2.  **Compute Max Flow:**
    -   By Max-Flow Min-Cut theorem, the max flow value equals the min cut capacity.
    -   This value is exactly the minimum weight vertex cover.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Weights:** Can be 0. Can be large (`10^9`). Use `long`.
-   **INF:** Use a value larger than sum of all weights (e.g., `1e18`).
-   **Output:** Only the cost is required, not the vertices.

## Naive Approach

### Intuition

Try all subsets of vertices (2^N).

### Time Complexity

-   **Exponential**: `O(2^N * M)`. Impossible for N=100,000.

## Optimal Approach (Dinic's Algorithm)

### Time Complexity

-   **O(E * sqrt(V))**: For bipartite matching type graphs (even with weights on source/sink edges, the structure is similar). In general `O(V^2 E)` or `O(VE^2)`, but much faster in practice.

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
2 2 3
3 1
2 2
0 0
1 0
1 1
```
-   `wU = [3, 1]`. `wV = [2, 2]`.
-   Edges: `0->0`, `1->0`, `1->1`.

**Graph:**
-   `S->U0` (3), `S->U1` (1).
-   `V0->T` (2), `V1->T` (2).
-   `U0->V0` (INF), `U1->V0` (INF), `U1->V1` (INF).

**Flow:**
1.  Path `S -> U1 -> V0 -> T`.
    -   Bottleneck: `min(1, INF, 2) = 1`.
    -   Flow += 1. `S->U1` full. `V0->T` used 1/2.
2.  Path `S -> U0 -> V0 -> T`.
    -   Bottleneck: `min(3, INF, 2-1) = 1`.
    -   Flow += 1. `S->U0` used 1/3. `V0->T` full.
3.  Path `S -> U0 -> V0 (blocked) ...`
    -   `S -> U0 -> V0` blocked.
    -   `S -> U1` blocked.
    -   `S -> U0 -> ??` (U0 only connects to V0).
    -   The direct paths are saturated, but another augmenting path exists.
    -   `U1->V1`? `S->U1` is full.
    -   Can we redirect?
    -   If we push 1 through `S->U1->V1->T`.
    -   Then `S->U1` is full.
    -   Then `S->U0->V0->T` takes 2.
    -   Total 3.
    -   Check the min cut.
    -   Cut `S->U1` (1) and `V0->T` (2). Total 3.
    -   Edges covered:
        -   `0->0`: covered by V0.
        -   `1->0`: covered by U1 and V0.
        -   `1->1`: covered by U1.
    -   Valid cover. Cost 3.
    -   Can we do better?
    -   Cover `U0` (3) and `U1` (1)? Cost 4.
    -   Cover `V0` (2) and `V1` (2)? Cost 4.
    -   Cover `U1` (1) and `V1` (2)? `0->0` not covered.
    -   Min cost is 3.

**Result:** 3. Correct.

## ✅ Proof of Correctness

-   **Kőnig's Theorem:** For unweighted bipartite graphs, Min Vertex Cover = Max Matching.
-   **Weighted Extension:** Min Weight Vertex Cover = Min Cut in the constructed network.
-   **Min-Cut Max-Flow:** We solve Min Cut using Max Flow.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Maximum Independent Set:** In bipartite graphs, Max Independent Set = Total Weight - Min Vertex Cover.
-   **General Graphs:** Vertex Cover is NP-Hard. Bipartite property is crucial.
-   **Recovering Solution:** To find the actual vertices, find the Min Cut partition (reachable from S in residual graph). `U_i` selected if `U_i` NOT reachable. `V_j` selected if `V_j` reachable.

### Common Mistakes to Avoid

1.  **INF Capacity:** Must be larger than sum of all weights.
2.  **Graph Direction:** `S->U`, `U->V`, `V->T`. All directed.
3.  **Zero Weights:** Algorithm works fine with zero weights (just 0 capacity edges).
