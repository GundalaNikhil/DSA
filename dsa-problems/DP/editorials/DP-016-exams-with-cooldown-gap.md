---
problem_id: DP_EXAMS_COOLDOWN_GAP__7731
display_id: DP-016
slug: exams-with-cooldown-gap
title: "Exams With Cooldown Gap"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Scheduling
  - Binary Search
tags:
  - dp
  - intervals
  - scheduling
  - medium
premium: true
subscription_tier: basic
---

# DP-016: Exams With Cooldown Gap

## 📋 Problem Summary

You have `n` exams with start time `start[i]`, end time `end[i]`, and score `score[i]`. You can take multiple exams, but between any two you must leave at least `g` units of time: if you finish exam A at `end[A]`, the next exam B must satisfy `start[B] >= end[A] + g`. Maximize the total score.

Constraints: `n` up to `1e5`, times up to `1e9`, scores up to `1e9`.

## 🌍 Real-World Scenario

**Scenario Title:** Certification Marathon With Mandatory Breaks

Imagine a student pursuing many short certifications. Each certification exam takes a fixed time window, and the testing center mandates a cooldown between attempts for proctoring and ID checks (`g` minutes). The student wants the highest total credential points in a semester.

This maps exactly to selecting a subset of non-overlapping intervals with a gap, maximizing their total score.

**Why This Problem Matters:**

- Extends classic **weighted interval scheduling** with a configurable gap.
- Reinforces **binary search** to find the latest compatible interval.
- Teaches how to model real scheduling rules (prep/commute buffers) in DP.

![Real-World Application](../images/DP-016/real-world-scenario.png)

## Detailed Explanation

Sort exams by end time. Let `dp[i]` = maximum score considering the first `i` exams (sorted), where `i`th exam can be chosen or skipped.

For exam `i` with `(s, e, w)`:

- Find the latest exam `j` that ends no later than `s - g` (so there is enough gap). Because exams are sorted by end time, binary search on the `end` array gives `j` in `O(log n)`.
- Transition:
  - Skip: `dp[i-1]`
  - Take: `dp[j] + w`
  - `dp[i] = max(skip, take)`

Base: `dp[0] = 0`. Answer: `dp[n]`.

## Naive Approach

**Intuition:**
Try all subsets or DFS over choices, enforcing the gap.

**Algorithm:**

1. Sort exams by start time.
2. Backtrack over each exam: either take it (if compatible with last chosen) or skip it.
3. Track best score.

**Time Complexity:** Exponential (`O(2^n)`).  
**Space Complexity:** `O(n)` recursion depth.

**Why This Works:**
Enumerates all feasible schedules.

**Limitations:**

- Impossible for `n = 1e5`.
- Lots of redundant overlapping states.

## Optimal Approach

**Key Insight:**
Sorting by end time linearizes compatibility checks; binary search finds the last non-conflicting exam for each interval, enabling a simple DP.

**Algorithm:**

1. Sort exams by `end`.
2. Prepare array `ends[i] = exam[i].end`.
3. For `i` from `1..n`:
   - `j = upper_bound(ends, start[i] - g)` (first end greater than `start[i] - g`).
   - `dp[i] = max(dp[i-1], dp[j] + score[i])`.
4. Return `dp[n]`.

**Time Complexity:** `O(n log n)` (sort + `n` binary searches).  
**Space Complexity:** `O(n)` for `dp` and `ends`.

**Why This Is Optimal:**
Each interval is processed once; the only extra work is a binary search to find compatibility, which is asymptotically optimal with sorting.

![Algorithm Visualization](../images/DP-016/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


### Common Mistakes to Avoid

1. **Using `start >= end` instead of `start >= end + g`.**

   - ❌ Ignores the required gap.
   - ✅ Binary search for `end <= start - g`.

2. **Sorting by start time.**

   - ❌ Breaks the DP because compatibility search expects end-sorted intervals.
   - ✅ Sort by end time and binary search on the `ends` array.

3. **Overflow of score sums.**
   - ❌ Storing totals in 32-bit integers when scores reach `1e9` and `n` is large.
   - ✅ Use 64-bit (or BigInt) for all totals.

## Related Concepts

- Weighted interval scheduling
- Binary search for compatibility
- Prefix DP arrays
