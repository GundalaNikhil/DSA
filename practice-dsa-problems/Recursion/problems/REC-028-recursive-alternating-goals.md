---
problem_id: REC_RECURSIVE_ALTERNATING_GOALS__7710
display_id: NTB-REC-7710
slug: recursive-alternating-goals
title: "Recursive Alternating Goals"
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
  - recursive-alternating-goals
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Alternating Goals

## Problem Statement

You are given a rooted tree where each node has a value. Define a recursive evaluation with alternating goals:

- At even depth (root depth 0), a node returns the maximum of its children's results.
- At odd depth, a node returns the minimum of its children's results.
- A leaf node returns its own value.

Compute the value returned by the root.

## Input Format

- First line: integer `n`
- Next `n` lines: `value parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= value <= 10^9`

## Clarifying Notes

- If an internal node has only one child, the max/min is that child's value.
- Depth is measured from the root.

## Example Input

```
5
3 0
1 1
4 1
2 2
6 2
```

## Example Output

```
2
```
