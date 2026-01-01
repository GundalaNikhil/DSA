---
problem_id: LNK_WORKSHOP_ODD_EVEN_GROUPING_STABLE__5392
display_id: LNK-015
slug: workshop-odd-even-grouping-stable
title: "Workshop Odd Even Grouping Stable"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Partitioning
  - Stable Ordering
tags:
  - linked-list
  - partition
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-015: Workshop Odd Even Grouping Stable

## Problem Statement

Reorder the list so that nodes with odd values appear first, followed by nodes with even values, preserving the original order within each group.

![Problem Illustration](../images/LNK-015/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)

## Output Format

- Single line: list values after grouping

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
4
2 5 4 7
```

**Output:**

```
5 7 2 4
```

**Explanation:**

Odd values in order: 5, 7

Even values in order: 2, 4

![Example Visualization](../images/LNK-015/example-1.png)

## Notes

- Build two chains (odd and even) and concatenate
- Preserve relative order within each chain
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Stable Partitioning, Parity

---

## Solution Template

### Java


### Python


### C++


### JavaScript

