---
problem_id: ARR_ARRAY_TEMPERATURE_BALANCE__2156
display_id: NTB-ARR-2156
slug: array-temperature-balance
title: "Array Temperature Balance"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - array-temperature-balance
  - arrays
  - coding-interviews
  - data-structures
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Array Temperature Balance

## Problem Statement

Given an array `a1..an`, define the normalized value of each element as `|a_i|`. Find the smallest index `i` such that:

```
sum_{j=1}^{i-1} |a_j| = sum_{j=i+1}^{n} |a_j|
```

If no such index exists, output `-1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: the smallest pivot index `i`, or `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The element at index `i` is not included in either sum.
- Indices are 1-based in the output.

## Example Input

```
4
1 -1 2 -2
```

## Example Output

```
3
```
