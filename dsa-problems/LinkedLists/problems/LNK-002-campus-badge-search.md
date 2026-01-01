---
problem_id: LNK_CAMPUS_BADGE_SEARCH__7294
display_id: LNK-002
slug: campus-badge-search
title: "Campus Badge Search"
difficulty: Easy
difficulty_score: 22
topics:
  - Linked List
  - Search
  - Linear Scan
tags:
  - linked-list
  - search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-002: Campus Badge Search

## Problem Statement

Given the head of a singly linked list and a target value, return the 0-based index of the first occurrence of the target. If the target does not appear, return `-1`.

![Problem Illustration](../images/LNK-002/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `target`

## Output Format

- Single integer: index of the first occurrence of `target`, or `-1`

## Constraints

- `1 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
4
5 1 5 9
9
```

**Output:**

```
3
```

**Explanation:**

List: 5 -> 1 -> 5 -> 9

The target 9 appears at index 3.

![Example Visualization](../images/LNK-002/example-1.png)

## Notes

- A single linear scan is sufficient
- Stop early once the target is found
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Linear Search

---

## Solution Template

### Java


### Python


### C++


### JavaScript

