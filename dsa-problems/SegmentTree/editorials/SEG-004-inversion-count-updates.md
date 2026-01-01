---
title: Inversion Count Updates
slug: inversion-count-updates
difficulty: Medium
difficulty_score: 58
tags:
- Inversion Count
- Fenwick Tree
- Segment Tree
problem_id: SEG_INVERSION_COUNT_UPDATES__5048
display_id: SEG-004
topics:
- Segment Tree
- Fenwick Tree
- Inversions
---
# Inversion Count Updates - Editorial

## Problem Summary

You are given an array `a`. You need to process `q` updates. Each update changes the value at a specific index `i` to `x`. After each update, you must output the total number of inversions in the array. An inversion is a pair `(i, j)` such that `i < j` and `a[i] > a[j]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Ranking System**. You have a list of players ranked by their current score. An "inversion" represents a pair of players where the one listed earlier actually has a higher score (if the list is supposed to be ascending) or vice-versa. When a player's score changes, you want to know how "unsorted" the list has become without re-scanning everyone.

## Problem Exploration

### 1. Naive Approach
After each update, recalculate inversions in `O(N^2)` or `O(N log N)`. With `Q` updates, this is `O(Q * N log N)`, which is too slow given `N, Q <= 200,000`.

### 2. Incremental Updates
When we change `a[i]` from `old_val` to `new_val`, how does the inversion count change?
Only pairs involving index `i` are affected.
-   **Pairs (j, i) where j < i**:
    -   If `a[j] > old_val`, we lose an inversion.
    -   If `a[j] > new_val`, we gain an inversion.
-   **Pairs (i, k) where i < k**:
    -   If `old_val > a[k]`, we lose an inversion.
    -   If `new_val > a[k]`, we gain an inversion.

So, `new_inversions = old_inversions - (inversions involving old a[i]) + (inversions involving new a[i])`.

### 3. Calculating Affected Inversions
To efficiently count `j < i` with `a[j] > val` or `k > i` with `val > a[k]`, we can use a data structure.
However, standard Fenwick/Segment trees count values in a range.
This problem is tricky because we need to count values *by index* and *by value*.
This looks like a 2D range query problem, or we can use **Square Root Decomposition** (Block Decomposition).
Can we do better? `O(Q log^2 N)`?
1.  Count `j < i` such that `a[j] > val`.
2.  Count `k > i` such that `a[k] < val`.
This requires a data structure that supports:
-   `update(index, val)`
-   `query_greater(index_range, value)`
-   `query_smaller(index_range, value)`

This is exactly what a **Merge Sort Tree** or **Segment Tree over Fenwick Tree** supports, but updates are hard.
Divide array into blocks of size `sqrtN`.
For each block, maintain a sorted version of its elements.
Update:
-   Remove `old_val` from block's sorted list.
-   Insert `new_val`.
-   This takes `O(sqrtN)`.
Query:
-   For blocks fully to left/right: binary search in sorted list (`O(log sqrtN)`).
-   For partial blocks: iterate (`O(sqrtN)`).
Total per update: `O(sqrtN log N)`. With `N=200,000`, `sqrtN ~= 450`. `450 x 18 ~= 8000`. `200,000 x 8000 ~= 1.6 x 10^9`. Might be tight for 2 seconds.

**Alternative approaches:**
- Coordinate Compression + Fenwick Tree would maintain frequencies of values but loses index information.
- Fenwick Tree over indices would maintain values but cannot efficiently count by value ranges.

For "Medium" difficulty with values up to `10^9` and 0-based indices, **Square Root Decomposition** (Block Decomposition) achieves `O(Q sqrtN log N)` complexity.

The key insight: count `j < i` with `a[j] > x` is essentially a 2D range sum query - counting points in rectangle `[0, i-1] x [x+1, infinity]`. While dynamic 2D range sums are complex, Square Root Decomposition provides an efficient solution for this difficulty level.

Let's refine the Square Root Decomposition approach.
Block size `B ~= sqrtN log N` or just `sqrtN`.
Maintain `blocks[b]` as a sorted list of values in that block.
To update `a[i]` from `u` to `v`:
1.  Calculate contribution of `u` to inversions (remove it).
    -   Iterate blocks to left: count elements `> u`.
    -   Iterate blocks to right: count elements `< u`.
    -   Iterate within `i`'s block: brute force.
2.  Update `a[i] = v`. Update block's sorted list.
3.  Calculate contribution of `v` to inversions (add it).
    -   Iterate blocks to left: count elements `> v`.
    -   Iterate blocks to right: count elements `< v`.
    -   Iterate within `i`'s block: brute force.

Complexity: `O(fracNB log B + B)`.
If `B = sqrtN log N`, this is efficient.
For `N=200,000`, `B ~= 1000`.
Operations: `200 x 10 + 1000 ~= 3000`.
`200,000 x 3000 = 6 x 10^8`.
This should pass in C++/Java. Python might struggle.

## Approaches

### Approach 1: Square Root Decomposition
1.  Divide array into blocks of size `K`.
2.  For each block, keep a sorted version `sorted_blocks[b]`.
3.  **Initial Inversions**: Compute using Fenwick Tree (`O(N log N)`).
4.  **Update(i, x)**:
    -   Let `old = a[i]`.
    -   **Subtract** inversions caused by `old` at `i`.
        -   Left blocks: `count > old`. (Binary search in sorted blocks).
        -   Right blocks: `count < old`.
        -   Same block: iterate elements.
    -   **Update** `a[i] = x`. Update `sorted_blocks[i/K]`.
    -   **Add** inversions caused by `x` at `i`.
        -   Left blocks: `count > x`.
        -   Right blocks: `count < x`.
        -   Same block: iterate elements.
    -   Update total count.

### Approach 2: Fenwick Tree (Offline)
If we process queries offline, we can use CDQ Divide and Conquer, but that's for static 2D range sums or batch updates. Here updates are dependent.
So Square Root Decomposition is the most viable online approach.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`3 1 2`
`SET 1 4`

1.  **Initial**: `[3, 1, 2]`. Inversions: `(3,1), (3,2)`. Count = 2.
2.  **Update**: `a[1]` changes `1 -> 4`.
    -   Remove `1` at index 1.
        -   Left `[3]`: `3 > 1`. Inversions -1.
        -   Right `[2]`: `2 < 1` (False).
        -   Count becomes 1.
    -   Insert `4` at index 1.
        -   Left `[3]`: `3 > 4` (False).
        -   Right `[2]`: `2 < 4` (True). Inversions +1.
        -   Count becomes 2.
3.  **Result**: 2.
    -   Array `[3, 4, 2]`. Inversions `(3,2), (4,2)`. Correct.

## Proof of Correctness

-   **Decomposition**: By splitting into blocks, we balance the cost of updating (small block size) and querying (few blocks).
-   **Counting**: We correctly identify all pairs `(j, i)` and `(i, k)` that form inversions with the updated index `i`.
-   **Sorted Blocks**: Allows `O(log B)` counting for full blocks.

## Interview Extensions

1.  **Range Updates?**
    -   Much harder. Requires Segment Tree Beats or advanced techniques.
2.  **Small Values (`A[i] <= N`)?**

### Common Mistakes

-   **Block Size**: Too small = slow query. Too large = slow update. `sqrtN log N` is a good balance.
-   **Binary Search**: `upper_bound` vs `lower_bound`.
    -   Count `> x`: `size - upper_bound`.
    -   Count `< x`: `lower_bound`.
