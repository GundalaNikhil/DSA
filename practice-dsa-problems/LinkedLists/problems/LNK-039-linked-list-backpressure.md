---
problem_id: LNK_LINKED_LIST_BACKPRESSURE__2215
display_id: NTB-LNK-2215
slug: linked-list-backpressure
title: "Linked List with Backpressure"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-backpressure
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Backpressure

## Problem Statement

The list has a maximum capacity `C`. Insertions are accepted only if the list size is strictly less than `C`.

Operations:

- `PUSH x`: append `x` (output `OK` or `BLOCKED`)
- `POP`: remove head (if any)
- `SIZE`: output current size

## Input Format

- First line: integers `C` and `q`
- Next `q` lines: operations

## Output Format

- For each `PUSH`, output `OK` or `BLOCKED`
- For each `SIZE`, output the size

## Constraints

- `1 <= C <= 200000`
- `1 <= q <= 200000`

## Clarifying Notes

- `POP` on an empty list does nothing.

## Example Input

```
2 5
PUSH 1
PUSH 2
PUSH 3
POP
PUSH 3
```

## Example Output

```
OK
OK
BLOCKED
OK
```
