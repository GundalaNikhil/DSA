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
    public List<String> rateLimit(long[] times, long t, int k) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long t = sc.nextLong();
        int k = sc.nextInt();
        long[] times = new long[n];
        for (int i = 0; i < n; i++) {
            times[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        List<String> result = solution.rateLimit(times, t, k);
        System.out.println(String.join(" ", result));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def rate_limit(times: List[int], t: int, k: int) -> List[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    t = int(next(it))
    k = int(next(it))
    times = [int(next(it)) for _ in range(n)]

    result = rate_limit(times, t, k)
    sys.stdout.write(" ".join(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> rateLimit(const vector<long long>& times, long long t, int k) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long t;
    int k;
    if (!(cin >> n >> t >> k)) return 0;
    vector<long long> times(n);
    for (int i = 0; i < n; i++) {
        cin >> times[i];
    }

    Solution solution;
    vector<string> result = solution.rateLimit(times, t, k);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  rateLimit(times, t, k) {
    // Your implementation here
    return [];
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
  const n = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const times = [];
  for (let i = 0; i < n; i++) {
    times.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.rateLimit(times, t, k);
  console.log(result.join(" "));
});
```
