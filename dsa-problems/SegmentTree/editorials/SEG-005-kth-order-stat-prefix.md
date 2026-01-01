---
title: K-th Order Statistic in Prefix
slug: kth-order-stat-prefix
difficulty: Medium
difficulty_score: 57
tags:
- Segment Tree
- Persistent Data Structures
- Order Statistics
problem_id: SEG_KTH_ORDER_STAT_PREFIX__7093
display_id: SEG-005
topics:
- Segment Tree
- Persistent Data Structures
- Order Statistics
---
# K-th Order Statistic in Prefix - Editorial

## Problem Summary

You are given an array `a`. You need to answer queries `PREFIX r k`: find the `k`-th smallest value in the prefix `a[0..r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`
## Real-World Scenario

Imagine a **Sales Performance Dashboard**.
-   You have a stream of sales data coming in over time.
-   A manager wants to know: "What was the median sale amount among the first 1000 transactions?" or "What was the 90th percentile sale in the first month?"
-   This corresponds to finding the `k`-th smallest value in a prefix of the data.

## Problem Exploration

### 1. Naive Approach
For each query `(r, k)`, take `a[0..r]`, sort it, and pick the `k`-th element.
-   Sorting takes `O(r log r)`.
-   Total time: `O(q * n log n)`. Too slow for `n, q = 200,000`.

### 2. Persistent Segment Tree
We can view the prefix `a[0..r]` as a collection of values.
If we build a Segment Tree over the **values** (coordinate compressed), we can find the `k`-th smallest in `O(log (value range))`.
However, we have different prefixes.
A **Persistent Segment Tree** allows us to store the state of the segment tree after inserting each element `a[i]`.
-   `root[i]` represents the segment tree containing values `a[0..i]`.
-   To find the `k`-th smallest in `a[0..r]`, we query `root[r]`.

### 3. Coordinate Compression
Since values can be large (`-10^9` to `10^9`), but `n` is small (`200,000`), we map the distinct values to ranks `0, 1, dots, m-1`.
The segment tree will cover the range `[0, m-1]`.

### 4. Query Logic
In a standard segment tree storing counts of values:
-   Let `cnt` be the number of elements in the left child.
-   If `k <= cnt`, recurse left.
-   Else, recurse right with `k - cnt`.

## Approaches

### Approach 1: Persistent Segment Tree
1.  **Coordinate Compress**: Map values to `0 dots m-1`.
2.  **Build Trees**:
    -   `root[-1]` is an empty tree (all zeros).
    -   For `i` from `0` to `n-1`:
        -   `root[i] = update(root[i-1], compressed_val[i], +1)`
        -   This creates a new version of the tree with count of `val` incremented.
3.  **Query**:
    -   For `PREFIX r k`, call `query(root[r], k)`.
    -   Map the result index back to the original value.

**Complexity**:
-   Build: `O(N log N)`.
-   Query: `O(log N)`.
-   Space: `O(N log N)` nodes.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`4 1`
`5 1 3 2`
`PREFIX 3 2`

1.  **Compression**: Unique sorted: `[1, 2, 3, 5]`. Map: `{1:0, 2:1, 3:2, 5:3}`.
2.  **Build**:
    -   `root[-1]`: Empty.
    -   `root[0]` (add 5 -> idx 3): `{3:1}`.
    -   `root[1]` (add 1 -> idx 0): `{0:1, 3:1}`.
    -   `root[2]` (add 3 -> idx 2): `{0:1, 2:1, 3:1}`.
    -   `root[3]` (add 2 -> idx 1): `{0:1, 1:1, 2:1, 3:1}`.
3.  **Query**: `PREFIX 3 2` (k=2 in `root[3]`).
    -   `root[3]` has counts `[1, 1, 1, 1]` for indices `0, 1, 2, 3`.
    -   Left child (indices 0-1) has count 2.
    -   `k=2 <= 2`. Go left.
    -   Left child (indices 0-1) split to `0` and `1`.
    -   Left child (index 0) has count 1.
    -   `k=2 > 1`. Go right with `k = 2-1 = 1`.
    -   Right child (index 1). Leaf. Return index 1.
4.  **Result**: `unique[1] = 2`.

## Proof of Correctness

-   **Persistence**: `root[r]` correctly represents the frequency array of `a[0..r]`.
-   **Structure**: The segment tree over value ranges allows binary searching for the `k`-th element by counting how many elements fall in the left half.
-   **Space**: Each update adds `log M` nodes, keeping space linear-logarithmic.

## Interview Extensions

1.  **Range [L, R] K-th Smallest?**
    -   Use `root[R]` and `root[L-1]`.
    -   Count in range `[L, R]` is `count(root[R]) - count(root[L-1])`.
    -   This is the standard usage of Persistent Segment Trees (MKTHNUM).
2.  **Dynamic Updates?**
    -   If array changes, Persistent Segment Tree is hard to update. Use **Fenwick Tree of Segment Trees** (or Segment Tree over Fenwick Tree), `O(log^2 N)` per op.

### Common Mistakes

-   **Memory Limit**: Persistent Segment Trees use a lot of memory. In C++, use pointers carefully or static array allocation. In Java/Python, GC handles it but can be slow or OOM.
-   **Coordinate Compression**: Essential when values are large.
-   **Base Cases**: Handle `k=1` or `k=r+1` correctly.
