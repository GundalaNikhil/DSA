---
problem_id: ARR_SUBARRAYS_BOUNDED_VARIANCE__3408
display_id: NTB-ARR-3408
slug: subarrays-bounded-variance
title: "Subarrays with Bounded Variance"
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
  - subarrays-bounded-variance
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Subarrays with Bounded Variance

## Problem Statement

Given an array `a1..an` and an integer `K`, count how many subarrays satisfy:

```
max(subarray) - min(subarray) <= K
```

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: number of qualifying subarrays

## Constraints

- `1 <= n <= 200000`
- `0 <= K <= 10^9`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.

## Example Input

```
3 1
1 3 2
```

## Example Output

```
4
```
