---
problem_id: REC_RECURSIVE_DECISION_TREE_WITH_MEMORY__5756
display_id: NTB-REC-5756
slug: recursive-decision-tree-with-memory
title: "Recursive Decision Tree with Memory"
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
  - recursive-decision-tree-with-memory
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Decision Tree with Memory

## Problem Statement

You build a binary string of length `n` using recursion. At each step you choose `0` or `1`. The choice is constrained by the last `L` characters chosen so far (memory window). You are given a set of forbidden length-`L` patterns; you may not choose a next bit if it would make the last `L` bits equal to a forbidden pattern.

Each complete string has a value given by a lookup table. Find the maximum value achievable.

## Input Format

- First line: integers `n` and `L`
- Second line: integer `f` (number of forbidden patterns)
- Next `f` lines: binary strings of length `L`
- Next line: integer `v` (number of value entries)
- Next `v` lines: `string value` (binary string of length `n` and its value)

Unlisted strings have value 0.

## Output Format

- Single integer: maximum achievable value

## Constraints

- `1 <= n <= 20`
- `1 <= L <= n`
- `0 <= f <= 2^L`
- `0 <= v <= 2^n`
- `-10^9 <= value <= 10^9`

## Clarifying Notes

- The recursion state includes the last `L` bits (or fewer at the beginning).
- Memory constraint applies once at least `L` bits have been chosen.

## Example Input

```
3 2
1
11
2
000 5
010 7
```

## Example Output

```
7
```
