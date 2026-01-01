---
problem_id: QUE_CAMPUS_SERVICE_LINE__4821
display_id: QUE-001
slug: campus-service-line
title: "Campus Service Line"
difficulty: Easy
difficulty_score: 18
topics:
  - Queue
  - Simulation
  - Data Streams
tags:
  - queue
  - simulation
  - easy
  - data-structures
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-001: Campus Service Line

## Problem Statement

A campus service desk handles students in a strict first-in-first-out order. You must implement a queue that supports the following commands:

- `ENQUEUE x`: add student ID `x` to the back of the line
- `DEQUEUE`: remove and report the student at the front
- `FRONT`: report the student at the front without removing

If a `DEQUEUE` or `FRONT` is issued when the queue is empty, output `EMPTY`.

![Problem Illustration](../images/QUE-001/problem-illustration.png)

## Input Format

- First line: integer `m` (number of commands)
- Next `m` lines: command is `ENQUEUE x`, `DEQUEUE`, or `FRONT`

## Output Format

- For each `DEQUEUE` or `FRONT`, output the front value or `EMPTY`

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`
- Commands are valid strings as described above

## Example

**Input:**

```
6
ENQUEUE 12
ENQUEUE -5
FRONT
DEQUEUE
FRONT
DEQUEUE
```

**Output:**

```
12
12
-5
-5
```

**Explanation:**

The queue starts empty. Sequence: ENQUEUE 12 -> [12], ENQUEUE -5 -> [12, -5], FRONT -> 12, DEQUEUE -> removes 12, FRONT -> -5, DEQUEUE -> removes -5.

![Example Visualization](../images/QUE-001/example-1.png)

## Notes

- A dynamic array with head/tail indices is sufficient
- Each command can be processed in O(1) amortized time
- Output is required only for `DEQUEUE` and `FRONT`
- Space complexity is O(m) in the worst case

## Related Topics

Queue, Simulation, FIFO

---

## Solution Template
### Java


### Python


### C++


### JavaScript

