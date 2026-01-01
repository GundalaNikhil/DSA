---
problem_id: QUE_SHUTTLE_SEAT_ASSIGNMENT__4407
display_id: QUE-010
slug: shuttle-seat-assignment
title: "Shuttle Seat Assignment"
difficulty: Medium
difficulty_score: 46
topics:
  - Scheduling
  - Priority Queue
  - Queue
tags:
  - scheduling
  - min-heap
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-010: Shuttle Seat Assignment

## Problem Statement

A shuttle service has a list of passenger arrival and departure times. Each passenger needs one seat for the entire interval `[arrival, departure)`.

Compute the minimum number of seats required so that no passenger has to wait.

![Problem Illustration](../images/QUE-010/problem-illustration.png)

## Input Format

- First line: integer `n` (number of passengers)
- Second line: `n` space-separated integers (arrival times)
- Third line: `n` space-separated integers (departure times)

## Output Format

- Single integer: minimum number of seats required

## Constraints

- `1 <= n <= 100000`
- `0 <= arrival[i], departure[i] <= 10^9`
- All times are integers

## Example

**Input:**

```
3
0 4 4
5 5 9
```

**Output:**

```
2
```

**Explanation:**

At time 4, two passengers overlap:

- Passenger 1: [0, 5)
- Passenger 2: [4, 5)
- Passenger 3: [4, 9)

Two seats are sufficient.

![Example Visualization](../images/QUE-010/example-1.png)

## Notes

- Sort passengers by arrival time
- Use a min-heap or queue of current departure times
- Reuse a seat when the earliest departure time <= current arrival
- Time complexity: O(n log n)

## Related Topics

Scheduling, Priority Queue, Interval Overlap

---

## Solution Template

### Java


### Python


### C++


### JavaScript

