---
problem_id: GRP_SCC_CONDENSATION_BOTTLENECK__1869
display_id: NTB-GRP-1869
slug: scc-condensation-bottleneck
title: "SCC Condensation with Minimum Capacity Path"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - graphs
  - scc-condensation-bottleneck
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SCC Condensation with Minimum Capacity Path

## Problem Statement

Each node has a capacity. Collapse SCCs into a DAG. The capacity of an SCC is defined as the **minimum** capacity among all its nodes.

A path's bottleneck is the minimum SCC-capacity along the path. Find the maximum possible bottleneck capacity from `S` to `T`.

## Input Format

- First line: `n`, `m`
- Second line: `n` integers `capacity[1] ... capacity[n]`
- Next `m` lines: `u v` (directed edges)
- Last line: `S`, `T`

## Output Format

- Single integer: Maximum achievable bottleneck capacity, or `0` if unreachable.

## Constraints

- `2 <= n <= 2*10^5`
- `1 <= m <= 3*10^5`
- `1 <= capacity[i] <= 10^9`

## Clarifying Notes

- Bottleneck is taken over the capacities of SCCs encountered on the condensation path.

## Example Input

```
5 6
10 20 5 30 15
1 2
2 3
3 2
3 4
4 5
1 4
1 5
```

## Example Output

```
10
```
