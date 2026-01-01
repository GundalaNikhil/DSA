---
problem_id: AGR_MAX_FLOW_VERTEX_CAPACITY__5913
display_id: AGR-002
slug: max-flow-vertex-capacity
title: "Max Flow With Vertex Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Max Flow
  - Vertex Capacities
tags:
  - advanced-graphs
  - max-flow
  - vertex-capacity
  - medium
premium: true
subscription_tier: basic
---

# AGR-002: Max Flow With Vertex Capacities

## 📋 Problem Summary

Compute the maximum flow in a network where not only edges but also **vertices** have capacity limits. A vertex capacity limits the total flow passing *through* that vertex.

## 🌍 Real-World Scenario

**Scenario Title:** Airport Passenger Throughput

Consider an air travel network:
-   **Edges** are flights. A flight from NYC to London has a capacity (number of seats).
-   **Vertices** are airports.
-   **Vertex Capacity:** Even if there are many incoming and outgoing flights, an airport (e.g., London Heathrow) has a limit on how many passengers it can process per hour (security, customs, baggage).
-   **Goal:** Find the max number of people that can travel from Source to Destination, respecting both flight seats and airport processing limits.

![Real-World Application](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186946/dsa-problems/AGR-002/editorial/rzif27pjtweeefkokyku.jpg)

## Detailed Explanation

### Concept Visualization

![Concept Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186948/dsa-problems/AGR-002/editorial/fm1dogp6yvuosdp4emvu.jpg)

Node B has a capacity of 5. Even though 10 units enter from A and 10 could leave to C, B can only handle 5.

**Transformed Graph (Vertex Splitting):**
```
      (10)          (5)           (10)
  A --------> B_in -----> B_out --------> C
```
We split B into `B_in` and `B_out`.
-   All incoming edges point to `B_in`.
-   All outgoing edges start from `B_out`.
-   Add a new edge `B_in -> B_out` with capacity equal to B's vertex capacity (5).

Now, standard Max Flow algorithms will naturally respect the vertex limit because all flow through B must pass through the `B_in -> B_out` edge.

### Algorithm Steps

1.  **Graph Transformation:**
    -   For each node `i` (0 to N-1), create two nodes in the new graph: `u_in` (index `2*i`) and `u_out` (index `2*i + 1`).
    -   Add edge `u_in -> u_out` with capacity `cap[i]`. (If `cap[i] == -1`, use Infinity).
    -   For each original edge `u -> v` with capacity `c`:
        -   Add edge `u_out -> v_in` with capacity `c`.
2.  **Run Max Flow:**
    -   Source in new graph: `s_in` (or `s_out`? Usually source has infinite capacity, so `s_in -> s_out` is infinite. We can start flow from `s_in`).
    -   Sink in new graph: `t_out`.
    -   Use **Dinic's Algorithm** (or Edmonds-Karp) to find max flow.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Infinite Capacity:** Input uses `-1`. Treat this as `10^18` (safe large number).
-   **Source/Sink:** The problem says `s` and `t` have unlimited capacity. So `s_in -> s_out` and `t_in -> t_out` should be Infinite.
-   **Node Indexing:** Original `i` maps to `2*i` and `2*i+1`. Total nodes `2*N`.

## Naive Approach

### Intuition

Try to modify the Max Flow algorithm to check vertex capacity every time we push flow. This is complex to implement correctly (need to track vertex usage separately) and error-prone.

## Optimal Approach (Vertex Splitting)

Reducing the problem to standard Max Flow is the cleanest and most robust way.

### Time Complexity

-   **O(V^2 E)**: Dinic's complexity. Here `V' = 2N`, `E' = M + N`. So roughly `O(N^2 (M+N))`. For N=2000, M=5000, this is well within limits (Dinic is usually much faster than worst case).

### Space Complexity

-   **O(N + M)**: To store the transformed graph.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 3 0 3
-1 3 2 -1
0 1 3
1 2 2
2 3 3
```
**Graph Construction:**
-   **Vertices:**
    -   `0_in -> 0_out` (INF)
    -   `1_in -> 1_out` (3)
    -   `2_in -> 2_out` (2)
    -   `3_in -> 3_out` (INF)
-   **Edges:**
    -   `0_out -> 1_in` (3)
    -   `1_out -> 2_in` (2)
    -   `2_out -> 3_in` (3)

**Path:** `0_in -> 0_out -> 1_in -> 1_out -> 2_in -> 2_out -> 3_in -> 3_out`
**Capacities:**
-   `0->0`: INF
-   `0->1`: 3
-   `1->1`: 3
-   `1->2`: 2
-   `2->2`: 2
-   `2->3`: 3
-   `3->3`: INF

**Bottleneck:** `min(INF, 3, 3, 2, 2, 3, INF) = 2`.
**Max Flow:** 2.

![Walkthrough Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186952/dsa-problems/AGR-002/editorial/ipxyvbgobhljhi4msyfi.jpg)

## ✅ Proof of Correctness

The construction ensures that any unit of flow passing through node `u` must traverse the edge `u_in -> u_out`. Since this edge has capacity `cap[u]`, the total flow through `u` cannot exceed `cap[u]`. Standard Max Flow correctness applies to the rest.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Min-Cost Max-Flow:** If edges/vertices have costs, use MCMF algorithms (SPFA/Dijkstra with potentials).
-   **Undirected Edges:** Split undirected `u-v` into directed `u->v` and `v->u`.
-   **Dynamic Capacities:** How to update flow if a vertex capacity increases/decreases?

### Common Mistakes to Avoid

1.  **Source/Sink Capacity:** Usually, source and sink are assumed to have infinite capacity unless specified otherwise. Don't accidentally cap them.
2.  **Node Indexing:** Be careful mapping `u` to `2*u` and `2*u+1`.
3.  **Edge Direction:** Original edge `u->v` goes from `u_out` to `v_in`. NOT `u_in` to `v_in`.
