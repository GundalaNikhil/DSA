---
problem_id: ARR_TWO_SUM_COST_OPTIMIZATION__8919
display_id: NTB-ARR-8919
slug: two-sum-cost-optimization
title: "Two Sum with Cost Optimization"
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
  - technical-interview-prep
  - two-pointers
  - two-sum-cost-optimization
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Two Sum with Cost Optimization

## Problem Statement

You are given two arrays of length `n`: values `a1..an` and costs `c1..cn`, and a target sum `T`. Find a pair of indices `(i, j)` with `i < j` such that `a_i + a_j = T`.

Among all valid pairs, choose the one with minimum `c_i + c_j`. If there is still a tie, choose the pair with the smallest `i`, and then the smallest `j`.

If no valid pair exists, output `-1`.

## Input Format

- First line: integers `n` and `T`
- Second line: `n` integers `a1 a2 ... an`
- Third line: `n` integers `c1 c2 ... cn`

## Output Format

- If a pair exists: output two integers `i j`
- Otherwise: output `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i, T <= 10^9`
- `0 <= c_i <= 10^9`

## Clarifying Notes

- Indices are 1-based in the output.
- Each index can be used at most once.

## Example Input

```
5 5
4 2 7 1 3
5 2 6 1 4
```

## Example Output

```
1 4
```
