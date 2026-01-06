---
problem_id: AGR_MST_POST_PROCESSING_PENALTIES__2495
display_id: NTB-AGR-2495
slug: mst-post-processing-penalties
title: "Minimum Spanning Tree with Post-Processing Penalties"
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
  - mst-post-processing-penalties
  - network-flow
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Minimum Spanning Tree with Post-Processing Penalties

## Problem Statement

You are given a connected, undirected graph with `n` nodes and `m` edges. Each edge has a base weight `w` and a penalty `p`.

Build a minimum spanning tree using **only the base weights** (standard Kruskal on `w`). After the MST is selected, the final cost is:

```
(sum of base weights in the MST) + (sum of penalties of the selected edges)
```

If the graph is not connected, output `-1`.

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w p`

## Output Format

- Single integer: final cost after adding penalties, or `-1` if no spanning tree exists

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `1 <= u, v <= n`
- `-10^9 <= w, p <= 10^9`

## Clarifying Notes

- Edge selection is based **only** on base weight `w` (penalties do not affect the choice).
- Among edges with the same base weight, the algorithm must prioritize edges with a **smaller penalty** to ensure a unique answer.

## Example Input

```
4 5
1 2 1 5
2 3 2 0
3 4 1 1
1 4 3 0
2 4 4 10
```

## Example Output

```
10
```
