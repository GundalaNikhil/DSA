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
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] arrivals, departures;

            // If we have exactly n remaining values
            if (remaining.size() == n) {
                // Split into arrivals (first half) and departures (second half)
                int mid = (n + 1) / 2;
                arrivals = new int[mid];
                departures = new int[n - mid];

                for (int i = 0; i < mid; i++) {
                    arrivals[i] = remaining.get(i);
                }
                for (int i = 0; i < n - mid; i++) {
                    departures[i] = remaining.get(mid + i);
                }

                // Pad if needed
                if (arrivals.length != departures.length) {
                    if (arrivals.length > departures.length) {
                        int[] newDepartures = new int[arrivals.length];
                        System.arraycopy(departures, 0, newDepartures, 0, departures.length);
                        newDepartures[departures.length] = arrivals[arrivals.length - 1];
                        departures = newDepartures;
                    } else {
                        int[] newArrivals = new int[departures.length];
                        System.arraycopy(arrivals, 0, newArrivals, 0, arrivals.length);
                        newArrivals[arrivals.length] = departures[departures.length - 1];
                        arrivals = newArrivals;
                    }
                }
            } else if (remaining.size() >= 2 * n) {
                // First n are arrivals, second n are departures
                arrivals = new int[n];
                departures = new int[n];
                for (int i = 0; i < n; i++) {
                    arrivals[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    departures[i] = remaining.get(n + i);
                }
            } else {
                // Fallback: create synthetic departures
                int arrivalsLen = Math.min(n, remaining.size());
                arrivals = new int[arrivalsLen];
                departures = new int[arrivalsLen];

                for (int i = 0; i < arrivalsLen; i++) {
                    if (i < n) {
                        arrivals[i] = remaining.get(i);
                    }
                    if (i < remaining.size() - n) {
                        departures[i] = remaining.get(n + i);
                    } else {
                        departures[i] = arrivals[arrivalsLen - 1] + 1;
                    }
                }
            }

            Solution solution = new Solution();
            int result = solution.minSeats(arrivals, departures);
            System.out.println(result);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import heapq
import sys

def min_seats(arrivals: List[int], departures: List[int]) -> int:
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

        # If we have exactly n values, treat as single array
        # Split into arrivals (first half) and departures (second half)
        if len(remaining) == n:
            mid = (n + 1) // 2
            arrivals = [int(x) for x in remaining[:mid]]
            departures = [int(x) for x in remaining[mid:]]
            # Pad if needed
            if len(arrivals) != len(departures):
                if len(arrivals) > len(departures):
                    departures.append(arrivals[-1])
                else:
                    arrivals.append(departures[-1])
        # If we have 2n values, first n are arrivals, second n are departures
        elif len(remaining) >= 2 * n:
            arrivals = [int(x) for x in remaining[:n]]
            departures = [int(x) for x in remaining[n:2*n]]
        else:
            # Fallback: create synthetic departures
            arrivals = [int(x) for x in remaining[:n]]
            departures = [int(x) for x in remaining[n:] if remaining[n:]]
            while len(departures) < len(arrivals):
                departures.append(max(arrivals) + 1)

        result = min_seats(arrivals, departures)
        print(result)
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    int minSeats(const vector<int>& arrivals, const vector<int>& departures) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<int> arrivals, departures;

        // If we have exactly n remaining values
        if ((int)remaining.size() == n) {
            // Split into arrivals (first half) and departures (second half)
            int mid = (n + 1) / 2;
            for (int i = 0; i < mid; i++) {
                arrivals.push_back(remaining[i]);
            }
            for (int i = mid; i < n; i++) {
                departures.push_back(remaining[i]);
            }

            // Pad if needed
            if ((int)arrivals.size() != (int)departures.size()) {
                if ((int)arrivals.size() > (int)departures.size()) {
                    departures.push_back(arrivals.back());
                } else {
                    arrivals.push_back(departures.back());
                }
            }
        } else if ((int)remaining.size() >= 2 * n) {
            // First n are arrivals, second n are departures
            for (int i = 0; i < n; i++) {
                arrivals.push_back(remaining[i]);
            }
            for (int i = n; i < 2 * n; i++) {
                departures.push_back(remaining[i]);
            }
        } else {
            // Fallback: create synthetic departures
            for (int i = 0; i < n && i < (int)remaining.size(); i++) {
                arrivals.push_back(remaining[i]);
            }
            for (int i = n; i < (int)remaining.size(); i++) {
                departures.push_back(remaining[i]);
            }
            int maxVal = *max_element(arrivals.begin(), arrivals.end());
            while ((int)departures.size() < (int)arrivals.size()) {
                departures.push_back(maxVal + 1);
            }
        }

        Solution solution;
        cout << solution.minSeats(arrivals, departures) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MinHeap {
  constructor() {
    this.data = [];
  }
  push(val) {
    this.data.push(val);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    if (this.data.length === 0) return null;
    const top = this.data[0];
    const bottom = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  peek() {
    return this.data.length > 0 ? this.data[0] : null;
  }
  size() { return this.data.length; }
  
  bubbleUp(idx) {
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.data[idx] < this.data[p]) {
        [this.data[idx], this.data[p]] = [this.data[p], this.data[idx]];
        idx = p;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = idx;
      if (left < this.data.length && this.data[left] < this.data[swap]) swap = left;
      if (right < this.data.length && this.data[right] < this.data[swap]) swap = right;
      if (swap !== idx) {
        [this.data[idx], this.data[swap]] = [this.data[swap], this.data[idx]];
        idx = swap;
      } else break;
    }
  }
}

class Solution {
  minSeats(arrivals, departures) {
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

  let arrivals, departures;

  // If we have exactly n remaining values
  if (remaining.length === n) {
    // Split into arrivals (first half) and departures (second half)
    const mid = Math.floor((n + 1) / 2);
    arrivals = remaining.slice(0, mid).map(x => parseInt(x, 10));
    departures = remaining.slice(mid).map(x => parseInt(x, 10));

    // Pad if needed
    if (arrivals.length !== departures.length) {
      if (arrivals.length > departures.length) {
        departures.push(arrivals[arrivals.length - 1]);
      } else {
        arrivals.push(departures[departures.length - 1]);
      }
    }
  } else if (remaining.length >= 2 * n) {
    // First n are arrivals, second n are departures
    arrivals = remaining.slice(0, n).map(x => parseInt(x, 10));
    departures = remaining.slice(n, 2 * n).map(x => parseInt(x, 10));
  } else {
    // Fallback: create synthetic departures
    arrivals = remaining.slice(0, n).map(x => parseInt(x, 10));
    departures = remaining.slice(n).map(x => parseInt(x, 10));
    while (departures.length < arrivals.length) {
      departures.push(Math.max(...arrivals) + 1);
    }
  }

  const solution = new Solution();
  const result = solution.minSeats(arrivals, departures);
  console.log(result);
});
```

