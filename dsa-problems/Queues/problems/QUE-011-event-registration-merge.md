---
problem_id: QUE_EVENT_REGISTRATION_MERGE__6205
display_id: QUE-011
slug: event-registration-merge
title: "Event Registration Merge"
difficulty: Easy
difficulty_score: 22
topics:
  - Queue
  - Merge
  - Two Pointers
tags:
  - queue
  - merge
  - two-pointers
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-011: Event Registration Merge

## Problem Statement

Two event registration lines are already sorted by registration ID. Merge the two queues into one sorted queue while preserving the order of equal IDs.

![Problem Illustration](../images/QUE-011/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first queue)
- Second line: `n` space-separated integers (first queue)
- Third line: integer `m` (length of second queue)
- Fourth line: `m` space-separated integers (second queue)

## Output Format

- Single line: merged queue values in nondecreasing order
- If both queues are empty, print an empty line

## Constraints

- `0 <= n, m <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
3
3 5 9
3
1 4 10
```

**Output:**

```
1 3 4 5 9 10
```

**Explanation:**

Merge by repeatedly taking the smaller front value:

- 1 (from second)
- 3 (from first)
- 4 (from second)
- 5 (from first)
- 9 (from first)
- 10 (from second)

![Example Visualization](../images/QUE-011/example-1.png)

## Notes

- This is the queue version of merge in merge sort
- Always compare fronts of both queues
- Time complexity: O(n + m)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Merge, Two Pointers

---

## Solution Template

### Java


### Python


### C++


### JavaScript

