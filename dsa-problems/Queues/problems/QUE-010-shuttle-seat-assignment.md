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
    public int minSeats(int[] arrivals, int[] departures) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arrivals = new int[n];
        int[] departures = new int[n];
        for (int i = 0; i < n; i++) {
            arrivals[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            departures[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.minSeats(arrivals, departures);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def min_seats(arrivals: List[int], departures: List[int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arrivals = [int(next(it)) for _ in range(n)]
    departures = [int(next(it)) for _ in range(n)]

    result = min_seats(arrivals, departures)
    sys.stdout.write(str(result))

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
    int minSeats(const vector<int>& arrivals, const vector<int>& departures) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arrivals(n), departures(n);
    for (int i = 0; i < n; i++) {
        cin >> arrivals[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> departures[i];
    }

    Solution solution;
    cout << solution.minSeats(arrivals, departures) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minSeats(arrivals, departures) {
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
  const arrivals = [];
  const departures = [];
  for (let i = 0; i < n; i++) {
    arrivals.push(parseInt(data[idx++], 10));
  }
  for (let i = 0; i < n; i++) {
    departures.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.minSeats(arrivals, departures);
  console.log(result.toString());
});
```
