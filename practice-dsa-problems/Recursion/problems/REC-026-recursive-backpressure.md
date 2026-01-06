---
problem_id: REC_RECURSIVE_BACKPRESSURE__5542
display_id: NTB-REC-5542
slug: recursive-backpressure
title: "Recursive Backpressure"
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
  - recursive-backpressure
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Backpressure

## Problem Statement

You are given a rooted tree. Each node has a base value `v` and a capacity `cap`. A recursive evaluation processes children in increasing node index order.

Define `Eval(node)` as returning `(value, backpressure)`:

- Initialize `value = v[node]`, `backpressure = 0`.
- For each child in order:
  - If the child returns `backpressure = 1`, stop processing remaining children and set `backpressure = 1`.
  - Otherwise add the child's `value` to `value`.
  - If `value > cap[node]`, set `value = cap[node]`, `backpressure = 1`, and stop processing remaining children.

Compute the `value` returned by the root.

## Input Format

- First line: integer `n`
- Next `n` lines: `v cap parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= v <= 10^9`
- `-10^9 <= cap <= 10^9`

## Clarifying Notes

- If a node's `value` exceeds its capacity at any point, it immediately signals backpressure.
- The evaluation order is fixed by node index.

## Example Input

```
5
5 10 0
4 6 1
3 20 1
2 5 2
1 7 2
```

## Example Output

```
10
```
