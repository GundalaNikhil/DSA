---
problem_id: LNK_LINKED_LIST_LEASE_EXPIRATION__3161
display_id: NTB-LNK-3161
slug: linked-list-lease-expiration
title: "Linked List with Lease Expiration"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-lease-expiration
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Lease Expiration

## Problem Statement

Each node has a lease that expires at time `t_expire`. Operations occur at given times. Expired nodes are removed before processing any operation at time `t`.

Operations:

- `INS pos x lease t`: insert value `x` at position `pos` with lease duration `lease` at time `t`
- `RENEW pos lease t`: extend the lease of node at `pos` by `lease`
- `GET pos t`: output value at position `pos` at time `t`, or `-1`

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values
- Third line: `n` integers: initial lease durations (starting at time 0)
- Fourth line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `0 <= lease, t <= 10^9`
- Timestamps are non-decreasing

## Clarifying Notes

- If a node expires at time `t`, it is removed before operations at time `t`.

## Example Input

```
2
5 6
3 1
3
GET 1 1
GET 2 1
GET 1 3
```

## Example Output

```
5
-1
-1
```
