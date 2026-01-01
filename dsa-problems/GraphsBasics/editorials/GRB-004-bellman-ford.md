---
problem_id: GRB_BELLMAN_FORD__3812
display_id: GRB-004
slug: bellman-ford
title: "Bellman-Ford with Negative Edges"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Shortest Path
  - Bellman-Ford
tags:
  - graphs-basics
  - bellman-ford
  - shortest-path
  - medium
premium: true
subscription_tier: basic
---

# GRB-004: Bellman-Ford with Negative Edges

## 📋 Problem Summary

You are given a directed graph with edges that can have **negative weights**. Find the shortest path distance from a source node `s` to all other nodes. If the graph contains a **negative cycle** reachable from `s`, output `NEGATIVE CYCLE`.

## 🌍 Real-World Scenario

**Scenario Title:** Currency Arbitrage

Imagine you are trading currencies.
-   **Nodes** are currencies (USD, EUR, JPY).
-   **Edges** are exchange rates.
-   **Weights:** Usually, we multiply rates, but if we take logarithms, we can turn multiplication into addition. A "negative weight" in this context could represent a profitable trade loop.
-   **Negative Cycle:** This is an "infinite money glitch" (Arbitrage). If you can trade USD -> EUR -> JPY -> USD and end up with *more* USD than you started, you can repeat this forever for infinite profit. In shortest path terms, the "cost" keeps decreasing forever.

The Bellman-Ford algorithm detects if such a loop exists.

![Real-World Application](../images/GRB-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      -1
  0 -----> 1
  ^        |
  | -1     | -1
  |        v
  3 <----- 2
```
**Cycle:** `0 -> 1 -> 2 -> 3 -> 0`
**Total Weight:** `-1 + (-1) + (-1) + (-1) = -4`.

**Analysis:**
-   Every time you go around this loop, the total distance decreases by 4.
-   Shortest path to any node in this loop is effectively `-infinity`.
-   Bellman-Ford detects this because distances keep updating even after `N-1` iterations.

### Algorithm Steps

1.  **Initialization:**
    -   `dist` array initialized to Infinity (`1e18` or similar large value).
    -   `dist[s] = 0`.
2.  **Relaxation (N-1 times):**
    -   Loop `i` from `1` to `n-1`.
    -   For every edge `(u, v, w)` in the graph:
        -   If `dist[u] != Infinity` and `dist[u] + w < dist[v]`:
            -   `dist[v] = dist[u] + w`.
3.  **Negative Cycle Check (N-th iteration):**
    -   Iterate through all edges one last time.
    -   If any edge `(u, v, w)` can *still* be relaxed (`dist[u] + w < dist[v]`), it means there is a negative cycle reachable from `s`.
4.  **Output:**
    -   If cycle detected: Print `NEGATIVE CYCLE`.
    -   Else: Print `dist` array (convert Infinity to `-1`).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Negative Weights:** Allowed.
-   **Negative Cycle:** A cycle where the sum of edge weights is negative.
-   **Reachable:** The cycle must be reachable from `s`. An unreachable negative cycle doesn't affect the shortest path from `s`.
-   **Infinity:** Use a value larger than any possible path (e.g., `1e18` for 64-bit integers).

## Naive Approach

### Intuition

Dijkstra's algorithm is the standard for shortest paths, but it fails with negative edges because it assumes that once a node is visited, its distance cannot be improved. With negative edges, you might find a "longer" path (more edges) that has a smaller total weight later on.

### Failure Case

`A -> B (cost 2)`, `A -> C (cost 5)`, `C -> B (cost -10)`.
Dijkstra might finalize B at cost 2. But `A -> C -> B` costs `5 - 10 = -5`. Dijkstra misses this.

## Optimal Approach (Bellman-Ford)

Bellman-Ford relaxes *all* edges `N-1` times. The intuition is that the shortest path in a graph with `N` nodes can have at most `N-1` edges (if it's simple). If we can still improve a path after `N-1` iterations, it must be because we are finding a path with `N` edges or more, which implies a cycle. If that cycle reduces the cost, it's a negative cycle.

### Time Complexity

-   **O(N * M)**: We iterate `N` times, and in each iteration, we check all `M` edges.

### Space Complexity

-   **O(N)**: Only need to store the `dist` array.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 2 0
0 1 -1
1 0 -1
```

**Initialization:**
-   `dist`: `[0, INF]`

**Iteration 1:**
-   Edge `0 -> 1` (w=-1): `dist[0] != INF`. `0 + (-1) < INF`. Update `dist[1] = -1`.
-   Edge `1 -> 0` (w=-1): `dist[1] != INF`. `-1 + (-1) < 0`. Update `dist[0] = -2`.
-   `dist`: `[-2, -1]`

**Iteration 2 (Negative Cycle Check):**
-   Edge `0 -> 1` (w=-1): `dist[0] = -2`. `-2 + (-1) = -3`. `dist[1] = -1`.
-   `-3 < -1`. Condition holds!
-   **Output:** `NEGATIVE CYCLE`.

## ✅ Proof of Correctness

1.  **Shortest Path Property:** A shortest path in a graph with `N` nodes and no negative cycles can have at most `N-1` edges.
2.  **Relaxation:** After `k` iterations of relaxing all edges, we have found the shortest paths with at most `k` edges.
3.  **Convergence:** After `N-1` iterations, all shortest paths (without cycles) are found.
4.  **Detection:** If a distance can still be reduced after `N-1` iterations, it implies a path with `N` edges is shorter, which means a node is repeated, forming a cycle with negative total weight.

## 💡 Interview Extensions (High-Value Add-ons)

-   **SPFA (Shortest Path Faster Algorithm):** An optimization of Bellman-Ford using a queue. Faster on average (O(kM)), but worst case is still exponential.
-   **Find the Cycle:** Instead of just returning true/false, reconstruct the nodes in the negative cycle (use `parent` array).
-   **Longest Path:** In a DAG, negate weights and run Bellman-Ford (or just use Topo Sort).

### Common Mistakes to Avoid

1.  **Unreachable Nodes:** Don't relax edges coming from `INF` distance nodes (`if dist[u] != INF`).
2.  **Disconnected Negative Cycles:** A negative cycle might exist but be unreachable from `s`. The problem usually asks for cycles *reachable* from `s`. Our implementation handles this by checking `dist[u] != INF`.
3.  **Order of Edges:** The order in which edges are processed can affect how quickly distances converge, but the result after `N-1` iterations is guaranteed to be correct.
