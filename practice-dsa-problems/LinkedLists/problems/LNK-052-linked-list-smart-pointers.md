---
problem_id: LNK_LINKED_LIST_SMART_POINTERS__2863
display_id: NTB-LNK-2863
slug: linked-list-smart-pointers
title: "Linked List with Smart Pointers"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-smart-pointers
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Smart Pointers

## Problem Statement

Each node has a strong reference count and outgoing strong pointers to other nodes. When a node's strong count becomes zero, it is destroyed and its outgoing strong pointers decrement their targets (cascading deletes).

Operations:

- `INC u`: increment strong count of node `u`
- `DEC u`: decrement strong count of node `u` (cannot go below 0)
- `LINK u v`: add a strong pointer from `u` to `v`
- `UNLINK u v`: remove a strong pointer from `u` to `v`

After all operations, output the set of nodes still alive (strong count > 0 or reachable through surviving nodes).

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial strong counts
- Third line: integer `m` (number of initial links)
- Next `m` lines: `u v` (link)
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- First line: integer `k` (alive count)
- Next line: `k` node ids in ascending order

## Constraints

- `1 <= n, q <= 200000`
- Total links <= 200000

## Clarifying Notes

- If a node is destroyed, all its outgoing links are removed immediately.

## Example Input

```
3
1 0 0
1
1 2
2
DEC 1
INC 3
```

## Example Output

```
1
3
```
