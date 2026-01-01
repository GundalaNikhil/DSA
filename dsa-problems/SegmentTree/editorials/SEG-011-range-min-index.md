---
title: Range Minimum Index
slug: range-min-index
difficulty: Medium
difficulty_score: 45
tags:
- Segment Tree
- Range Minimum Query
- Tie Breaking
problem_id: SEG_RANGE_MIN_INDEX__3926
display_id: SEG-011
topics:
- Segment Tree
- Range Queries
- Tie Breaking
---
# Range Minimum Index - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SET i x**: Update `a[i] = x`.
2.  **MINIDX l r**: Find the index of the minimum value in `a[l..r]`. If there are ties, return the smallest index.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Task Scheduler**.
-   You have a list of servers, each with a current load.
-   You want to assign a new task to the server with the **minimum load**.
-   If multiple servers have the same minimum load, you pick the one with the lowest ID (index) to maintain a consistent tie-breaking rule.
-   Server loads change dynamically as tasks finish or start.

## Problem Exploration

### 1. Standard RMQ
Standard Range Minimum Query (RMQ) returns the minimum *value*.
Here we need the *index*.
We can store pairs `(value, index)` in the Segment Tree nodes.

### 2. Merge Logic
When merging two nodes `left` and `right`:
-   If `left.value < right.value`: result is `left`.
-   If `right.value < left.value`: result is `right`.
-   If `left.value == right.value`: result is `left` (since `left.index < right.index`).

### 3. Segment Tree Structure
-   Leaf `i`: stores `(a[i], i)`.
-   Internal Node: stores `min(left, right)` based on the comparison logic above.
-   Query: Standard range query returning the best pair.

## Approaches

### Approach 1: Segment Tree with Pairs
-   **Build**: `O(N)`.
-   **Update**: `O(log N)`.
-   **Query**: `O(log N)`.
-   Space: `O(N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`4 2 2`
`MINIDX 0 2`

1.  **Build**:
    -   Leaves: `(4, 0)`, `(2, 1)`, `(2, 2)`.
    -   Root merges `(2, 1)` and `(2, 2)`.
    -   Values equal (2 == 2). Indices 1 < 2. Pick `(2, 1)`.
2.  **Query**: `MINIDX 0 2`.
    -   Returns `(2, 1)`.
3.  **Result**: 1.

## Proof of Correctness

-   **Merge Logic**: Correctly implements strict inequality for values and tie-breaking with indices.
-   **Segment Tree**: Standard structure guarantees `O(log N)` operations.

## Interview Extensions

1.  **Range Max Index?**
    -   Same logic, just flip comparison.
2.  **K-th Smallest Index?**
    -   Harder. Requires Merge Sort Tree or Persistent Segment Tree.
3.  **First Element < X?**
    -   Segment Tree Walk. Check if `min(left) < X`. If so, go left, else go right.

### Common Mistakes

-   **Tie-Breaking**: Forgetting to check indices when values are equal.
-   **Infinity**: Use a sufficiently large value for out-of-bounds queries.
