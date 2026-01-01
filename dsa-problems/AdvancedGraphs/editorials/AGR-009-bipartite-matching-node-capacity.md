---
problem_id: AGR_BIPARTITE_MATCHING_NODE_CAPACITY__8194
display_id: AGR-009
slug: bipartite-matching-node-capacity
title: "Maximum Matching with Node Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Bipartite Matching
  - Max Flow
tags:
  - advanced-graphs
  - bipartite-matching
  - max-flow
  - medium
premium: true
subscription_tier: basic
---

# AGR-009: Maximum Matching with Node Capacities

## 📋 Problem Summary

Find the maximum number of edges we can select in a bipartite graph such that each node `u` in the left set is incident to at most `capU[u]` selected edges, and each node `v` in the right set is incident to at most `capV[v]` selected edges.

## 🌍 Real-World Scenario

**Scenario Title:** Job Fair Hiring

Imagine a job fair with Candidates (Left) and Companies (Right).
-   **Candidates:** Each candidate `u` can accept up to `capU[u]` job offers (for example, multiple part-time gigs).
-   **Companies:** Each company `v` has `capV[v]` open positions.
-   **Edges:** Valid applications/interviews.
-   **Goal:** Maximize the total number of job placements.

![Real-World Application](../images/AGR-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph Construction:**
```
      (capU[0])        (1)        (capV[0])
  S ------------> U0 -------> V0 ------------> T
                  |
                  | (1)
                  v
                  V1 ------------> T
                               (capV[1])
```
-   **Source (S):** Connects to all `U` nodes. Edge capacity `S -> U_i` is `capU[i]`.
-   **Sink (T):** All `V` nodes connect to `T`. Edge capacity `V_j -> T` is `capV[j]`.
-   **Middle:** Original edges `U_i -> V_j` have capacity 1 (since each specific job-candidate pair happens once).

### Algorithm: Max Flow (Dinic's Algorithm)

1.  **Construct Network:**
    -   Create a source node `S` and sink node `T`.
    -   Add edges `S -> u` with capacity `capU[u]`.
    -   Add edges `v -> T` with capacity `capV[v]`.
    -   For every edge `u-v` in input, add directed edge `u -> v` with capacity 1.
2.  **Run Max Flow:**
    -   The maximum flow from `S` to `T` corresponds exactly to the maximum matching size.
    -   Flow conservation ensures node capacities are respected.
    -   Integrality theorem ensures we can find an integer flow (matching).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Capacities:** Can be large (`10^9`), so use `long` (64-bit integer) for flow.
-   **Node Indexing:** Input gives `u` (0 to nU-1) and `v` (0 to nV-1). In the flow graph, you can map them to `1..nU` and `nU+1..nU+nV`.
-   **Multiple Edges:** If input contains duplicate `u-v` edges, they are effectively parallel edges with capacity 1 each (total capacity > 1). Usually, matching implies unique edges, but if "multigraph" is allowed, just sum capacities. Standard assumption: simple graph, capacity 1 per pair.

## Naive Approach

### Intuition

Greedy matching? Sort by capacity?

### Failure Case

Greedy often fails in flow problems. Taking an edge can block a better path that satisfies more demand.

## Optimal Approach (Dinic's Algorithm)

### Time Complexity

-   **O(E * sqrt(V))**: For unit networks (simple bipartite matching), Dinic is `O(E * sqrt(V))`. Here, capacities are not 1, but the "middle" edges are unit capacity. The complexity is generally bounded by `O(E * sqrt(V))` or `O(V * E)` depending on implementation details, which is fast enough for V, E ~ 200,000.

### Space Complexity

-   **O(V + E)**: To store the graph.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 2 3
1 2
1 1
0 0
1 0
1 1
```
-   `nU=2, nV=2`.
-   `capU = [1, 2]`. `capV = [1, 1]`.
-   Edges: `0->0`, `1->0`, `1->1`.

**Graph:**
-   `S -> U0` (cap 1)
-   `S -> U1` (cap 2)
-   `U0 -> V0` (cap 1)
-   `U1 -> V0` (cap 1)
-   `U1 -> V1` (cap 1)
-   `V0 -> T` (cap 1)
-   `V1 -> T` (cap 1)

**Flow:**
1.  Path `S -> U0 -> V0 -> T`. Flow 1.
    -   `S->U0` full. `V0->T` full.
2.  Path `S -> U1 -> V1 -> T`. Flow 1.
    -   `S->U1` used 1/2. `V1->T` full.
3.  Any other path?
    -   `S -> U1 -> V0` blocked (V0->T full).
    -   `S -> U0` blocked.
    -   Max Flow = 2.

**Result:** 2. Correct.

## ✅ Proof of Correctness

-   **Reduction:** This is a standard reduction from Bipartite Matching to Max Flow.
-   **Capacities:** The capacities on `S->U` and `V->T` enforce the node constraints. The capacity 1 on `U->V` ensures each edge is used at most once.
-   **Integrality:** Since all capacities are integers, Max Flow guarantees an integer solution.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Min Cost Max Flow:** If edges have costs (e.g., hiring cost), use MCMF.
-   **Dynamic Matching:** If edges are added/removed, can we update flow? (Yes, dynamic graph algorithms).
-   **Hopcroft-Karp:** For standard bipartite matching (all caps 1), Hopcroft-Karp is `O(E sqrt(V))`, which is essentially Dinic on unit networks.

### Common Mistakes to Avoid

1.  **Node Indexing:** Ensure U and V nodes don't collide. Offset V indices by `nU`.
2.  **Capacity Overflow:** Use `long long` (Java `long`, JS `BigInt`) for flow variables, even if capacities fit in int, total flow can exceed int (though here max flow <= M).
3.  **Infinite Loops:** In DFS, ensure `level[v] == level[u] + 1` check is strict to avoid cycles (though BFS levels prevent this).
