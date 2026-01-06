---
problem_id: DP_MEMORY_ALLOCATOR__9258
display_id: NTB-DP-9258
slug: memory-allocator
title: "Memory Allocator DP"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - memory-allocator
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Memory Allocator DP

## Problem Statement

You manage a linear memory of size `M`. You receive `n` allocation requests, each requiring `size_i` units. For each request you may choose any contiguous free block to place it or reject it. The cost of a placement is the number of free segments after placement.

Minimize total cost over all requests.

## Input Format

- First line: integers `M` and `n`
- Second line: `n` integers: request sizes

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= M <= 30`
- `1 <= n <= 20`
- `1 <= size_i <= M`

## Clarifying Notes

- Memory is initially one free segment.
- Rejecting a request adds no cost.

## Example Input

```
5 2
2 3
```

## Example Output

```
1
```
