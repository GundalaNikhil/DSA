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

![Problem Illustration](../images/GRD-012/problem-illustration.png)

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

class Solution {
    public int compareTo(Task other) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();

        List<Solution.Task> tasks = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char name = sc.next().charAt(0);
            int count = sc.nextInt();
            int priority = sc.nextInt();
            tasks.add(new Solution.Task(name, count, priority));
        }

        Solution solution = new Solution();
        System.out.println(solution.minSlots(tasks, k));
        sc.close();
    }
}
```

### Python

```python
import heapq
import sys

def min_slots(tasks_data: list, k: int) -> int:
    # Implementation here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    k = int(next(iterator))
    
    tasks = []
    for _ in range(n):
        name = next(iterator)
        count = int(next(iterator))
        priority = int(next(iterator))
        tasks.append((name, count, priority))

    result = min_slots(tasks, k)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minSlots(vector<Task>& inputTasks, int k) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<Task> tasks(n);
    for (int i = 0; i < n; i++) {
        cin >> tasks[i].name >> tasks[i].count >> tasks[i].priority;
    }

    Solution solution;
    cout << solution.minSlots(tasks, k) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minSlots(tasksData, k) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const [n, k] = data[ptr++].split(" ").map(Number);
  
  const tasks = [];
  for (let i = 0; i < n; i++) {
    const parts = data[ptr++].split(" ");
    const name = parts[0];
    const count = parseInt(parts[1]);
    const priority = parseInt(parts[2]);
    tasks.push({ name, count, priority });
  }

  const solution = new Solution();
  console.log(solution.minSlots(tasks, k));
});
```
