---
problem_id: LNK_LINKED_LIST_PROBABILISTIC_ROUTING__5860
display_id: NTB-LNK-5860
slug: linked-list-probabilistic-routing
title: "Linked List with Probabilistic Routing"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-probabilistic-routing
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Probabilistic Routing

## Problem Statement

Each node has a `next` pointer and an optional `jump` pointer. At node `i`, you move to `jump` with probability `p_i/1000` and to `next` with probability `(1000 - p_i)/1000`. If `jump` is 0, you always go to `next`.

Compute the expected number of steps to reach null from the head.

## Input Format

- First line: integer `n`
- Second line: `n` integers: `jump` indices (0 if none)
- Third line: `n` integers: `p_i` (0..1000)

## Output Format

- Single integer: expected steps multiplied by 1000 (i.e., expected value * 1000)

## Constraints

- `1 <= n <= 200000`
- `0 <= p_i <= 1000`

## Clarifying Notes

- Expectation is deterministic from inputs; no simulation.
- Output is an integer rational scaled by 1000.

## Example Input

```
2
2 0
500 0
```

## Example Output

```
1500
```
