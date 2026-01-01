---
problem_id: AGR_MINCOST_FLOW_DEMANDS__7702
display_id: AGR-012
slug: mincost-flow-demands
title: "Minimum-Cost Flow With Demands"
difficulty: Hard
difficulty_score: 70
topics:
  - Graphs
  - Min-Cost Flow
  - Circulation
tags:
  - advanced-graphs
  - min-cost-flow
  - demands
  - hard
premium: true
subscription_tier: basic
---

# AGR-012: Minimum-Cost Flow With Demands

## 📋 Problem Summary

Find a flow in a network that satisfies node supply/demand constraints and edge lower/upper bound capacity constraints, while minimizing the total cost.

## 🌍 Real-World Scenario

**Scenario Title:** Supply Chain Optimization

Imagine a logistics network.
-   **Nodes:** Factories (Supply > 0), Warehouses (Supply = 0), Retailers (Supply < 0, i.e., Demand).
-   **Edges:** Transport routes.
-   **Lower Bound:** Minimum contract amount (must ship at least X units).
-   **Upper Bound:** Truck capacity.
-   **Cost:** Shipping cost per unit.
-   **Goal:** Satisfy all retailer demands from factories at minimum shipping cost.

![Real-World Application](../images/AGR-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Transformation:**
Original Edge `u -> v` `[low, high, cost]`:
```
    (u) --[cap: high-low, cost: cost]--> (v)
```
-   **Pre-flow:** We force `low` units through `u->v`.
-   **Cost:** Add `low * cost` to total.
-   **Balance Update:** `b[u] -= low`, `b[v] += low`.

**Super Source/Sink:**
After processing all edges, we have updated `b` values.
-   **Super Source S:** Connect to all `i` where `b[i] > 0`. Cap `b[i]`, Cost 0.
-   **Super Sink T:** Connect all `i` where `b[i] < 0` to `T`. Cap `-b[i]`, Cost 0.

**Feasibility:**
Run Min-Cost Max-Flow from S to T.
-   If `max_flow == sum(positive b)`, then feasible.
-   Total Cost = `Initial Cost` + `MCMF Cost`.

### Algorithm: Successive Shortest Path using Potentials

1.  **Graph Setup:** Transform edges (handle lower bounds) and add S/T.
2.  **Potentials:** Since costs can be negative, standard Dijkstra fails.
    -   Use **SPFA (Shortest Path Faster Algorithm)** or **Bellman-Ford** once to compute initial potentials `h[]`.
    -   Reweight edges: `cost'(u,v) = cost(u,v) + h[u] - h[v]`. Now `cost' >= 0`.
3.  **Augmentation:**
    -   Run **Dijkstra** on reweighted graph to find shortest path from S to T.
    -   Push flow along path.
    -   Update potentials: `h[v] += dist[v]`.
    -   Repeat until no path from S to T.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Infeasible:** If `sum(positive b) != sum(negative b)` (after adjustments), or if max flow < required supply.
-   **Negative Costs:** Allowed. Potentials handle this (unless negative cycle exists, but "circulation" usually implies finding optimal flow in DAG-like structure or saturating negative cycles).
-   **Constraints:** N=500 is small enough for `O(F * E log V)` or `O(k * E)` SPFA.

## Naive Approach

### Intuition

Linear Programming (Simplex).

### Complexity

-   **Exponential** in worst case, though often fast. Overkill to implement from scratch.

## Optimal Approach (MCMF with Potentials)

### Time Complexity

-   **O(F * E log V)**: Where F is total flow. With Dijkstra and Potentials.

### Space Complexity

-   **O(V + E)**.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 1
5 -5
0 1 2 5 1
```
-   `b = [5, -5]`.
-   Edge `0->1`: `low=2, high=5, cost=1`.
-   **Pre-process:**
    -   Push 2 units `0->1`. Cost `2*1 = 2`.
    -   `b[0] -= 2 => 3`.
    -   `b[1] += 2 => -3`.
    -   Add edge `0->1` cap `5-2=3`, cost 1.
-   **Super Source/Sink:**
    -   `S->0` cap 3 (supply), cost 0.
    -   `1->T` cap 3 (demand), cost 0.
-   **MCMF:**
    -   Path `S->0->1->T`.
    -   Cap: `min(3, 3, 3) = 3`.
    -   Cost: `0 + 1 + 0 = 1` per unit. Total `3*1 = 3`.
-   **Total:**
    -   Base Cost 2 + MCMF Cost 3 = 5.
    -   Flow 3 matches supply 3. Feasible.

**Result:** 5. Correct.

## ✅ Proof of Correctness

-   **Lower Bounds:** Satisfied by pre-pushing flow and adjusting demands.
-   **Demands:** Satisfied by saturating edges from S and to T.
-   **Min Cost:** MCMF algorithms guarantee min cost for a given flow amount in networks without negative cycles (or if handled via potentials).

## 💡 Interview Extensions (High-Value Add-ons)

-   **Negative Cycles:** If the graph has negative cycles, we must saturate them. This requires Bellman-Ford or SPFA to find and cancel negative cycles, or a specific "Min Cost Circulation" algorithm.
-   **Simplex:** Network Simplex is often faster in practice for these problems.
-   **Applications:** Airline scheduling, image segmentation (with costs).

### Common Mistakes to Avoid

1.  **Potentials:** Forgetting to update potentials `h[v] += dist[v]` after each Dijkstra run.
2.  **Reduced Cost:** `cost + h[u] - h[v]` must be non-negative.
3.  **SPFA:** Use it for the first iteration if costs are negative.
