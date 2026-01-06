---
problem_id: LNK_LINKED_LIST_GARBAGE_COLLECTION__6932
display_id: NTB-LNK-6932
slug: linked-list-garbage-collection
title: "Linked List Garbage Collection"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-garbage-collection
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List Garbage Collection

## Problem Statement

You are given `n` nodes with `next` pointers (forming a general directed graph). A set of root nodes are considered reachable. Perform mark-and-sweep and output which nodes remain.

## Input Format

- First line: integers `n` and `r`
- Next `n` lines: `value next_id` (next_id is 0 if null)
- Next line: `r` integers: root node ids

## Output Format

- First line: integer `k` (number of reachable nodes)
- Next `k` lines: `id value` of reachable nodes, sorted by id

## Constraints

- `1 <= n <= 200000`
- `0 <= r <= n`
- `-10^9 <= value <= 10^9`

## Clarifying Notes

- A node is reachable if it is a root or reachable from a root by following `next` pointers.

## Example Input

```
4 1
10 2
20 0
30 4
40 0
1
```

## Example Output

```
2
1 10
2 20
```
