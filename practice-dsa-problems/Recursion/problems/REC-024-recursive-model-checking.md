---
problem_id: REC_RECURSIVE_MODEL_CHECKING__8669
display_id: NTB-REC-8669
slug: recursive-model-checking
title: "Recursive Model Checking"
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
  - recursive-model-checking
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Model Checking

## Problem Statement

You are given a directed graph of system states. Each state is one of:

- `T`: terminal state with fixed value `0` or `1`
- `A`: universal state (all successors must satisfy the property)
- `E`: existential state (at least one successor must satisfy the property)

You are also given a step limit `K`. Define `Check(node, k)` as:

- If `k == 0` and the node is not terminal, return `0`.
- If the node is terminal, return its fixed value.
- If the node is type `A`, return `1` if all successors return `1` with `k-1`, else `0`.
- If the node is type `E`, return `1` if any successor returns `1` with `k-1`, else `0`.

Compute `Check(S, K)` for the given start state `S`.

## Input Format

- First line: integers `n`, `m`, `K`, `S`
- Next `n` lines: `type value` where `type` is `T`, `A`, or `E`
  - For non-terminal nodes, `value` is ignored
- Next `m` lines: directed edges `u v`

## Output Format

- Single integer: `0` or `1`

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `0 <= K <= 60`
- `1 <= S <= n`

## Clarifying Notes

- The step limit is strict: only `K` transitions are allowed.
- If a non-terminal node has no outgoing edges, it evaluates to `0` unless it is terminal.

## Example Input

```
4 4 2 1
A 0
E 0
T 1
T 0
1 2
1 3
2 4
2 3
```

## Example Output

```
1
```
