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
---

# GRD-001: Campus Shuttle Driver Swaps

## 📋 Problem Summary

You are given a schedule of `n` shuttle trips, each with a start and end time. Two drivers, A and B, have specific availability windows. You need to assign every trip to a driver who is available for the entire duration of that trip. The goal is to minimize the number of times you switch drivers between consecutive trips. If it's impossible to cover all trips, return -1.

## 🌍 Real-World Scenario

**Scenario Title:** Efficient Shift Management in Logistics

Imagine a logistics company managing a delivery route that runs 24/7. They have two primary drivers on a shift, but each driver has strict legal limits on when they can operate (e.g., Driver A can work 8 AM - 4 PM, Driver B can work 2 PM - 10 PM).

The delivery schedule consists of specific "legs" or trips that cannot be interrupted. Switching drivers requires the truck to stop, drivers to swap keys, log hours, and potentially relocate, which costs time and money. The company wants to cover all scheduled delivery legs while minimizing these costly handovers.

**Why This Problem Matters:**

- **Operational Efficiency:** Minimizing handovers keeps the fleet moving and reduces downtime.
- **Resource Constraints:** Real-world scheduling always involves fixed availability windows (shifts, maintenance blocks).
- **Cost Reduction:** Every switch might incur a fixed cost (setup time, administrative overhead).

