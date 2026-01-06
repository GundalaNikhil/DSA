---
problem_id: GRP_MIN_COST_PATH_BACKTRACK_PENALTY__2403
display_id: NTB-GRP-2403
slug: min-cost-path-backtrack-penalty
title: "Minimum-Cost Path with Backtrack Edge Penalty"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - graphs
  - min-cost-path-backtrack-penalty
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Minimum-Cost Path with Backtrack Edge Penalty

## Problem Statement

You are given an undirected weighted graph. Each edge `{u, v}` has base cost `w` and backtrack penalty `f`.

If you traverse `u → v` and the very next move traverses the same edge back `v → u`, then that backtrack move costs `w + f` (instead of `w`). All other traversals cost `w`.

Find the minimum cost from `S` to `T`.

## Input Format

- First line: `n`, `m`
- Next `m` lines: `u v w f`
- Last line: `S`, `T`

## Output Format

- Single integer: Minimum achievable cost, or `-1` if unreachable.

## Constraints

- `2 <= n <= 10^5`
- `1 <= m <= 2*10^5`
- `1 <= w <= 10^9`
- `0 <= f <= 10^9`

## Clarifying Notes

- Only an immediate reversal on the same edge triggers the penalty.
- Consecutive pattern `u → v → u` triggers the penalty on the second move ONLY.

## Example Input

```
4 4
1 2 5 100
2 3 5 100
3 4 5 100
1 4 20 0
1 4
```

## Example Output

```
15
```
