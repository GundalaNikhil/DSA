---
title: Longest Increasing Subarray After Updates
slug: longest-increasing-subarray-updates
difficulty: Medium
difficulty_score: 55
tags:
- Segment Tree
- Range Merge
- Dynamic Updates
problem_id: SEG_LONGEST_INCREASING_SUBARRAY_UPDATES__2654
display_id: SEG-008
topics:
- Segment Tree
- Dynamic Arrays
- Monotonicity
---
# Longest Increasing Subarray After Updates - Editorial

## Problem Summary

You are given an array `a`. You need to handle point updates `SET i x` and after each update, output the length of the longest **strictly increasing contiguous subarray**.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
## Real-World Scenario

Imagine a **Stock Market Analysis Tool**.
-   You track the price of a stock over time.
-   A "bull run" is a period where the price strictly increases every day.
-   As historical data is corrected or new data comes in, you want to know the duration of the longest bull run ever recorded in the dataset.

## Problem Exploration

### 1. Contiguous vs. Subsequence
The problem asks for a **subarray** (contiguous), not a subsequence. This simplifies things greatly.
-   Subsequence: LIS problem (`O(N log N)`). Dynamic LIS is hard.
-   Subarray: Can be solved by checking adjacent elements.

### 2. Segment Tree Approach
We can use a Segment Tree to maintain information about increasing subarrays in each range.
For a range `[L, R]`, what do we need to know to merge it with a neighbor?
-   `maxLen`: The length of the longest increasing subarray fully inside this range.
-   `prefLen`: The length of the increasing subarray starting at `L` and extending into the range.
-   `suffLen`: The length of the increasing subarray ending at `R` and extending backwards.
-   `len`: Total length of the range (constant `R - L + 1`).
-   `leftVal`: Value at `a[L]`.
-   `rightVal`: Value at `a[R]`.

### 3. Merge Logic
When merging left child `left` and right child `right`:
-   **New `maxLen`**: Max of:
    -   `left.maxLen`
    -   `right.maxLen`
    -   If `left.rightVal < right.leftVal`: `left.suffLen + right.prefLen` (crossing boundary).
-   **New `prefLen`**:
    -   `left.prefLen`
    -   If `left.prefLen == left.len` (entire left is increasing) AND `left.rightVal < right.leftVal`: `left.len + right.prefLen`.
-   **New `suffLen`**:
    -   `right.suffLen`
    -   If `right.suffLen == right.len` (entire right is increasing) AND `left.rightVal < right.leftVal`: `right.len + left.suffLen`.
-   **New `leftVal`**: `left.leftVal`.
-   **New `rightVal`**: `right.rightVal`.

## Approaches

### Approach 1: Segment Tree
-   **Build**: `O(N)`.
-   **Update**: `O(log N)`.
-   **Query**: Root node's `maxLen`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`1 2 1`
`SET 2 3`

1.  **Initial**: `[1, 2, 1]`.
    -   Root merges `[1, 2]` and `[1]`.
    -   Left `[1, 2]`: maxLen 2, suffLen 2, rightVal 2.
    -   Right `[1]`: maxLen 1, prefLen 1, leftVal 1.
    -   `2 < 1` is False. No merge across boundary.
    -   Root maxLen = max(2, 1) = 2.
2.  **Update**: `a[2] = 3`. Array `[1, 2, 3]`.
    -   Right leaf `[3]`: maxLen 1, prefLen 1, leftVal 3.
    -   Left child `[1, 2]`: rightVal 2.
    -   `2 < 3` is True.
    -   Merge: `maxLen = max(2, 1, 2+1) = 3`.
3.  **Result**: 3.

## Proof of Correctness

-   **Merge Logic**: Covers all cases:
    1.  Longest subarray is entirely in left child.
    2.  Longest subarray is entirely in right child.
    3.  Longest subarray crosses the midpoint (requires `left.rightVal < right.leftVal`).
-   **Prefix/Suffix**: Correctly maintained to support case 3 for the parent node.

## Interview Extensions

1.  **Longest Non-Decreasing?**
    -   Change `<` to `<=`.
2.  **Number of Increasing Subarrays?**
    -   Different problem. Just sum lengths? No, combinatorial.
3.  **Query Range [L, R]?**
    -   Return `Node` from query function and check `maxLen`.

### Common Mistakes

-   **Empty Range**: Base cases for recursion.
-   **Boundary Check**: `left.rightVal < right.leftVal` is the only condition for merging across boundary.
-   **Prefix/Suffix Update**: Only extend prefix if the *entire* left side is increasing. Similarly for suffix.
