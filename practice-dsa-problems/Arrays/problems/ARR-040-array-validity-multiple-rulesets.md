---
problem_id: ARR_ARRAY_VALIDITY_MULTIPLE_RULESETS__9217
display_id: NTB-ARR-9217
slug: array-validity-multiple-rulesets
title: "Array Validity Under Multiple Rulesets"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - array-validity-multiple-rulesets
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

# Array Validity Under Multiple Rulesets

## Problem Statement

You are given an array `a1..an` and a list of `r` rules. Each rule is one of the following types:

- `MAX l r x`: the maximum value in `a[l..r]` must be `<= x`
- `MIN l r x`: the minimum value in `a[l..r]` must be `>= x`
- `SUM l r x`: the sum of `a[l..r]` must be `<= x`

Initially, no rule is active. You are then given `q` toggle operations. Each toggle activates a rule if it is inactive, or deactivates it if it is active. After each toggle, output whether the array satisfies **all active rules**.

## Input Format

- First line: integers `n`, `r`, and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `r` lines: one rule per line in the formats above
- Next `q` lines: `TOGGLE id` where `id` is 1-based rule index

## Output Format

- For each toggle, output `VALID` if all active rules are satisfied, otherwise `INVALID`

## Constraints

- `1 <= n, r, q <= 200000`
- `-10^9 <= a_i, x <= 10^9`
- `1 <= l <= r <= n`

## Clarifying Notes

- Rules are checked against the current fixed array; there are no value updates.
- Multiple active rules of different types can overlap.

## Example Input

```
5 2 3
1 2 3 4 5
MAX 1 3 3
SUM 2 5 12
TOGGLE 1
TOGGLE 2
TOGGLE 2
```

## Example Output

```
VALID
INVALID
VALID
```
