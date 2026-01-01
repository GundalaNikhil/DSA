---
problem_id: GRB_BFS_SHORTEST_PATH_UNWEIGHTED__4821
display_id: GRB-001
slug: bfs-shortest-path-unweighted
title: "BFS Shortest Path in Unweighted Graph"
difficulty: Easy
difficulty_score: 25
topics:
  - Graphs
  - BFS
  - Shortest Path
tags:
  - graphs-basics
  - bfs
  - shortest-path
  - easy
premium: true
subscription_tier: basic
---

# GRB-001: BFS Shortest Path in Unweighted Graph

## 📋 Problem Summary

You are given an undirected, unweighted graph with `n` nodes and `m` edges. You need to find the shortest distance from a starting node `s` to all other nodes. If a node is unreachable, its distance is `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** The "Six Degrees of Separation" Game

Imagine a social network where people are nodes and friendships are edges.
-   **You** are the source node `s`.
-   **Your friends** are 1 step away (distance 1).
-   **Friends of your friends** (who aren't already your friends) are 2 steps away (distance 2).
-   And so on.

The goal is to find out how many "handshakes" away everyone else is from you. If someone is completely disconnected from your social circle, they are unreachable (distance -1). BFS is exactly how social networks suggest "People You May Know" (2nd degree connections) or calculate your "Bacon Number".

![Real-World Application](../images/GRB-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    0 -- 1 -- 2
    |
    3
```
**Source:** 0

**BFS Layers:**
-   **Layer 0:** Node 0 (Distance 0)
-   **Layer 1:** Neighbors of 0 -> Nodes 1, 3 (Distance 1)
-   **Layer 2:** Neighbors of 1 -> Node 2 (Distance 2). (3 is already visited).

**Result:**
-   0: 0
-   1: 1
-   2: 2
-   3: 1

### Algorithm Steps

1.  **Adjacency List:** Convert the input edge list into an adjacency list `adj` where `adj[u]` contains all neighbors of `u`.
2.  **Queue & Distance Array:**
    -   Create a `queue` for BFS and add the source `s`.
    -   Create a `dist` array of size `n`, initialized to `-1` (to mark unvisited).
    -   Set `dist[s] = 0`.
3.  **BFS Loop:**
    -   While the queue is not empty:
        -   Dequeue the current node `u`.
        -   For each neighbor `v` of `u`:
            -   If `dist[v] == -1` (unvisited):
                -   Set `dist[v] = dist[u] + 1`.
                -   Enqueue `v`.
4.  **Output:** Return the `dist` array.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Graph Type:** Undirected. If `u-v` is an edge, you can go `u->v` and `v->u`.
-   **Unweighted:** All edges have weight 1.
-   **Disconnected Components:** Nodes not reachable from `s` will remain `-1` in the `dist` array, which matches the required output.
-   **Self-loops/Multi-edges:** Constraints say they don't exist, so no need to handle them specifically.

## Naive Approach

### Intuition

A naive approach might be to use DFS (Depth First Search) to find paths. However, DFS does **not** guarantee the shortest path in an unweighted graph. It might go deep down a long path before finding a shorter one. To make DFS work, you'd have to explore *all* paths and keep the minimum length found, which is exponential in time complexity.

### Time Complexity

-   **Exponential**: O(N!) in the worst case for finding shortest paths via exhaustive DFS.

## Optimal Approach (BFS)

Breadth-First Search (BFS) explores the graph layer by layer. It visits all nodes at distance 1, then all at distance 2, etc. The first time BFS reaches a node, it is guaranteed to be via the shortest path.

### Algorithm

1.  Initialize `dist` array with `-1`.
2.  `dist[s] = 0`, `queue.push(s)`.
3.  While `queue` not empty:
    -   `u = queue.pop()`.
    -   For `v` in `adj[u]`:
        -   If `dist[v] == -1`:
            -   `dist[v] = dist[u] + 1`
            -   `queue.push(v)`

### Time Complexity

-   **O(N + M)**: We visit every node once and process every edge once (twice in undirected graph).

### Space Complexity

-   **O(N + M)**: To store the adjacency list and the distance array/queue.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 3 0
0 1
1 2
0 3
```

**Initialization:**
-   `n=4`, `s=0`
-   `adj`: `0:[1,3], 1:[0,2], 2:[1], 3:[0]`
-   `dist`: `[-1, -1, -1, -1]`
-   `queue`: `[0]`
-   `dist[0] = 0` -> `[0, -1, -1, -1]`

**Iteration 1:**
-   Pop `0`. Neighbors: `1, 3`.
-   Visit `1`: `dist[1] = 0 + 1 = 1`. Queue: `[1]`.
-   Visit `3`: `dist[3] = 0 + 1 = 1`. Queue: `[1, 3]`.
-   `dist`: `[0, 1, -1, 1]`

**Iteration 2:**
-   Pop `1`. Neighbors: `0, 2`.
-   `0` visited.
-   Visit `2`: `dist[2] = 1 + 1 = 2`. Queue: `[3, 2]`.
-   `dist`: `[0, 1, 2, 1]`

**Iteration 3:**
-   Pop `3`. Neighbors: `0`.
-   `0` visited. Queue: `[2]`.

**Iteration 4:**
-   Pop `2`. Neighbors: `1`.
-   `1` visited. Queue: `[]`.

**Result:** `0 1 2 1`

## ✅ Proof of Correctness

BFS guarantees finding the shortest path in unweighted graphs because:
1.  It explores nodes in increasing order of their distance from the source (layer by layer).
2.  The first time a node is visited, it is reached via the minimum number of edges possible.
3.  Since edge weights are uniform (1), minimum edges = minimum distance.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Path Reconstruction:** How would you print the actual path? (Store `parent` pointers).
-   **0-1 BFS:** What if edges have weights 0 or 1? (Use Deque).
-   **Multi-Source BFS:** Find shortest distance from *any* of multiple sources (Initialize queue with all sources).

### Common Mistakes to Avoid

1.  **Not marking visited:** Forgetting to check `if dist[v] == -1` leads to infinite loops in cyclic graphs.
2.  **Using DFS:** DFS does not guarantee shortest paths in unweighted graphs.
3.  **Queue Operations:** In JavaScript/Python, using `shift()` or `pop(0)` is O(N), making BFS O(N^2). Use a pointer or `deque`.
