---
problem_id: LNK_LAB_ROSTER_APPEND__3582
display_id: LNK-001
slug: lab-roster-append
title: "Lab Roster Append"
difficulty: Easy
difficulty_score: 20
topics:
  - Linked List
  - Data Structures
  - Implementation
tags:
  - linked-list
  - implementation
  - append
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-001: Lab Roster Append

## Problem Statement

Implement a singly linked list that supports two operations:

- `push_back value`: append `value` to the end of the list
- `to_array`: output all elements in order

For each `to_array` operation, print the current list contents.

![Problem Illustration](../images/LNK-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of operations)
- Next `n` lines: either `push_back value` or `to_array`

## Output Format

- For each `to_array`, print list values space-separated on one line
- If the list is empty, print an empty line

## Constraints

- `1 <= n <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5
push_back 3
push_back 7
to_array
push_back -2
to_array
```

**Output:**

```
3 7
3 7 -2
```

**Explanation:**

Operation sequence:

1. push_back 3 -> list: [3]
2. push_back 7 -> list: [3, 7]
3. to_array -> output: 3 7
4. push_back -2 -> list: [3, 7, -2]
5. to_array -> output: 3 7 -2

![Example Visualization](../images/LNK-001/example-1.png)

## Notes

- Track both head and tail pointers for O(1) append
- Handle empty list carefully
- Time complexity: O(1) per push_back, O(n) per to_array
- Space complexity: O(n)

## Related Topics

Linked List Implementation, Tail Pointer, Array Conversion

---

## Solution Template

### Java


### Python


### C++


### JavaScript

