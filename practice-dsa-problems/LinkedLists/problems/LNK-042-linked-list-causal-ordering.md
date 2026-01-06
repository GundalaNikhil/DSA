---
problem_id: LNK_LINKED_LIST_CAUSAL_ORDERING__6144
display_id: NTB-LNK-6144
slug: linked-list-causal-ordering
title: "Linked List with Causal Ordering"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-causal-ordering
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Causal Ordering

## Problem Statement

You are given a log of operations with dependency ids. Each operation `i` may list prerequisite operation ids that must appear earlier in the log. Determine the first operation that violates causal ordering.

## Input Format

- First line: integer `q`
- Next `q` lines: `k dep1 dep2 ... depk` (the dependency list for operation i)

## Output Format

- The 1-based index of the first violation, or `0` if none

## Constraints

- `1 <= q <= 200000`
- Total number of dependencies <= 200000

## Clarifying Notes

- Dependencies refer to operation indices.

## Example Input

```
3
0
1 1
1 3
```

## Example Output

```
3
```
