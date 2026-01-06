---
problem_id: LNK_ALTERNATING_DIRECTION_TRAVERSAL__9754
display_id: NTB-LNK-9754
slug: alternating-direction-traversal
title: "Alternating Direction Traversal"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - alternating-direction-traversal
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Alternating Direction Traversal

## Problem Statement

You are given a doubly linked list of `n` nodes. Starting from the head, traverse the list in blocks of size `K`, alternating direction after each block. The first block moves forward. If the traversal cannot complete a block due to reaching the end, it stops.

Output the sequence of visited values.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers: node values in order

## Output Format

- One line with the visited values separated by spaces

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`

## Clarifying Notes

- When direction switches, continue from the current node.
- The head is visited first.

## Example Input

```
7 2
1 2 3 4 5 6 7
```

## Example Output

```
1 2 2 1 1 2
```
