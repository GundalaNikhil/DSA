---
problem_id: LNK_REDIS_STYLE_EXPIRATION__7079
display_id: NTB-LNK-7079
slug: redis-style-expiration
title: "Redis-Style Expiration"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - pointers
  - redis-style-expiration
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Redis-Style Expiration

## Problem Statement

Each node may have an expiration time. Two strategies are used:

- Passive: access to an expired node removes it immediately.
- Active: every `S` operations, an active sweep removes all expired nodes.

Operations:

- `SET pos x ttl t`: set value at position `pos` with TTL from time `t`
- `GET pos t`: output value or `-1`

## Input Format

- First line: integers `n`, `S`
- Second line: `n` integers: initial values
- Third line: `n` integers: initial TTLs (0 means no expiration)
- Fourth line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output value or `-1`

## Constraints

- `1 <= n, q <= 200000`
- `0 <= ttl, t <= 10^9`

## Clarifying Notes

- If `ttl = 0`, the node never expires.
- Active sweep occurs before processing the `S`-th, `2S`-th, ... operation.

## Example Input

```
2 2
5 6
1 0
3
GET 1 1
GET 1 2
GET 2 2
```

## Example Output

```
5
-1
6
```
