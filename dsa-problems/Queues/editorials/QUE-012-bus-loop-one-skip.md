---
problem_id: QUE_BUS_LOOP_ONE_SKIP__2986
display_id: QUE-012
slug: bus-loop-one-skip
title: "Bus Loop With One Free Skip"
difficulty: Medium
difficulty_score: 58
topics:
  - Greedy
  - Queue
  - Circular Route
tags:
  - greedy
  - circular
  - queue
  - medium
premium: true
subscription_tier: basic
---

# QUE-012: Bus Loop With One Free Skip

## 📋 Problem Summary

We have a circular route with `N` stops. At stop `i`, we gain `gain[i]` fuel and spend `cost[i]` to move to the next stop.
- We must complete one full loop.
- We **must** skip refueling at exactly one stop (we lose the `gain` at that stop, but still pay the `cost`).
- Find a starting index that makes this possible. If none, return -1.

## 🌍 Real-World Scenario

**Scenario Title:** Formula 1 Pit Stop Strategy

Imagine an F1 race car.
- It refuels at every pit stop to make it to the next sector.
- However, due to a penalty or a mechanical failure, the fuel pump at **one** pit stop will fail (you get 0 fuel).
- The team needs to calculate: "If we start the lap sequence at Sector X, can we survive the entire lap even if one refueling fails?"
- They need to pick a starting sector such that the accumulated fuel buffer is high enough to absorb the loss of one station.

**Why This Problem Matters:**

- **Fault Tolerance:** Designing systems that survive single-point failures.
- **Financial Planning:** Ensuring cash flow stays positive even if one client defaults.

