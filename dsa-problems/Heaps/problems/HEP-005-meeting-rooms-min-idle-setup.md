---
problem_id: HEP_MEETING_ROOMS_MIN_IDLE_SETUP__3108
display_id: HEP-005
slug: meeting-rooms-min-idle-setup
title: "Meeting Rooms Min Idle with Setup Time"
difficulty: Medium
difficulty_score: 54
topics:
  - Heaps
  - Scheduling
  - Intervals
tags:
  - heaps
  - scheduling
  - intervals
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-005: Meeting Rooms Min Idle with Setup Time

## Problem Statement

You must assign meetings to `k` rooms. Each meeting is a time interval `[start, end]`. After a meeting ends, the room requires `s` units of setup time before it can host the next meeting. If two meetings `i` and `j` are in the same room, then:

```
end_i + s <= start_j
```

The slack between consecutive meetings in a room is:

```
start_j - (end_i + s)
```

Minimize the total slack across all rooms. Input guarantees that a valid schedule exists.

![Problem Illustration](../images/HEP-005/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `s`
- Next `n` lines: two integers `start` and `end`

## Output Format

- Single integer: minimum total slack

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- `0 <= s <= 10^6`
- `0 <= start <= end <= 10^9`

## Example

**Input:**

```
3 2 1
0 10
5 8
13 20
```

**Output:**

```
2
```

**Explanation:**

Assign meetings as:

- Room 1: [0,10] then [13,20] -> slack = 13 - (10 + 1) = 2
- Room 2: [5,8] -> no slack

Total slack = 2.

![Example Visualization](../images/HEP-005/example-1.png)

## Notes

- Sort meetings by start time
- Use a heap of room availability times
- Choose the room that becomes available latest but still <= start
- Time complexity: O(n log k)
- Space complexity: O(k)

## Related Topics

Heaps, Scheduling, Interval Partitioning, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minTotalSlack(int[][] meetings, int k, int s) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int s = sc.nextInt();
        int[][] meetings = new int[n][2];
        for (int i = 0; i < n; i++) {
            meetings[i][0] = sc.nextInt();
            meetings[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.minTotalSlack(meetings, k, s));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def min_total_slack(meetings: List[List[int]], k: int, s: int) -> int:
    # Your implementation here
    return 0

def main():
    n, k, s = map(int, input().split())
    meetings = []
    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append([start, end])

    result = min_total_slack(meetings, k, s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long minTotalSlack(const vector<vector<int>>& meetings, int k, int s) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, s;
    cin >> n >> k >> s;
    vector<vector<int>> meetings(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> meetings[i][0] >> meetings[i][1];
    }

    Solution solution;
    cout << solution.minTotalSlack(meetings, k, s) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minTotalSlack(meetings, k, s) {
    // Your implementation here
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
  const n = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const s = parseInt(data[idx++], 10);
  const meetings = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(data[idx++], 10);
    const end = parseInt(data[idx++], 10);
    meetings.push([start, end]);
  }

  const solution = new Solution();
  console.log(solution.minTotalSlack(meetings, k, s));
});
```
