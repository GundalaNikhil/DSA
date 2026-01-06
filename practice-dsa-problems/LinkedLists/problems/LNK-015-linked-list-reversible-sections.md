---
problem_id: LNK_LINKED_LIST_REVERSIBLE_SECTIONS__8058
display_id: NTB-LNK-8058
slug: linked-list-reversible-sections
title: "Linked List with Reversible Sections"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-reversible-sections
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Reversible Sections

## Problem Statement

Each node is marked reversible (1) or immutable (0). You must process range-reversal operations that are allowed only if **all nodes in the range are reversible**.

Operations:

- `REV l r`: reverse the sublist from position `l` to `r`

Invalid operations are ignored. Output the final list and the count of invalid operations.

## Input Format

- First line: integer `n`
- Second line: `n` integers: node values
- Third line: `n` integers: flags (1 reversible, 0 immutable)
- Fourth line: integer `q`
- Next `q` lines: operations

## Output Format

- First line: invalid operation count
- Second line: final list values

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- Positions are 1-based in the current list state.

## Example Input

```
4
1 2 3 4
1 0 1 1
2
REV 1 3
REV 2 4
```

## Example Output

```
1
1 2 4 3
```
