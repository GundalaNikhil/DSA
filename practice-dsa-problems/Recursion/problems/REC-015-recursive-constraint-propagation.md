---
problem_id: REC_RECURSIVE_CONSTRAINT_PROPAGATION__4131
display_id: NTB-REC-4131
slug: recursive-constraint-propagation
title: "Recursive Constraint Propagation"
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
  - recursive-constraint-propagation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Constraint Propagation

## Problem Statement

You are given a rooted tree. Each node has a value `v`. A recursive check passes down an allowed range `[L, R]`. At node `u`, the range tightens to `[L + v_u, R - v_u]` for its children. If `L > R` at any point, the subtree is invalid.

Determine whether the entire tree is valid starting with range `[L0, R0]` at the root.

## Input Format

- First line: integers `n`, `L0`, `R0`
- Next `n` lines: `value parent` (parent is 0 for root)

## Output Format

- `YES` if valid, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= values, L0, R0 <= 10^9`

## Clarifying Notes

- Range tightening happens before visiting children.

## Example Input

```
3 0 5
2 0
1 1
1 1
```

## Example Output

```
YES
```
