---
title: Longest Consecutive After At Most One Change
slug: longest-consecutive-one-change
difficulty: Medium
difficulty_score: 53
tags:
- Arrays
- Prefix Suffix
- Optimization
problem_id: SRT_LONGEST_CONSECUTIVE_ONE_CHANGE__6194
display_id: SRT-011
topics:
- Sorting
- Prefix Suffix
- Arrays
---
# Longest Consecutive After At Most One Change - Editorial

## Problem Summary

You are given an array of integers `a`. You can change **at most one** element to any integer value. Your goal is to maximize the length of a contiguous subarray that is strictly increasing.

## Real-World Scenario

Imagine you are a **Road Engineer** inspecting a highway.
-   The highway is made of segments with different elevation levels.
-   A "smooth" section is one where the elevation strictly increases (uphill).
-   You notice a long smooth section, then a sudden bump or dip, and then another smooth section.
-   You have the budget to fix (regrade) exactly one segment to any elevation you want.
-   By fixing one bad segment, can you connect two smooth sections into one giant smooth uphill drive?

## Problem Exploration

### 1. Strictly Increasing Subarrays
-   Without any changes, the answer is simply the longest strictly increasing contiguous subarray. We can find this in `O(N)` by iterating and resetting count when `a[i] <= a[i-1]`.
-   With one change allowed, we can potentially bridge two increasing subarrays.
-   Suppose we have `... A, B, X, C, D ...` where `...A, B` is increasing and `C, D...` is increasing.
-   If we change `X` to `Y`, can we make `...A, B, Y, C, D...` strictly increasing?
-   This requires `B < Y < C`.
-   Since `Y` can be any integer, such a `Y` exists if and only if `C - B >= 2`.
-   So we can bridge the subarrays ending at `i-1` and starting at `i+1` if `a[i+1] - a[i-1] >= 2`.
-   The new length would be `len(ending at i-1) + 1 (for X) + len(starting at i+1)`.

### 2. Prefix and Suffix Arrays
-   Let `L[i]` be the length of the longest strictly increasing subarray ending at `i`.
    -   If `a[i] > a[i-1]`, `L[i] = L[i-1] + 1`.
    -   Else `L[i] = 1`.
-   Let `R[i]` be the length of the longest strictly increasing subarray starting at `i`.
    -   If `a[i] < a[i+1]`, `R[i] = R[i+1] + 1`.
    -   Else `R[i] = 1`.
-   Both `L` and `R` can be computed in `O(N)`.

### 3. Trying Every Change
-   Iterate `i` from `0` to `n-1`. Assume we change `a[i]`.
-   Option 1: Just extend the left part. New length `L[i-1] + 1`. (Valid for any `i > 0`).
-   Option 2: Just extend the right part. New length `R[i+1] + 1`. (Valid for any `i < n-1`).
-   Option 3: Bridge both. Valid if `i > 0` and `i < n-1` and `a[i+1] - a[i-1] >= 2`. New length `L[i-1] + 1 + R[i+1]`.
-   The answer is the maximum of all these options (and the original max length without changes, though "at most one" includes zero changes).

### 4. Edge Cases
-   `n=1`: Length 1.
-   `n=2`: Can always make length 2 (change one to be larger/smaller).
-   `a[i+1] - a[i-1] < 2`: Cannot bridge. But we can still extend left or right by changing `a[i]`. E.g., `1, 5, 5, 2`. Change `5` (index 2) to `6`. `1, 5, 6`. Length 3.
    -   Make `a[i] = a[i-1] + 1`. Then length is `L[i-1] + 1`.
    -   Make `a[i] = a[i+1] - 1`. Then length is `R[i+1] + 1`.
-   So we always consider `L[i-1] + 1` and `R[i+1] + 1` as candidates.

## Approaches

### Approach 1: Prefix/Suffix Arrays
-   Compute `L` array (left-to-right).
-   Compute `R` array (right-to-left).
-   Iterate `i` to find max bridged length.
-   Complexity: `O(N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`6`
`1 2 3 7 5 6`

1.  **L Array**: `[1, 2, 3, 4, 1, 2]`.
    -   `1`: Start.
    -   `2 > 1`: 2.
    -   `3 > 2`: 3.
    -   `7 > 3`: 4.
    -   `5 < 7`: Reset to 1.
    -   `6 > 5`: 2.
2.  **R Array**: `[4, 3, 2, 1, 2, 1]`.
    -   `6`: End.
    -   `5 < 6`: 2.
    -   `7 > 5`: Reset to 1.
    -   `3 < 7`: 2.
    -   `2 < 3`: 3.
    -   `1 < 2`: 4.
3.  **Check Index 3 (Value 7)**:
    -   `i=3`. `L[2]=3` (val 3). `R[4]=2` (val 5).
    -   Bridge condition: `arr[4] - arr[2] = 5 - 3 = 2 >= 2`. Valid.
    -   Len: `3 + 1 + 2 = 6`.
    -   We effectively change `7` to `4` (or `3.5` if allowed, but must be integer, `4` works).
4.  **Result**: 6.

## Proof of Correctness

-   **Exhaustive Search**: We check every possible position `i` to perform the change.
-   **Optimality**: For a fixed `i`, `L[i-1]` and `R[i+1]` represent the max possible extensions to the left and right. Combining them gives the global maximum for that pivot.

## Interview Extensions

1.  **K Changes?**
    -   Much harder. `O(N * K)` DP or `O(N log N)` with complex structures.
2.  **Longest Arithmetic Subarray with 1 Change?**
    -   Check all possible differences? Harder.

### Common Mistakes

-   **Index Bounds**: Checking `i-1` and `i+1` without bounds checks.
-   **Bridge Condition**: Forgetting `arr[i+1] - arr[i-1] >= 2`. If difference is 1 (e.g., `3, 4`), no integer fits strictly between them.
-   **Single Element**: Handling `n=1`.
