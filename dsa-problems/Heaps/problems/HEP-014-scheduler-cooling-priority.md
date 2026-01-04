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

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxPriorityScore(int m, int k, int t, List<String[]> tasks) {
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
        int m = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);
        int t = Integer.parseInt(parts[2]);

        List<String[]> tasks = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            tasks.add(br.readLine().trim().split("\\s+"));
        }

        Solution sol = new Solution();
        System.out.println(sol.maxPriorityScore(m, k, t, tasks));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_priority_score(self, m, k, t, tasks):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    first_line = input_data[0].split()
    m = int(first_line[0])
    k = int(first_line[1])
    t = int(first_line[2])

    tasks = []
    for i in range(1, m + 1):
        tasks.append(input_data[i].split())

    sol = Solution()
    print(sol.max_priority_score(m, k, t, tasks))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    long long maxPriorityScore(int m, int k, int t, vector<vector<string>>& tasks) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m, k, t;
    if (!(cin >> m >> k >> t)) return 0;

    vector<vector<string>> tasks(m, vector<string>(3));
    for (int i = 0; i < m; i++) {
        cin >> tasks[i][0] >> tasks[i][1] >> tasks[i][2];
    }

    Solution sol;
    cout << sol.maxPriorityScore(m, k, t, tasks) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxPriorityScore(m, k, t, tasks) {
    // Implement here
    return 0n;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const firstLine = input[0].trim().split(/\s+/);
  const m = parseInt(firstLine[0]);
  const k = parseInt(firstLine[1]);
  const t = parseInt(firstLine[2]);

  const tasks = [];
  for (let i = 1; i <= m; i++) {
    tasks.push(input[i].trim().split(/\s+/));
  }

  const sol = new Solution();
  console.log(sol.maxPriorityScore(m, k, t, tasks).toString());
}

solve();
```
