---
problem_id: REC_RECURSION_WITH_CASCADING_SIDE_EFFECTS__2487
display_id: NTB-REC-2487
slug: recursion-with-cascading-side-effects
title: "Recursion with Cascading Side Effects"
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
  - recursion-with-cascading-side-effects
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursion with Cascading Side Effects

## Problem Statement

You are given a rooted tree. A pre-order traversal visits children in increasing node id order. Each node `u` has value `val_u` and side effect `s_u`.

When node `u` is visited, its side effect decreases the value of **all nodes not yet visited** by `s_u` (values may become negative). The traversal then continues with the updated values.

Compute the total sum of values at the moment each node is visited.

## Input Format

- First line: integer `n`
- Next `n` lines: `val_u s_u parent` (parent is 0 for root)

## Output Format

- Single integer: total sum

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= val_u, s_u <= 10^9`

## Clarifying Notes

- Side effects apply to all unvisited nodes globally, not just siblings.

## Example Input

```
3
5 1 0
4 2 1
3 0 1
```

## Example Output

```
9
```
