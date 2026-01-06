---
problem_id: GRP_SHORTEST_PATH_COLOR_SEGMENTS__2327
display_id: NTB-GRP-2327
slug: shortest-path-color-segments
title: "Shortest Path with Color Precedence and Segment Length Limit"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - graphs
  - search
  - shortest-path-color-segments
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Shortest Path with Color Precedence and Segment Length Limit

## Problem Statement

You are given a directed weighted graph where each node has a color in `1..C`. A valid path from `S` to `T` must satisfy:

1. The path is composed of contiguous color segments (maximal consecutive nodes of the same color).
2. Each segment length is at most `K` nodes.
3. Each color may appear in at most one segment in the entire path.
4. Precedence rules form a DAG over colors. If `(a → b)` is a rule, then the segment of color `a` (if used) must appear before the segment of color `b` (if used).

Find the minimum-cost valid path from `S` to `T`.

## Input Format

- First line: `n`, `m`, `C`, `K`
- Second line: `n` integers `color[1] ... color[n]`
- Next `m` lines: `u v w`
- Next line: `P` (number of precedence rules)
- Next `P` lines: `a b` (precedence rule: color `a` before color `b`)
- Last line: `S`, `T`

## Output Format

- Single integer: Minimum path cost, or `-1` if impossible.

## Constraints

- `2 <= n <= 3*10^4`
- `1 <= m <= 6*10^4`
- `1 <= C <= 18`
- `1 <= K <= 10`
- `1 <= w <= 10^9`
- Precedence rules form a DAG.

## Clarifying Notes

- Starting node begins the first segment.
- Moving to a node of a new color starts a new segment.
- Returning to an old color is forbidden by rule #3.

## Example Input

```
5 6 3 2
1 2 2 3 3
1 2 5
2 3 5
3 4 5
4 5 5
1 4 15
2 5 10
1
1 3
1 5
```

## Example Output

```
20
```
