---
title: Task Stream Rate Limit
slug: task-stream-rate-limit
difficulty: Medium
difficulty_score: 44
tags:
- Queue
- Sliding Window
- Streaming
problem_id: QUE_TASK_STREAM_RATE_LIMIT__7319
display_id: QUE-013
topics:
- Queue
- Sliding Window
- Streaming
---
# Task Stream Rate Limit - Editorial

## Problem Summary

You are given a stream of requests arriving at specific integer timestamps. A request is allowed if and only if the number of *allowed* requests in the last `t` time units (inclusive of the current time) is strictly less than `k`. You need to process these requests in order and determine for each whether it is `true` (allowed) or `false` (rejected).

## Real-World Scenario

Think of an **API Rate Limiter** for a popular public API (like Twitter or GitHub). To prevent abuse and ensure fair usage, the system enforces a policy: "A user can make at most `k` API calls within any `t` second window."

When a user sends a request:
1.  The system checks how many requests this user has successfully made in the last `t` seconds.
2.  If this count is less than `k`, the request is accepted. The system records this new timestamp.
3.  If the count is already `k`, the request is rejected (429 Too Many Requests). The timestamp of this rejected request is *not* recorded for future counts because it didn't consume any resources.

This ensures the server isn't overwhelmed by a single user flooding it with requests.

## Problem Exploration

### 1. Understanding the Constraints
-   `n` (number of requests) up to `10^5`.
-   Timestamps are non-decreasing.
-   `t` can be very large (`10^9`), so we cannot use a fixed-size array representing every second.
-   `k` up to `n`.

### 2. The Sliding Window
For a request at time `current_time`, the relevant window is `[current_time - t, current_time]`. We only care about requests that were *allowed* within this range. Rejected requests do not affect the count for future requests.

### 3. Data Structure Choice
Since timestamps are non-decreasing, the "allowed" timestamps naturally form a sorted sequence. As time progresses, old timestamps fall out of the window from the left (smallest values), and new allowed timestamps are added to the right (largest values). This First-In-First-Out behavior suggests using a **Queue**.

## Approaches

### Approach 1: Naive Simulation (Time Limit Exceeded)

For each incoming request, we can store a list of all previously allowed timestamps. To check if the current request is allowed, we iterate through this list and count how many timestamps fall within the range `[current_time - t, current_time]`.

-   **Algorithm**:
    1.  Maintain a list `allowed_history`.
    2.  For each `time` in input:
        a.  Count elements in `allowed_history` such that `val >= time - t`.
        b.  If count < `k`, add `time` to `allowed_history` and output `true`.
        c.  Else, output `false`.

-   **Complexity**:
    -   Time: `O(N^2)` in the worst case (e.g., all requests allowed, `t` is large). With `N=10^5`, this will TLE.
    -   Space: `O(N)` to store history.

### Approach 2: Optimal Queue-Based Sliding Window

We can optimize the counting process. We don't need to iterate through the entire history every time. We only care about the valid window. Since timestamps are sorted, we can remove timestamps from the front of our history that are too old (`< current_time - t`).

-   **Algorithm**:
    1.  Initialize an empty queue (or deque) `Q`.
    2.  For each `time` in the input:
        a.  **Clean up**: Remove elements from the front of `Q` while `Q.front() < time - t`. These requests are no longer in the window.
        b.  **Check**: If `Q.size() < k`:
            -   The request is allowed.
            -   Push `time` to the back of `Q`.
            -   Output `true`.
        c.  **Else**:
            -   The request is rejected.
            -   Do not push anything to `Q`.
            -   Output `false`.

-   **Visual Execution**:
    `t = 4`, `k = 1`
    Requests: `[2, 4, 6, 9]`

    1.  **Time 2**:
        -   Window: `[-2, 2]`.
        -   Q: `[]`. No cleanup needed.
        -   Size 0 < 1. Allowed.
        -   Q: `[2]`. Output: `true`.

    2.  **Time 4**:
        -   Window: `[0, 4]`.
        -   Q: `[2]`. `2 >= 4-4` (0). Keep 2.
        -   Size 1 is not < 1. Rejected.
        -   Q: `[2]`. Output: `false`.

    3.  **Time 6**:
        -   Window: `[2, 6]`.
        -   Q: `[2]`. `2 >= 6-4` (2). Keep 2.
        -   Size 1 is not < 1. Rejected.
        -   Q: `[2]`. Output: `false`.

    4.  **Time 9**:
        -   Window: `[5, 9]`.
        -   Q: `[2]`. `2 < 9-4` (5). Remove 2.
        -   Q: `[]`.
        -   Size 0 < 1. Allowed.
        -   Q: `[9]`. Output: `true`.

