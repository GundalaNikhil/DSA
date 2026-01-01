---
problem_id: HEP_TASK_SCHEDULER_ENERGY__9471
display_id: HEP-006
slug: task-scheduler-energy
title: "Task Scheduler with Energy"
difficulty: Medium
difficulty_score: 56
topics:
  - Heaps
  - Greedy
  - Scheduling
tags:
  - heaps
  - greedy
  - energy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-006: Task Scheduler with Energy

## Problem Statement

You have `n` tasks. Task `i` has a duration `d_i` and an energy gain `g_i`. You start with energy `E`. You may execute tasks in any order, but you can only start a task if your current energy is at least its duration. After completing a task, your energy becomes:

```
E = E - d_i + g_i
```

Each task can be executed at most once. Return the maximum number of tasks you can complete.

![Problem Illustration](../images/HEP-006/problem-illustration.png)

## Input Format

- First line: integers `n` and `E`
- Next `n` lines: two integers `d_i` and `g_i`

## Output Format

- Single integer: maximum number of tasks completed

## Constraints

- `1 <= n <= 100000`
- `0 <= E <= 10^9`
- `1 <= d_i, g_i <= 10^9`

## Example

**Input:**

```
2 3
2 3
3 1
```

**Output:**

```
2
```

**Explanation:**

One valid order:

- Execute (2,3): energy becomes 3 - 2 + 3 = 4
- Execute (3,1): energy becomes 4 - 3 + 1 = 2

Both tasks are completed.

![Example Visualization](../images/HEP-006/example-1.png)

## Notes

- Consider tasks you can afford with current energy
- Use a heap to choose tasks that improve energy the most
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Heaps, Greedy Scheduling, Resource Management

---

## Solution Template

### Java


### Python


### C++


### JavaScript

