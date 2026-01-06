---
problem_id: LNK_LINKED_LIST_BYZANTINE_FAULT_TOLERANCE__3994
display_id: NTB-LNK-3994
slug: linked-list-byzantine-fault-tolerance
title: "Linked List with Byzantine Fault Tolerance"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-byzantine-fault-tolerance
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Byzantine Fault Tolerance

## Problem Statement

You receive `R` replicas of the same list. Up to `B` replicas may be malicious and send arbitrary values. For each position, accept the value that appears at least `R - B` times; otherwise mark the position as corrupted.

Output the reconstructed list with corrupted positions as `*`.

## Input Format

- First line: integers `n`, `R`, `B`
- Next `R` lines: `n` integers each (replica lists)

## Output Format

- One line: reconstructed list values, with `*` for corrupted positions

## Constraints

- `1 <= n <= 200000`
- `1 <= R <= 20`
- `0 <= B < R`

## Clarifying Notes

- If multiple values reach the threshold, choose the smallest.

## Example Input

```
3 3 1
1 2 3
1 9 3
1 2 4
```

## Example Output

```
1 2 *
```
