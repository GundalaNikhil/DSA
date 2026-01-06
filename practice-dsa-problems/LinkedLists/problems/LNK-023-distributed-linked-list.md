---
problem_id: LNK_DISTRIBUTED_LINKED_LIST__8146
display_id: NTB-LNK-8146
slug: distributed-linked-list
title: "Distributed Linked List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - distributed-linked-list
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Distributed Linked List

## Problem Statement

A linked list is partitioned into shards. Each node belongs to a shard. An operation is valid only if it holds all required shard locks.

Operations:

- `INS pos x locks...`: insert value `x` at position `pos`
- `DEL pos locks...`: delete node at position `pos`

For each operation, you are given the list of shard ids whose locks are held. The operation is valid if and only if the set of locks includes all shards touched by the operation (the shard of the node at `pos` and its predecessor, if any).

Report the index of the first invalid operation, or `0` if all are valid. Apply only valid operations.

## Input Format

- First line: integers `n`, `S`, and `q`
- Second line: `n` integers: initial list values
- Third line: `n` integers: shard id for each node
- Next `q` lines: `type pos x k lock1 ... lockk` for `INS`, and `type pos k lock1 ... lockk` for `DEL`

## Output Format

- Single integer: index of first invalid operation, or `0`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= S <= 200000`
- Total locks listed <= 200000

## Clarifying Notes

- If `pos = 1`, only the shard of the current head is required for `DEL`.
- For `INS`, the inserted node inherits the shard of the node at `pos` (or head if inserting at position 1).

## Example Input

```
3 2 2
5 6 7
1 2 1
INS 2 9 1 2
DEL 1 1 1
```

## Example Output

```
2
```
