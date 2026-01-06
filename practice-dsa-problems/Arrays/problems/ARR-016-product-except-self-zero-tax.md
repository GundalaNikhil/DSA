---
problem_id: ARR_PRODUCT_EXCEPT_SELF_ZERO_TAX__9971
display_id: NTB-ARR-9971
slug: product-except-self-zero-tax
title: "Product Except Self with Zero Tax"
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
  - product-except-self-zero-tax
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Product Except Self with Zero Tax

## Problem Statement

You are given an array `a1..an` and an integer `T` called the zero tax. For each index `i`, compute:

```
P_i = product of all values for j != i
```

where each factor is:

- `a_j` if `a_j != 0`
- `T` if `a_j = 0`

Output all `P_i` modulo `1,000,000,007`.

## Input Format

- First line: integers `n` and `T`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n` integers: `P_1 P_2 ... P_n` modulo `1,000,000,007`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`
- `0 <= T <= 10^9`

## Clarifying Notes

- Negative values should be handled under modulo arithmetic.
- If there are multiple zeros, each contributes a factor of `T`.

## Example Input

```
3 5
2 0 3
```

## Example Output

```
15 6 10
```
