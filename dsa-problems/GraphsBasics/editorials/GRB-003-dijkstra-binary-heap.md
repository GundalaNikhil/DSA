---
problem_id: GRB_DIJKSTRA_BINARY_HEAP__6041
display_id: GRB-003
slug: dijkstra-binary-heap
title: "Dijkstra with Binary Heap"
difficulty: Medium
difficulty_score: 45
topics:
  - Graphs
  - Dijkstra
  - Shortest Path
tags:
  - graphs-basics
  - dijkstra
  - shortest-path
  - medium
premium: true
subscription_tier: basic
---

# GRB-003: Dijkstra with Binary Heap

## 📋 Problem Summary

You are given a directed graph with **non-negative** edge weights. Find the shortest path distance from a source node `s` to all other nodes. If a node is unreachable, the distance is `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** GPS Navigation

Imagine you are driving from your home (source `s`) to various destinations in a city.
-   **Intersections** are nodes.
-   **Roads** are edges.
-   **Traffic/Time** is the edge weight (cost).
-   Some roads are one-way (directed).

You want to find the fastest route to every other location. Unlike the "Six Degrees" game (BFS), roads have different travel times. A short road with heavy traffic (high weight) might be slower than a longer, empty highway (low weight). Dijkstra's algorithm helps your GPS find the path with the minimum total travel time.

![Real-World Application](../images/GRB-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (1)
  0 ------> 1
  |         |
  | (5)     | (2)
  v         v
  2 <------ 3
      (1)
```
**Source:** 0

**Steps:**
1.  **Start at 0:** Dist to 0 is 0. Push `(0, 0)` to Min-Heap.
2.  **Pop (0, 0):** Neighbors:
    -   1: Cost `0 + 1 = 1`. Push `(1, 1)`.
    -   2: Cost `0 + 5 = 5`. Push `(5, 2)`.
3.  **Pop (1, 1):** Neighbors:
    -   3: Cost `1 + 2 = 3`. Push `(3, 3)`.
4.  **Pop (3, 3):** Neighbors:
    -   2: Cost `3 + 1 = 4`.
    -   Current dist to 2 is 5. `4 < 5`, so update dist to 2. Push `(4, 2)`.
5.  **Pop (4, 2):** No neighbors.
6.  **Pop (5, 2):** Old entry for node 2. `5 > 4` (current best). Ignore.

**Result:** `0:0, 1:1, 2:4, 3:3`

### Algorithm Steps

1.  **Initialization:**
    -   `dist` array initialized to Infinity (`-1` for unreachable in output).
    -   `dist[s] = 0`.
    -   Min-Heap (Priority Queue) storing pairs `(distance, node)`. Push `(0, s)`.
2.  **Processing:**
    -   While heap is not empty:
        -   Pop the element with the smallest distance: `(d, u)`.
        -   **Lazy Deletion Check:** If `d > dist[u]`, this is an outdated entry. Continue/Skip.
        -   For each neighbor `v` of `u` with weight `w`:
            -   If `dist[u] + w < dist[v]`:
                -   `dist[v] = dist[u] + w`
                -   Push `(dist[v], v)` to heap.
3.  **Output:** Convert Infinity to `-1` if necessary and return.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Weights:** Non-negative. This is crucial for Dijkstra.
-   **Large Distances:** Sum of weights can exceed 2^31-1. Use 64-bit integers (`long` in Java/C++, `Number` is safe in JS up to 2^53).
-   **Unreachable:** Output `-1`.

## Naive Approach

### Intuition

We could use a simple array to find the minimum distance node at each step instead of a heap.

### Time Complexity

-   **O(N^2)**: Finding the minimum distance node takes O(N), and we do this N times. This is fine for dense graphs but slow for sparse ones (large N, small M).

## Optimal Approach (Binary Heap)

Using a Min-Heap allows us to extract the closest node in O(log N) time.

### Algorithm

(Described in "Algorithm Steps" above).

### Time Complexity

-   **O(M log N)**: Each edge is processed once, potentially adding an entry to the heap. Heap operations take O(log N).

### Space Complexity

-   **O(N + M)**: Adjacency list + Heap + Distance array.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3 0
0 1 1
1 2 2
0 2 5
```

**Initialization:**
-   `dist`: `[0, -1, -1]`
-   `pq`: `[(0, 0)]`

**Step 1:**
-   Pop `(0, 0)`. Neighbors: `1 (w=1)`, `2 (w=5)`.
-   Update `dist[1] = 1`. Push `(1, 1)`.
-   Update `dist[2] = 5`. Push `(5, 2)`.
-   `pq`: `[(1, 1), (5, 2)]`

**Step 2:**
-   Pop `(1, 1)`. Neighbors: `2 (w=2)`.
-   New path to 2: `dist[1] + 2 = 1 + 2 = 3`.
-   `3 < 5` (current `dist[2]`). Update `dist[2] = 3`. Push `(3, 2)`.
-   `pq`: `[(3, 2), (5, 2)]` (Note: `(5, 2)` is now outdated).

**Step 3:**
-   Pop `(3, 2)`. Neighbors: None.

**Step 4:**
-   Pop `(5, 2)`. `dist[2]` is 3. `5 > 3`. Ignore.

**Result:** `0 1 3`

## ✅ Proof of Correctness

Dijkstra's greedy strategy works because:
1.  We always process the closest unvisited node.
2.  Since weights are non-negative, extending a path can never reduce its total weight.
3.  Therefore, once we extract a node from the heap, we have found the absolute shortest path to it.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Path Restoration:** Store `parent[v] = u` when relaxing edges to reconstruct the path.
-   **Dense Graphs:** For dense graphs (M ≈ N^2), the O(N^2) array implementation is actually faster than O(M log N) heap implementation.
-   **Negative Weights:** Dijkstra fails. Use Bellman-Ford.

### Common Mistakes to Avoid

1.  **Negative Edges:** Dijkstra loops infinitely or gives wrong answers with negative weights.
2.  **Visited Array:** Standard Dijkstra doesn't use a simple boolean `visited` array like BFS. It uses the distance check `d > dist[u]` to handle re-visits/updates.
3.  **Integer Overflow:** Edge weights can sum up to > 2 billion. Use `long long` in C++ / `long` in Java.
