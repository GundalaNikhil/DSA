---
problem_id: GRP_LAYERED_MANDATORY_ORDER__5831
display_id: NTB-GRP-5831
slug: layered-mandatory-order
title: "Shortest Path with Mandatory Layer Ordering"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - graphs
  - layered-mandatory-order
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Shortest Path with Mandatory Layer Ordering

## Problem Statement

Nodes belong to layers `1..L`. A path is valid only if along every used edge `u → v`, `layer[v] > layer[u]` (strictly increasing layers; you may skip layers).

Find the minimum path cost from `S` to `T`.

## Input Format

- First line: `n`, `m`, `L`
- Second line: `n` integers `layer[1] ... layer[n]`
- Next `m` lines: `u v w`
- Last line: `S`, `T`

## Output Format

- Single integer: Minimum cost, or `-1`.

## Constraints

- `2 <= n <= 10^5`
- `1 <= m <= 2*10^5`
- `1 <= L <= 50`
- `1 <= w <= 10^9`

## Clarifying Notes

- Edges violating `layer[v] > layer[u]` are unusable.
- This is effectively a shortest path on a DAG formed by layer constraints.

## Example Input

```
4 4 3
1 2 3 3
1 2 1
2 3 1
3 4 1
1 4 10
1 4
```

## Example Output

```
3
```