![Real-World Application](../images/GRD-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Timeline Visualization

```text
Time:   1   2   3   4   5   6   7   8   9   10
        |---|---|---|---|---|---|---|---|---|
Trips:  [ T1  ]     [ T2  ]     [ T3  ]

Driver A: [===========================] (1 to 8)
Driver B:         [===========================] (3 to 10)

Analysis:
T1 (1-3): Covered by A? Yes. Covered by B? Yes (barely, starts at 3).
T2 (4-6): Covered by A? Yes. Covered by B? Yes.
T3 (7-9): Covered by A? No (ends at 8). Covered by B? Yes.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Chronological Order:** The trips are guaranteed to be sorted by their start times.
- **Non-overlapping:** No two trips occur at the same time; `end` of one trip <= `start` of the next.
- **Availability:** A driver is available for a trip `[s, e]` if and only if `DriverStart <= s` AND `e <= DriverEnd`.
- **Switches:** A switch happens when Trip `i` is driven by A and Trip `i+1` is driven by B (or vice versa). The first driver assignment does not count as a switch.

## Naive Approach

### Intuition

We can try every possible valid assignment for each trip. For each trip, we check if Driver A can take it and if Driver B can take it. We recursively explore all valid paths and count the switches.

### Algorithm

1. Define a recursive function `solve(tripIndex, lastDriver)`.
2. Base case: If `tripIndex == n`, return 0 (all trips covered).
3. Recursive step:
   - Try assigning Driver A: If valid, cost is `(lastDriver != A) + solve(tripIndex + 1, A)`.
   - Try assigning Driver B: If valid, cost is `(lastDriver != B) + solve(tripIndex + 1, B)`.
4. Return the minimum of valid options.

### Time Complexity

- **O(2^N)**: In the worst case, both drivers are available for every trip, creating a binary decision tree of depth N.

### Space Complexity

- **O(N)**: Recursion stack depth.

### Limitations

- With `n` up to $10^5$, $2^{100000}$ is impossibly large. We need a more efficient approach.

## Optimal Approach

### Key Insight

Since we process trips in order, the only information that matters for the *future* is **who drove the last trip**. This suggests a Dynamic Programming approach or a greedy strategy with state tracking.

We can maintain two values as we iterate through the trips:
1. `costA`: The minimum switches needed to cover all trips up to the current one, ending with **Driver A**.
2. `costB`: The minimum switches needed to cover all trips up to the current one, ending with **Driver B**.

### Algorithm

1. **Initialize:**
   - Check Trip 0.
   - `costA = 0` if A can cover Trip 0, else `infinity`.
   - `costB = 0` if B can cover Trip 0, else `infinity`.

2. **Iterate** from Trip 1 to `n-1`:
   - Calculate `newCostA`:
     - If A cannot cover current trip, `newCostA = infinity`.
     - Else, `newCostA = min(costA, costB + 1)`. (Stay with A costs 0 extra, switch from B costs 1).
   - Calculate `newCostB`:
     - If B cannot cover current trip, `newCostB = infinity`.
     - Else, `newCostB = min(costB, costA + 1)`. (Stay with B costs 0 extra, switch from A costs 1).
   - Update `costA = newCostA`, `costB = newCostB`.

3. **Final Result:**
   - `ans = min(costA, costB)`.
   - If `ans` is still `infinity`, return `-1`.

### Time Complexity

- **O(N)**: We iterate through the trips once.

### Space Complexity

- **O(1)**: We only store two integer variables (`costA`, `costB`).

### Why This Is Optimal

We make a locally optimal decision at each step by carrying forward the best possible cost to reach that state (ending with A or ending with B). Since the history before the last driver doesn't affect future constraints, this state is sufficient.

![Algorithm Visualization](../images/GRD-001/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int minDriverSwaps(int[][] trips, int[] driverA, int[] driverB) {
        int n = trips.length;
        // Costs to reach current trip ending with Driver A or Driver B
        // Use a large number for infinity, but safe from overflow when adding 1
        int INF = Integer.MAX_VALUE / 2;
        int costA = INF;
        int costB = INF;

        // Base case: Trip 0
        if (canCover(trips[0], driverA)) costA = 0;
        if (canCover(trips[0], driverB)) costB = 0;

        for (int i = 1; i < n; i++) {
            int nextCostA = INF;
            int nextCostB = INF;

            // If Driver A can take current trip
            if (canCover(trips[i], driverA)) {
                // Option 1: Continued from A (0 cost)
                // Option 2: Switched from B (1 cost)
                nextCostA = Math.min(costA, costB + 1);
            }

            // If Driver B can take current trip
            if (canCover(trips[i], driverB)) {
                // Option 1: Continued from B (0 cost)
                // Option 2: Switched from A (1 cost)
                nextCostB = Math.min(costB, costA + 1);
            }

            costA = nextCostA;
            costB = nextCostB;
        }

        int result = Math.min(costA, costB);
        return result >= INF ? -1 : result;
    }

    private boolean canCover(int[] trip, int[] driver) {
        return driver[0] <= trip[0] && trip[1] <= driver[1];
    }
}

public class Main {
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
    n = len(trips)
    INF = float('inf')
    
    # cost_a: min switches ending with A
    # cost_b: min switches ending with B
    cost_a = INF
    cost_b = INF
    
    # Helper to check coverage
    def can_cover(trip, driver):
        return driver[0] <= trip[0] and trip[1] <= driver[1]
    
    # Base case: Trip 0
    if can_cover(trips[0], driver_a):
        cost_a = 0
    if can_cover(trips[0], driver_b):
        cost_b = 0
        
    for i in range(1, n):
        next_cost_a = INF
        next_cost_b = INF
        
        # Try assigning current trip to A
        if can_cover(trips[i], driver_a):
            next_cost_a = min(cost_a, cost_b + 1)
            
        # Try assigning current trip to B
        if can_cover(trips[i], driver_b):
            next_cost_b = min(cost_b, cost_a + 1)
            
        cost_a = next_cost_a
        cost_b = next_cost_b
        
    result = min(cost_a, cost_b)
    return result if result != INF else -1

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
        int n = trips.size();
        const int INF = 1e9;
        
        int costA = INF;
        int costB = INF;
        
        auto canCover = [](pair<int,int>& trip, pair<int,int>& driver) {
            return driver.first <= trip.first && trip.second <= driver.second;
        };
        
        // Base case
        if (canCover(trips[0], driverA)) costA = 0;
        if (canCover(trips[0], driverB)) costB = 0;
        
        for (int i = 1; i < n; i++) {
            int nextCostA = INF;
            int nextCostB = INF;
            
            if (canCover(trips[i], driverA)) {
                nextCostA = min(costA, costB + 1);
            }
            
            if (canCover(trips[i], driverB)) {
                nextCostB = min(costB, costA + 1);
            }
            
            costA = nextCostA;
            costB = nextCostB;
        }
        
        int result = min(costA, costB);
        return result >= INF ? -1 : result;
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
    const n = trips.length;
    const INF = Number.MAX_SAFE_INTEGER;
    
    let costA = INF;
    let costB = INF;
    
    const canCover = (trip, driver) => {
      return driver[0] <= trip[0] && trip[1] <= driver[1];
    };
    
    // Base case
    if (canCover(trips[0], driverA)) costA = 0;
    if (canCover(trips[0], driverB)) costB = 0;
    
    for (let i = 1; i < n; i++) {
      let nextCostA = INF;
      let nextCostB = INF;
      
      if (canCover(trips[i], driverA)) {
        nextCostA = Math.min(costA, costB + 1);
      }
      
      if (canCover(trips[i], driverB)) {
        nextCostB = Math.min(costB, costA + 1);
      }
      
      costA = nextCostA;
      costB = nextCostB;
    }
    
    let result = Math.min(costA, costB);
    return result >= INF ? -1 : result;
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

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
1 3
4 6
7 9
1 8
3 10
```

**State Initialization:**
- Driver A: [1, 8]
- Driver B: [3, 10]
- Trips: T1[1,3], T2[4,6], T3[7,9]

**Step-by-Step Execution:**

| Step | Trip | Can A? | Can B? | `costA` (end with A) | `costB` (end with B) | Explanation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | T1 [1,3] | ✅ Yes | ✅ Yes | 0 | 0 | Both can start. No switches yet. |
| **1** | T2 [4,6] | ✅ Yes | ✅ Yes | min(0, 0+1) = 0 | min(0, 0+1) = 0 | A continues from A (0). B continues from B (0). |
| **2** | T3 [7,9] | ❌ No | ✅ Yes | INF | min(0, 0+1) = 1 | A fails (ends at 8). B can take it; switching from A costs 1. |

**Final Result:**
- `min(costA, costB) = min(INF, 1) = 1`.

**Output:** `1`

![Example Visualization](../images/GRD-001/example-1.png)

## ✅ Proof of Correctness

### Invariant
At step `i`, `costA` correctly stores the minimum number of switches required to cover trips `0` through `i` ending with Driver A. Similarly for `costB`.

### Inductive Step
Assume `costA` and `costB` are correct for trip `i-1`.
For trip `i`:
- To end with A: We could have come from A (cost `costA`) or from B (cost `costB + 1`). We take the minimum. This covers all valid ways to reach state "Trip `i` covered by A".
- Same logic applies to ending with B.
Since we exhaustively check all valid transitions (A->A, B->A, B->B, A->B) and accumulate costs, the final values at `n-1` must be optimal.

## 💡 Interview Extensions

- **Extension 1:** What if there are `k` drivers instead of 2?
  - *Approach:* `dp[i][d]` = min switches ending with driver `d`. Complexity becomes $O(N \cdot K)$.
- **Extension 2:** What if switching drivers has a cost (e.g., salary difference)?
  - *Approach:* Instead of `+1`, add `+switchCost`. The logic remains identical.
- **Extension 3:** What if drivers have multiple disjoint availability intervals?
  - *Approach:* Pre-process availability into a lookup or interval tree. The DP state might need to track *which* interval was used if it matters, but usually just "Driver ID" is enough.

### C++ommon Mistakes to Avoid

1. **Greedy Misstep**
   - ❌ Wrong: Always picking the driver who can cover the *next* trip too.
   - ✅ Correct: Sometimes you must pick a driver who *can't* cover the next trip to save a switch later (though in this specific 2-driver problem, simple greedy often works, DP is safer and same complexity).

2. **Off-by-one Errors**
   - ❌ Wrong: Counting the first assignment as a switch.
   - ✅ Correct: Initialize costs to 0. Only increment when `prev != curr`.

3. **Ignoring Impossible Cases**
   - ❌ Wrong: Returning a large number instead of -1.
   - ✅ Correct: Check if result >= INF and return -1.

## Related Concepts

- **Dynamic Programming:** State transition optimization.
- **Interval Scheduling:** Managing resources over time.
- **Activity Selection:** Similar greedy choice structures.
