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
    public int maxTasks(int E, int[] duration, int[] gain) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int E = sc.nextInt();
            int[] duration = new int[n];
            int[] gain = new int[n];
            for (int i = 0; i < n; i++) {
                duration[i] = sc.nextInt();
                gain[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.maxTasks(E, duration, gain));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def max_tasks(E: int, duration: list, gain: list) -> int:
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        E = int(next(it))
        duration = []
        gain = []
        for _ in range(n):
            duration.append(int(next(it)))
            gain.append(int(next(it)))

        print(max_tasks(E, duration, gain))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Task {
    int d, g;
};

class Solution {
public:
    int maxTasks(long long E, const vector<int>& duration, const vector<int>& gain) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long E;
    if (cin >> n >> E) {
        vector<int> duration(n), gain(n);
        for (int i = 0; i < n; i++) cin >> duration[i] >> gain[i];

        Solution solution;
        cout << solution.maxTasks(E, duration, gain) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxTasks(E, duration, gain) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++]);
  const E = parseInt(data[idx++]);
  const duration = [];
  const gain = [];
  for (let i = 0; i < n; i++) {
    duration.push(parseInt(data[idx++]));
    gain.push(parseInt(data[idx++]));
  }

  const solution = new Solution();
  console.log(solution.maxTasks(E, duration, gain));
});
```
