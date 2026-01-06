---
problem_id: LNK_DEFERRED_OPERATIONS_LIST__2124
display_id: NTB-LNK-2124
slug: deferred-operations-list
title: "Deferred Operations List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - deferred-operations-list
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Deferred Operations List

## Problem Statement

Operations are queued and applied in batches. Each batch is applied simultaneously using conflict rules.

Operations:

- `QUEUE INS pos x pr`: queue insertion at position `pos` with priority `pr`
- `QUEUE DEL pos pr`: queue deletion at position `pos` with priority `pr`
- `APPLY`: apply all queued operations simultaneously, then clear the queue
- `PRINT`: output the current list

Conflict rules per position:

1. Higher priority wins.
2. If tied, insertion beats deletion.
3. If still tied, earlier queued order wins.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `PRINT`, output the list values

## Constraints

- `1 <= n, q <= 200000`
- Total queued operations across input <= 200000

## Clarifying Notes

- Positions refer to the list state before the batch.
- `DEL` on a non-existent position is ignored.

## Example Input

```
3
1 2 3
5
QUEUE INS 2 9 1
QUEUE DEL 2 2
APPLY
PRINT
```

## Example Output

```
1 3
```
