---
title: Dynamic Connectivity Over Time (Offline)
slug: dynamic-connectivity-offline
difficulty: Hard
difficulty_score: 78
tags:
- Segment Tree
- DSU Rollback
- Offline Queries
problem_id: SEG_DYNAMIC_CONNECTIVITY_OFFLINE__6384
display_id: SEG-016
topics:
- Segment Tree
- DSU Rollback
- Offline Queries
---
# Dynamic Connectivity Over Time (Offline) - Editorial

## Problem Summary

You are given a sequence of `m` events on a graph with `n` nodes:
1.  **ADD u v**: Add an edge between `u` and `v`.
2.  **REMOVE u v**: Remove the edge between `u` and `v`.
3.  **QUERY u v**: Check if `u` and `v` are connected.

You must answer the queries in the order they appear.


## Constraints

- `1 <= n <= 100000`
- `1 <= m <= 200000`
- `1 <= u, v <= n`
## Real-World Scenario

Imagine a **Network Simulation Tool**.
-   You are simulating a network where links (cables) are constantly being plugged in and unplugged.
-   At various points in time, you need to verify if two servers can communicate.
-   Since this is a simulation (or a log replay), you have all events available beforehand (offline).

## Problem Exploration

### 1. Dynamic Connectivity
-   Fully dynamic connectivity (online) is very hard (`O(log^2 N)` or `O(sqrtN)`).
-   Offline dynamic connectivity is solvable using **Segment Tree over Time**.

### 2. Segment Tree over Time
-   The "time" is the index of the operation (0 to `m-1`).
-   An edge `(u, v)` exists for a set of time intervals.
    -   If added at `t_1` and removed at `t_2`, it exists in `[t_1, t_2-1]`.
    -   If added at `t_1` and never removed, it exists in `[t_1, m-1]`.
-   We can map each edge to a list of intervals.
-   We build a Segment Tree where leaves represent time points.
-   We add each edge to the Segment Tree nodes covering its intervals.
    -   Just like range updates, but instead of updating a value, we append the edge to a list in the node.

### 3. DFS Traversal with DSU Rollback
-   Traverse the Segment Tree (DFS).
-   When entering a node:
    -   Apply all edges stored in this node using DSU (Union-Find).
    -   Keep track of operations to rollback (store which nodes were merged and rank changes).
-   When reaching a leaf (time `t`):
    -   If the operation at `t` is a QUERY, answer it using the current DSU state.
-   When exiting a node:
    -   Rollback the DSU operations performed at this node to restore state for the sibling.

### 4. Complexity
-   Each edge covers `O(log m)` nodes in the Segment Tree.
-   DSU operations take `O(log n)` or `O(alpha(n))` (with path compression, but rollback usually prevents path compression, so we use union by rank/size which is `O(log n)`).
-   Total time: `O(m log m log n)`.

## Approaches

### Approach 1: Segment Tree Divide & Conquer (Offline)
-   Map edges to intervals.
-   Build Segment Tree.
-   DFS with DSU Rollback.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 4`
`ADD 1 2`
`QUERY 1 2`
`REMOVE 1 2`
`QUERY 1 2`

1.  **Events**:
    -   0: ADD 1 2. Active.
    -   1: QUERY 1 2.
    -   2: REMOVE 1 2. Edge (1,2) interval: `[0, 1]`.
    -   3: QUERY 1 2.
2.  **Segment Tree**:
    -   Edge (1,2) added to range `[0, 1]`.
3.  **DFS**:
    -   Enter `[0, 1]`: Union(1, 2).
    -   Leaf 0: No query.
    -   Leaf 1: Query 1 2. Connected? Yes. Output `true`.
    -   Exit `[0, 1]`: Rollback.
    -   Enter `[2, 3]`: No edges.
    -   Leaf 2: No query.
    -   Leaf 3: Query 1 2. Connected? No. Output `false`.

## Proof of Correctness

-   **Time Intervals**: Correctly maps edge lifespan to segment tree nodes.
-   **DSU Rollback**: Ensures state is valid for the current time interval during DFS traversal.
-   **Offline**: All queries processed in correct temporal order.

## Interview Extensions

1.  **Dynamic MST?**
    -   Same approach, but maintain MST edges. Rollback is harder if we need to query total weight efficiently.
2.  **Bipartite Check?**
    -   Maintain bipartite property in DSU (distance to root parity).

### Common Mistakes

-   **Path Compression**: Cannot use path compression with rollback easily (it destroys structure). Must use Union by Rank/Size only.
-   **Edge Intervals**: Be careful with indices (inclusive/exclusive) when edge is removed.
