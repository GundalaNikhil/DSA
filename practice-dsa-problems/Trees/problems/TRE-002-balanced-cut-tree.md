---
problem_id: TRE_BALANCED_CUT_TREE__4033
display_id: NTB-TRE-4033
slug: balanced-cut-tree
title: "Minimum Cut Edge in a Tree with Balance and Forced Sides"
difficulty: Medium
difficulty_score: 50
topics:
  - Trees
tags:
  - algorithms
  - balanced-cut-tree
  - binary-trees
  - coding-interviews
  - data-structures
  - technical-interview-prep
  - traversal
  - trees
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Minimum Cut Edge in a Tree with Balance and Forced Sides

## Problem Statement

You are given a connected tree with weighted edges. Removing exactly one edge splits it into two connected components `A` and `B`.

You are also given two disjoint node sets `X` and `Y`. A split is valid if:

1. All nodes in `X` are in `A`.
2. All nodes in `Y` are in `B`.
3. `| |A| - |B| | <= threshold`.

Among all valid splits, minimize the weight of the removed edge.

## Input Format

- First line: `n`, `threshold`
- Next `n-1` lines: `u v w`
- Next line: `xCount x1 x2 ... xCount`
- Next line: `yCount y1 y2 ... yCount`

## Output Format

- Single integer: Minimum removable edge weight, or `-1` if impossible.

## Constraints

- `4 <= n <= 2*10^5`
- `0 <= threshold <= n`
- `1 <= w <= 10^9`
- `X ∩ Y = ∅, |X| >= 1, |Y| >= 1`

## Clarifying Notes

- Exactly one edge must be removed.
- Components are labeled such that `A` contains `X` and `B` contains `Y`.

## Example Input

```
6 1
1 2 5
2 3 4
3 4 7
4 5 3
4 6 6
2 1 2
1 6
```

## Example Output

```
7
```
