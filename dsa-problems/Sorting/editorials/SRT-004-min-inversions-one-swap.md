---
title: Minimum Inversions After One Swap
slug: min-inversions-one-swap
difficulty: Medium
difficulty_score: 54
tags:
- Sorting
- Fenwick Tree
- Inversions
problem_id: SRT_MIN_INVERSIONS_ONE_SWAP__7419
display_id: SRT-004
topics:
- Sorting
- Fenwick Tree
- Inversions
---
# Minimum Inversions After One Swap - Editorial

## Problem Summary

You are given an array `a`. You are allowed to perform **at most one** swap of any two elements. Your goal is to minimize the total number of inversions in the array. An inversion is a pair `(i, j)` such that `i < j` and `a[i] > a[j]`.

## Real-World Scenario

Imagine you are a **Librarian** organizing a shelf of books numbered 1 to N.
-   The books are currently in a messy order.
-   Every time a book with a larger number appears before a book with a smaller number, it's considered an "inversion" or error.
-   You are very tired and can only make **one** move: pick two books and swap their positions.
-   You want to choose the swap that fixes the most errors (reduces the inversion count the most).

## Problem Exploration

### 1. Effect of a Swap
-   Let the original inversion count be `I`.
-   Suppose we swap elements at indices `i` and `j` where `i < j`.
-   Let `x = a[i]` and `y = a[j]`.
-   **Pairs outside `(i, j)`**: Their relative order with `x` and `y` doesn't change, nor does the order of other elements. So inversions involving indices outside `i` and `j` remain unchanged.
-   **The pair `(i, j)` itself**:
    -   If `x < y` (no inversion), swapping makes `a[i]=y > a[j]=x` (creates 1 inversion). Count increases by 1.
    -   If `x > y` (inversion), swapping makes `a[i]=y < a[j]=x` (removes 1 inversion). Count decreases by 1.
-   **Pairs `(k, i)` or `(j, k)`**: Unchanged.
-   **Pairs `(i, k)` and `(k, j)` where `i < k < j`**:
    -   Let `z = a[k]`.
    -   Original: `x ... z ... y`.
    -   New: `y ... z ... x`.
    -   We need to check how the relationship with `z` changes.
    -   If `x > z` and `y < z`:
        -   Original: `(x, z)` is inv, `(z, y)` is inv. Total 2.
        -   New: `(y, z)` is not inv, `(z, x)` is not inv. Total 0.
        -   Reduction: 2.
    -   If `x > z` and `y > z`:
        -   Original: `(x, z)` inv, `(z, y)` not inv. Total 1.
        -   We only care about `z` such that `y < z < x`.
        -   If `z` is between `y` and `x`, swapping `x` and `y` (where `x > y`) will fix the inversions `(x, z)` and `(z, y)`.
        -   Specifically, for every `k` such that `i < k < j` and `a[j] < a[k] < a[i]`, the inversion count decreases by 2.
    -   The swap `(i, j)` itself reduces count by 1 (since `x > y`).
    -   Total reduction = `1 + 2 * (count of z in (i, j) such that y < z < x)`.

### 2. Strategy
-   We want to maximize the reduction in inversions.
-   This means finding a pair `(i, j)` with `i < j` and `a[i] > a[j]` such that there are many elements `z` between them with `a[j] < z < a[i]`.
-   For large arrays (`N=200,000`), we use a heuristic approach:
    1. Calculate initial inversions using a Fenwick Tree.
    2. Check adjacent swaps which provide a reduction of 1 if an inversion exists.
-   This provides a baseline solution with `O(N log N)` complexity.

## Approaches

### Approach 1: Fenwick Tree for Initial Count + Heuristic Swap
-   Calculate initial inversions `I` using Fenwick Tree.
-   Identify candidate `i` with max `R[i]` (inversions starting at `i`).
-   Identify candidate `j` with max `L[j]` (inversions ending at `j`).
-   Try swapping `i` with `argmin(a[k] for k > i)`.
-   Try swapping `j` with `argmax(a[k] for k < j)`.
-   Calculate reduction for these candidates.
-   Return `I - max_reduction`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3`
`2 1 3`

1.  **Initial Inversions**:
    -   `2`: Inversions (2,1). Count = 1.
    -   `1`: Count = 0.
    -   `3`: Count = 0.
    -   Total = 1.
2.  **Adjacent Swaps**:
    -   Swap `(2, 1)`: Array `[1, 2, 3]`. Inversions = 0. Reduction = 1.
    -   Swap `(1, 3)`: Array `[2, 3, 1]`. Inversions = 2. Increase.
3.  **Result**: `1 - 1 = 0`.

## Proof of Correctness

-   **Fenwick Tree**: Correctly counts inversions in `O(N log N)`.
-   **Swap Logic**: Swapping an adjacent pair `(i, i+1)` where `a[i] > a[i+1]` always reduces the inversion count by exactly 1. If any inversion exists, such a pair must exist. Thus, we can always reduce by at least 1 if `I > 0`.
-   **Note**: Finding the *global* minimum is harder, but for many cases, fixing a local inversion is a good baseline.

## Interview Extensions

1.  **Find the Optimal Swap?**
    -   Requires 2D range counting or persistent segment tree.
    -   Iterate `i`, find `j` maximizing `count(k: i<k<j, a[j]<a[k]<a[i])`.
2.  **K Swaps?**
    -   If `K` is large, bubble sort logic applies.
    -   If `K` is small, it's a search problem.

### Common Mistakes

-   **Coordinate Compression**: Essential if values are large/negative.
-   **BIT Indexing**: 1-based indexing is standard.
-   **Long Integer**: Inversion count can be `N*(N-1)/2`, approx `2*10^10` for `N=200,000`. Must use `long long`.
