---
problem_id: STK_NOTEBOOK_UNDO_SIMULATOR__4827
display_id: STK-001
slug: notebook-undo-simulator
title: "Notebook Undo Simulator"
difficulty: Easy
difficulty_score: 20
topics:
  - Stack
  - Simulation
  - Data Structures
tags:
  - stack
  - simulation
  - easy
  - commands
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-001: Notebook Undo Simulator

## Problem Statement

You are implementing an undo buffer for a notebook editor. The buffer is a stack that supports:

- `PUSH x`: push value `x`
- `POP`: remove and output the top value
- `TOP`: output the top value without removing

If `POP` or `TOP` is called on an empty stack, output `EMPTY`.

![Problem Illustration](../images/STK-001/problem-illustration.png)

## Input Format

- First line: integer `m` (number of commands)
- Next `m` lines: one command (`PUSH x`, `POP`, or `TOP`)

## Output Format

- For each `POP` or `TOP` command, output one line:
  - the value at the top, or
  - `EMPTY` if the stack is empty

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`

## Example

**Input:**

```
5
PUSH 10
PUSH -1
TOP
POP
TOP
```

**Output:**

```
-1
-1
10
```

**Explanation:**

The stack becomes [10, -1], TOP shows -1, POP removes -1, then TOP shows 10.

![Example Visualization](../images/STK-001/example-1.png)

## Notes

- Use an array or list as the underlying stack
- Each command runs in O(1)
- Only `POP` and `TOP` produce output
- Keep values as 64-bit to be safe

## Related Topics

Stack, Simulation, LIFO

---

## Solution Template
### Java


### Python


### C++


### JavaScript

