---
problem_id: GRB_DSU_BASICS__1728
display_id: GRB-012
slug: dsu-basics
title: "Disjoint Set Union Basics"
difficulty: Easy
difficulty_score: 30
topics:
  - Graphs
  - DSU
  - Connectivity
tags:
  - graphs-basics
  - dsu
  - connectivity
  - easy
premium: true
subscription_tier: basic
---

# GRB-012: Disjoint Set Union Basics

## 📋 Problem Summary

You are managing `N` elements, initially in separate sets. You need to process `Q` queries:
1.  **Union(u, v):** Merge the set containing `u` and the set containing `v`.
2.  **Find(u, v):** Check if `u` and `v` are currently in the same set.

## 🌍 Real-World Scenario

**Scenario Title:** Social Network Friendships

Imagine a social network where friendship is transitive (if A is friends with B, and B is friends with C, then A is connected to C).
-   **Nodes** are people.
-   **Union(u, v):** Person `u` and Person `v` become friends. This merges their entire friend circles.
-   **Find(u, v):** Check if Person `u` and Person `v` are connected (can they see each other's posts?).

As millions of friendships are formed, we need an ultra-fast way to check connectivity.

![Real-World Application](../images/GRB-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Initial State:**
`{0}, {1}, {2}, {3}`

**Query: Union(0, 1)**
-   Merge sets `{0}` and `{1}`.
-   State: `{0, 1}, {2}, {3}`.
-   Tree: `1 -> 0` (1 points to 0).

**Query: Union(2, 3)**
-   Merge `{2}` and `{3}`.
-   State: `{0, 1}, {2, 3}`.
-   Tree: `3 -> 2`.

**Query: Union(1, 3)**
-   Find root of 1 -> `0`.
-   Find root of 3 -> `2`.
-   Merge roots `0` and `2`.
-   State: `{0, 1, 2, 3}`.
-   Tree: `2 -> 0` (2 points to 0). Structure: `1->0`, `3->2->0`.

**Query: Find(1, 3)**
-   Root(1) is 0.
-   Root(3) is 0.
-   Same root -> **True**.

### Algorithm Steps (DSU with Optimizations)

1.  **Data Structure:** Array `parent` where `parent[i]` is the parent of node `i`. Initially `parent[i] = i`.
2.  **Find(i):** Returns the representative (root) of the set containing `i`.
    -   **Path Compression:** As we traverse up to the root, point every node on the path directly to the root. This flattens the tree.
3.  **Union(i, j):**
    -   Find roots: `rootI = Find(i)`, `rootJ = Find(j)`.
    -   If `rootI != rootJ`:
        -   **Union by Rank/Size:** Attach the shorter tree to the taller tree to keep height small.
        -   `parent[rootI] = rootJ`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Output:** Only print for `find` queries.
-   **Dynamic:** Queries are processed online (one by one).

## Naive Approach

### Intuition

Use an array `id[i]` storing the set ID for each node.
-   **Find:** Check if `id[u] == id[v]`. O(1).
-   **Union:** To merge sets ID `A` and `B`, iterate through ALL nodes. If `id[k] == A`, change it to `B`. O(N).

### Time Complexity

-   **O(N * Q)**: Too slow for N, Q = 200,000.

## Optimal Approach (DSU with Path Compression & Union by Rank)

This is the standard efficient solution.

### Time Complexity

-   **O(Q * α(N))**: `α` is the Inverse Ackermann function, which is nearly constant (≤ 4 for all practical inputs).

### Space Complexity

-   **O(N)**: To store parent and rank arrays.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 3
union 0 1
union 2 3
find 0 3
```

**Initialization:**
-   `parent`: `[0, 1, 2, 3]`

**Query 1: union 0 1**
-   `find(0)=0`, `find(1)=1`.
-   `union(0, 1)`. `parent[0]=1`.
-   `parent`: `[1, 1, 2, 3]`

**Query 2: union 2 3**
-   `find(2)=2`, `find(3)=3`.
-   `union(2, 3)`. `parent[2]=3`.
-   `parent`: `[1, 1, 3, 3]`

**Query 3: find 0 3**
-   `find(0)` -> parent is 1 -> parent is 1. Root 1.
-   `find(3)` -> parent is 3. Root 3.
-   `1 != 3`. Return `false`.

**Output:** `false`

## ✅ Proof of Correctness

DSU correctly maintains connected components.
-   **Reflexivity:** `find(i) == find(i)` is always true.
-   **Symmetry:** `union(i, j)` makes `find(i) == find(j)`.
-   **Transitivity:** `union(i, j)` and `union(j, k)` implies `find(i) == find(k)`.
Path compression ensures that future queries are extremely fast by flattening the structure.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Component Size:** Modify `union` to track the size of each set.
-   **Number of Components:** Track a global counter `count`, decrement on every successful union.
-   **Rollback DSU:** Implement DSU that supports "undoing" the last union (useful for some advanced algorithms, requires no path compression).

### Common Mistakes to Avoid

1.  **Missing Path Compression:** Without it, complexity degrades to O(N) per query.
2.  **Confusing Parent with Root:** Always call `find()` to get the root before comparing or merging. `parent[i]` might not be the root.
3.  **Union Logic:** Ensure you attach the *root* of one tree to the *root* of the other, not the nodes themselves.
