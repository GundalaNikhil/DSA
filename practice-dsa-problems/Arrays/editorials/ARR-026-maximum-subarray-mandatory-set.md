---
problem_id: ARR_MANDATORY_SET__7221
display_id: ARR-026
slug: maximum-subarray-mandatory-set
title: "Maximum Subarray with Mandatory Inclusion Set"
difficulty: Hard
difficulty_score: 55
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - optimization
  - searching
  - sliding-window
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-026: Maximum Subarray with Mandatory Inclusion Set

## 📋 Problem Summary

Find the maximum sum of a contiguous subarray that contains **at least one occurrence of every value** from a given set `S`.
If impossible, output `IMPOSSIBLE`.

## 🌍 Real-World Scenario

**Scenario Title:** 🥗 The Perfect Salad

### The Problem

You are at a salad bar (a sequence of ingredients).
You want to scoop a contiguous portion of the bar onto your plate.
To make it a "Complete Meal", it MUST contain:

- At least one Tomato (`S1`).
- At least one Cucumber (`S2`).
- At least one Olive (`S3`).
  Each inch of the bar has a "Taste Score" (some negative, some positive).
  You want to maximize the total taste of your scoop while ensuring it's "Complete".

### Real-World Relevance

- **Gene Sequencing:** Finding a gene segment with highest expression that contains all necessary activator markers.
- **Log Analysis:** Finding a time window with maximal anomalies that captures _all_ types of critical errors for a root cause analysis.

## 🚀 Detailed Explanation

### 1. The Constraints

We need `Set S` to be fully present in `Range [L, R]`.
Inside that valid range, we want `Sum(L...R)` to be maximal.
However, usually "Minimizing length" of such a window is a standard Two Pointers problem.
Here, we want to maximize **Sum**. The window might need to be huge to embrace large positive numbers, or small to avoid negatives.

### 2. Strategy

Iterate `R` from `0` to `N-1`.
For a fixed `R`, what is the valid range of `L`?
Let `Last[v]` be the last seen position of value `v`.
To include all element of `S`, the subarray must start _before or at_ the minimum of `Last[s]` for all `s in S`.
Let `MaxValidL = min(Last[s])` for all `s` in `S`.
If any `s` has not been seen yet, `MaxValidL` is undefined (no valid subarray ends at `R`).
If defined, any `L <= MaxValidL` is a valid start point for a subarray ending at `R`.
To maximize `Sum(L...R) = Prefix[R] - Prefix[L-1]`, we need to minimize `Prefix[L-1]` where `0 <= L-1 < MaxValidL`.
Wait. `L` can range from `0` to `MaxValidL`. So `L-1` ranges from `-1` to `MaxValidL - 1`.
We need `min(Prefix[k])` for `-1 <= k < MaxValidL`.

### 3. Algorithm

1. Use a Map to track `Last[value]` for items in `S`.
2. Maintain a "Window Count" of how many unique items from `S` we have seen so far.
3. Also, we need `min(Last[s])`. A simple variable won't work because updating one `Last[s]` changes the minimum.
   - We can use a Min-Heap or Multiset to store `{Last[s]}` for all `s`.
   - When we see `arr[R]`:
     - If `arr[R]` in `S`:
       - Remove old `Last[arr[R]]` from multiset.
       - Update `Last[arr[R]] = R`.
       - Insert new into multiset.
4. If Multiset size == `|S|`:
   - `Limit = Multiset.min()`.
   - We need `min_prefix` in range `[-1, Limit-1]`.
   - `CurrentSum = Prefix[R] - query_min_prefix(-1, Limit-1)`.
   - Update Global Max.
5. To query `min_prefix` efficiently as `Limit` moves?
   - Actually `Limit` doesn't always increase. It can jump around (though `R` increases, `min(Last)` generally increases? Yes, `Last[s]` only increases).
   - So `Limit` is non-decreasing!
   - We can maintain a running minimum of prefix sums up to `Limit-1`.

### 4. Logic Check

Since indices move forward, `Last[s]` only grows.
Thus `Limit = min(Last[s])` is non-decreasing.
As `Limit` increases, the range `[-1, Limit-1]` grows.
We can maintain `CurrentMinPrefix` variable.
While `processed_idx < Limit - 1`: update `CurrentMinPrefix`.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Init LastPos map, Multiset for MinPos]
    B --> C[Loop R from 0 to N-1]
    C --> D{Is arr[R] in S?}
    D -- Yes --> E[Update LastPos, Update Multiset]
    D -- No --> F[Continue]
    E --> G{Has all S?}
    G -- Yes --> H[Limit = Multiset.min()]
    H --> I[Expand RunningMinPrefix to Limit-1]
    I --> J[Score = Prefix[R] - RunningMinPrefix]
    J --> K[MaxScore = max(MaxScore, Score)]
    K --> C
    C -- End Loop --> L[Return MaxScore]
```

## 🧪 Edge Cases to Test

1.  **Impossible:** S has value never in Array.
    - Check if `MaxScore` was ever updated. Initialize with `-Infinity` or flag.
2.  **S is Empty:** Technically all subarrays valid? Problem says `1 <= m`.
3.  **One Element S:** Standard Kadane? No, must contain `S`.
    - If `S={5}`, subarray must contain 5.

## 🏃 Naive vs Optimal Approach

### Naive O(N^3)

Check every subarray.

### Sliding Window + Prefix Min O(N log M)

- **Time:** O(N log M) due to Multiset operations (finding min position).
- **Space:** O(M) to store positions.
  Optimal.
