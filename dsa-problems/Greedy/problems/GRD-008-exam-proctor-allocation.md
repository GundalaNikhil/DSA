---
problem_id: GRD_EXAM_PROCTOR_ALLOCATION__3517
display_id: GRD-008
slug: exam-proctor-allocation
title: "Exam Proctor Allocation"
difficulty: Medium
difficulty_score: 40
topics:
  - Greedy Algorithms
  - Sweep Line
  - Intervals
tags:
  - greedy
  - sweep-line
  - intervals
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-008: Exam Proctor Allocation

## Problem Statement

You have `n` exam sessions, where each session `i` occurs during time interval `[start[i], end[i]]`. Each proctor can supervise up to `r` simultaneously occurring exams.

Your task is to find the minimum number of proctors needed to cover all exam sessions.

![Problem Illustration](../images/GRD-008/problem-illustration.png)

## Input Format

- First line: two integers `n r` (number of exams and max exams per proctor)
- Next `n` lines: two integers `start end` representing each exam's time interval

## Output Format

- Single integer: minimum number of proctors needed

## Constraints

- `1 <= n <= 10^5`
- `1 <= r <= 10^9`
- `0 <= start < end <= 10^9`

## Example

**Input:**
```
3 2
0 10
5 7
6 9
```

**Output:**
```
2
```

**Explanation:**

Exams:
- Exam 1: [0, 10]
- Exam 2: [5, 7]  
- Exam 3: [6, 9]

Each proctor can handle up to r = 2 exams simultaneously.

Timeline analysis:
- At time 5: Exams 1 and 2 are active (2 exams)
- At time 6: Exams 1, 2, and 3 are active (3 exams)
- Maximum overlap: 3 exams

Proctors needed: ceil(3 / 2) = ceil(1.5) = 2

![Example Visualization](../images/GRD-008/example-1.png)

## Notes

- Use sweep line algorithm to track overlapping intervals
- Track maximum number of simultaneously active exams
- Answer = ceil(max_overlap / r)
- Create events for exam start (+1) and exam end (-1)
- Sort events by time and process in order
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Sweep Line, Interval Scheduling, Resource Allocation

---

## Solution Template

### Java


### Python


### C++


### JavaScript
