---
problem_id: LNK_LINKED_LIST_DIFF_ENGINE__9673
display_id: NTB-LNK-9673
slug: linked-list-diff-engine
title: "Linked List Diff Engine"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-diff-engine
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List Diff Engine

## Problem Statement

Given two lists `A` and `B`, compute the minimum cost to transform `A` into `B` using these operations:

- Insert a value (cost `ci`)
- Delete a value (cost `cd`)
- Replace a value (cost `cr`)

Order must be preserved.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: list `A`
- Third line: `m` integers: list `B`
- Fourth line: integers `ci`, `cd`, `cr`

## Output Format

- Single integer: minimum cost

## Constraints

- `1 <= n, m <= 2000`
- `0 <= ci, cd, cr <= 10^9`

## Clarifying Notes

- Replacing a value changes it to any other value.

## Example Input

```
3 2
1 3 4
1 4
1 1 2
```

## Example Output

```
1
```
