---
problem_id: DP_CAUSAL_GRAPH__2395
display_id: NTB-DP-2395
slug: causal-graph
title: "DP on Causal Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - causal-graph
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Causal Graph

## Problem Statement

You are given a DAG of tasks. Each task has reward `v`. You must choose a path from source `S` to sink `T`. A task can be taken only after all its predecessors on the path are taken (causal ordering).

Maximize total reward along the path.

## Input Format

- First line: integers `n`, `m`
- Second line: integers `S`, `T`
- Third line: `n` integers: rewards
- Next `m` lines: edges `u v`

## Output Format

- Single integer: maximum reward from `S` to `T`, or `-1` if no path

## Constraints

- `1 <= n <= 200000`
- `1 <= m <= 200000`

## Clarifying Notes

- The graph is acyclic.

## Example Input

```
4 4
1 4
1 2 3 4
1 2
2 4
1 3
3 4
```

## Example Output

```
8
```
