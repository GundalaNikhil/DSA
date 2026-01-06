---
problem_id: LNK_LINKED_LIST_WRITE_AHEAD_LOG__5619
display_id: NTB-LNK-5619
slug: linked-list-write-ahead-log
title: "Linked List with Write-Ahead Log"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-write-ahead-log
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Write-Ahead Log

## Problem Statement

You are given a write-ahead log (WAL) of operations. Each log entry has a `commit` flag. Only committed entries are applied to the list.

Operations:

- `INS pos x`
- `DEL pos`
- `SET pos x`

Reconstruct the final list by replaying committed entries in order.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: `commit type pos [x]` where `commit` is 0 or 1

## Output Format

- One line: final list values

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- Invalid positions in committed operations are ignored.

## Example Input

```
3
1 2 3
3
1 INS 2 9
0 DEL 1
1 SET 3 7
```

## Example Output

```
1 9 7 3
```
