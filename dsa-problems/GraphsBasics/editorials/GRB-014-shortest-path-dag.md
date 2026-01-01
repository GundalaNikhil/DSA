---
problem_id: GRB_SHORTEST_PATH_DAG__7291
display_id: GRB-014
slug: shortest-path-dag
title: "Shortest Path in DAG"
difficulty: Easy
difficulty_score: 38
topics:
  - Graphs
  - DAG
  - Shortest Path
tags:
  - graphs-basics
  - dag
  - shortest-path
  - easy
premium: true
subscription_tier: basic
---

# GRB-014: Shortest Path in DAG

## 📋 Problem Summary

Given a **Directed Acyclic Graph (DAG)** with weighted edges (possibly negative), find the shortest path distance from a source node `s` to all other nodes. If a node is unreachable, output `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** Project Scheduling (Critical Path)

Imagine managing a software project.
-   **Nodes** are milestones (e.g., "Design Complete", "Backend Ready").
-   **Edges** are tasks with durations (weights). `A -> B` with weight 5 means task A must finish before B, taking 5 days.
-   **DAG:** There are no cycles (you can't need B to finish A if A is needed for B).
-   **Shortest Path?** In scheduling, we often look for the *Longest Path* (Critical Path) to determine minimum project duration. However, finding the *Shortest Path* is mathematically identical (just negate weights).
-   This algorithm is used in tools like Jira or Asana to calculate dependencies and timelines efficiently.

![Real-World Application](../images/GRB-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (2)      (1)
  0 ------> 1 ------> 3
  |         ^
  | (5)     | (-2)
  v         |
  2 --------+
```
**Topological Sort:** `0, 2, 1, 3` (One valid order).

**Relaxation Order:**
1.  **Process 0:** `dist[0]=0`.
    -   `0->1` (w=2): `dist[1] = min(inf, 0+2) = 2`.
    -   `0->2` (w=5): `dist[2] = min(inf, 0+5) = 5`.
2.  **Process 2:** `dist[2]=5`.
    -   `2->1` (w=-2): `dist[1] = min(2, 5-2) = 3`. (Updated!)
3.  **Process 1:** `dist[1]=3`.
    -   `1->3` (w=1): `dist[3] = min(inf, 3+1) = 4`.
4.  **Process 3:** `dist[3]=4`. No outgoing edges.

**Final Distances:** `0:0, 1:3, 2:5, 3:4`.

### Algorithm Steps

1.  **Topological Sort:** Perform a topological sort (using DFS or Kahn's Algorithm) to get a linear ordering of nodes.
2.  **Initialize Distances:** `dist[s] = 0`, all others `infinity`.
3.  **Relax in Order:** Iterate through nodes `u` in topological order.
    -   If `dist[u]` is `infinity`, skip (unreachable).
    -   For each neighbor `v` with weight `w`:
        -   `dist[v] = min(dist[v], dist[u] + w)`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Negative Weights:** Allowed! Standard Dijkstra fails here, but DAG property makes it solvable in linear time.
-   **Unreachable:** Output `-1`.
-   **Infinity:** Use a sufficiently large number (e.g., `1e18` for 64-bit integers).

## Naive Approach

### Intuition

Run Bellman-Ford.

### Time Complexity

-   **O(N * M)**: Works, but overkill. DAGs allow O(N+M).

## Optimal Approach (Topological Sort + Relaxation)

By processing nodes in topological order, we guarantee that when we visit node `u`, we have already processed all possible predecessors of `u`. Thus, `dist[u]` is already final.

### Time Complexity

-   **O(N + M)**: Linear time. Much faster than Dijkstra (O(M log N)) or Bellman-Ford (O(NM)).

### Space Complexity

-   **O(N + M)**: Adjacency list + Recursion stack/Queue.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 2 0
0 1 1
1 2 2
```
**Graph:** `0 -> 1 (1)`, `1 -> 2 (2)`.

**Topological Sort:**
-   DFS(0) -> DFS(1) -> DFS(2) -> Push 2 -> Push 1 -> Push 0.
-   Stack: `[2, 1, 0]` (Top is 0).

**Relaxation:**
1.  Pop 0. `dist[0]=0`.
    -   `0->1`: `dist[1] = min(inf, 1) = 1`.
2.  Pop 1. `dist[1]=1`.
    -   `1->2`: `dist[2] = min(inf, 1+2) = 3`.
3.  Pop 2. `dist[2]=3`. No neighbors.

**Output:** `0 1 3`.

## ✅ Proof of Correctness

In a DAG, if there is a path from `u` to `v`, `u` must appear before `v` in the topological sort. When we relax edges from `u`, `dist[u]` is guaranteed to be the shortest distance because all paths to `u` come from nodes that have already been processed.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Longest Path:** Just negate edge weights (or use `max` instead of `min`) and run the same algorithm.
-   **Count Paths:** Use DP on the topological order to count the number of paths from `s` to `t`.
-   **All-Pairs Shortest Path:** In DAG, can be done in O(N*(N+M)) by running this from every node.

### Common Mistakes to Avoid

1.  **Cycle Detection:** This algorithm assumes input is a DAG. If there's a cycle, topological sort is invalid (or partial), and results are meaningless.
2.  **Unreachable Nodes:** Don't relax edges starting from an unreachable node (`dist[u] == INF`).
3.  **Recursion Depth:** For deep DAGs (like a line), Python/JS recursion limit might be hit. Use iterative DFS (Kahn's Algorithm) if needed.
