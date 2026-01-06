---
problem_id: SEG_PERSISTENT_SEGMENT_TREE_HISTORICAL_QUERIES__8670
display_id: NTB-SEG-8670
slug: persistent-segment-tree-historical-queries
title: "Persistent Segment Tree for Historical Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Segment Tree
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - persistent-segment-tree-historical-queries
  - range-queries
  - segmenttree
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Persistent Segment Tree for Historical Queries

## Problem Statement

You are given an initial array `a1..an`. Each update creates a **new version** of the array by modifying a single index. Queries can be performed on any version.

- Version `0` is the initial array.
- Each update creates the next version ID in order: `1, 2, 3, ...`.

Support two operations:

- `U v idx val`: create a new version based on version `v` where `a[idx]` becomes `val`.
- `Q v l r`: return the sum of `a[l..r]` in version `v`.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: operations `U` or `Q` as defined above

## Output Format

- For each `Q` operation, output the range sum on its own line

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, val <= 10^9`
- `1 <= idx <= n`
- `1 <= l <= r <= n`

## Clarifying Notes

- Updates do not modify earlier versions.
- Version IDs are 0-based, and update operations always create the next version ID.
- The intended data structure is a persistent segment tree with `O(log n)` per operation.

## Example Input

```
5 5
1 2 3 4 5
Q 0 1 3
U 0 3 10
Q 1 2 4
U 1 5 -2
Q 2 4 5
```

## Example Output

```
6
16
2
```
