---
problem_id: GRB_DETECT_CYCLE_DIRECTED__8425
display_id: GRB-006
slug: detect-cycle-directed
title: "Detect Cycle in Directed Graph"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - DFS
  - Cycle Detection
tags:
  - graphs-basics
  - cycle-detection
  - dfs
  - easy
premium: true
subscription_tier: basic
---

# GRB-006: Detect Cycle in Directed Graph

## 📋 Problem Summary

You are given a **Directed Graph**. Determine if it contains at least one cycle. A cycle is a path that starts and ends at the same node, following the direction of edges.

## 🌍 Real-World Scenario

**Scenario Title:** Deadlock Detection

Imagine a computer system with multiple processes and resources.
-   **Nodes** are processes.
-   **Edges** represent waiting. `A -> B` means Process A is waiting for Process B to release a resource.
-   **Cycle:** `A -> B -> C -> A`. A waits for B, B waits for C, and C waits for A. No one can proceed. This is a **Deadlock**.
-   Detecting a cycle in this "Wait-For Graph" is crucial for operating systems to identify and resolve deadlocks.

![Real-World Application](../images/GRB-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
  0 ----> 1
  ^       |
  |       v
  3 <---- 2
```
**DFS Path:**
1.  Start at 0. Mark 0 as **Visiting**.
2.  Go to 1. Mark 1 as **Visiting**.
3.  Go to 2. Mark 2 as **Visiting**.
4.  Go to 3. Mark 3 as **Visiting**.
5.  Edge `3 -> 0`. Node 0 is currently **Visiting**.
    -   **Cycle Detected!** `0 -> 1 -> 2 -> 3 -> 0`.

**No Cycle:**
```
  0 ----> 1
          |
          v
  3 <---- 2
```
1.  Start at 0. Visiting.
2.  Go to 1. Visiting.
3.  Go to 2. Visiting.
4.  Go to 3. Visiting. No neighbors. Mark 3 as **Visited**.
5.  Backtrack to 2. Mark 2 as **Visited**.
6.  Backtrack to 1. Mark 1 as **Visited**.
7.  Backtrack to 0. Mark 0 as **Visited**.
8.  No back-edge found.

### Algorithm Steps (DFS with Colors)

We use 3 colors (states) for each node:
-   **0 (White):** Unvisited.
-   **1 (Gray):** Visiting (currently in the recursion stack).
-   **2 (Black):** Visited (finished processing).

1.  **Iterate:** Loop through all nodes `i` from `0` to `n-1`.
2.  **Launch DFS:** If node `i` is White (0), call `dfs(i)`.
3.  **DFS(u):**
    -   Mark `u` as Gray (1).
    -   For each neighbor `v`:
        -   If `v` is Gray (1): **Cycle Found!** Return `true`.
        -   If `v` is White (0): Recursively call `dfs(v)`. If it returns `true`, propagate `true`.
    -   Mark `u` as Black (2).
    -   Return `false`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Self-loops:** `u -> u` is a cycle of length 1. The algorithm detects this (`u` is Gray, neighbor `u` is Gray).
-   **Disconnected Components:** The outer loop ensures we check all components.
-   **Directed:** `u -> v` is different from `v -> u`. A cycle must follow arrows.

## Naive Approach

### Intuition

For every node, start a DFS and see if you can return to the start node.

### Time Complexity

-   **O(N * (N+M))**: In the worst case, we might traverse the entire graph for each starting node. This is too slow.

## Optimal Approach (DFS with 3 Colors)

By distinguishing between "currently visiting" (Gray) and "completely visited" (Black), we avoid re-processing nodes and detect back-edges efficiently.

### Time Complexity

-   **O(N + M)**: Each node and edge is processed once.

### Space Complexity

-   **O(N)**: Recursion stack and color array.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1
1 2
2 0
```

**Initialization:**
-   `state`: `[0, 0, 0]`

**DFS(0):**
-   `state[0] = 1`. Neighbors: `1`.
-   **DFS(1):**
    -   `state[1] = 1`. Neighbors: `2`.
    -   **DFS(2):**
        -   `state[2] = 1`. Neighbors: `0`.
        -   `state[0]` is 1 (Gray). **Cycle Detected!** Return `true`.
    -   Return `true`.
-   Return `true`.

**Output:** `true`

## ✅ Proof of Correctness

1.  **Cycle Definition:** A cycle exists if and only if there is a back-edge to a node that is currently in the recursion stack (an ancestor in the DFS tree).
2.  **Gray State:** The "Gray" state perfectly captures nodes currently in the recursion stack.
3.  **Completeness:** DFS visits every node and edge. If a cycle exists, the back-edge closing the cycle will be traversed while the start of the cycle is still Gray.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Print Cycle:** Store `parent` pointers. When `v` is Gray, backtrack from `u` to `v` using `parent` array to print the cycle.
-   **Undirected Graph:** For undirected graphs, we just check `v != parent` instead of 3 colors.
-   **Kahn's Algorithm:** Another way to detect cycles. If topological sort processes fewer than `N` nodes, there's a cycle.

### Common Mistakes to Avoid

1.  **Using Boolean Visited:** A simple `visited` boolean is not enough for directed graphs. It can't distinguish between "visited in current path" (cycle) and "visited in a previous path" (cross edge, valid).
2.  **Cross Edges:** `0 -> 1`, `0 -> 2`, `1 -> 2`. When at 1 we visit 2. Later at 0 we visit 2 again. 2 is Black. This is NOT a cycle. The 3-color method handles this correctly (Black is ignored).
