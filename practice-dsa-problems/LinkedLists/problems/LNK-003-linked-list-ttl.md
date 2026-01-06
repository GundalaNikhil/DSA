---
problem_id: LNK_LINKED_LIST_TTL__6640
display_id: NTB-LNK-6640
slug: linked-list-ttl
title: "Linked List with Time-to-Live"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-ttl
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Time-to-Live

## Problem Statement

Each node has a time-to-live (TTL) in steps. The list processes `q` operations; **each operation advances time by 1**. A node inserted at time `t` with TTL `T` expires at time `t + T`. Expired nodes are removed automatically before each operation.

Operations:

- `PUSH x T`: insert node with value `x` and TTL `T` at the tail
- `POP`: remove the head node (if any)
- `FRONT`: output the value at the head (after pruning), or `-1`
- `COUNT`: output the number of nodes (after pruning)

## Input Format

- First line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `FRONT` or `COUNT`, output one integer

## Constraints

- `1 <= q <= 200000`
- `0 <= T <= 10^9`
- Values are 32-bit signed integers

## Clarifying Notes

- If `T = 0`, the node expires immediately before the next operation.
- Pruning happens before executing the current operation.

## Example Input

```
6
PUSH 5 2
COUNT
PUSH 7 1
FRONT
COUNT
FRONT
```

## Example Output

```
1
5
1
-1
```
