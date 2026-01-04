---
problem_id: QUE_TASK_STREAM_RATE_LIMIT__7319
display_id: QUE-013
slug: task-stream-rate-limit
title: "Task Stream Rate Limit"
difficulty: Medium
difficulty_score: 44
topics:
  - Queue
  - Sliding Window
  - Streaming
tags:
  - queue
  - rate-limit
  - sliding-window
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-013: Task Stream Rate Limit

## Problem Statement

A task scheduler receives requests at integer timestamps. A request is allowed only if there have been fewer than `k` allowed requests in the last `t` time units (inclusive).

Given the timestamps in nondecreasing order, output `true` or `false` for each request indicating whether it is allowed. Rejected requests do not count toward the limit.

![Problem Illustration](../images/QUE-013/problem-illustration.png)

## Input Format

- First line: three integers `n`, `t`, and `k`
- Second line: `n` space-separated integers (timestamps)

## Output Format

- Single line: `n` space-separated values (`true` or `false`)

## Constraints

- `1 <= n <= 100000`
- `1 <= t <= 10^9`
- `1 <= k <= n`
- Timestamps are nondecreasing integers in `[0, 10^9]`

## Example

**Input:**

```
4 4 1
2 4 6 9
```

**Output:**

```
true false false true
```

**Explanation:**

- Time 2 -> allowed (0 in window)
- Time 4 -> window [0, 4] contains 1 allowed -> reject
- Time 6 -> window [2, 6] still has 1 allowed -> reject
- Time 9 -> window [5, 9] has 0 allowed -> allow

![Example Visualization](../images/QUE-013/example-1.png)

## Notes

- Maintain a queue of timestamps for allowed requests
- Remove timestamps < current_time - t
- Allow if queue size < k, then push current timestamp
- Time complexity: O(n)

## Related Topics

Queue, Sliding Window, Rate Limiting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void rateLimit(int n, int t, int k, int[] timestamps) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int t = sc.nextInt();
        int k = sc.nextInt();
        int[] timestamps = new int[n];
        for (int i = 0; i < n; i++) timestamps[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.rateLimit(n, t, k, timestamps);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def rate_limit(self, n, t, k, timestamps):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    t = int(input_data[1])
    k = int(input_data[2])
    timestamps = [int(x) for x in input_data[3:3+n]]
    sol = Solution()
    sol.rate_limit(n, t, k, timestamps)

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
    void rateLimit(int n, int t, int k, const vector<int>& timestamps) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, t, k;
    if (!(cin >> n >> t >> k)) return 0;
    vector<int> timestamps(n);
    for (int i = 0; i < n; i++) cin >> timestamps[i];
    Solution sol;
    sol.rateLimit(n, t, k, timestamps);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  rateLimit(n, t, k, timestamps) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const n = parseInt(input[0]);
  const t = parseInt(input[1]);
  const k = parseInt(input[2]);
  const timestamps = [];
  for (let i = 0; i < n; i++) timestamps.push(parseInt(input[3 + i]));
  const sol = new Solution();
  sol.rateLimit(n, t, k, timestamps);
}

solve();
```
