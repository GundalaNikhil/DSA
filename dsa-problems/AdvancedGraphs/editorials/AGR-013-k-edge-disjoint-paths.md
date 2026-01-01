---
problem_id: AGR_K_EDGE_DISJOINT_PATHS__2167
display_id: AGR-013
slug: k-edge-disjoint-paths
title: "K-Edge-Disjoint Paths"
difficulty: Hard
difficulty_score: 68
topics:
  - Graphs
  - Max Flow
  - Disjoint Paths
tags:
  - advanced-graphs
  - disjoint-paths
  - max-flow
  - hard
premium: true
subscription_tier: basic
---

# AGR-013: K-Edge-Disjoint Paths

## 📋 Problem Summary

Determine if there are at least `k` paths from a source `s` to a sink `t` such that no two paths share an edge.

## 🌍 Real-World Scenario

**Scenario Title:** Redundant Network Routing

In a communication network, reliability is key.
-   **Goal:** Send data packets from Server A to Server B.
-   **Constraint:** If a link fails, we need backup paths.
-   **Requirement:** We want `k` independent paths. If any `k-1` links fail, at least one path remains operational.
-   **Edge-Disjoint:** Paths don't share wires (edges), ensuring failure of one wire doesn't affect others.

![Real-World Application](../images/AGR-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (1)        (1)
  S --------> A --------> T
  |                       ^
  | (1)                   | (1)
  v                       |
  B ----------------------+
```
-   Path 1: `S -> A -> T`.
-   Path 2: `S -> B -> T`.
-   Edges used: `(S,A), (A,T), (S,B), (B,T)`.
-   Are they disjoint? Yes, no shared edges.
-   Max Flow = 2. If `k=2`, YES. If `k=3`, NO.

### Algorithm: Max Flow (Menger's Theorem)

1.  **Menger's Theorem:** The maximum number of edge-disjoint paths from `s` to `t` is equal to the minimum number of edges whose removal disconnects `s` from `t` (Min-Cut).
2.  **Max-Flow Min-Cut:** By the Max-Flow Min-Cut theorem, this value is exactly the maximum flow in a network where every edge has **capacity 1**.
3.  **Procedure:**
    -   Construct a flow network.
    -   Assign capacity 1 to every directed edge.
    -   Run Max Flow (Dinic).
    -   If `max_flow >= k`, return YES.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Directed:** Edges are directed. `u->v` is distinct from `v->u`.
-   **Optimization:** You can stop the max flow algorithm as soon as the flow reaches `k`.
-   **Constraints:** `N=100,000`. Dinic is efficient on unit capacity networks (`O(min(V^{2/3}, E^{1/2}) * E)`).

## Naive Approach

### Intuition

Find a path (BFS), remove edges, repeat.

### Failure Case

Greedy path finding can block future paths.
Example:
```
    A
  /   \
S - M - T
  \   /
    B
```
Edges: `S->A, A->M, M->B, B->T`, `S->M`, `M->T`.
If we greedily take `S->M->T`, we block `M`.

## Optimal Approach (Dinic's Algorithm)

### Time Complexity

-   **O(E * min(V^(2/3), E^(1/2)))**: For unit networks. With `K` limit, it's effectively `O(k * E)` or faster.

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
4 4 0 3 2
0 1
1 3
0 2
2 3
```
-   `s=0, t=3, k=2`.
-   Edges: `0->1`, `1->3`, `0->2`, `2->3`.
-   **Dinic:**
    -   BFS: `0->1->3` (len 2), `0->2->3` (len 2).
    -   DFS:
        -   Push 1 along `0->1->3`. Flow=1.
        -   Push 1 along `0->2->3`. Flow=2.
    -   Limit reached (2). Return 2.
-   **Result:** `2 >= 2` -> YES.

## ✅ Proof of Correctness

-   **Menger's Theorem:** Max edge-disjoint paths = Max Flow with unit capacities.
-   **Dinic:** Correctly computes Max Flow.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Vertex-Disjoint:** Split each node `u` into `u_in` and `u_out` with capacity 1 edge.
-   **Weighted:** Min-cost k-disjoint paths (MCMF).
-   **Undirected:** Replace undirected edge `u-v` with `u->v` and `v->u` both capacity 1? No, that allows `u->v` and `v->u` simultaneously (cycle). For edge-disjoint in undirected, standard max flow works if we treat edge as a single capacity 1 link (flow in one direction blocks other).

### Common Mistakes to Avoid

1.  **Capacity:** Must be 1 for edge-disjoint.
2.  **Direction:** Respect edge direction.
3.  **Self-Loops:** Ignore or handle (though usually irrelevant for s-t paths).