![Real-World Application](../images/QUE-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Fuel Balance

Stops: 0, 1, 2.
Gain: `[4, 5, 1]`. Cost: `[3, 3, 2]`.
Net (Gain-Cost): `[+1, +2, -1]`.

Try Start 0:
- Stop 0: Net +1. Tank = 1.
- Stop 1: Net +2. Tank = 3.
- Stop 2: Net -1. Tank = 2.
- Loop complete.
- **Skip Logic:** We must skip exactly one `gain`.
  - Skip 0 (gain 4): Net becomes `-3`. Fail.
  - Skip 1 (gain 5): Net becomes `-3`. Tank path: `1 -> -2`. Fail.
  - Skip 2 (gain 1): Net becomes `-2`. Tank path: `1 -> 3 -> 1`. Success.
- Start 0 is valid when skipping Stop 2.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `gain` array, `cost` array.
- **Output:** Starting index.
- **Skip:** For a chosen starting point, we select which stop to skip to maximize success. The tank must never drop below zero during the trip. This is a variation of the "Gas Station" problem.

## Naive Approach

### Intuition

Try every starting point `S`. For each `S`, try skipping every possible stop `K`. Simulate.

### Algorithm

1. Loop `start` from 0 to `n-1`.
2. Loop `skip` from 0 to `n-1`.
3. Simulate the route. If tank >= 0 always, return `start`.

### Limitations

- **Time Complexity:** `O(N^3)` or `O(N^2)` if optimized.
- With `N=100,000`, we need `O(N)`.

## Optimal Approach

### Key Insight

This is the **Gas Station** problem with a twist: we lose one `gain` value. The optimal strategy is to skip the stop with the minimum gain, as this minimizes the total fuel loss while still completing the loop.

Given the constraint that we must skip exactly one refueling stop, the greedy approach is to identify and skip the stop with the smallest gain. This creates the "worst-case" scenario for total fuel availability. If a valid starting point exists under this condition, it represents a solution to the problem.

### Algorithm

Given the constraint that we must skip exactly one refueling stop, the optimal strategy is to skip the stop with the minimum gain.
1. Find the index with minimum gain in the array.
2. Temporarily set that gain to 0 (simulate skipping it).
3. Run the standard Gas Station greedy algorithm.
4. If total balance is non-negative, return the starting index found.
5. Otherwise, return -1.

### Time Complexity

- **O(N)**. Finding min is `O(N)`, Gas Station is `O(N)`.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/QUE-012/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-012/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int findStart(int[] gain, int[] cost) {
        int n = gain.length;
        
        // 1. Find index of minimum gain
        int minGainIndex = -1;
        int minGain = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (gain[i] < minGain) {
                minGain = gain[i];
                minGainIndex = i;
            }
        }
        
        // 2. Temporarily remove that gain (simulate skip)
        int originalGain = gain[minGainIndex];
        gain[minGainIndex] = 0;
        
        // 3. Run standard Gas Station algorithm
        int totalTank = 0;
        int currTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            int net = gain[i] - cost[i];
            totalTank += net;
            currTank += net;
            if (currTank < 0) {
                start = i + 1;
                currTank = 0;
            }
        }
        
        // Restore gain (good practice)
        gain[minGainIndex] = originalGain;
        
        return totalTank >= 0 ? start : -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] gain = new int[n];
            int[] cost = new int[n];
            for (int i = 0; i < n; i++) {
                gain[i] = sc.nextInt();
            }
            for (int i = 0; i < n; i++) {
                cost[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            System.out.println(solution.findStart(gain, cost));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

def find_start(gain: List[int], cost: List[int]) -> int:
    n = len(gain)
    
    # 1. Find min gain index
    min_gain_idx = 0
    for i in range(1, n):
        if gain[i] < gain[min_gain_idx]:
            min_gain_idx = i
            
    # 2. Zero it out
    original_val = gain[min_gain_idx]
    gain[min_gain_idx] = 0
    
    # 3. Standard Gas Station
    total_tank = 0
    curr_tank = 0
    start = 0
    
    for i in range(n):
        net = gain[i] - cost[i]
        total_tank += net
        curr_tank += net
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
            
    # Restore
    gain[min_gain_idx] = original_val
    
    return start if total_tank >= 0 else -1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        gain = [int(next(iterator)) for _ in range(n)]
        cost = [int(next(iterator)) for _ in range(n)]
        
        result = find_start(gain, cost)
        print(result)
    except StopIteration:
        pass

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
    int findStart(vector<int>& gain, const vector<int>& cost) {
        int n = gain.size();
        
        // 1. Find min gain
        int minGainIdx = 0;
        for (int i = 1; i < n; i++) {
            if (gain[i] < gain[minGainIdx]) {
                minGainIdx = i;
            }
        }
        
        // 2. Skip it
        int original = gain[minGainIdx];
        gain[minGainIdx] = 0;
        
        // 3. Standard Greedy
        long long totalTank = 0;
        long long currTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            int net = gain[i] - cost[i];
            totalTank += net;
            currTank += net;
            if (currTank < 0) {
                start = i + 1;
                currTank = 0;
            }
        }
        
        gain[minGainIdx] = original;
        
        return totalTank >= 0 ? start : -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> gain(n), cost(n);
        for (int i = 0; i < n; i++) {
            cin >> gain[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> cost[i];
        }
    
        Solution solution;
        cout << solution.findStart(gain, cost) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findStart(gain, cost) {
    const n = gain.length;
    
    // 1. Find min gain
    let minGainIdx = 0;
    for (let i = 1; i < n; i++) {
      if (gain[i] < gain[minGainIdx]) {
        minGainIdx = i;
      }
    }
    
    // 2. Skip
    const original = gain[minGainIdx];
    gain[minGainIdx] = 0;
    
    // 3. Greedy
    let totalTank = 0;
    let currTank = 0;
    let start = 0;
    
    for (let i = 0; i < n; i++) {
      const net = gain[i] - cost[i];
      totalTank += net;
      currTank += net;
      if (currTank < 0) {
        start = i + 1;
        currTank = 0;
      }
    }
    
    gain[minGainIdx] = original;
    
    return totalTank >= 0 ? start : -1;
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
  const gain = [];
  const cost = [];
  for (let i = 0; i < n; i++) {
    gain.push(parseInt(data[idx++], 10));
  }
  for (let i = 0; i < n; i++) {
    cost.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  console.log(solution.findStart(gain, cost));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: Gain `4 5 1`, Cost `3 3 2`.
1. Min gain is `1` at index 2.
2. Modify Gain: `4 5 0`. Cost: `3 3 2`.
3. Net: `+1, +2, -2`.
4. Greedy:
   - `i=0`: Net +1. Curr 1. Total 1.
   - `i=1`: Net +2. Curr 3. Total 3.
   - `i=2`: Net -2. Curr 1. Total 1.
5. Total >= 0. Return start 0.

Matches example.

## ✅ Proof of Correctness

### Invariant
If a solution exists, it must satisfy the total fuel constraint (Total Gain - Min Gain >= Total Cost). The standard greedy algorithm finds the starting point for a valid circular route if the total balance is non-negative.

### Why the approach is correct
By removing the smallest gain, we create the "worst-case" scenario for total fuel. If the greedy algorithm finds a path in this scenario, it is a valid path.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Skip K stops?
  - *Hint:* Much harder. Requires sliding window minimum or DP.
- **Extension 2:** Maximize fuel at end?
  - *Hint:* Just sum(gain) - sum(cost).

### Common Mistakes to Avoid

1. **Skipping Max Gain**
   - ❌ Wrong: Skipping the largest gain makes it hardest to complete the loop.
   - ✅ Correct: Skip smallest gain to preserve max fuel.
2. **Not checking Total**
   - ❌ Wrong: Returning `start` even if `totalTank < 0`.
   - ✅ Correct: Must check total feasibility.

## Related Concepts

- **Gas Station (LeetCode 134):** The base problem.
- **Kadane's Algorithm:** Similar logic for max subarray.
