---
problem_id: GRP_BATTERY_ARCHIPELAGO__3928
display_id: GRP-010
slug: battery-archipelago-analyzer
title: "Battery Archipelago Analyzer"
difficulty: Medium-Hard
difficulty_score: 65
topics:
  - Shortest Path
  - Dijkstra Variant
  - Custom Constraints
tags:
  - graph
  - dijkstra
  - shortest-path
  - constraints
  - hard
premium: true
subscription_tier: premium
---

# GRP-010: Battery Archipelago Analyzer

## 📋 Problem Summary

Find the minimum cost path between a source and destination in a weighted undirected graph, considering only edges with weights less than or equal to a battery capacity `B`.

## 🌍 Real-World Scenario

**Scenario Title:** EV Route Planning with Range Anxiety

Imagine planning a route for an Electric Vehicle (EV) across an archipelago of islands connected by bridges.
-   **Nodes:** Islands with charging stations.
-   **Edges:** Bridges with specific energy costs (lengths).
-   **Battery Capacity (B):** The maximum energy your car can spend on a *single* bridge crossing without running out of power mid-bridge.
-   **Goal:** Find the route that consumes the least total energy, but you can *only* cross bridges that your battery can handle in one go. If a bridge is too long (weight > B), it's impassable regardless of total path length.

![Real-World Application](../images/GRP-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Constrained Path

**Graph:**
```
      (10)        (50)
  S -------- A -------- D
  |          |          |
  | (20)     | (20)     | (5)
  |          |          |
  +--------- B ---------+
```
**Battery B = 25**

-   **Edge S-A (10):** OK (10 <= 25).
-   **Edge A-D (50):** BLOCKED (50 > 25).
-   **Edge S-B (20):** OK (20 <= 25).
-   **Edge A-B (20):** OK (20 <= 25).
-   **Edge B-D (5):** OK (5 <= 25).

**Valid Paths:**
1.  `S -> A -> B -> D`: Cost `10 + 20 + 5 = 35`.
2.  `S -> B -> D`: Cost `20 + 5 = 25`.

**Shortest Valid Path:** `S -> B -> D` (Cost 25).
Note that `S -> A -> D` would be length 60, but it's invalid because `A -> D` requires 50 battery.

### Algorithm: Constrained Dijkstra

1.  **Filter Edges:** Conceptually, remove all edges with `weight > B`.
2.  **Run Dijkstra:** Perform standard Dijkstra's algorithm on the filtered graph.
    -   Initialize `dist` array with infinity, `dist[s] = 0`.
    -   Use a Priority Queue to pick the node with the smallest distance.
    -   Relax neighbors: For neighbor `v` of `u` with weight `w`:
        -   **Constraint Check:** If `w <= B`:
            -   If `dist[u] + w < dist[v]`:
                -   `dist[v] = dist[u] + w`
                -   `pq.push(v, dist[v])`
3.  **Result:** Return `dist[d]`. If `dist[d]` is still infinity, return `-1`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Graph:** Undirected.
-   **Constraints:** `N` up to 10^5, `M` up to 2*10^5.
-   **Weights:** Up to 10^6.
-   **Battery B:** Up to 10^6.
-   **Output:** -1 if no path exists.

## Naive Approach

### Intuition

BFS or DFS to find all paths, check constraints, and pick minimum.

### Time Complexity

-   **Exponential:** Finding all paths is too slow.

## Optimal Approach (Dijkstra)

### Time Complexity

-   **O(M log N)**: Standard Dijkstra. The constraint check `w <= B` is O(1).

### Space Complexity

-   **O(N + M)**: Adjacency list and distance array.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 5
0 1 10
0 2 50
1 2 20
1 3 30
2 3 5
0 3 25
```
**Battery B = 25**

1.  **Init:** `dist=[0, INF, INF, INF]`, `pq=[(0, 0)]`.
2.  **Pop (0, 0):**
    -   Neighbors of 0:
        -   1 (w=10): 10 <= 25. Update `dist[1]=10`. Push `(10, 1)`.
        -   2 (w=50): 50 > 25. Skip.
3.  **Pop (10, 1):**
    -   Neighbors of 1:
        -   0 (w=10): `10+10 >= 0`. Skip.
        -   2 (w=20): 20 <= 25. Update `dist[2]=10+20=30`. Push `(30, 2)`.
        -   3 (w=30): 30 > 25. Skip.
4.  **Pop (30, 2):**
    -   Neighbors of 2:
        -   0 (w=50): Skip.
        -   1 (w=20): `30+20 >= 10`. Skip.
        -   3 (w=5): 5 <= 25. Update `dist[3]=30+5=35`. Push `(35, 3)`.
5.  **Pop (35, 3):**
    -   Target reached? Yes. Return `dist[3]=35`.

    **Final Output:** 35.

    **Verification:**
    -   Path 0->1->2->3 uses edges with weights 10, 20, 5.
    -   All weights are <= 25 (Battery).
    -   Total Cost: 10 + 20 + 5 = 35.
    -   Other paths like 0->1->3 involve edge 1-3 (weight 30 > 25), so they are invalid.
    -   The logic holds.

## ✅ Proof of Correctness

-   **Dijkstra's Optimality:** Dijkstra guarantees shortest path in non-negative weighted graphs.
-   **Constraint Handling:** By ignoring edges with `w > B`, we effectively run Dijkstra on the subgraph of valid edges. The shortest path in this subgraph is the answer.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Max Capacity Path:** Find path maximizing the bottleneck capacity (Modified Prim's/Dijkstra).
-   **Battery Charging:** If nodes are charging stations, how to reach D with min time? (State space search `(u, charge)`).

### Common Mistakes to Avoid

1.  **Summing Weights vs Max Weight:** The constraint is on *individual* edge weights, not the sum.
2.  **Directed vs Undirected:** Problem is undirected.
3.  **Infinity Check:** Return -1 if destination is unreachable.
