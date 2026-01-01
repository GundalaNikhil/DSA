---
title: Weighted Median of Two Sorted Arrays
slug: weighted-median-two-sorted
difficulty: Medium
difficulty_score: 60
tags:
- Median
- Binary Search
- Sorted Arrays
problem_id: SRT_WEIGHTED_MEDIAN_TWO_SORTED__3086
display_id: SRT-009
topics:
- Sorting
- Binary Search
- Median
---
# Weighted Median of Two Sorted Arrays - Editorial

## Problem Summary

You are given two sorted arrays `A` and `B`. Each element in `A` has a weight `wA` (meaning it appears `wA` times) and each element in `B` has a weight `wB`. You need to find the median of the combined multiset of numbers. If the total number of elements is even, return the average of the two middle elements.

## Real-World Scenario

Imagine you are analyzing **Salary Data** from two different departments.
-   Dept A has `N` distinct salary bands, but each band applies to `wA` employees.
-   Dept B has `M` distinct salary bands, but each band applies to `wB` employees.
-   You want to find the **Median Salary** of the entire company.
-   Since the data is already sorted by salary bands, you don't want to list out every single employee (which could be millions). You want to compute the median directly from the summarized data.

## Problem Exploration

### 1. Total Count and Median Position
-   Let `Total = n * wA + m * wB`.
-   If `Total` is odd, the median is the element at index `Total / 2` (0-indexed).
-   If `Total` is even, the median is the average of elements at `Total / 2 - 1` and `Total / 2`.
-   We need a function `findKth(k)` that returns the `k`-th smallest element in the combined multiset.

### 2. Finding K-th Element in Two Weighted Sorted Arrays
-   This is a variation of the classic "Median of Two Sorted Arrays".
-   However, since elements have weights, we can't just use indices directly.
    -   Array A: `A[0]` appears `wA` times, `A[1]` appears `wA` times...
    -   Array B: `B[0]` appears `wB` times...
-   This means the cumulative count of elements from `A` less than or equal to `A[i]` is `(i + 1) * wA`.
-   We can use **Binary Search on the Answer** (Value Range) or **Binary Search on Index**.
-   **Binary Search on Value**:
    -   Range `[min(A[0], B[0]), max(A[n-1], B[m-1])]`.
    -   For a value `V`, count how many elements are `<= V`.
    -   Count = `(upper_bound(A, V) * wA) + (upper_bound(B, V) * wB)`.
    -   If `Count > k`, then the answer is `<= V`.
    -   This works if values are integers and range is small. Constraints say values fit in integer, but range can be large (`10^9`). `log(10^9) = 30` iterations. This is feasible.
-   **Alternative: K-th Element Logic**:
    -   We can binary search on the index of `A`. Suppose we pick `A[i]`.
    -   This `A[i]` is greater than `i` elements in `A` (contributing `i * wA` count).
    -   We can find how many elements in `B` are less than `A[i]` using binary search (`j` elements, contributing `j * wB`).
    -   Total rank of the first copy of `A[i]` is `i * wA + j * wB`.
    -   The last copy of `A[i]` is at rank `(i + 1) * wA + j * wB - 1`.
    -   If `k` falls in this range, `A[i]` is the answer.
    -   We can do this for `A` and `B`.
    -   Since we need the exact value, checking `A` and `B` covers all candidates.
    -   Complexity: `O(log N * log M)` or `O(log N + log M)`.

### 3. Handling Even Total Count
-   If `Total` is even, we need `findKth(Total/2 - 1)` and `findKth(Total/2)`.
-   Usually these are the same or adjacent values.
-   We can call the `findKth` function twice.

### 4. Algorithm Details (Binary Search on Value)
-   Range `[L, R] = [-2e9, 2e9]` (safe bounds).
-   While `L <= R`:
    -   `mid = L + (R - L) / 2`.
    -   `count = countLessEqual(mid)`.
    -   If `count > k`: `ans = mid`, `R = mid - 1`.
    -   Else: `L = mid + 1`.
-   `countLessEqual(val)`:
    -   Find `idxA` such that `A[idxA] <= val` (using `upper_bound` logic). Count `idxA * wA`.
    -   Find `idxB` such that `B[idxB] <= val`. Count `idxB * wB`.
    -   Total count.
-   Complexity: `O(log(Range) * (log N + log M))`.
-   With `Range ~ 2*10^9`, `log Range ~ 31`. `log N ~ 17`. Total ops ~ `31 * 34 ~ 1000`. Very fast.

## Approaches

### Approach 1: Binary Search on Value
-   Since we need to find the `k`-th value, and the function `count(x)` (number of elements <= x) is monotonic, we can binary search for the smallest `x` such that `count(x) > k`.
-   Note: We want the element at 0-based index `k`. This is the `(k+1)`-th smallest. So we look for smallest `x` with `count(x) >= k + 1`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`2 2`
`1 3`
`2 7`
`1 2`

1.  **Setup**: `A=[1, 3]`, `B=[2, 7]`. `wA=1`, `wB=2`.
2.  **Total**: `2*1 + 2*2 = 6`. Even.
3.  **Targets**: `k1 = 6/2 - 1 = 2`. `k2 = 6/2 = 3`.
4.  **Find K=2**:
    -   Try `mid=2`.
    -   `A`: `<=2` is `[1]` (count 1 * 1 = 1).
    -   `B`: `<=2` is `[2]` (count 1 * 2 = 2).
    -   Total `<=2` is 3. `3 > 2`. `ans=2`. `high=1`.
    -   Try `mid=1`. Total `<=1` is 1. `1 <= 2`. `low=2`.
    -   Result `2`.
5.  **Find K=3**:
    -   Try `mid=2`. Total `<=2` is 3. `3 <= 3`. `low=3`.
    -   Try `mid=3`.
    -   `A`: `<=3` is `[1, 3]` (count 2).
    -   `B`: `<=3` is `[2]` (count 2).
    -   Total 4. `4 > 3`. `ans=3`.
    -   Result `3`.
6.  **Average**: `(2 + 3) / 2 = 2.5`.

## Proof of Correctness

-   **Monotonicity**: The count of elements `<= x` is non-decreasing with `x`.
-   **Binary Search**: Correctly finds the smallest `x` such that `count(<= x) > k`. This `x` is the `(k+1)`-th element (0-indexed `k`).
-   **Coverage**: Since we check the combined count from both arrays, we correctly account for all elements and their weights.

## Interview Extensions

1.  **Median of K Sorted Arrays?**
    -   Same logic: Binary search on value, sum counts from all K arrays. `O(K log N * log Range)`.
2.  **Fractional Weights?**
    -   Multiply all weights by a common denominator to make them integers.

### Common Mistakes

-   **Integer Overflow**: Total weight can be large. Use `long long` / `BigInt`.
-   **Binary Search Range**: Ensure range covers all possible input values.
-   **Off-by-one**: `k` is 0-indexed. `count > k` finds the element at index `k`.
