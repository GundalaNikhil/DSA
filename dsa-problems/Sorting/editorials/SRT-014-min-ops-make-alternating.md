---
title: Minimum Operations to Make Array Alternating
slug: min-ops-make-alternating
difficulty: Medium
difficulty_score: 51
tags:
- Greedy
- Counting
- Arrays
problem_id: SRT_MIN_OPS_MAKE_ALTERNATING__4621
display_id: SRT-014
topics:
- Sorting
- Counting
- Greedy
---
# Minimum Operations to Make Array Alternating - Editorial

## Problem Summary

You are given an array `a`. You want to make it alternating, meaning `a[0] == a[2] == a[4]...` and `a[1] == a[3] == a[5]...`, with the condition that `a[0] != a[1]`. You can change any element to any value. Find the minimum number of changes required.

## Real-World Scenario

Imagine you are a **Tiler** laying a floor.
-   The design requires a checkerboard-like pattern in 1D: Black, White, Black, White...
-   You have a row of tiles already laid out, but they are a mix of colors.
-   You want to paint over the minimum number of tiles to achieve the alternating pattern.
-   However, you are not restricted to Black and White; you can pick any two distinct colors (e.g., Red and Blue) that maximize the number of tiles you *don't* have to paint.

## Problem Exploration

### 1. Even and Odd Indices
-   The problem requires all even indices `0, 2, 4...` to have the same value `X`.
-   It requires all odd indices `1, 3, 5...` to have the same value `Y`.
-   Constraint: `X != Y`.
-   To minimize changes, we want to maximize the number of elements that are *already* `X` at even positions and `Y` at odd positions.
-   Total Changes = `(Total Evens - Count of X at Evens) + (Total Odds - Count of Y at Odds)`.
-   This simplifies to: `Total Elements - (Count of X at Evens + Count of Y at Odds)`.
-   So we need to maximize `Count(X, Even) + Count(Y, Odd)` subject to `X != Y`.

### 2. Frequency Analysis
-   Count frequencies of all numbers at even indices. Let the top two most frequent be `(E1_val, E1_count)` and `(E2_val, E2_count)`.
-   Count frequencies of all numbers at odd indices. Let top two be `(O1_val, O1_count)` and `(O2_val, O2_count)`.
-   Why top two? Because if the best even value `E1_val` is the same as the best odd value `O1_val`, we can't use both. We must pick the second best for one of them.

### 3. Cases
-   **Case 1**: `E1_val != O1_val`.
    -   Best combo is simply `E1` and `O1`.
    -   Kept elements = `E1_count + O1_count`.
-   **Case 2**: `E1_val == O1_val`.
    -   We have a conflict. We can't use `E1` and `O1` together.
    -   Option A: Use `E1` and `O2`. Kept = `E1_count + O2_count`.
    -   Option B: Use `E2` and `O1`. Kept = `E2_count + O1_count`.
    -   Take the max of Option A and Option B.
-   Note: If a position (even or odd) has all distinct elements appearing once, or is empty, counts are small. We should handle cases where `E2` or `O2` doesn't exist (count 0).

### 4. Edge Cases
-   `n=1`: 0 changes.
-   Array with all same elements: `[2, 2, 2]`. Even: `2` (count 2). Odd: `2` (count 1). `E1=2`, `O1=2`. Conflict.
    -   Option A: Keep even `2`s. Change odds to something else. Kept `2 + 0`. Changes `1`.
    -   Option B: Keep odd `2`s. Change evens. Kept `1 + 0`. Changes `2`.
    -   Best is 1 change.

## Approaches

### Approach 1: Frequency Counting
-   Count frequencies for even/odd positions.
-   Find top 2 frequent elements for both.
-   Check conflict and compute max kept.
-   Result = `N - max_kept`.
-   Complexity: `O(N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`4`
`1 1 1 2`

1.  **Indices**:
    -   Even (0, 2): `[1, 1]`. Counts: `{1: 2}`.
    -   Odd (1, 3): `[1, 2]`. Counts: `{1: 1, 2: 1}`.
2.  **Top Two**:
    -   Even: `E1=(1, 2)`, `E2=(-1, 0)`.
    -   Odd: `O1=(1, 1)`, `O2=(2, 1)`. (Order of 1 and 2 in odd doesn't strictly matter for O1, but let's say 1 is O1).
3.  **Check**:
    -   `E1.val (1) == O1.val (1)`. Conflict.
    -   Option 1: Use `E1` and `O2`. Kept = `2 + 1 = 3`. Changes = `4 - 3 = 1`.
    -   Option 2: Use `E2` and `O1`. Kept = `0 + 1 = 1`. Changes = `4 - 1 = 3`.
    -   Min changes: 1.
4.  **Result**: 1. (Change odd index 1 from 1 to 2 -> `1 2 1 2`).

## Proof of Correctness

-   **Greedy**: We want to maximize the number of unchanged elements.
-   **Cases**: Since we only need to pick one value for evens and one for odds, checking the top 2 candidates covers all optimal scenarios. If the best choices conflict, the next best choice for one of them combined with the best of the other is guaranteed to be optimal.

## Interview Extensions

1.  **Alternating Period K?**
    -   `a[i] == a[i+K]`. Count frequencies modulo K. Solve K independent problems? No, distinct values constraint might apply between adjacent groups?
    -   Usually "alternating" implies period 2.
2.  **Cost to change values?**
    -   If changing `x` to `y` has cost `C(x, y)`, this becomes a min-cost matching or flow problem.

### Common Mistakes

-   **Empty Maps**: Handling cases where all elements are at even indices (not possible if n > 1) or only 1 distinct element exists.
-   **Tie Breaking**: The order of top 2 doesn't matter as long as we check both cross combinations.
