---
problem_id: LNK_LAB_LOOP_DETECTOR_ENTRY_LENGTH__8412
display_id: LNK-006
slug: lab-loop-detector-entry-length
title: "Lab Loop Detector with Entry Index and Cycle Length"
difficulty: Medium
difficulty_score: 56
topics:
  - Linked List
  - Cycle Detection
  - Two Pointers
tags:
  - linked-list
  - cycle
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-006: Lab Loop Detector with Entry Index and Cycle Length

## Problem Statement

Detect whether a singly linked list has a cycle. If a cycle exists, return:

- `entry_index`: 0-based index of the cycle entry node
- `cycle_length`: number of nodes in the cycle
- `max_value_in_cycle`: maximum node value within the cycle

If no cycle exists, return `-1 0 0`.

![Problem Illustration](../images/LNK-006/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `pos` (0-based index where the tail connects, or `-1` for no cycle)

## Output Format

- Three integers: `entry_index cycle_length max_value_in_cycle`

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer
- `-1 <= pos < n`

## Example

**Input:**

```
4
1 2 3 4
1
```

**Output:**

```
1 3 4
```

**Explanation:**

The tail connects to index 1 (value 2). The cycle is 2 -> 3 -> 4 -> back to 2.

- entry_index = 1
- cycle_length = 3
- max_value_in_cycle = 4

![Example Visualization](../images/LNK-006/example-1.png)

## Notes

- Use Floyd's cycle detection to find a meeting point
- After detection, find the entry index by moving pointers
- Traverse the cycle once to compute length and maximum value
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Cycle Detection, Floyd's Algorithm

---

## Solution Template

### Java


### Python


### C++


### JavaScript

