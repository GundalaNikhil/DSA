---
problem_id: LNK_LINKED_LIST_STATE_MACHINE__2637
display_id: NTB-LNK-2637
slug: linked-list-state-machine
title: "Linked List State Machine"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-state-machine
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List State Machine

## Problem Statement

Each node is a state in `0..S-1`. A list is **valid** if for every adjacent pair `(u, v)`, the transition `u -> v` is allowed by a given transition matrix.

You must process updates and output whether the list is valid after each update.

Operations:

- `SET pos x`: set the state at position `pos` to `x`

## Input Format

- First line: integers `n` and `S`
- Second line: `n` integers: initial states
- Next `S` lines: `S` integers (0/1) transition matrix
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- After each update, output `VALID` or `INVALID`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= S <= 50`

## Clarifying Notes

- A list with one node is always valid.

## Example Input

```
3 2
0 1 0
1 1
0 1
2
SET 2 0
SET 3 1
```

## Example Output

```
VALID
INVALID
```
