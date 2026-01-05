---
problem_id: GRD_WORKSHOP_TASK_COOLDOWN_PRIORITY__7539
display_id: GRD-012
slug: workshop-task-cooldown-priority
title: "Workshop Task Cooldown with Priority Interrupts"
difficulty: Medium
difficulty_score: 60
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
  - Scheduling
tags:
  - greedy
  - heap
  - priority-queue
  - scheduling
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-012: Workshop Task Cooldown with Priority Interrupts

## Problem Statement

You have tasks labeled A-Z with counts `c[i]` and priority levels `p[i]` in {1, 2, 3} where higher numbers indicate higher priority.

**Cooldown rule**: Between two identical tasks, at least `k` different tasks must be executed.

**Priority interrupt rule**: When a higher-priority task is scheduled, it resets the cooldown counter for all lower-priority tasks currently in cooldown. This means lower-priority tasks must wait an additional `k` slots from when the high-priority task runs.

**Idle slots**: If no task can be scheduled (all available tasks are in cooldown), insert an idle slot (costs 1 time unit).

Your goal is to minimize the total time slots (including idle slots) needed to complete all tasks.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-012.jpg)

## Input Format

- First line: two integers `n k` (number of task types and cooldown period)
- Next `n` lines: character `task`, integer `count`, integer `priority` representing each task type

## Output Format

- Single integer: minimum total time slots needed

## Constraints

- `1 <= n <= 26`
- `1 <= total tasks <= 10^5`
- `0 <= k <= 10^5`
- `1 <= priority <= 3`
- Tasks are uppercase letters A-Z

## Example

**Input:**

```
2 1
A 3 2
B 2 1
```

**Output:**

```
7
```

**Explanation:**

Tasks:

- Task A: count=3, priority=2 (medium)
- Task B: count=2, priority=1 (low)

Cooldown k=1 (need 1 different task between identical tasks)

Schedule:

- Slot 1: A (priority 2) → cooldown list: [A waits 2 slots]
- Slot 2: B (priority 1) → cooldown list: [A waits 1, B waits 2]
- Slot 3: A (priority 2, cooldown expired) → B's cooldown reset to 3 → cooldown: [A waits 2, B waits 3]
- Slot 4: B cannot be used (still in cooldown) → IDLE
- Slot 5: A (cooldown expired) → cooldown: [A waits 2, B waits 2]
- Slot 6: B (cooldown expired) → cooldown: [B waits 2]

Total tasks: A(3 times) + B(2 times) = 5 tasks completed in 6 time slots.

![Example Visualization](../images/GRD-012/example-1.png)

## Notes

- Use a max-heap ordered by (priority, remaining count)
- Maintain a cooldown queue with (task, ready_time, priority)
- When scheduling a high-priority task, increment ready_time for all lower-priority tasks in cooldown
- Time complexity: O(T log n) where T is total time slots

## Related Topics

Greedy Algorithms, Heap, Priority Queue, Task Scheduling, Cooldown Management

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minTotalTime(int n, int k, List<TaskType> tasks) {
        // Implement here
        return 0;
    }

    static class TaskType {
        char id;
        int count;
        int priority;
        TaskType(char id, int count, int priority) {
            this.id = id;
            this.count = count;
            this.priority = priority;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nkLine = br.readLine();
        if (nkLine == null) return;
        String[] nk = nkLine.trim().split("\\s+");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);

        List<Solution.TaskType> tasks = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] tLine = br.readLine().trim().split("\\s+");
            tasks.add(new Solution.TaskType(tLine[0].charAt(0), Integer.parseInt(tLine[1]), Integer.parseInt(tLine[2])));
        }

        Solution sol = new Solution();
        System.out.println(sol.minTotalTime(n, k, tasks));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_total_time(self, n, k, tasks):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    nk = input_data[0].split()
    n = int(nk[0])
    k = int(nk[1])

    tasks = []
    for i in range(1, n + 1):
        line = input_data[i].split()
        tasks.append({'id': line[0], 'count': int(line[1]), 'priority': int(line[2])})

    sol = Solution()
    print(sol.min_total_time(n, k, tasks))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct TaskType {
    char id;
    int count;
    int priority;
};

class Solution {
public:
    long long minTotalTime(int n, int k, vector<TaskType>& tasks) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<TaskType> tasks(n);
    for (int i = 0; i < n; i++) {
        cin >> tasks[i].id >> tasks[i].count >> tasks[i].priority;
    }

    Solution sol;
    cout << sol.minTotalTime(n, k, tasks) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minTotalTime(n, k, tasks) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const nk = input[0].trim().split(/\s+/);
  const n = parseInt(nk[0]);
  const k = parseInt(nk[1]);

  const tasks = [];
  for (let i = 1; i <= n; i++) {
    const line = input[i].trim().split(/\s+/);
    tasks.push({
      id: line[0],
      count: parseInt(line[1]),
      priority: parseInt(line[2]),
    });
  }

  const sol = new Solution();
  console.log(sol.minTotalTime(n, k, tasks).toString());
}

solve();
```
