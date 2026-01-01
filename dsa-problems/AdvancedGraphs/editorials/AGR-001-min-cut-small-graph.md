---
problem_id: AGR_MIN_CUT_SMALL_GRAPH__4182
display_id: AGR-001
slug: min-cut-small-graph
title: "Minimum Cut on Small Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Min Cut
  - Stoer-Wagner
tags:
  - advanced-graphs
  - min-cut
  - stoer-wagner
  - medium
premium: true
subscription_tier: basic
---

# AGR-001: Minimum Cut on Small Graph

## 📋 Problem Summary

Given an undirected weighted graph, find the **Global Minimum Cut**. This is the minimum total weight of edges that, if removed, would disconnect the graph into two non-empty components.

## 🌍 Real-World Scenario

**Scenario Title:** The Weakest Link in the Power Grid

Imagine a city's power grid where power stations and substations are connected by transmission lines. Each line has a "cost" to cut (e.g., how robust it is).
-   **Goal:** Identify the most vulnerable set of lines that, if failed (or sabotaged), would split the city's power grid into two isolated islands.
-   **Why?** By finding this "Minimum Cut", engineers know exactly where to reinforce the network to prevent a total blackout separation.

![Real-World Application](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185634/dsa-problems/AGR-001/editorial/w5iuzwibb3qes3llp9ad.jpg)

## Detailed Explanation

### Concept Visualization
![Concept Graph Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186392/dsa-problems/AGR-001/editorial/ll6zm88un3k4cqwktayh.jpg)
**Possible Cuts:**
1.  Cut `{A}` from `{B, C, D}`: Edges `(A,B), (A,C), (A,D)`. Cost: `2 + 1 + 3 = 6`.
2.  Cut `{C}` from `{A, B, D}`: Edges `(C,A), (C,D)`. Cost: `1 + 1 = 2`. **(Minimum)**

### Algorithm: Stoer-Wagner

Unlike the s-t Min Cut (which uses Max Flow), the Global Min Cut does not fix source and sink nodes. We could run s-t Min Cut for a fixed `s` and all other `t`, but that's slow. **Stoer-Wagner** is a deterministic algorithm specifically for this.

**Core Idea (Minimum Cut Phase):**
1.  Start with an arbitrary node `a`.
2.  Repeatedly add the node that is "most tightly connected" to the set of already added nodes (similar to Prim's algorithm).
3.  The **last two nodes** added to the set, say `s` and `t`, have a special property: The cut that separates `t` from the rest of the graph is a candidate for the global min cut.
4.  **Merge** `s` and `t` into a single super-node.
5.  Repeat until only one node remains. The minimum of all "cut-of-the-last-phase" values is the global answer.

### Algorithm Steps

1.  Initialize `min_cut = infinity`.
2.  While graph has > 1 node:
    -   Run **MinimumCutPhase**:
        -   Start with node 0.
        -   Maintain `weights` array (sum of edges to current set).
        -   Extract max `weight` node, add to set.
        -   Record the last two nodes added: `s` (second to last) and `t` (last).
        -   Update `min_cut = min(min_cut, weight_of_t)`.
    -   **Merge** `s` and `t`:
        -   Add all edges from `t` to `s`.
        -   Remove `t` from graph (mark as merged).

![Merge Step Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186394/dsa-problems/AGR-001/editorial/his2cdctczm35nmtqzwm.jpg)

3.  Return `min_cut`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Disconnected Graph:** If the graph is initially disconnected, the min cut is 0. Stoer-Wagner handles this naturally (a phase will find a 0-weight cut).
-   **Self-Loops:** Merging nodes creates self-loops. These must be ignored or removed.
-   **Adjacency Matrix:** Since N <= 200, an adjacency matrix `adj[N][N]` is efficient and simplifies merging.

## Naive Approach

### Intuition

Fix node 0 as source. Iterate all other nodes `i` as sink. Run Max-Flow Min-Cut (Dinic/Edmonds-Karp) for each pair `(0, i)`.

### Time Complexity

-   **O(N * MaxFlow)**: For N=200, this is roughly `200 * O(V^2 E)`. This is too slow; Stoer-Wagner is `O(N^3)` and simpler to implement for undirected graphs.

## Optimal Approach (Stoer-Wagner)

### Time Complexity

-   **O(N^3)**: Each phase takes `O(N^2)` (scanning weights), and there are `N-1` phases. With Fibonacci heap, it can be `O(N E + N^2 log N)`, but simple array scan is `O(N^3)`.

### Space Complexity

-   **O(N^2)**: Adjacency matrix.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4
0 1 1
1 2 2
2 3 1
0 3 2
```
**Phase 1:**
- Start at 0. Initial weights: `[0, 1, 0, 2]`.
- Pick 3 (max weight 2). Update: weight[2] becomes 1.
- Pick 1 (tie with 2). Update: weight[2] becomes 3.
- Pick 2 last. Phase cut = 3. Merge 2 into 1.

![Phase 1 Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186725/dsa-problems/AGR-001/editorial/khw2mvggwyqbimgsgokd.jpg)

**Phase 2:**
- Remaining nodes: 0, 1, 3.
- Start at 0. Pick 3 (weight 2). Update: weight[1] becomes 2.
- Pick 1 last. Phase cut = 2. Merge 1 into 3.

![Phase 2 Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186807/dsa-problems/AGR-001/editorial/k2cjbbna9hpaaop0yehi.jpg)

**Phase 3:**
- Remaining nodes: 0, 3.
- Phase cut = 3.

![Phase 3 Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186754/dsa-problems/AGR-001/editorial/kspksfewbg6v6a8kb6aj.jpg)

**Result:** 2.
