---
problem_id: REC_RECURSIVE_VOTING_SYSTEMS__3271
display_id: NTB-REC-3271
slug: recursive-voting-systems
title: "Recursive Voting Systems"
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
  - recursive-voting-systems
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Voting Systems

## Problem Statement

You are given a rooted tree. Each node has a base value `v`. There are `S` recursive strategies, each defined by an operator applied to child results:

- `SUM`: sum of child results
- `MIN`: minimum of child results
- `MAX`: maximum of child results

For each node and each strategy `s`, compute `value_s(node)` by applying the strategy operator to its children's `value_s`, then adding `v[node]`. A leaf uses `value_s(node) = v[node]`.

The node's final value is the median of the `S` strategy values (with `S` guaranteed to be odd).

Compute the final value of the root.

## Input Format

- First line: integers `n` and `S`
- Second line: `S` strings describing the strategies (each is `SUM`, `MIN`, or `MAX`)
- Next `n` lines: `v parent` (parent is 0 for root)

## Output Format

- Single integer: root final value

## Constraints

- `1 <= n <= 200000`
- `1 <= S <= 5`, `S` is odd
- `-10^9 <= v <= 10^9`

## Clarifying Notes

- `MIN` and `MAX` are computed over the children only; then `v[node]` is added.
- If a node has no children, the operator is ignored and `value_s = v[node]`.

## Example Input

```
4 3
SUM MIN MAX
5 0
2 1
7 1
1 2
```

## Example Output

```
12
```
