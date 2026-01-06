---
problem_id: ARR_SUBARRAY_COST_SUM_TIMES_GCD__7348
display_id: NTB-ARR-7348
slug: subarray-cost-sum-times-gcd
title: "Subarray Cost = sum x gcd"
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
  - subarray-cost-sum-times-gcd
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Subarray Cost = sum x gcd

## Problem Statement

Given an array `a1..an`, define the cost of a subarray as:

```
cost = (sum of elements in the subarray) * (gcd of elements in the subarray)
```

Find the maximum cost over all subarrays.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum subarray cost

## Constraints

- `1 <= n <= 200000`
- `1 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.
- GCD is computed over the absolute values of elements.

## Example Input

```
3
2 4 6
```

## Example Output

```
36
```
