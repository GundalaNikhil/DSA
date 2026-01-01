---
problem_id: TRE_SEMINAR_LEVEL_ORDER_ODD__5168
display_id: TRE-004
slug: seminar-level-order-odd
title: "Seminar Level Order Odd-Depth Only"
difficulty: Easy
difficulty_score: 26
topics:
  - Trees
  - BFS
  - Level Order
tags:
  - trees
  - bfs
  - traversal
  - easy
premium: true
subscription_tier: basic
---

# TRE-004: Seminar Level Order Odd-Depth Only

## 📋 Problem Summary

Perform a **level-order traversal** (BFS) of a binary tree, but only output the values of nodes located at **odd depths**. The root is considered to be at depth 0. For each odd depth, print the node values in a single line, from left to right.

## 🌍 Real-World Scenario

**Scenario Title:** University Course Prerequisites

Imagine a university curriculum structured as a tree.
-   **Depth 0 (Root):** "Intro to CS" (Freshman Fall).
-   **Depth 1:** "Data Structures", "Algorithms" (Freshman Spring).
-   **Depth 2:** "OS", "Networks" (Sophomore Fall).
-   **Depth 3:** "Distributed Systems", "AI" (Sophomore Spring).

The university wants to schedule seminars specifically for the Spring semester courses (which happen to be at odd depths 1, 3, etc.). By filtering the tree traversal to only odd depths, you can generate the list of courses that need seminar rooms for the Spring term.

![Real-World Application](../images/TRE-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      10 (Depth 0)
     /  \
    5    12 (Depth 1)
   /
  7 (Depth 2)
```
**Levels:**
-   **Depth 0:** [10] -> Even. Skip.
-   **Depth 1:** [5, 12] -> Odd. **Output**.
-   **Depth 2:** [7] -> Even. Skip.

**Output:**
```
5 12
```

### Algorithm Steps

1.  Use a **Queue** for Breadth-First Search (BFS).
2.  Start with the root at `depth = 0`.
3.  While the queue is not empty:
    -   Get the number of nodes at the current level (`size`).
    -   Initialize a list for the current level's values.
    -   Process `size` nodes:
        -   Add children to the queue.
        -   Add value to the list.
    -   If `depth % 2 != 0`, print/store the list.
    -   Increment `depth`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Root Depth:** 0 (Even).
-   **Empty Tree:** Output nothing (or a blank line depending on specific constraints, here blank line).
-   **Order:** Left-to-right is preserved by standard queue-based BFS.

## Naive Approach

### Intuition

We can traverse the tree using DFS (Preorder) and store nodes in a list of lists `levels[depth]`. After traversing the whole tree, we iterate through `levels` and print only those at odd indices.

### Algorithm

1.  `levels = []`.
2.  `dfs(node, depth)`:
    -   If `depth >= levels.size()`, add new list.
    -   `levels[depth].add(node.val)`.
    -   `dfs(left, depth + 1)`.
    -   `dfs(right, depth + 1)`.
3.  Print `levels[1], levels[3], ...`.

### Time Complexity

-   **O(N)**: Visit every node.

### Space Complexity

-   **O(N)**: To store all node values in the list of lists.

## Optimal Approach (BFS)

BFS is more natural for level-order problems. We can process level by level and discard the values immediately after printing, saving space compared to storing everything (though we still need the queue).

### Algorithm

1.  If `n=0`, return empty.
2.  Queue `q`, add `0`. `depth = 0`.
3.  Loop while `q` not empty:
    -   `count = q.size()`.
    -   `currentLevelNodes = []`.
    -   Loop `count` times:
        -   `u = q.poll()`.
        -   If `depth % 2 != 0`, add `values[u]` to `currentLevelNodes`.
        -   Add children of `u` to `q`.
    -   If `currentLevelNodes` is not empty, add to result.
    -   `depth++`.

### Time Complexity

-   **O(N)**: Each node processed once.

### Space Complexity

-   **O(W)**: Max width of tree (queue size).

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
10 1 2
5 3 -1
12 -1 -1
7 -1 -1
```

**Execution:**
1.  `q = [0]`, `depth = 0`.
2.  **Level 0 (Even):**
    -   Pop 0 (10). Push 1 (5), 2 (12).
    -   `isOdd = false`. Do not add 10.
    -   `q = [1, 2]`.
3.  **Level 1 (Odd):**
    -   Pop 1 (5). Push 3 (7). Add 5 to list.
    -   Pop 2 (12). No children. Add 12 to list.
    -   `isOdd = true`. List: `[5, 12]`. Add to result.
    -   `q = [3]`.
4.  **Level 2 (Even):**
    -   Pop 3 (7). No children.
    -   `isOdd = false`. Do not add 7.
    -   `q = []`.
5.  End.

**Output:** `5 12`. Correct.

## ✅ Proof of Correctness

The BFS algorithm guarantees that nodes are visited level by level, and within each level, from left to right (assuming children are enqueued left then right).
By maintaining a `depth` counter and checking `depth % 2 != 0`, we strictly filter for odd levels.
The queue ensures that we process all nodes at depth `d` before any node at depth `d+1`.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Zigzag Traversal**
    -   Print odd levels left-to-right, even levels right-to-left.
-   **Extension 2: Average of Levels**
    -   Compute average value of nodes at each level.
-   **Extension 3: Connect Next Pointers**
    -   Populate a `next` pointer for each node pointing to its right neighbor in the same level.

### Common Mistakes to Avoid

1.  **Depth Indexing:**
    -   ❌ Assuming root is depth 1.
    -   ✅ Problem states root is depth 0.
2.  **Queue Size Loop:**
    -   ❌ `for (int i=0; i<q.size(); i++)` inside while loop. `q.size()` changes!
    -   ✅ Capture `size = q.size()` before the loop.

## Related Concepts

-   **BFS**
-   **Queue Data Structure**
-   **Tree Depth vs Height**
