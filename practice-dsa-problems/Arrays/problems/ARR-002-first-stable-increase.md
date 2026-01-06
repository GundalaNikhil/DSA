---
problem_id: ARR_FIRST_STABLE_INCREASE__8152
display_id: NTB-ARR-8152
slug: first-stable-increase
title: "First Stable Increase"
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
  - first-stable-increase
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# First Stable Increase

## Problem Statement

Given an array `a1..an`, find the smallest index `i` (1-based) such that:

```
a_i < a_{i+1} < a_{i+2} < a_{i+3}
```

This represents three consecutive day-to-day increases. If no such index exists, output `-1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: the smallest valid index `i`, or `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- A valid sequence requires four consecutive values with three strict increases.
- Indices are 1-based in the output.

## Example Input

```
7
5 6 7 4 5 6 7
```

## Example Output

```
4
```
