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

class Solution {
    public int minDriverSwaps(int[][] trips, int[] driverA, int[] driverB) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        int[][] trips = new int[n][2];
        for (int i = 0; i < n; i++) {
            trips[i][0] = sc.nextInt();
            trips[i][1] = sc.nextInt();
        }
        
        int[] driverA = new int[2];
        driverA[0] = sc.nextInt();
        driverA[1] = sc.nextInt();
        
        int[] driverB = new int[2];
        driverB[0] = sc.nextInt();
        driverB[1] = sc.nextInt();
        
        Solution solution = new Solution();
        System.out.println(solution.minDriverSwaps(trips, driverA, driverB));
        sc.close();
    }
}
```

### Python

```python
import sys

def min_driver_swaps(trips, driver_a, driver_b) -> int:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    
    trips = []
    for _ in range(n):
        start = int(next(iterator))
        end = int(next(iterator))
        trips.append((start, end))
        
    a_start = int(next(iterator))
    a_end = int(next(iterator))
    driver_a = (a_start, a_end)
    
    b_start = int(next(iterator))
    b_end = int(next(iterator))
    driver_b = (b_start, b_end)
    
    print(min_driver_swaps(trips, driver_a, driver_b))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDriverSwaps(vector<pair<int,int>>& trips, pair<int,int> driverA, pair<int,int> driverB) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<pair<int,int>> trips(n);
    for (int i = 0; i < n; i++) {
        cin >> trips[i].first >> trips[i].second;
    }
    
    pair<int,int> driverA, driverB;
    cin >> driverA.first >> driverA.second;
    cin >> driverB.first >> driverB.second;
    
    Solution solution;
    cout << solution.minDriverSwaps(trips, driverA, driverB) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minDriverSwaps(trips, driverA, driverB) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  
  const trips = [];
  for (let i = 0; i < n; i++) {
    const [start, end] = data[ptr++].split(" ").map(Number);
    trips.push([start, end]);
  }
  
  const [aStart, aEnd] = data[ptr++].split(" ").map(Number);
  const driverA = [aStart, aEnd];
  
  const [bStart, bEnd] = data[ptr++].split(" ").map(Number);
  const driverB = [bStart, bEnd];
  
  const solution = new Solution();
  console.log(solution.minDriverSwaps(trips, driverA, driverB));
});
```

