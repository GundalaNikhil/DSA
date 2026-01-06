---
problem_id: DP_RESOURCE_CONVERSION__3837
display_id: NTB-DP-3837
slug: resource-conversion
title: "Resource Conversion DP"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - resource-conversion
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Resource Conversion DP

## Problem Statement

You have `r` resource types with integer quantities. Over `n` steps, you may perform at most one conversion per step. A conversion from type `i` to type `j` multiplies by a rational rate `p/q` and floors the result.

Maximize the final amount of resource type 1 after `n` steps.

## Input Format

- First line: integers `n` and `r`
- Second line: `r` integers: initial quantities
- Third line: integer `c` (number of conversions)
- Next `c` lines: `i j p q`

## Output Format

- Single integer: maximum possible amount of resource type 1 after `n` steps

## Constraints

- `1 <= n <= 30`
- `1 <= r <= 5`
- `0 <= quantity <= 50`
- `1 <= c <= 10`
- `1 <= p, q <= 10`

## Clarifying Notes

- Each step can apply at most one conversion or skip.
- State includes step and capped resource amounts.

## Example Input

```
2 2
10 0
1
1 2 1 2
```

## Example Output

```
10
```
