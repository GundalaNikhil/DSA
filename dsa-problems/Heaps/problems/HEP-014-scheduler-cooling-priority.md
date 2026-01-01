---
problem_id: HEP_SCHEDULER_COOLING_PRIORITY__5382
display_id: HEP-014
slug: scheduler-cooling-priority
title: "Scheduler With Cooling and Priority"
difficulty: Medium
difficulty_score: 57
topics:
  - Heaps
  - Scheduling
  - Greedy
tags:
  - heaps
  - cooldown
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-014: Scheduler With Cooling and Priority

## Problem Statement

You have task types with counts and priority weights. In each time slot, you may execute one task whose cooldown has expired. After executing a task of type `X`, you cannot execute `X` again for the next `k` time slots.

You are given a total time limit `T`. Maximize the total priority score of executed tasks. If no task is available in a slot, you may idle.

![Problem Illustration](../images/HEP-014/problem-illustration.png)

## Input Format

- First line: integers `m`, `k`, and `T`
- Next `m` lines: `task_id count priority`

## Output Format

- Single integer: maximum total priority score

## Constraints

- `1 <= m <= 26`
- `0 <= k <= 100000`
- `1 <= T <= 100000`
- `1 <= count <= 100000`
- `1 <= priority <= 10^9`

## Example

**Input:**

```
2 1 3
A 2 3
B 1 5
```

**Output:**

```
11
```

**Explanation:**

One optimal schedule is A, B, A:

- A gives 3
- B gives 5
- A gives 3

Total = 11.

![Example Visualization](../images/HEP-014/example-1.png)

## Notes

- Use a max-heap of available tasks by priority
- Track cooldown using a queue with next available time
- Each time slot is processed once
- Time complexity: O(T log m)
- Space complexity: O(m)

## Related Topics

Heaps, Scheduling, Cooldown Queues, Greedy

---

## Solution Template

### Java


### Python


### C++


### JavaScript

