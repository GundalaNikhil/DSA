---
problem_id: LNK_LINKED_LIST_RULE_MINING__6681
display_id: NTB-LNK-6681
slug: linked-list-rule-mining
title: "Linked List with Rule Mining"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-rule-mining
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Rule Mining

## Problem Statement

You are given an access log of positions. A rule is a pair `(a, b)` meaning an access to position `a` is followed by an access to position `b` within the next `W` events.

Find the rule `(a, b)` with the highest count. Break ties by smaller `a`, then smaller `b`.

## Input Format

- First line: integers `n` and `W`
- Second line: integer `m` (number of log events)
- Third line: `m` integers: accessed positions

## Output Format

- Two integers: `a b` of the most frequent rule

## Constraints

- `1 <= n <= 200000`
- `1 <= m <= 200000`
- `1 <= W <= m`

## Clarifying Notes

- A pair is counted if `b` appears in the next `W` events after an `a` event.

## Example Input

```
5 2
6
1 2 1 3 2 1
```

## Example Output

```
1 2
```
