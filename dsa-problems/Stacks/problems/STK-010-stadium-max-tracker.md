---
problem_id: STK_STADIUM_MAX_TRACKER__3658
display_id: STK-010
slug: stadium-max-tracker
title: "Stadium Max Tracker"
difficulty: Medium
difficulty_score: 40
topics:
  - Stack
  - Data Structures
  - Design
tags:
  - stack
  - max-stack
  - design
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-010: Stadium Max Tracker

## Problem Statement

Design a stack that supports:

- `PUSH x`
- `POP`: remove and output the top
- `TOP`: output the top without removing
- `GETMAX`: output the current maximum element

If the stack is empty for `POP`, `TOP`, or `GETMAX`, output `EMPTY`.

![Problem Illustration](../images/STK-010/problem-illustration.png)

## Input Format

- First line: integer `m`
- Next `m` lines: commands

## Output Format

- For each command except `PUSH`, output one line with the result

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`

## Example

**Input:**

```
6
PUSH 2
PUSH 9
PUSH 5
GETMAX
POP
GETMAX
```

**Output:**

```
9
5
9
```

**Explanation:**

Max is 9, POP removes 5, then max is still 9.

![Example Visualization](../images/STK-010/example-1.png)

## Notes

- Maintain an auxiliary stack for current maxima
- Each operation is O(1)
- Popping must update the max stack
- Use 64-bit integers if needed

## Related Topics

Stack Design, Max Stack, Data Structures

---

## Solution Template
### Java


### Python


### C++


### JavaScript

