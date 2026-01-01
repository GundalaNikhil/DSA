---
problem_id: LNK_HOSTEL_CLEANUP_DEDUPLICATE_TWO__6294
display_id: LNK-004
slug: hostel-cleanup-deduplicate-two
title: "Hostel Cleanup Deduplicate (At Most Two)"
difficulty: Medium
difficulty_score: 45
topics:
  - Linked List
  - Two Pointers
  - Deduplication
tags:
  - linked-list
  - duplicates
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-004: Hostel Cleanup Deduplicate (At Most Two)

## Problem Statement

Given a sorted singly linked list, remove extra duplicates so that each distinct value appears at most twice. Return the head of the modified list.

![Problem Illustration](../images/LNK-004/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers in non-decreasing order

## Output Format

- Single line: list values after cleanup, space-separated
- If the list is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
6
1 1 1 2 2 3
```

**Output:**

```
1 1 2 2 3
```

**Explanation:**

Only two occurrences of each value are kept.

![Example Visualization](../images/LNK-004/example-1.png)

## Notes

- Track the count of the current value as you traverse
- Unlink nodes beyond the second occurrence
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Deduplication, Two Pointers

---

## Solution Template

### Java


### Python


### C++


### JavaScript

