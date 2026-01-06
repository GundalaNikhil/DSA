---
problem_id: ARR_K_NONOVERLAPPING_MAX_SUBARRAYS__6606
display_id: NTB-ARR-6606
slug: k-nonoverlapping-max-subarrays
title: "K Non-Overlapping Max Subarrays"
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
  - k-nonoverlapping-max-subarrays
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# K Non-Overlapping Max Subarrays

## Problem Statement

Given an array `a1..an` and an integer `K`, choose exactly `K` non-overlapping, non-empty subarrays to maximize the total sum of their elements.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum total sum using exactly `K` subarrays

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays must be contiguous and cannot overlap.
- You must select exactly `K` subarrays.

## Example Input

```
5 2
1 2 -1 2 3
```

## Example Output

```
8
```
