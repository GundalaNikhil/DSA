---
problem_id: ARR_SUBARRAY_SCORE_MIN_TIMES_LENGTH__4027
display_id: NTB-ARR-4027
slug: subarray-score-min-times-length
title: "Subarray Score = min x length"
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
  - searching
  - subarray-score-min-times-length
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Subarray Score = min x length

## Problem Statement

Given an array `a1..an`, define the score of a subarray as:

```
score = (minimum value in the subarray) * (subarray length)
```

Find the maximum possible score across all subarrays.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum subarray score

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.
- The minimum value can be negative, which may produce a negative score.

## Example Input

```
4
2 2 1 3
```

## Example Output

```
4
```
