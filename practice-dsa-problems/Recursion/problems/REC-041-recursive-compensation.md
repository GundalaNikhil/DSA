---
problem_id: REC_RECURSIVE_COMPENSATION__7674
display_id: NTB-REC-7674
slug: recursive-compensation
title: "Recursive Compensation"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-compensation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Compensation

## Problem Statement

You are given a rooted tree. Each node has a value `v` and a required threshold `T`. A node is successful if the sum of its own value and the values of its successful children is at least `T`.

If a child fails, you must pay that child's compensation cost `c[child]`, and its value does not contribute to the parent.

Compute the total compensation cost needed for the root to be successful. If the root cannot be successful, output `IMPOSSIBLE`.

## Input Format

- First line: integer `n`
- Next `n` lines: `v T c parent` (parent is 0 for root)

## Output Format

- Single integer: total compensation cost, or `IMPOSSIBLE`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= v <= 10^9`
- `-10^15 <= T <= 10^15`
- `0 <= c <= 10^9`

## Clarifying Notes

- Compensation is paid only for failed children that were evaluated.
- A leaf succeeds if `v >= T`.

## Example Input

```
4
5 8 3 0
2 3 4 1
1 5 2 1
6 6 1 2
```

## Example Output

```
4
```
