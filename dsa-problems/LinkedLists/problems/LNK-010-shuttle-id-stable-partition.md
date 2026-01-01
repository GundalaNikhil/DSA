---
problem_id: LNK_SHUTTLE_ID_STABLE_PARTITION__7184
display_id: LNK-010
slug: shuttle-id-stable-partition
title: "Shuttle ID Stable Partition"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Partitioning
  - Stable Ordering
tags:
  - linked-list
  - partition
  - stable
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-010: Shuttle ID Stable Partition

## Problem Statement

Stable-partition the list so that nodes with value less than `x` come first, then nodes equal to `x`, then nodes greater than `x`. Preserve the original relative order within each group.

![Problem Illustration](../images/LNK-010/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `x`

## Output Format

- Single line: list values after stable partition

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
5
5 1 4 2 5
4
```

**Output:**

```
1 2 4 5 5
```

**Explanation:**

Values less than 4: 1, 2

Values equal to 4: 4

Values greater than 4: 5, 5

![Example Visualization](../images/LNK-010/example-1.png)

## Notes

- Build three lists: less, equal, greater
- Concatenate in order while keeping internal stability
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Stable Partitioning

---

## Solution Template

### Java


### Python


### C++


### JavaScript

