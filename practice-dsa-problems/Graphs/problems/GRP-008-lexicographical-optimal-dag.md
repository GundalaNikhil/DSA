---
problem_id: GRP_LEXICOGRAPHICAL_OPTIMAL_DAG__4697
display_id: NTB-GRP-4697
slug: lexicographical-optimal-dag
title: "Lexicographically Optimal Path with One-Time Node Rewards (DAG)"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - graphs
  - lexicographical-optimal-dag
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Lexicographically Optimal Path with One-Time Node Rewards (DAG)

## Problem Statement

You are given a directed acyclic graph (DAG) with edge costs `w` and node resources `resource[v]` (which may be negative).

Find a path from `S` to `T` that optimizes lexicographically in this order:

1. Minimize total edge cost.
2. Maximize total collected resource.
3. Minimize number of edges.

Resource for a node is collected once when the node is visited. Since the graph is a DAG, no node can be visited more than once in a path.

## Input Format

- First line: `n`, `m`
- Second line: `resource[1] ... resource[n]`
- Next `m` lines: `u v w`
- Last line: `S`, `T`

## Output Format

- If reached: `min_cost max_resource path_length`
- If impossible: `-1`

## Constraints

- `2 <= n <= 2*10^5`
- `1 <= m <= 3*10^5`
- `-10^3 <= resource[i] <= 10^3`
- `1 <= w <= 10^9`
- The graph is a DAG.

## Example Input

```
4 5
10 -5 20 15
1 2 5
2 3 5
3 4 5
1 3 10
3 4 5
1 4
```

## Example Output

```
15 45 2
```
