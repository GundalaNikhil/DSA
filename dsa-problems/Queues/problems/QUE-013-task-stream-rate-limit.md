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
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Long> remaining = new ArrayList<>();
            while (sc.hasNextLong()) {
                remaining.add(sc.nextLong());
            }

            long[] times;
            long t = 1;
            int k = 1;

            // If we have exactly n remaining values
            if (remaining.size() == n) {
                times = new long[n];
                for (int i = 0; i < n; i++) {
                    times[i] = remaining.get(i);
                }
                t = 1;
                k = 1;
            } else if (remaining.size() == n + 2) {
                // First two are t and k
                t = remaining.get(0);
                k = remaining.get(1).intValue();
                times = new long[n];
                for (int i = 0; i < n; i++) {
                    times[i] = remaining.get(i + 2);
                }
            } else {
                // Fallback
                if (remaining.size() > 0) {
                    t = remaining.get(0);
                }
                if (remaining.size() > 1) {
                    k = remaining.get(1).intValue();
                }
                int start = 2;
                times = new long[Math.min(n, remaining.size() - start)];
                for (int i = 0; i < times.length; i++) {
                    times[i] = remaining.get(start + i);
                }
            }

            Solution sol = new Solution();
            List<String> results = sol.rateLimit(times, t, k);
            for (int i = 0; i < results.size(); i++) {
                if (i > 0) System.out.print(" ");
                System.out.print(results.get(i));
            }
            System.out.println();
        }
    }
}
```

### Python

```python
from collections import deque
from typing import List
import sys

def rate_limit(times: List[int], t: int, k: int) -> List[str]:
    # //Implement here
    return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly n values, use as times with default t and k
        if len(remaining) == n:
            times = [int(x) for x in remaining]
            t = 1  # Default time window
            k = 1  # Default capacity
        # If we have n + 2 values, first two are t and k
        elif len(remaining) == n + 2:
            t = int(remaining[0])
            k = int(remaining[1])
            times = [int(x) for x in remaining[2:n+2]]
        # If we have more than n, assume first two are parameters
        else:
            t = int(remaining[0]) if len(remaining) > 0 else 1
            k = int(remaining[1]) if len(remaining) > 1 else 1
            times = [int(x) for x in remaining[2:n+2]]

        result = rate_limit(times, t, k)
        print(" ".join(result))
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <deque>

using namespace std;

class Solution {
public:
    vector<string> rateLimit(const vector<long long>& times, long long t, int k) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<long long> remaining;
        long long val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<long long> times;
        long long t = 1;
        int k = 1;

        // If we have exactly n remaining values
        if ((int)remaining.size() == n) {
            times.assign(remaining.begin(), remaining.end());
            t = 1;
            k = 1;
        } else if ((int)remaining.size() == n + 2) {
            // First two are t and k
            t = remaining[0];
            k = (int)remaining[1];
            times.assign(remaining.begin() + 2, remaining.begin() + n + 2);
        } else {
            // Fallback
            if (!remaining.empty()) {
                t = remaining[0];
            }
            if (remaining.size() > 1) {
                k = (int)remaining[1];
            }
            int start = 2;
            for (int i = start; i < start + n && i < (int)remaining.size(); i++) {
                times.push_back(remaining[i]);
            }
        }

        Solution sol;
        vector<string> results = sol.rateLimit(times, t, k);
        for (int i = 0; i < (int)results.size(); i++) {
            cout << (i ? " " : "") << results[i];
        }
        cout << endl;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  rateLimit(times, t, k) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let t, k, times;

  // If we have exactly n remaining values
  if (remaining.length === n) {
    times = remaining.slice(0, n).map(x => parseInt(x, 10));
    t = 1;  // Default
    k = 1;  // Default
  } else if (remaining.length === n + 2) {
    // First two are t and k
    t = parseInt(remaining[0], 10);
    k = parseInt(remaining[1], 10);
    times = remaining.slice(2, n + 2).map(x => parseInt(x, 10));
  } else {
    // Fallback: assume first two (if present) are t and k
    t = remaining.length > 0 ? parseInt(remaining[0], 10) : 1;
    k = remaining.length > 1 ? parseInt(remaining[1], 10) : 1;
    times = remaining.slice(2, n + 2).map(x => parseInt(x, 10));
  }

  const solution = new Solution();
  const result = solution.rateLimit(times, t, k);
  console.log(result.join(" "));
});
```

