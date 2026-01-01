---
problem_id: LNK_EXAM_SEATING_INTERSECTION_SUM__5629
display_id: LNK-011
slug: exam-seating-intersection-sum
title: "Exam Seating Intersection Sum"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Intersection
  - Two Pointers
tags:
  - linked-list
  - intersection
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-011: Exam Seating Intersection Sum

## Problem Statement

Two singly linked lists may intersect (share nodes). Return the sum of values in the shared suffix. If there is no intersection, return `0`.

![Problem Illustration](../images/LNK-011/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m` (lengths of list A and list B)
- Second line: `n` space-separated integers (list A values)
- Third line: `m` space-separated integers (list B values)
- Fourth line: two integers `ia` and `ib`

If `ia` and `ib` are both `-1`, the lists do not intersect. Otherwise, the node at index `ib` of list B is connected to the node at index `ia` of list A (0-based). Any nodes after index `ib` in list B are ignored after the connection.

## Output Format

- Single integer: sum of values in the shared suffix

## Constraints

- `0 <= n, m <= 100000`
- Node values fit in 32-bit signed integer
- `-1 <= ia < n`, `-1 <= ib < m`

## Example

**Input:**

```
4 3
1 2 3 4
9 3 4
2 1
```

**Output:**

```
7
```

**Explanation:**

List A: 1 -> 2 -> 3 -> 4

List B starts as 9 -> 3 -> 4, but index 1 in B connects to index 2 in A.

Shared suffix is 3 -> 4, sum = 7.

![Example Visualization](../images/LNK-011/example-1.png)

## Notes

- You can find the intersection using length alignment or hashing
- Once the intersection node is found, sum to the end
- Time complexity: O(n + m)
- Space complexity: O(1)

## Related Topics

Linked Lists, Intersection, Two Pointers

---

## Solution Template

### Java


### Python


### C++


### JavaScript

