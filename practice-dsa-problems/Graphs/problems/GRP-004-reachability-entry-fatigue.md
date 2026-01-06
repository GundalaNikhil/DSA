---
problem_id: GRP_REACHABILITY_ENTRY_FATIGUE__4036
display_id: NTB-GRP-4036
slug: reachability-entry-fatigue
title: "Reachability Under Entry-Fatigue Constraints"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - graphs
  - reachability-entry-fatigue
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Reachability Under Entry-Fatigue Constraints

## Problem Statement

You are given an undirected graph with `n` nodes and `m` edges. Each node `v` has a fatigue cost `fatigue[v]`.

Starting at node `S`, you pay `fatigue[S]` once immediately. Every time you traverse an edge into node `v`, you additionally pay `fatigue[v]`. Revisiting a node costs you its fatigue each time you enter it.

Determine whether there exists a path from `S` to `T` with total fatigue cost ≤ `F`.

## Input Format

- First line: `n`, `m`, `F`
- Second line: `n` integers `fatigue[1] ... fatigue[n]`
- Next `m` lines: `u v` (undirected edges)
- Last line: `S`, `T`

## Output Format

- `YES` if reachable within budget, else `NO`.

## Constraints

- `2 <= n <= 10^5`
- `1 <= m <= 2*10^5`
- `0 <= F <= 10^14`
- `1 <= fatigue[i] <= 10^9`

## Clarifying Notes

- The cost is paid on entry EACH time you move into a node.
- The start node's fatigue is counted exactly once at the beginning.

## Example Input

```
5 5 7
1 2 3 2 4
1 2
2 3
3 4
4 5
1 5
1 5
```

## Example Output

```
YES
```
