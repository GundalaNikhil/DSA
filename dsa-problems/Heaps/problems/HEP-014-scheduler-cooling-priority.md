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

class Solution {
    public long maxPriority(int T, int cooldown, String[] ids, int[] count, long[] priority) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int cooldown = sc.nextInt();
            int T = sc.nextInt();
            String[] ids = new String[m];
            int[] count = new int[m];
            long[] priority = new long[m];
            for (int i = 0; i < m; i++) {
                ids[i] = sc.next();
                count[i] = sc.nextInt();
                priority[i] = sc.nextLong();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maxPriority(T, cooldown, ids, count, priority));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def max_priority(T: int, cooldown: int, ids: list, count: list, priority: list) -> int:
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        m = int(next(it))
        cooldown = int(next(it))
        T = int(next(it))
        ids = []
        count = []
        priority = []
        for _ in range(m):
            ids.append(next(it))
            count.append(int(next(it)))
            priority.append(int(next(it)))
            
        print(max_priority(T, cooldown, ids, count, priority))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

struct Task {
    string id;
    int count;
    long long priority;
    int x;
};

class Solution {
public:
    long long maxPriority(int T, int cooldown, const vector<string>& ids,
                          const vector<int>& count, const vector<long long>& priority) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int m, cooldown, T;
    if (cin >> m >> cooldown >> T) {
        vector<string> ids(m);
        vector<int> count(m);
        vector<long long> priority(m);
        for (int i = 0; i < m; i++) cin >> ids[i] >> count[i] >> priority[i];
        
        Solution solution;
        cout << solution.maxPriority(T, cooldown, ids, count, priority) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxPriority(T, cooldown, ids, count, priority) {
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
  const m = parseInt(data[idx++]);
  const cooldown = parseInt(data[idx++]);
  const T = parseInt(data[idx++]);
  const ids = [];
  const count = [];
  const priority = [];
  for (let i = 0; i < m; i++) {
    ids.push(data[idx++]);
    count.push(parseInt(data[idx++]));
    priority.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.maxPriority(T, cooldown, ids, count, priority));
});
```

