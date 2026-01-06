---
problem_id: ARR_ARRAY_PROBABILISTIC_WEIGHTS__8756
display_id: NTB-ARR-8756
slug: array-probabilistic-weights
title: "Array with Probabilistic Weights (Deterministic Input)"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - array-probabilistic-weights
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

# Array with Probabilistic Weights (Deterministic Input)

## Problem Statement

You are given an array of values `a1..an` and inclusion probabilities `p1..pn` in per-mille units (0 to 1000). Each element `a_i` contributes to a random sum with probability `p_i / 1000` and contributes `0` otherwise.

For any subarray, its **expected sum** equals:

```
E = sum(a_i * p_i) for i in the subarray
```

Compute the maximum expected sum over all non-empty subarrays. Output the maximum expected sum multiplied by `1000` (i.e., the integer value of `sum(a_i * p_i)`).

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`
- Third line: `n` integers `p1 p2 ... pn` (0..1000)

## Output Format

- Single integer: maximum expected sum times `1000`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`
- `0 <= p_i <= 1000`

## Clarifying Notes

- There is no randomness in the computation; probabilities are inputs used to compute expectations.
- The result fits in signed 64-bit if computed as `sum(a_i * p_i)`.

## Example Input

```
4
5 -2 3 1
1000 500 1000 250
```

## Example Output

```
7750
```
