---
title: Partial Selection Sort Stats
slug: partial-selection-sort-stats
difficulty: Easy
difficulty_score: 24
tags:
- Sorting
- Simulation
- Arrays
problem_id: SRT_PARTIAL_SELECTION_SORT_STATS__6835
display_id: SRT-001
topics:
- Sorting
- Simulation
- Arrays
---
# Partial Selection Sort Stats - Editorial

## Problem Summary

You are given an array of integers and a number `k`. You need to simulate the first `k` iterations of the **Selection Sort** algorithm. In each iteration `i` (from 0 to `k-1`), you find the minimum element in the unsorted suffix `a[i..n-1]` and swap it with `a[i]`. Return the state of the array after these `k` swaps.

## Real-World Scenario

Imagine you are organizing a bookshelf.
-   You want to arrange books by height, shortest to tallest.
-   You scan the entire shelf to find the absolute shortest book and place it in the first slot.
-   Then you scan the remaining books to find the next shortest and place it in the second slot.
-   However, you get interrupted after placing just the first `k` books.
-   The shelf now has the `k` shortest books in order at the start, and the rest are still jumbled in the remaining slots. This is exactly what the problem asks for.

## Problem Exploration

### 1. Selection Sort Mechanism
Selection Sort works by repeatedly selecting the smallest element from the unsorted portion and moving it to the beginning.
-   **Pass 0**: Find min in `a[0..n-1]`, swap with `a[0]`.
-   **Pass 1**: Find min in `a[1..n-1]`, swap with `a[1]`.
-   ...
-   **Pass k-1**: Find min in `a[k-1..n-1]`, swap with `a[k-1]`.

### 2. Constraints Analysis
-   `N <= 100,000`.
-   `K <= N`.
-   A full Selection Sort takes `O(N^2)`, which is too slow for `N=100,000`.
-   However, we only need to perform `k` iterations.
-   The complexity will be roughly `O(K * N)`.
-   For `N=10^5`, a full `O(N^2)` selection sort would typically be too slow.
-   The time complexity `O(k * n)` is acceptable when `K` is small or the time limit is generous.
-   The standard simulation approach is required.

### 3. Edge Cases
-   `k=0`: Array remains unchanged.
-   `k=n-1`: Full sort.
-   Duplicate minimums: Selection sort is typically unstable depending on implementation, but the standard description says "swap with the first occurrence" or "swap with a[i]". Usually we pick the *first* minimum index in the range to be stable-ish or standard. The problem says "find the minimum... swap it". If duplicates exist, usually the one with lower index is picked. We should stick to finding the first occurrence of the minimum.

## Approaches

### Approach 1: Direct Simulation
-   Loop `i` from `0` to `k-1`.
-   Inner loop `j` from `i+1` to `n-1` to find `minIndex`.
-   Swap `a[i]` and `a[minIndex]`.
-   Complexity: `O(K * N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`4 2`
`4 3 1 2`

1.  **Iteration 0**:
    -   Range `a[0..3]`: `[4, 3, 1, 2]`.
    -   Min is `1` at index 2.
    -   Swap `a[0]` (4) and `a[2]` (1).
    -   Array: `[1, 3, 4, 2]`.
2.  **Iteration 1**:
    -   Range `a[1..3]`: `[3, 4, 2]`.
    -   Min is `2` at index 3.
    -   Swap `a[1]` (3) and `a[3]` (2).
    -   Array: `[1, 2, 4, 3]`.
3.  **End**: Return `[1, 2, 4, 3]`.

## Proof of Correctness

-   **Invariant**: After `i` iterations, the first `i` elements are the `i` smallest elements of the array, sorted in ascending order.
-   **Step**: In iteration `i`, we find the minimum of the remaining unsorted suffix and place it at `i`. This extends the sorted prefix by one.
-   **Termination**: After `k` steps, the prefix `a[0..k-1]` is sorted and contains the `k` smallest elements.

## Interview Extensions

1.  **What if K is large?**
    -   If `K` is close to `N`, this is `O(N^2)`. For large `N`, use Heap Sort (`O(N \log N)`) or Merge Sort.
    -   However, Selection Sort specifically minimizes *swaps* (`O(N)` swaps), which is useful if writing to memory is expensive (e.g., Flash memory).
2.  **Stability?**
    -   Selection Sort is generally **not stable** because swapping an element might move it past a duplicate.
    -   Example: `[2, 2, 1]`. Swap `2` (index 0) with `1` (index 2) -> `[1, 2, 2]`. The original first `2` moved to the end, changing relative order.

### Common Mistakes

-   **Inner Loop Start**: Must start from `i + 1`, not `0` or `1`.
-   **Swapping**: Ensure you swap `a[i]` with `a[minIndex]`, not `a[minIndex]` with `a[minIndex+1]`.
-   **Min Index Initialization**: Start assuming `minIndex = i`.
