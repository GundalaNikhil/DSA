---
problem_id: LNK_LINKED_LIST_FUZZY_MEMBERSHIP__3175
display_id: NTB-LNK-3175
slug: linked-list-fuzzy-membership
title: "Linked List with Fuzzy Membership"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-fuzzy-membership
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Fuzzy Membership

## Problem Statement

Each node belongs to the list with probability `p_i/1000`. The **confidence score** of a prefix of length `k` is the expected number of present nodes in that prefix.

For each query `k`, output the confidence score multiplied by 1000.

## Input Format

- First line: integer `n`
- Second line: `n` integers: `p_i` (0..1000)
- Third line: integer `q`
- Next `q` lines: `k`

## Output Format

- For each query, output the expected count * 1000

## Constraints

- `1 <= n, q <= 200000`
- `0 <= p_i <= 1000`

## Clarifying Notes

- Expectation is deterministic and additive.

## Example Input

```
3
500 1000 0
2
1
3
```

## Example Output

```
500
1500
```
