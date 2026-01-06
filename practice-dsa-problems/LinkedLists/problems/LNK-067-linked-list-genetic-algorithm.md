---
problem_id: LNK_LINKED_LIST_GENETIC_ALGORITHM__7791
display_id: NTB-LNK-7791
slug: linked-list-genetic-algorithm
title: "Linked List with Genetic Algorithm"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-genetic-algorithm
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Genetic Algorithm

## Problem Statement

Each list is an individual. The fitness is the sum of its values. You are given a deterministic sequence of genetic operations:

- `CROSS a b`: replace list `a` with the first half of `a` followed by second half of `b`
- `MUTATE a pos x`: set position `pos` of list `a` to `x`

After all operations, output the id of the fittest list (tie by smaller id).

## Input Format

- First line: integers `p` and `n` (population size and list length)
- Next `p` lines: `n` integers: lists
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- Single integer: id of fittest list

## Constraints

- `1 <= p <= 2000`
- `1 <= n <= 2000`
- `1 <= q <= 200000`

## Clarifying Notes

- List ids are 1-based.

## Example Input

```
2 4
1 1 1 1
2 2 2 2
2
CROSS 1 2
MUTATE 2 3 5
```

## Example Output

```
2
```
