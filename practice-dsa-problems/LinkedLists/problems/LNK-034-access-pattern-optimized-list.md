---
problem_id: LNK_ACCESS_PATTERN_OPTIMIZED_LIST__5388
display_id: NTB-LNK-5388
slug: access-pattern-optimized-list
title: "Access-Pattern Optimized List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - access-pattern-optimized-list
  - algorithms
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Access-Pattern Optimized List

## Problem Statement

Each `ACCESS pos` operation increases the access count of that node. A `REORDER` operation stably sorts the list by decreasing access count, preserving relative order among ties.

Process operations and output the final list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- One line: final list values

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- Access counts start at 0.
- `ACCESS` refers to current list positions.

## Example Input

```
4
10 20 30 40
5
ACCESS 2
ACCESS 2
ACCESS 4
REORDER
ACCESS 1
```

## Example Output

```
20 40 10 30
```
