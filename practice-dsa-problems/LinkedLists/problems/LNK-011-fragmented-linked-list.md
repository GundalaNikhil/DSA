---
problem_id: LNK_FRAGMENTED_LINKED_LIST__1828
display_id: NTB-LNK-1828
slug: fragmented-linked-list
title: "Fragmented Linked List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - fragmented-linked-list
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Fragmented Linked List

## Problem Statement

A linked list is composed of **fragments**. Each fragment is a contiguous block of nodes. You must support splitting and merging fragments while preserving node order.

Operations:

- `SPLIT f k`: split fragment `f` after its first `k` nodes, creating a new fragment immediately after `f`.
- `MERGE f`: merge fragment `f` with the fragment immediately after it.
- `LEN f`: output the length of fragment `f`.

Fragments are identified by ids assigned at creation time; the initial list is a single fragment with id `1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `LEN`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total number of fragments created <= 200000

## Clarifying Notes

- `SPLIT f k` is invalid if `k` is 0 or `k` equals fragment length; ignore invalid operations.
- `MERGE f` is invalid if `f` is the last fragment; ignore invalid operations.

## Example Input

```
5
1 2 3 4 5
4
LEN 1
SPLIT 1 2
LEN 2
MERGE 1
```

## Example Output

```
5
3
```
