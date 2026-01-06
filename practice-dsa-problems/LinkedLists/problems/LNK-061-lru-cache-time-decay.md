---
problem_id: LNK_LRU_CACHE_TIME_DECAY__2159
display_id: NTB-LNK-2159
slug: lru-cache-time-decay
title: "LRU Cache with Time-Decay"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linkedlists
  - lru-cache-time-decay
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LRU Cache with Time-Decay

## Problem Statement

You maintain a cache of capacity `C`. Each item has a score:

```
score = last_access_time - decay * age
```

where `age = current_time - last_access_time`. On `PUT` when full, evict the item with lowest score (tie by oldest access time).

Operations:

- `GET key t`
- `PUT key value t`

Output the value for each `GET` or `-1` if missing.

## Input Format

- First line: integers `C` and `decay`
- Second line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output value or `-1`

## Constraints

- `1 <= C <= 200000`
- `0 <= decay <= 10^9`
- Timestamps are non-decreasing

## Clarifying Notes

- `GET` updates `last_access_time` if hit.
- `PUT` updates value if key exists.

## Example Input

```
2 1
4
PUT a 1 0
PUT b 2 1
GET a 2
PUT c 3 3
```

## Example Output

```
1
```
