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

```java
import java.util.*;
import java.io.*;

class Solution {
    public int maxTasksCompleted(int n, long e, long[][] tasks) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        long e = Long.parseLong(parts[1]);

        long[][] tasks = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] tParts = br.readLine().trim().split("\\s+");
            tasks[i][0] = Long.parseLong(tParts[0]);
            tasks[i][1] = Long.parseLong(tParts[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.maxTasksCompleted(n, e, tasks));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_tasks_completed(self, n, e, tasks):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx++])
    e = int(input_data[idx++])

    tasks = []
    for _ in range(n):
        d = int(input_data[idx++])
        g = int(input_data[idx++])
        tasks.append([d, g])

    sol = Solution()
    print(sol.max_tasks_completed(n, e, tasks))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxTasksCompleted(int n, long long e, vector<pair<long long, long long>>& tasks) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long e;
    if (!(cin >> n >> e)) return 0;

    vector<pair<long long, long long>> tasks(n);
    for (int i = 0; i < n; i++) {
        cin >> tasks[i].first >> tasks[i].second;
    }

    Solution sol;
    cout << sol.maxTasksCompleted(n, e, tasks) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxTasksCompleted(n, e, tasks) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const e = BigInt(input[idx++]);

  const tasks = [];
  for (let i = 0; i < n; i++) {
    const d = BigInt(input[idx++]);
    const g = BigInt(input[idx++]);
    tasks.push([d, g]);
  }

  const sol = new Solution();
  console.log(sol.maxTasksCompleted(n, e, tasks));
}

solve();
```
