---
problem_id: REC_RECURSIVE_GARBAGE_COLLECTOR__9837
display_id: NTB-REC-9837
slug: recursive-garbage-collector
title: "Recursive Garbage Collector"
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
  - recursive-garbage-collector
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Garbage Collector

## Problem Statement

You are given a directed graph of objects and a set of root objects. A mark phase uses recursion, but the call stack has a depth limit `L`.

The algorithm works as follows:

- Perform a recursive DFS from each root.
- If the recursion depth would exceed `L`, stop recursing and enqueue that node for an iterative phase.
- After all recursive calls complete, process the queued nodes with an iterative DFS (no depth limit).

Compute how many objects are marked by the recursive phase and how many by the iterative phase.

## Input Format

- First line: integers `n`, `m`, `r`, and `L`
- Second line: `r` integers, the root nodes
- Next `m` lines: directed edges `u v`

## Output Format

- Two integers: `recursive_marked` and `iterative_marked`

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `1 <= r <= n`
- `0 <= L <= 200000`

## Clarifying Notes

- A node is marked at most once; if already marked, it is not added again.
- The iterative phase processes all queued nodes after recursion finishes.

## Example Input

```
5 5 1 1
1
1 2
2 3
3 4
4 5
2 5
```

## Example Output

```
2 3
```
