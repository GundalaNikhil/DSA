---
problem_id: LNK_HOSTEL_NUMBER_REMOVE_MTH__4285
display_id: LNK-012
slug: hostel-number-remove-mth
title: "Hostel Number Remove Mth from Start"
difficulty: Medium
difficulty_score: 44
topics:
  - Linked List
  - Deletion
  - Single Pass
tags:
  - linked-list
  - deletion
  - single-pass
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-012: Hostel Number Remove Mth from Start

## Problem Statement

Remove the M-th node from the start of a singly linked list (1-indexed). If `M` is larger than the list length, return the original list.

![Problem Illustration](../images/LNK-012/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `M`

## Output Format

- Single line: list values after removal

## Constraints

- `1 <= n <= 100000`
- `1 <= M <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
4
9 8 7 6
2
```

**Output:**

```
9 7 6
```

**Explanation:**

The 2nd node (value 8) is removed.

![Example Visualization](../images/LNK-012/example-1.png)

## Notes

- Use a dummy head to handle removal of the first node
- A single pass with a counter is enough
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Deletion

---

## Solution Template

### Java


### Python


### C++


### JavaScript

