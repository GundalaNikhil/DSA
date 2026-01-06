---
problem_id: LNK_LINKED_LIST_CONFLICT_RESOLVER__4646
display_id: NTB-LNK-4646
slug: linked-list-conflict-resolver
title: "Linked List Conflict Resolver"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-conflict-resolver
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List Conflict Resolver

## Problem Statement

You are given an initial list and a batch of insertion proposals. Each proposal targets a position `pos` (1-based) in the list **as it existed at the start of the batch**. Multiple proposals may target the same position.

For each position, resolve conflicts by:

1. Higher priority wins.
2. If tied, earlier timestamp wins.
3. If tied, smaller proposer id wins.

Apply all winning insertions simultaneously, keeping original order of unaffected nodes. Output the final list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `p` (number of proposals)
- Next `p` lines: `pos value priority time proposer_id`

## Output Format

- One line: final list values

## Constraints

- `1 <= n <= 200000`
- `0 <= p <= 200000`
- `1 <= pos <= n+1`
- `-10^9 <= value <= 10^9`

## Clarifying Notes

- Insertions at the same `pos` are resolved to a single winning node.
- Positions refer to the original list before the batch.

## Example Input

```
3
1 2 3
3
2 9 5 10 1
2 8 5 9 2
4 7 1 1 3
```

## Example Output

```
1 8 2 3 7
```
