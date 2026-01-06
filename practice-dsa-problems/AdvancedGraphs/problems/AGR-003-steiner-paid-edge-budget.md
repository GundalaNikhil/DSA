---
problem_id: AGR_STEINER_PAID_EDGE_BUDGET__1346
display_id: NTB-AGR-1346
slug: steiner-paid-edge-budget
title: "Steiner Connection with Paid-Edge Budget"
difficulty: Medium
difficulty_score: 50
topics:
  - Advanced Graphs
tags:
  - advanced-algorithms
  - advancedgraphs
  - algorithms
  - coding-interviews
  - data-structures
  - graph-theory
  - network-flow
  - steiner-paid-edge-budget
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Steiner Connection with Paid-Edge Budget

## Problem Statement

You are given an undirected graph with `k` terminal nodes that must be connected.

Each edge has:

- `paid` ∈ {0, 1} (whether using it consumes 1 unit of budget)
- `activation cost` `a` (paid if the edge is included in the final connected subgraph)

You may choose a connected subgraph that connects all terminals using at most `B` paid edges. Minimize the sum of activation costs of all edges used.

## Input Format

- First line: `n`, `m`, `k`, `B`
- Second line: `k` terminals `t1 ... tk`
- Next `m` lines: `u v paid a`

## Output Format

- Single integer: Minimum activation cost, or `-1` if impossible.

## Constraints

- `2 <= k <= 10`
- `2 <= n <= 5000`
- `1 <= m <= 10^4`
- `0 <= B <= 30`
- `paid` ∈ {0, 1}
- `0 <= a <= 10^9`

## Clarifying Notes

- Budget counts only the number of edges with `paid=1` that are used.
- Activation cost is counted once per used edge in the final subgraph.

## Example Input

```
5 6 3 1
1 3 5
1 2 1 2
2 3 0 2
3 4 0 5
4 5 0 5
1 4 1 1
2 5 0 9
```

## Example Output

```
14
```
