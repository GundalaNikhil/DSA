---
problem_id: QUE_SHUTTLE_SEAT_ASSIGNMENT__4407
display_id: QUE-010
slug: shuttle-seat-assignment
title: "Shuttle Seat Assignment"
difficulty: Medium
difficulty_score: 46
topics:
  - Scheduling
  - Priority Queue
  - Queue
tags:
  - scheduling
  - min-heap
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-010: Shuttle Seat Assignment

## Problem Statement

A shuttle service has a list of passenger arrival and departure times. Each passenger needs one seat for the entire interval `[arrival, departure)`.

Compute the minimum number of seats required so that no passenger has to wait.

![Problem Illustration](../images/QUE-010/problem-illustration.png)

## Input Format

- First line: integer `n` (number of passengers)
- Second line: `n` space-separated integers (arrival times)
- Third line: `n` space-separated integers (departure times)

## Output Format

- Single integer: minimum number of seats required

## Constraints

- `1 <= n <= 100000`
- `0 <= arrival[i], departure[i] <= 10^9`
- All times are integers

## Example

**Input:**

```
3
0 4 4
5 5 9
```

**Output:**

```
2
```

**Explanation:**

At time 4, two passengers overlap:

- Passenger 1: [0, 5)
- Passenger 2: [4, 5)
- Passenger 3: [4, 9)

Two seats are sufficient.

![Example Visualization](../images/QUE-010/example-1.png)

## Notes

- Sort passengers by arrival time
- Use a min-heap or queue of current departure times
- Reuse a seat when the earliest departure time <= current arrival
- Time complexity: O(n log n)

## Related Topics

Scheduling, Priority Queue, Interval Overlap

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minSeats(int n, int[] arrivals, int[] departures) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arrivals = new int[n];
        for (int i = 0; i < n; i++) arrivals[i] = sc.nextInt();
        int[] departures = new int[n];
        for (int i = 0; i < n; i++) departures[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.minSeats(n, arrivals, departures));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def min_seats(self, n, arrivals, departures):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arrivals = [int(x) for x in input_data[1:1+n]]
    departures = [int(x) for x in input_data[1+n:1+2*n]]
    sol = Solution()
    print(sol.min_seats(n, arrivals, departures))

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
    int minSeats(int n, const vector<int>& arrivals, const vector<int>& departures) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> arrivals(n), departures(n);
    for (int i = 0; i < n; i++) cin >> arrivals[i];
    for (int i = 0; i < n; i++) cin >> departures[i];
    Solution sol;
    cout << sol.minSeats(n, arrivals, departures) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minSeats(n, arrivals, departures) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const arrivals = [];
  for (let i = 0; i < n; i++) arrivals.push(parseInt(input[1 + i]));
  const departures = [];
  for (let i = 0; i < n; i++) departures.push(parseInt(input[1 + n + i]));
  const sol = new Solution();
  console.log(sol.minSeats(n, arrivals, departures));
}

solve();
```
