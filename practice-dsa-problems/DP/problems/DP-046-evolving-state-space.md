---
problem_id: DP_EVOLVING_STATE_SPACE__3887
display_id: NTB-DP-3887
slug: evolving-state-space
title: "DP over Evolving State Space"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - evolving-state-space
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP over Evolving State Space

## Problem Statement

You move through a directed graph over `n` steps. The graph evolves: at step `t`, a set of edges becomes available. You start at node 1. Taking an edge yields reward `w` for that edge.

Maximize total reward after exactly `n` steps.

## Input Format

- First line: integers `n`, `m`, `e`
- Next `e` lines: `t u v w` meaning edge `u -> v` with reward `w` becomes available at step `t` (1-based)

## Output Format

- Single integer: maximum total reward, or `-1` if no walk of length `n` exists

## Constraints

- `1 <= n <= 200`
- `1 <= m <= 200`
- `1 <= e <= 5000`
- `-10^9 <= w <= 10^9`

## Clarifying Notes

- An edge remains available after its activation time.
- You must take exactly one edge per step.

## Example Input

```
3 3 3
1 1 2 5
2 2 3 4
1 1 3 1
```

## Example Output

```
9
```
