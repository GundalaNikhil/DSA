---
problem_id: GRD_SHUTTLE_SCHEDULE_DELAY_MINIMIZER__8457
display_id: GRD-016
slug: shuttle-schedule-delay-minimizer
title: "Shuttle Schedule Delay Minimizer"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Scheduling
  - Sorting
tags:
  - greedy
  - scheduling
  - sorting
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-016: Shuttle Schedule Delay Minimizer

## Problem Statement

You have `n` shuttle trips to schedule. Each trip `i` has:

- Planned start time `s[i]`
- Duration `d[i]`

Trips must be executed sequentially (one at a time). If a trip starts later than its planned time, it incurs a delay. This delay propagates: if trip `i` is delayed by `x` time units, all subsequent trips are also delayed by at least `x` units.

Your goal is to choose an execution order that minimizes the total accumulated delay across all trips.

**Delay calculation**: If trip `i` actually starts at time `t` but was planned for time `s[i]`, its delay is `max(0, t - s[i])`.

Return the minimum total delay.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-016.jpg)

## Input Format

- First line: integer `n` (number of trips)
- Next `n` lines: two integers `s d` representing planned start time and duration for each trip

## Output Format

- Single integer: minimum total delay

## Constraints

- `1 <= n <= 10^5`
- `0 <= s[i], d[i] <= 10^9`

## Example

**Input:**

```
2
0 3
1 2
```

**Output:**

```
2
```

**Explanation:**

Trips:

- Trip 0: planned start=0, duration=3
- Trip 1: planned start=1, duration=2

**Order 1: Execute [Trip 0, Trip 1]**

- Trip 0 starts at time 0 (planned), delay=0, ends at time 3
- Trip 1 starts at time 3 (planned for 1), delay=2, ends at time 5
- Total delay = 0 + 2 = 2

**Order 2: Execute [Trip 1, Trip 0]**

- Trip 1 starts at time 0 (planned for 1), delay=0 (early is OK, no negative delay), ends at time 2
- Trip 0 starts at time 2 (planned for 0), delay=2, ends at time 5
- Total delay = 0 + 2 = 2

Both orders give the same total delay of 2.

Output: 2

![Example Visualization](../images/GRD-016/example-1.png)

## Notes

- Sort trips by a specific criteria to minimize weighted completion time
- Use shortest processing time (SPT) rule variant
- Consider sorting by `s[i] - d[i]` or similar metric
- Greedy strategy: Execute trips in order that minimizes cumulative delay
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Scheduling Theory, Weighted Completion Time, Sorting, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minTotalDelay(int n, long[][] trips) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[][] trips = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] tLine = br.readLine().trim().split("\\s+");
            trips[i][0] = Long.parseLong(tLine[0]);
            trips[i][1] = Long.parseLong(tLine[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minTotalDelay(n, trips));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_total_delay(self, n, trips):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1
    trips = []
    for _ in range(n):
        trips.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.min_total_delay(n, trips))

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
    long long minTotalDelay(int n, vector<vector<long long>>& trips) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> trips(n, vector<long long>(2));
    for (int i = 0; i < n; i++) {
        cin >> trips[i][0] >> trips[i][1];
    }

    Solution sol;
    cout << sol.minTotalDelay(n, trips) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minTotalDelay(n, trips) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const trips = [];
  for (let i = 0; i < n; i++) {
    trips.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.minTotalDelay(n, trips).toString());
}

solve();
```
