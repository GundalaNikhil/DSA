---
problem_id: SEG_INVERSION_COUNT_WEIGHTED_PENALTIES__1757
display_id: NTB-SEG-1757
slug: inversion-count-weighted-penalties
title: "Inversion Count with Weighted Penalties"
difficulty: Medium
difficulty_score: 50
topics:
  - Segment Tree
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - inversion-count-weighted-penalties
  - range-queries
  - segmenttree
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Inversion Count with Weighted Penalties

## Problem Statement

You are given an array `a1..an` and an integer percentage `P` (0 to 100). An inversion is a pair `(i, j)` with `i < j` and `a_i > a_j`.

Define the **high-value set** `H` as the indices of the top `ceil(P * n / 100)` elements when the array is sorted by value descending. If values tie, the smaller index comes first in the ranking.

Each inversion has a penalty cost:

- Cost = 2 if `i` is in `H` or `j` is in `H`
- Cost = 1 otherwise

Compute the total penalty-adjusted inversion count.

## Input Format

- First line: integers `n` and `P`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: total penalty-adjusted inversion count

## Constraints

- `1 <= n <= 200000`
- `0 <= P <= 100`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The high-value set size is `ceil(P * n / 100)`.
- If multiple elements share the same value, smaller indices are ranked earlier.
- The intended solution uses a Fenwick Tree (Binary Indexed Tree) or a segment tree.

## Example Input

```
5 40
4 1 3 2 5
```

## Example Output

```
7
```
