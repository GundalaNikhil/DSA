---
problem_id: LNK_WEIGHTED_LINKED_LIST__5454
display_id: NTB-LNK-5454
slug: weighted-linked-list
title: "Weighted Linked List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
  - weighted-linked-list
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Weighted Linked List

## Problem Statement

Each node has a value and a weight. Starting from the head, the traversal cost is the sum of weights of visited nodes. For each query with budget `B`, find the **last node value** that can be visited without exceeding total cost `B`. If even the head exceeds the budget, output `-1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers: node values in order
- Third line: `n` integers: node weights in order
- Fourth line: integer `q`
- Next `q` lines: budget `B`

## Output Format

- For each query, output the value of the last reachable node, or `-1`

## Constraints

- `1 <= n, q <= 200000`
- `0 <= weight <= 10^9`
- Values are 32-bit signed integers

## Clarifying Notes

- Traversal is strictly from head to tail with no skipping.

## Example Input

```
4
5 6 7 8
2 3 5 1
3
2
7
11
```

## Example Output

```
5
6
8
```
