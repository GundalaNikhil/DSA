---
problem_id: LNK_LINKED_LIST_SCHEDULER__5156
display_id: NTB-LNK-5156
slug: linked-list-scheduler
title: "Linked List Scheduler"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-scheduler
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List Scheduler

## Problem Statement

Each node represents a task with a start time and duration. A task is active at time `t` if `start <= t < start + duration`.

Process queries to count active tasks in a sublist.

## Input Format

- First line: integer `n`
- Next `n` lines: `value start duration` for each node in list order
- Next line: integer `q`
- Next `q` lines: `l r t` queries (1-based positions)

## Output Format

- For each query, output the count of active tasks in positions `[l, r]` at time `t`

## Constraints

- `1 <= n, q <= 200000`
- `0 <= start, duration, t <= 10^9`

## Clarifying Notes

- Duration can be 0, which means the task is never active.

## Example Input

```
3
10 0 5
20 3 2
30 4 10
2
1 3 4
2 3 6
```

## Example Output

```
3
1
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    static class Task {
        int value;
        long start, duration;
        Task(int value, long start, long duration) {
            this.value = value;
            this.start = start;
            this.duration = duration;
        }
    }

    public List<Integer> countActiveTasks(int n, Task[] tasks, int[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Task:
    def __init__(self, value, start, duration):
        self.value = value
        self.start = start
        self.duration = duration

class Solution:
    def countActiveTasks(self, n: int, tasks: list[Task], queries: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

struct Task {
    int value;
    long long start, duration;
};

class Solution {
public:
    vector<int> countActiveTasks(int n, vector<Task>& tasks, vector<vector<long long>>& queries) {
        // Your code here
        return {};
    }
};
```

```javascript
class Task {
  constructor(value, start, duration) {
    this.value = value;
    this.start = start;
    this.duration = duration;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {Task[]} tasks
   * @param {number[][]} queries
   * @returns {number[]}
   */
  countActiveTasks(n, tasks, queries) {
    // Your code here
    return [];
  }
}
```
