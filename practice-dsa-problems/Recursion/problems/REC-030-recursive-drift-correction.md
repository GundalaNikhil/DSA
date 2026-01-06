---
problem_id: REC_RECURSIVE_DRIFT_CORRECTION__9520
display_id: NTB-REC-9520
slug: recursive-drift-correction
title: "Recursive Drift Correction"
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
  - recursive-drift-correction
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Drift Correction

## Problem Statement

You are given a rooted tree. Each node has a value `v`. Define a recursive sum:

- `sum(node) = v[node] + sum(child sums)`

To prevent drift, apply correction at depths that are multiples of `P` (including depth 0):

- Replace `sum(node)` by the nearest multiple of `K`.
- If exactly halfway between two multiples, round down.

Compute the corrected sum at the root.

## Input Format

- First line: integers `n`, `P`, `K`
- Next `n` lines: `v parent` (parent is 0 for root)

## Output Format

- Single integer: corrected sum at the root

## Constraints

- `1 <= n <= 200000`
- `1 <= P <= 200000`
- `1 <= K <= 10^9`
- `-10^9 <= v <= 10^9`

## Clarifying Notes

- Correction is applied after all children of a node are processed.
- Depth of root is 0.

## Example Input

```
3 1 5
6 0
2 1
4 1
```

## Example Output

```
10
```
