---
problem_id: AGR_OFFLINE_LCA_WITH_MODS__9025
display_id: AGR-016
slug: offline-lca-with-mods
title: "Offline Lowest Common Ancestor with Modifications"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Trees
  - LCA
tags:
  - advanced-graphs
  - lca
  - offline
  - hard
premium: true
subscription_tier: basic
---

# AGR-016: Offline Lowest Common Ancestor with Modifications

## 📋 Problem Summary

Given an initial tree, process `cut` (remove edge), `link` (add edge), and `query` (find LCA) operations. The active edges always form a forest.

## 🌍 Real-World Scenario

**Scenario Title:** Network Hierarchy Management

Imagine a corporate network where departments (nodes) are organized in a hierarchy (tree).

- **Restructuring:** Occasionally, a department is moved (cut link to old manager, link to new manager).
- **Query:** Find the common manager (LCA) of two departments to resolve disputes.
- **Offline:** If we have the log of all changes, we can process them efficiently to answer historical queries.

![Real-World Application](../images/AGR-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Initial:**

```
    0
   / \
  1   2
```

**Cut (0, 1):**

```
    0   1
     \
      2
```

**Link (1, 2):**

```
    0
     \
      2
     /
    1
```

**Query (1, 2):**

- Active path: `1-2`. LCA is 2.
- Note: If we used the _initial_ tree, LCA(1, 2) was 0.
- **Crucial Assumption:** The problem statement implies we solve this using "Binary Lifting in Base Tree". This technique is valid **ONLY IF** the `link` operations restore edges from the initial tree (or a fixed superset). If `link` creates arbitrary edges (like `1-2` above which wasn't in initial), the geometry changes, and static LCA is invalid.
- **However:** Given the hint "Binary Lifting in Base Tree", we assume `link` operations **only toggle** edges from the initial tree. If the problem meant arbitrary dynamic trees, it would require Link-Cut Trees (LCT) and wouldn't mention a "base tree".
- **Interpretation:** We assume `link u v` restores the edge `(u, v)` that existed in the initial tree.

### Algorithm: Dynamic Connectivity (Segment Tree + DSU)

1.  **Time Intervals:**
    - Each edge `(u, v)` exists for certain time intervals `[t_start, t_end]`.
    - Initial edges start at 0. `cut` ends an interval. `link` starts a new one.
2.  **Segment Tree:**
    - Build a Segment Tree over the query range `[0, Q]`.
    - Add each edge's active intervals to the corresponding nodes in the Segment Tree.
3.  **DFS with DSU Rollback:**
    - Traverse the Segment Tree.
    - **Enter Node:** Union all edges present in this node. Use DSU with rank/size and **rollback** (no path compression or path compression with rollback stack).
    - **Leaf Node (Query):** If it's a query `(u, v)`:
      - Check `find(u) == find(v)`.
      - If connected, output `LCA(u, v)` from the **static initial tree**.
      - If not connected, output `-1`.
    - **Exit Node:** Rollback DSU operations to restore state.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Base Tree:** We assume `link` restores initial edges.
- **Disconnected:** Output -1.
- **Offline:** We read all queries first.

## Naive Approach

### Intuition

Simulate operations. For query, run BFS to find path and LCA.

### Time Complexity

- **O(N)** per query. Total `O(NQ)`. Too slow.

## Optimal Approach (Offline Dynamic Connectivity)

### Time Complexity

- **O(Q log Q log N)**: Segment tree depth `log Q`. DSU operations `log N`.
- **LCA Precalc:** `O(N log N)`. LCA Query `O(1)` or `O(log N)`.

### Space Complexity

- **O(N + Q)**: Storage for tree and queries.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
4
0 1
1 2
1 3
4
query 2 3
cut 1 3
query 2 3
link 1 3
```

- **Init:** Edges `0-1, 1-2, 1-3`. LCA(2, 3) = 1.
- **Ops:** 0. `query 2 3`.
  1.  `cut 1 3`.
  2.  `query 2 3`.
  3.  `link 1 3`.
- **Intervals:**
  - `0-1`: `[0, 4]` (never cut).
  - `1-2`: `[0, 4]` (never cut).
  - `1-3`: `[0, 0]` (cut at 1, so active 0..0). Then linked at 3, active `[4, 4]`.
- **Queries:**
  - Time 0: `2 3`. Active edges: `0-1, 1-2, 1-3`. Connected. LCA=1.
  - Time 2: `2 3`. Active edges: `0-1, 1-2`. `1-3` inactive.
    - 2 connected to 1, 0.
    - 3 isolated.
    - Not connected. Result -1.
- **Output:** `1`, `-1`. Correct.

## ✅ Proof of Correctness

- **Dynamic Connectivity:** Segment Tree + DSU Rollback correctly maintains connectivity for any time `t`.
- **LCA:** Since `link` only restores edges from the base tree, the path between connected nodes `u, v` is unique and identical to the path in the base tree. Thus, static LCA is valid.

## 💡 Interview Extensions (High-Value Add-ons)

- **Link-Cut Trees:** If `link` could add _any_ edge (changing tree structure), we'd need LCT.
- **Euler Tour Tree:** Another dynamic tree approach.
- **Online:** If queries must be answered online, LCT is required.

### Common Mistakes to Avoid

1.  **Interval Bounds:** `cut` at `i` means edge active up to `i-1`. `link` at `i` means active from `i+1` (or `i` depending on convention, usually next query).
2.  **DSU:** Must use rollback (stack). No path compression (or careful path compression). Rank/Size optimization is crucial for `log N`.
3.  **Base Tree:** Ensure `link` doesn't violate base tree assumption (problem constraints imply this).
