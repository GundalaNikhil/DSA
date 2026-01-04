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
import java.io.*;

class Solution {
    public long minTotalSlack(int n, int k, int s, int[][] meetings) {
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
        int k = Integer.parseInt(parts[1]);
        int s = Integer.parseInt(parts[2]);

        int[][] meetings = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] mParts = br.readLine().trim().split("\\s+");
            meetings[i][0] = Integer.parseInt(mParts[0]);
            meetings[i][1] = Integer.parseInt(mParts[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minTotalSlack(n, k, s, meetings));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_total_slack(self, n, k, s, meetings):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx++])
    k = int(input_data[idx++])
    s = int(input_data[idx++])

    meetings = []
    for _ in range(n):
        start = int(input_data[idx++])
        end = int(input_data[idx++])
        meetings.append([start, end])

    sol = Solution()
    print(sol.min_total_slack(n, k, s, meetings))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minTotalSlack(int n, int k, int s, vector<pair<int, int>>& meetings) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k, s;
    if (!(cin >> n >> k >> s)) return 0;

    vector<pair<int, int>> meetings(n);
    for (int i = 0; i < n; i++) {
        cin >> meetings[i].first >> meetings[i].second;
    }

    Solution sol;
    cout << sol.minTotalSlack(n, k, s, meetings) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minTotalSlack(n, k, s, meetings) {
    // Implement here
    return 0n;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);
  const s = parseInt(input[idx++]);

  const meetings = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(input[idx++]);
    const end = parseInt(input[idx++]);
    meetings.push([start, end]);
  }

  const sol = new Solution();
  console.log(sol.minTotalSlack(n, k, s, meetings).toString());
}

solve();
```
