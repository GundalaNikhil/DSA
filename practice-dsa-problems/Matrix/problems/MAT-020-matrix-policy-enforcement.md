---
problem_id: MAT_MATRIX_POLICY_ENFORCEMENT__9206
display_id: NTB-MAT-9206
slug: matrix-policy-enforcement
title: "Matrix Policy Enforcement"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - data-structures
  - grids
  - matrix
  - matrix-policy-enforcement
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Policy Enforcement

## Problem Statement

You are given a matrix and a list of policies. Each policy applies to all `2 x 2` blocks:

- `SUM_LE X`: the sum of the 2 x 2 block must be `<= X`
- `HAS_ZERO`: the 2 x 2 block must contain at least one zero

Report all violations.

## Input Format

- First line: integers `n`, `m`, `p`
- Next `n` lines: `m` integers (matrix)
- Next `p` lines: policies (either `SUM_LE X` or `HAS_ZERO`)

## Output Format

- First line: integer `v`, number of violations
- Next `v` lines: `policy_id r c` where `r, c` are the top-left indices of the violating 2 x 2 block

## Constraints

- `2 <= n, m <= 500`
- `1 <= p <= 200000`
- `-10^9 <= matrix values <= 10^9`

## Clarifying Notes

- Policy ids are 1-based in input order.
- Output violations in increasing `policy_id`, then increasing `r`, then `c`.

## Example Input

```
2 3 2
1 2 3
4 0 6
SUM_LE 6
HAS_ZERO
```

## Example Output

```
1
1 1 2
```
