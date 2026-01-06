---
problem_id: ARR_ARRAY_INFLUENCE_PROPAGATION__2081
display_id: NTB-ARR-2081
slug: array-influence-propagation
title: "Array Influence Propagation"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-influence-propagation
  - array-manipulation
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

# Array Influence Propagation

## Problem Statement

You are given an array `a1..an` and an integer distance `D`. Each element spreads its influence to all positions within distance `D` (inclusive). The final array `b1..bn` is defined as:

```
b_j = sum of a_i for all i such that |i - j| <= D
```

Compute and output the final array `b`.

## Input Format

- First line: integers `n` and `D`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n` integers: the final array `b1 b2 ... bn`

## Constraints

- `1 <= n <= 200000`
- `0 <= D <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Influence uses index distance, not value difference.
- When `D = 0`, the output is the original array.

## Example Input

```
5 1
1 2 3 4 5
```

## Example Output

```
3 6 9 12 9
```
