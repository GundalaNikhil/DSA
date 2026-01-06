---
problem_id: REC_RECURSION_WITH_ADAPTIVE_DEPTH__6121
display_id: NTB-REC-6121
slug: recursion-with-adaptive-depth
title: "Recursion with Adaptive Depth"
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
  - recursion-with-adaptive-depth
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursion with Adaptive Depth

## Problem Statement

You are given a rooted tree. Each node has a value `v` and a depth adjustment `delta`. A recursive evaluation starts at the root with an initial depth limit `L`.

Define `Eval(node, limit)` as:

- If `limit < 0`, return `0`.
- Otherwise return `v[node] + sum(Eval(child, limit + delta[node]))` over all children.

Compute the value returned at the root.

## Input Format

- First line: integers `n` and `L`
- Next `n` lines: `v delta parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `-50 <= L <= 50`
- `-5 <= delta <= 5`
- `-10^9 <= v <= 10^9`

## Clarifying Notes

- The adaptive depth limit applies independently to each subtree call.
- If `limit` becomes negative at a node, none of its children are evaluated.

## Example Input

```
4 1
5 -1 0
3 0 1
2 1 1
4 -2 2
```

## Example Output

```
10
```
