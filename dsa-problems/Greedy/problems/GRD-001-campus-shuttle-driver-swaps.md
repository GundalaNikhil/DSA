---
problem_id: GRD_CAMPUS_SHUTTLE_DRIVER_SWAPS__3847
display_id: GRD-001
slug: campus-shuttle-driver-swaps
title: "Campus Shuttle Driver Swaps"
difficulty: Easy
difficulty_score: 30
topics:
  - Greedy Algorithms
  - Intervals
  - Coverage
tags:
  - greedy
  - intervals
  - scheduling
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-001: Campus Shuttle Driver Swaps

## Problem Statement

You have `n` shuttle trips that need to be covered by drivers. Each trip has a specific time interval `[start, end]`. Two drivers, A and B, are available with their own availability intervals:

- Driver A is available during interval `[A_start, A_end]`
- Driver B is available during interval `[B_start, B_end]`

Each trip must be assigned to exactly one driver who is available during that entire trip. Your goal is to minimize the number of driver switches (transitions from driver A to driver B or vice versa) while ensuring all trips are covered.

Return the minimum number of switches needed, or `-1` if it's impossible to cover all trips.

![Problem Illustration](../images/GRD-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of trips)
- Next `n` lines: two integers `start end` representing each trip's time interval
- Next line: two integers `A_start A_end` (Driver A's availability)
- Next line: two integers `B_start B_end` (Driver B's availability)

## Output Format

- Single integer: minimum number of driver switches, or `-1` if impossible

## Constraints

- `1 <= n <= 10^5`
- `1 <= start < end <= 10^9`
- `1 <= A_start < A_end <= 10^9`
- `1 <= B_start < B_end <= 10^9`
- All trips are non-overlapping (no two trips happen at the same time)

## Example

**Input:**

```
3
1 3
4 6
7 9
1 8
3 10
```

**Output:**

```
1
```

**Explanation:**

Trips:

- Trip 1: [1, 3]
- Trip 2: [4, 6]
- Trip 3: [7, 9]

Driver availabilities:

- Driver A: [1, 8]
- Driver B: [3, 10]

Optimal assignment:

- Trip 1 [1, 3]: Assign to Driver A (A is available during [1, 8])
- Trip 2 [4, 6]: Assign to Driver A (continue with same driver)
- Trip 3 [7, 9]: Assign to Driver B (A ends at 8, so switch to B)

Total switches: 1 (from A to B before trip 3)

![Example Visualization](../images/GRD-001/example-1.png)

## Notes

- A "switch" occurs when consecutive trips are assigned to different drivers
- Trips are given in chronological order (sorted by start time)
- If a trip cannot be covered by either driver, return -1
- Greedy strategy: Extend the current driver as far as possible; switch only when necessary
- Consider which driver to start with based on coverage of early trips

## Related Topics

Greedy Algorithms, Interval Scheduling, Coverage Problems, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int minSwaps(int n, int[][] trips, int[] driverA, int[] driverB) {
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

        int[][] trips = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] tripLine = br.readLine().trim().split("\\s+");
            trips[i][0] = Integer.parseInt(tripLine[0]);
            trips[i][1] = Integer.parseInt(tripLine[1]);
        }

        String[] aLine = br.readLine().trim().split("\\s+");
        int[] driverA = {Integer.parseInt(aLine[0]), Integer.parseInt(aLine[1])};

        String[] bLine = br.readLine().trim().split("\\s+");
        int[] driverB = {Integer.parseInt(bLine[0]), Integer.parseInt(bLine[1])};

        Solution sol = new Solution();
        System.out.println(sol.minSwaps(n, trips, driverA, driverB));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_swaps(self, n, trips, driver_a, driver_b):
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

    driver_a = [int(input_data[idx]), int(input_data[idx+1])]
    idx += 2
    driver_b = [int(input_data[idx]), int(input_data[idx+1])]

    sol = Solution()
    print(sol.min_swaps(n, trips, driver_a, driver_b))

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
    int minSwaps(int n, vector<vector<int>>& trips, vector<int>& driverA, vector<int>& driverB) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> trips(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> trips[i][0] >> trips[i][1];
    }

    vector<int> driverA(2), driverB(2);
    cin >> driverA[0] >> driverA[1];
    cin >> driverB[0] >> driverB[1];

    Solution sol;
    cout << sol.minSwaps(n, trips, driverA, driverB) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minSwaps(n, trips, driverA, driverB) {
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
    trips.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const driverA = [parseInt(input[idx++]), parseInt(input[idx++])];
  const driverB = [parseInt(input[idx++]), parseInt(input[idx++])];

  const sol = new Solution();
  console.log(sol.minSwaps(n, trips, driverA, driverB));
}

solve();
```
