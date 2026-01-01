---
problem_id: HEP_PRIORITY_QUEUE_DECREASE_KEY__8091
display_id: HEP-016
slug: priority-queue-decrease-key
title: "Priority Queue with Decrease-Key"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Priority Queue
  - Data Structures
tags:
  - heaps
  - priority-queue
  - decrease-key
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-016: Priority Queue with Decrease-Key

## Problem Statement

Implement a priority queue that supports:

- `INSERT id value`
- `DECREASE id delta` (decrease the key of `id` by `delta`)
- `EXTRACT` (remove and output the minimum key)

If `EXTRACT` is called on an empty queue, output `EMPTY`. If multiple ids have the same key, return the lexicographically smallest id.

![Problem Illustration](../images/HEP-016/problem-illustration.png)

## Input Format

- First line: integer `q`
- Next `q` lines: one of the operations above

## Output Format

- For each `EXTRACT`, output `value id` or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= value, delta <= 10^9`
- `1 <= |id| <= 20` (alphanumeric)

## Example

**Input:**

```
5
INSERT id1 5
INSERT id2 3
DECREASE id1 4
EXTRACT
EXTRACT
```

**Output:**

```
1 id1
3 id2
```

**Explanation:**

- id1 decreases from 5 to 1
- Extracts return id1 (1) then id2 (3)

![Example Visualization](../images/HEP-016/example-1.png)

## Notes

- Use a binary heap with a position map
- Decrease-key can be O(log n) with index tracking
- Time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Heaps, Priority Queue, Decrease-Key, Data Structures

---

## Solution Template

### Java


### Python


### C++


### JavaScript

