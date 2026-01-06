---
problem_id: REC_RECURSIVE_BIDIRECTIONAL_SEARCH__7585
display_id: NTB-REC-7585
slug: recursive-bidirectional-search
title: "Recursive Bidirectional Search"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-bidirectional-search
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Bidirectional Search

## Problem Statement

You are given a directed graph with start node `S` and target node `T`. A bidirectional recursive search explores forward from `S` and backward from `T` (using reverse edges).

You are given step limits `L1` and `L2`. Find the minimum `d1 + d2` such that there exists a node `u` with:

- reachable from `S` in `d1` steps, where `0 <= d1 <= L1`
- reachable from `T` in `d2` steps using reverse edges, where `0 <= d2 <= L2`

If no such node exists, output `-1`.

## Input Format

- First line: integers `n`, `m`, `S`, `T`, `L1`, `L2`
- Next `m` lines: directed edges `u v`

## Output Format

- Single integer: minimum `d1 + d2`, or `-1`

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `0 <= L1, L2 <= 60`

## Clarifying Notes

- A node can serve as the meeting point even if it is `S` or `T`.
- If multiple meeting nodes exist, choose the smallest possible `d1 + d2`.

## Example Input

```
5 6 1 5 2 2
1 2
2 3
3 5
1 4
4 5
2 4
```

## Example Output

```
2
```
