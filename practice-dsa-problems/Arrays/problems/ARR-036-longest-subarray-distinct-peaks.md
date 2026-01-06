---
problem_id: ARR_LONGEST_SUBARRAY_DISTINCT_PEAKS__7875
display_id: NTB-ARR-7875
slug: longest-subarray-distinct-peaks
title: "Longest Subarray with <= K Distinct Peaks"
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
  - longest-subarray-distinct-peaks
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Longest Subarray with <= K Distinct Peaks

## Problem Statement

Given an array `a1..an` and an integer `K`, find the length of the longest contiguous subarray that contains at most `K` peaks.

For a subarray `a_l..a_r`, an index `i` (l < i < r) is a peak if:

```
a_i > a_{i-1} and a_i > a_{i+1}
```

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum subarray length with at most `K` peaks

## Constraints

- `1 <= n <= 200000`
- `0 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Peaks are evaluated within the subarray, not globally.
- The endpoints of the subarray are never peaks.

## Example Input

```
7 1
1 3 1 2 5 1 2
```

## Example Output

```
5
```
