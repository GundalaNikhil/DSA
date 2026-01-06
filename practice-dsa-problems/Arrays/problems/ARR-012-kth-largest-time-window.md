---
problem_id: ARR_KTH_LARGEST_TIME_WINDOW__2292
display_id: NTB-ARR-2292
slug: kth-largest-time-window
title: "Kth Largest with Time Window"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - kth-largest-time-window
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Kth Largest with Time Window

## Problem Statement

Given an array `a1..an`, a window size `W`, and an integer `K`, compute the `K`-th largest element for each index `i` considering only the last `W` elements ending at `i`.

For each `i`, the window is:

```
[L, i] where L = max(1, i - W + 1)
```

If the window length is less than `K`, output `-1` for that index.

## Input Format

- First line: integers `n`, `K`, and `W`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n` integers separated by spaces: the answer for each index `i` from 1 to `n`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `1 <= W <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The `K`-th largest is based on descending order.
- Each window is a suffix ending at `i`.

## Example Input

```
5 2 3
4 1 5 2 3
```

## Example Output

```
-1 1 4 2 3
```