-   **Complexity**:
    -   **Time**: `O(N)`. Each timestamp is added to the queue at most once and removed at most once.
    -   **Space**: `O(k)`. The queue will never hold more than `k` elements because we stop adding when size reaches `k`.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public List<String> rateLimit(long[] times, long t, int k) {
        List<String> result = new ArrayList<>();
        Deque<Long> queue = new ArrayDeque<>();
        
        for (long time : times) {
            // Remove expired requests
            while (!queue.isEmpty() && queue.peekFirst() < time - t) {
                queue.pollFirst();
            }
            
            if (queue.size() < k) {
                queue.offerLast(time);
                result.add("true");
            } else {
                result.add("false");
            }
        }
        
        return result;
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
    q = deque()
    result = []
    
    for time in times:
        # Remove timestamps that are outside the window [time - t, time]
        while q and q[0] < time - t:
            q.popleft()
            
        if len(q) < k:
            q.append(time)
            result.append("true")
        else:
            result.append("false")
            
    return result

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
        deque<long long> q;
        vector<string> result;
        result.reserve(times.size());
        
        for (long long time : times) {
            // Remove expired requests
            while (!q.empty() && q.front() < time - t) {
                q.pop_front();
            }
            
            if (q.size() < k) {
                q.push_back(time);
                result.push_back("true");
            } else {
                result.push_back("false");
            }
        }
        
        return result;
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
    const queue = [];
    let front = 0;
    const result = [];
    
    for (const time of times) {
      while (front < queue.length && queue[front] < time - t) {
        front++;
      }
      
      if (queue.length - front < k) {
        queue.push(time);
        result.push("true");
      } else {
        result.push("false");
      }
    }
    
    return result;
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

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`n = 6`, `t = 10`, `k = 2`
`times = [1, 5, 8, 11, 15, 20]`

1.  **Time 1**:
    -   Window `[-9, 1]`. Queue `[]`.
    -   Size 0 < 2. Allow.
    -   Queue `[1]`. Output `true`.

2.  **Time 5**:
    -   Window `[-5, 5]`. Queue `[1]`.
    -   `1 >= 5-10` (-5). Keep.
    -   Size 1 < 2. Allow.
    -   Queue `[1, 5]`. Output `true`.

3.  **Time 8**:
    -   Window `[-2, 8]`. Queue `[1, 5]`.
    -   `1 >= 8-10` (-2). Keep.
    -   Size 2 is not < 2. Reject.
    -   Queue `[1, 5]`. Output `false`.

4.  **Time 11**:
    -   Window `[1, 11]`. Queue `[1, 5]`.
    -   `1 >= 11-10` (1). Keep.
    -   Size 2 is not < 2. Reject.
    -   Queue `[1, 5]`. Output `false`.

5.  **Time 15**:
    -   Window `[5, 15]`. Queue `[1, 5]`.
    -   `1 < 15-10` (5). Remove 1.
    -   Queue `[5]`. `5 >= 5`. Keep.
    -   Size 1 < 2. Allow.
    -   Queue `[5, 15]`. Output `true`.

6.  **Time 20**:
    -   Window `[10, 20]`. Queue `[5, 15]`.
    -   `5 < 20-10` (10). Remove 5.
    -   Queue `[15]`. `15 >= 10`. Keep.
    -   Size 1 < 2. Allow.
    -   Queue `[15, 20]`. Output `true`.

**Final Output:** `true true false false true true`

## Proof of Correctness

The algorithm correctly implements the problem statement by maintaining the invariant that the queue contains exactly the timestamps of *allowed* requests that fall within the window `[current_time - t, current_time]`.
1.  **Cleanup**: By removing elements `< current_time - t`, we ensure no expired requests count towards the limit.
2.  **Check**: We compare the count of valid requests against `k`.
3.  **Update**: We only add the current timestamp if it is allowed, consistent with the rule that rejected requests don't count.
Since the input is sorted, the queue naturally remains sorted, allowing efficient removal from the front.

## Interview Extensions

1.  **What if timestamps are not sorted?**
    -   If timestamps are not sorted, we would first need to sort them (`O(N log N)`). If the problem implies real-time processing where sorting isn't possible, we'd need a different approach, but "rate limiting" usually implies chronological order.

2.  **What if `t` is small but `n` is huge (streaming)?**
    -   The queue approach still works perfectly. The memory usage is bounded by `k`, not `n`.

3.  **What if we need to support different users?**
    -   We would use a Hash Map where keys are user IDs and values are the Queues described above.

4.  **How to handle high-precision timestamps (e.g., doubles)?**
    -   The logic remains the same, just change data types. Floating point comparisons should use an epsilon if strict equality is needed, but for inequalities, standard operators usually suffice.

### Common Mistakes

-   **Including rejected requests**: A common bug is to add *every* timestamp to the queue and then check the size. The problem states rejected requests do not count.
-   **Off-by-one in window**: The window is `t` time units. Usually, this means `[now - t, now]` is inclusive or exclusive depending on definition. Here, "last `t` time units" usually implies `time - t` is the boundary. If the problem said "within `t` seconds", `time - t` is generally the cutoff.
-   **Using `k` as window size**: `k` is the *count* limit, `t` is the *time* window. Don't confuse them.

## Related Concepts

-   **Sliding Window**: The core pattern used here.
-   **Leaky Bucket / Token Bucket**: Standard algorithms for rate limiting in system design.
-   **Queue**: The underlying data structure.
