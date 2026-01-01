---
problem_id: GRB_TOPO_SORT_KAHN__7394
display_id: GRB-005
slug: topo-sort-kahn
title: "Topological Sort (Kahn)"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - Topological Sort
  - BFS
tags:
  - graphs-basics
  - topo-sort
  - bfs
  - easy
premium: true
subscription_tier: basic
---

# GRB-005: Topological Sort (Kahn)

## 📋 Problem Summary

You are given a **Directed Acyclic Graph (DAG)**. You need to find a **linear ordering** of its nodes such that for every directed edge `u -> v`, node `u` comes before node `v` in the ordering. This is called a Topological Sort.

## 🌍 Real-World Scenario

**Scenario Title:** University Course Prerequisites

Imagine you are planning your class schedule for college.
-   **Nodes** are courses (e.g., "Intro to CS", "Data Structures", "Algorithms").
-   **Edges** are prerequisites. An edge `Intro -> Data Structures` means you *must* take "Intro" before you can take "Data Structures".
-   **Topological Sort:** This is a valid sequence of taking classes so that you never take a class before its prerequisite. You start with classes that have no prerequisites, finish them, which "unlocks" the next level of classes, and so on.

![Real-World Application](../images/GRB-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
  0 ----> 1
  |       |
  v       v
  2 ----> 3
```
**Edges:** `0->1`, `0->2`, `1->3`, `2->3`

**Indegrees (Incoming Edges):**
-   0: 0 (Start here!)
-   1: 1 (from 0)
-   2: 1 (from 0)
-   3: 2 (from 1, 2)

**Process:**
1.  **Queue:** `[0]` (Indegree 0).
2.  **Pop 0:** Add to result. Remove edges `0->1`, `0->2`.
    -   Indegree of 1 becomes 0. Push 1.
    -   Indegree of 2 becomes 0. Push 2.
    -   Queue: `[1, 2]`
3.  **Pop 1:** Add to result. Remove edge `1->3`.
    -   Indegree of 3 becomes 1.
    -   Queue: `[2]`
4.  **Pop 2:** Add to result. Remove edge `2->3`.
    -   Indegree of 3 becomes 0. Push 3.
    -   Queue: `[3]`
5.  **Pop 3:** Add to result. Queue empty.

**Result:** `0, 1, 2, 3` (or `0, 2, 1, 3`)

### Algorithm Steps (Kahn's Algorithm)

1.  **Calculate Indegrees:** Iterate through all edges. For every edge `u -> v`, increment `indegree[v]`.
2.  **Initialize Queue:** Add all nodes with `indegree == 0` to a queue.
3.  **Process Queue:**
    -   While queue is not empty:
        -   Dequeue node `u`. Add `u` to the result list.
        -   For each neighbor `v` of `u`:
            -   Decrement `indegree[v]`.
            -   If `indegree[v]` becomes 0, enqueue `v`.
4.  **Output:** The result list.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **DAG Guarantee:** The problem states the graph is a DAG, so a solution always exists.
-   **Multiple Solutions:** Any valid topological sort is accepted.
-   **Disconnected Components:** Kahn's algorithm naturally handles disconnected components (it just picks any 0-indegree node from any component).

## Naive Approach

### Intuition

A naive approach might be to use DFS and add nodes to a list *after* visiting all their children (post-order traversal), then reverse the list. This is actually an optimal approach too (DFS-based Topo Sort). However, Kahn's algorithm (BFS-based) is often more intuitive for "unlocking dependencies."

## Optimal Approach (Kahn's Algorithm)

Kahn's algorithm is optimal and iterative. It explicitly models the "dependency resolution" process.

### Time Complexity

-   **O(N + M)**: We visit every node once and process every edge once (decrementing indegrees).

### Space Complexity

-   **O(N + M)**: Adjacency list + Indegree array + Queue.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 2
0 1
1 2
```

**Initialization:**
-   `indegree`: `[0, 1, 1]`
-   `queue`: `[0]`

**Iteration 1:**
-   Pop `0`. Result: `[0]`.
-   Neighbor `1`: `indegree[1]` becomes 0. Push `1`.
-   `queue`: `[1]`

**Iteration 2:**
-   Pop `1`. Result: `[0, 1]`.
-   Neighbor `2`: `indegree[2]` becomes 0. Push `2`.
-   `queue`: `[2]`

**Iteration 3:**
-   Pop `2`. Result: `[0, 1, 2]`.
-   No neighbors.
-   `queue`: `[]`

**Result:** `0 1 2`

## ✅ Proof of Correctness

1.  **Acyclicity:** In a DAG, there must be at least one node with indegree 0.
2.  **Progress:** Removing a node and its edges creates a new DAG with remaining nodes, which again must have a 0-indegree node.
3.  **Completion:** Since we remove one node at a time, we will eventually process all `N` nodes.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Cycle Detection:** If `result.length < n` at the end, the graph has a cycle! This is a common way to detect cycles in directed graphs.
-   **Lexicographically Smallest:** Use a Min-Priority Queue instead of a regular Queue to get the lexicographically smallest topological sort.
-   **Parallel Processing:** Nodes in the queue at the same time can be processed in parallel (e.g., compiling independent files).

### Common Mistakes to Avoid

1.  **Undirected Graphs:** Topological sort is only defined for Directed Acyclic Graphs (DAGs).
2.  **Cycles:** If the graph has a cycle, Kahn's algorithm will output fewer than `N` nodes.
3.  **Queue vs Stack:** Using a stack (DFS) gives a valid order but in reverse (if pushing to stack on finish). Kahn's uses a queue.
