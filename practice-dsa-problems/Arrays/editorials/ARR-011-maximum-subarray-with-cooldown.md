---
problem_id: ARR_COOLDOWN_MAX_SUB__0773
display_id: ARR-011
slug: maximum-subarray-with-cooldown
title: "Maximum Subarray with Cooldown"
difficulty: Medium
difficulty_score: 35
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - kadane
  - modification
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-011: Maximum Subarray with Cooldown

## 📋 Problem Summary

Choose one or more non-overlapping subarrays from `arr`.
Constraint: If you pick a subarray ending at index `i`, the next subarray cannot start until index `i + X + 1`. There is a mandatory "cooldown" gap of `X` elements where you cannot pick anything.
Goal: Maximize the total sum of elements in your chosen subarrays.

## 🌍 Real-World Scenario

**Scenario Title:** 🏋️ The Interval Training Schedule

### The Problem

You are planning a high-intensity interval training (HIIT) workout.

- The array represents the "gains" (or calories burned) available for each minute.
- Negative numbers mean the exercise at that minute is detrimental/exhausting beyond gain.
- You can work out for a continuous block of time (subarray).
- However, after any block of intense workout, you MUST rest for `X` minutes (cooldown) before starting another block.

You want to plan your sets to maximize total gains.

### Real-World Relevance

- **Machine Maintenance:** Operating a machine for a shift (subarray) requires a cooling-off period of `X` hours before the next shift.
- **Harvesting:** Harvesting a plot of land requires leaving it fallow for `X` seasons before replanting.

## 🚀 Detailed Explanation

### 1. Simple Case: X = 0

If `X = 0`, we just need to find the maximum sum of non-overlapping subarrays. Since "non-overlapping" with 0 gap just means adjacent... effectively we can pick _any_ segments.
Actually, if `X=0`, we can just pick all positive numbers?
The problem says "one or more subarrays".
If we pick `[1, 2]` ending at `i=1`. Next starts `1+0+1 = 2`.
So contiguous selection is fine.
If `X=0`, we effectively just sum all `max(0, arr[i])`? Not exactly, subarrays must be contiguous blocks.
For `X=0`, we can treat it as: "Pick any disjoint subarrays". We would just pick all positive segments.

### 2. With Cooldown X > 0

We need Dynamic Programming.
Let `DP[i]` be the max score we can get considering elements `0` to `i`.
State definition:

- `MAX_at[i]`: Max total sum ending at or before `i`.

Transition:
At index `i`, we have two choices:

1. Don't include `arr[i]` in a subarray ending at `i`.
   - Score: `MAX_at[i-1]`
2. Include `arr[i]` as the _end_ of a subarray.
   - We need to decide where this current subarray started. Say it started at `j <= i`.
   - Subarray Sum: `Sum(j...i)`.
   - Previous valid part must end at `j - X - 1` or earlier.
   - Total: `MAX_at[j - X - 1] + Sum(j...i)`.

This `O(N^2)` approach is too slow.

### 3. Optimized DP

Let's maintain `DP[i]`: Max score ending EXACTLY at `i` (meaning `arr[i]` is part of a selected subarray).
Let `Global[i]`: Max score in the range `0...i` (could end earlier).

`DP[i] = arr[i] + max(0, DP[i-1], Global[i-X-1])`

- `arr[i]`: Start a new subarray here (previous was `Global` far away) OR extend current subarray (`DP[i-1]`).
- Wait.
  - Extend current: `DP[i-1] + arr[i]`.
  - Start new: `arr[i] + Global[i-X-1]` (Best score from valid past).
  - Can we just take `arr[i]` alone? Yes (if `Global` is negative/zero).

Recurrence:
`DP[i] = arr[i] + max(DP[i-1], Global[i-X-1])` (assuming we treat out-of-bounds as 0).
`Global[i] = max(Global[i-1], DP[i])`.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Initialize DP array and Global array]
    B --> C[Loop i from 0 to N-1]
    C --> D[PrevGlobal = (i-X-1 >= 0) ? Global[i-X-1] : 0]
    D --> E[OptionExtend = DP[i-1]]
    D --> F[OptionNew = PrevGlobal]
    E --> G[DP[i] = arr[i] + max(0, OptionExtend, OptionNew)]
    G --> H[Global[i] = max(Global[i-1], DP[i])]
    H --> C
    C -- End Loop --> I[Return Global[N-1]]
```

## 🧪 Edge Cases to Test

1.  **All Negative:** Must pick at least one subarray? Problem says "select one or more".
    - `DP` logic will pick the "least negative" single element if forced, or we might need to initialize `Global` with `-Infinity`.
    - If "maximum subarray" logic usually allows empty = 0, but problem says "one or more". So like Kadane's, answer is max single element if all negative.
2.  **X large:** `X >= N`. Can only pick one subarray. Reduces to standard Max Subarray Sum (Kadane's).

## 🏃 Naive vs Optimal Approach

### Naive Recursive O(2^N)

Try every possible start/end. Too slow.

### Linear DP O(N)

- **Time:** O(N).
- **Space:** O(N) for arrays (can optimize to O(X) or even O(1) if careful, but O(N) space is safe and easy).
