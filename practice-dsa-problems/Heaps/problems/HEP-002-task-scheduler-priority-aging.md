---
problem_id: HEP_TASK_SCHEDULER_PRIORITY_AGING__2672
display_id: NTB-HEP-2672
slug: task-scheduler-priority-aging
title: "Task Scheduler with Priority Aging (Capped)"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - heaps
  - priority-queues
  - sorting
  - task-scheduler-priority-aging
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Task Scheduler with Priority Aging (Capped)

## Problem Statement

You must simulate a single-core scheduler that runs tasks in discrete time ticks starting at `t = 1`. There are `n` task types. Task type `i` has:

- `cnt_i`: number of executions required
- `cool_i`: cooldown in ticks between two executions of the same type
- `deadline_i`: the last tick where it is considered on time
- `base_i`: base priority

All task types are available at `t = 1` (subject to cooldown). Each execution takes exactly one tick.

At each tick `t`:

1. A task type `i` is **available** if `cnt_i > 0` and its last execution time `last_i` satisfies `t >= last_i + cool_i + 1`. (Initially, `last_i = -infinity`, so every type is available at `t = 1`.)
2. If at least one task type is available, execute exactly one task using these deterministic rules:
   - Choose the available type with highest current priority `base_i + age_i`.
   - Break ties by smaller `deadline_i`, then smaller `i`.
   - Decrease `cnt_i` by 1 and set `last_i = t`.
3. If no task type is available, the CPU is idle for this tick. For every task type with `cnt_i > 0` and `t > deadline_i`, increase `age_i` by 1, but cap it so that `age_i <= cap`.

Aging only happens on idle ticks. Your task is to compute the total number of ticks until all tasks are completed.

## Input Format

- First line: integers `n` and `cap`
- Next `n` lines: `cnt_i cool_i deadline_i base_i` for task type `i` (1-based)

## Output Format

- Single integer: total number of ticks to complete all tasks

## Constraints

- `1 <= n <= 200000`
- `1 <= cnt_i <= 200000`
- `sum(cnt_i) <= 200000`
- `0 <= cool_i <= 10^9`
- `0 <= deadline_i <= 10^9`
- `0 <= base_i <= 10^9`
- `0 <= cap <= 10^9`

## Clarifying Notes

- Cooldown means a task type executed at tick `t` cannot be executed again until tick `t + cool_i + 1`.
- Aging is applied only on idle ticks and only to task types that are already past their deadline.
- The schedule is fully determined by the rules above; no alternate schedules are allowed.

## Example Input

```
2 3
3 2 2 5
2 1 1 4
```

## Example Output

```
7
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    static class TaskType {
        int cnt;
        long cool, deadline, base;
        TaskType(int cnt, long cool, long deadline, long base) {
            this.cnt = cnt;
            this.cool = cool;
            this.deadline = deadline;
            this.base = base;
        }
    }

    public long totalTicks(int n, int cap, TaskType[] tasks) {
        // Your code here
        return 0;
    }
}
```

```python
import heapq

class TaskType:
    def __init__(self, cnt, cool, deadline, base):
        self.cnt = cnt
        self.cool = cool
        self.deadline = deadline
        self.base = base

class Solution:
    def totalTicks(self, n: int, cap: int, tasks: list[TaskType]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct TaskType {
    int cnt;
    long long cool, deadline, base;
};

class Solution {
public:
    long long totalTicks(int n, int cap, vector<TaskType>& tasks) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} cap
   * @param {Array<{cnt: number, cool: number, deadline: number, base: number}>} tasks
   * @returns {number}
   */
  totalTicks(n, cap, tasks) {
    // Your code here
    return 0;
  }
}
```
