---
problem_id: ARR_SUBARRAY_XOR_RANK__3329
display_id: NTB-ARR-3329
slug: subarray-xor-rank
title: "Subarray XOR Rank Queries"
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
  - subarray-xor-rank
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Subarray XOR Rank Queries

## Problem Statement

Given an array `a1..an` and an integer `K`, consider the XOR value of every subarray. There are `n * (n + 1) / 2` subarrays in total.

Find the `K`-th smallest XOR value among all subarrays (1-based). If `K` is outside the valid range, output `-1`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: the `K`-th smallest subarray XOR, or `-1`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n * (n + 1) / 2`
- `0 <= a_i <= 10^9`

## Clarifying Notes

- XOR is computed using bitwise XOR.
- The `K`-th smallest is based on ascending order of values.

## Example Input

```
2 2
1 2
```

## Example Output

```
2
```
