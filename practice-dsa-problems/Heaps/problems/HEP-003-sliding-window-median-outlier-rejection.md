---
problem_id: HEP_SLIDING_WINDOW_MEDIAN_OUTLIER_REJECTION__5592
display_id: NTB-HEP-5592
slug: sliding-window-median-outlier-rejection
title: "Sliding Window Median with Deterministic Outlier Rejection"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - heaps
  - priority-queues
  - sliding-window-median-outlier-rejection
  - sorting
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Sliding Window Median with Deterministic Outlier Rejection

## Problem Statement

You are given an array `a1..an` and a window size `W`. For every window of length `W`, you must compute the median after applying a deterministic outlier replacement rule.

For a window `a[L..R]` (where `R - L + 1 = W`):

1. Compute the **raw median** `m` of the window values.
2. Any value `x` in the window with `x > 2 * m` is an outlier.
3. Replace each outlier by the average of its nearest non-outlier neighbors **within the same window**:
   - Let `Lx` be the closest index to the left of the outlier whose value is not an outlier.
   - Let `Rx` be the closest index to the right of the outlier whose value is not an outlier.
   - If both exist, replacement value is `floor((a[Lx] + a[Rx]) / 2)`.
   - If only one side exists, replacement value equals that side's value.

After all replacements, compute the median of the adjusted window. Output this median for each window, from left to right.

The median is defined as the middle element after sorting; when `W` is even, use the lower middle (the `W/2`-th element in 1-based indexing).

## Input Format

- First line: integers `n` and `W`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n - W + 1` integers separated by spaces: the adjusted median for each window

## Constraints

- `1 <= n <= 200000`
- `1 <= W <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The raw median used for outlier detection is computed from the original window values before any replacement.
- There is always at least one non-outlier value in a window because the median itself is not an outlier.
- The intended data structure for medians is a two-heap balance (max-heap + min-heap).

## Example Input

```
5 3
2 3 100 4 5
```

## Example Output

```
3 3 4
```
