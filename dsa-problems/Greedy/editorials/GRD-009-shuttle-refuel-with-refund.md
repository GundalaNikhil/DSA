---
problem_id: GRD_SHUTTLE_REFUEL_WITH_REFUND__6724
display_id: GRD-009
slug: shuttle-refuel-with-refund
title: "Shuttle Refuel with Refund"
difficulty: Medium
difficulty_score: 55
topics:
  - Greedy Algorithms
  - Circular Array
  - Kadane's Algorithm
tags:
  - greedy
  - circular-array
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# GRD-009: Shuttle Refuel with Refund

## 📋 Problem Summary

You have a circular route with `n` stops. At each stop, you gain some fuel and spend some fuel to reach the next stop. You have a **single-use coupon** that refunds the cost of one segment (makes it free). Find a starting stop such that you can complete the full circle.

## 🌍 Real-World Scenario

**Scenario Title:** Road Trip with a Free Tank Voucher

You are planning a road trip around a scenic loop. You have a limited budget for gas.
- At each town, you can earn some money (busking, odd jobs) to buy gas.
- Driving between towns consumes gas.
- You have a voucher from a sponsor that pays for the gas for **one single leg** of the trip, no matter how long or expensive that leg is.

You want to know where to start your journey so that you never run out of gas, using your voucher strategically on the most difficult leg of the trip.

**Why This Problem Matters:**

- **Financial Planning:** Managing cash flow with a one-time relief option.
- **Logistics:** Optimizing routes with a single "teleport" or "free pass" option.

![Real-World Application](../images/GRD-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Fuel Tank

Stops: 0, 1, 2.
Gain: [1, 4, 2]
Cost: [3, 2, 3]
Net: [-2, +2, -1]

Without Coupon:
Total Net = -1. Impossible (need >= 0).

With Coupon (refund max cost):
Max Cost is 3 (at index 0 or 2).
If we refund index 0 (Cost 3 -> 0):
Net becomes: [+1, +2, -1]. Total = +2. Possible!

Start at 1:
Stop 1: Tank = 4. Travel to 2 (Cost 2). Tank = 2.
Stop 2: Tank = 2+2=4. Travel to 0 (Cost 3). Tank = 1.
Stop 0: Tank = 1+1=2. Travel to 1 (Cost 3). Tank = -1.
Wait! We have a coupon. Use it on leg 0->1 (Cost 3).
Tank = 2 (Cost 0). Arrive at 1 with 2. Success.

```text
Route: 1 -> 2 -> 0 -> 1
Fuel:  4 -> 2 -> 1 -> 2 (Coupon used on 0->1)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Coupon Strategy:** You should use the coupon on the edge that saves you the most fuel? Not necessarily. You use it on an edge that *allows* you to complete the cycle. But intuitively, refunding the largest cost is best for the *total* balance.
- **Circular Route:** Indices wrap around: `n-1` goes to `0`.
- **Validity:** To complete the circuit, your fuel must never drop below zero at any point.

## Naive Approach

### Intuition

Try every possible starting point `i` from `0` to `n-1`. For each start, try using the coupon on every possible edge `j`.

### Algorithm

1. Loop `start` from 0 to `n-1`.
2. Loop `coupon_edge` from 0 to `n-1`.
3. Simulate the journey. If successful, return `start`.

### Time Complexity

- **O(N^3)**: Three nested loops (start, coupon, simulation).
- **O(N^2)**: If we smartly pick the coupon (max cost edge in the path).

### Limitations

- `N=10^5` makes `O(N^2)` too slow.

## Optimal Approach

### Key Insight 1: Total Balance
If `sum(gain) - sum(cost) + max(cost) < 0`, it's impossible. Even with the best refund, we don't have enough total fuel.

### Key Insight 2: Coupon Usage
Since we want to maximize our chance of survival, does it always make sense to refund the *largest* cost edge in the entire cycle?
Yes. Refunding the max cost edge adds `max(cost)` to our total balance. If we can survive the loop with this boost, we are good.
Suppose the max cost edge is at the very end. We might die before reaching it.
However, in the "Gas Station" problem (without coupon), if `total >= 0`, there *always* exists a starting point.
Here, if we effectively set one `cost[k] = 0` (where `cost[k]` is max), the problem reduces to the standard Gas Station problem with modified costs.
Since we can choose *any* start, we can choose a start that allows us to reach the "free" edge?
So, if `sum(gain) - (sum(cost) - max(cost)) >= 0`, there exists a solution!
We just need to find the start node for this modified setup.

### Algorithm

1. **Identify Max Cost:** Find index `k` such that `cost[k]` is maximized.
2. **Modify Cost:** Temporarily set `cost[k] = 0`.
3. **Check Feasibility:** If `sum(gain) < sum(new_cost)`, return -1.
4. **Standard Greedy Scan:**
   - Initialize `tank = 0`, `start = 0`.
   - Iterate `i` from 0 to `n-1` (or `2n` to handle wrap-around, but standard algorithm works in one pass if we assume a solution exists).
   - `tank += gain[i] - new_cost[i]`.
   - If `tank < 0`:
     - We failed. The start must be after `i`.
     - Set `start = i + 1`.
     - Reset `tank = 0`.
5. **Return `start`**. (If `start >= n`, it means impossible, but the initial check covers this).

What if there are multiple edges with max cost? Any one will do.
What if the "standard" solution picks a start that requires crossing the "coupon" edge *before* we actually reach it?
The standard algorithm guarantees we can traverse the *entire* circle `0 -> 1 -> ... -> n-1 -> 0`.
Since the modified costs form a valid cycle (total `>=` 0), the standard algorithm will find a valid start for this modified cycle.
The coupon is "used" on edge `k`. This is valid regardless of where we start, because we traverse edge `k` exactly once in a full loop.

### Time Complexity

- **O(N)**: One pass to find max, one pass for standard greedy.

### Space Complexity

- **O(1)**: No extra arrays needed.

### Why This Is Optimal

The problem reduces to the classic "Gas Station" problem once we fix the coupon usage. Since we want to maximize total fuel, using the coupon on the most expensive edge is strictly optimal for the *total* constraint. The Gas Station theorem guarantees that if the total constraint is met, a valid start exists.

![Algorithm Visualization](../images/GRD-009/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int findStart(int n, int[] gain, int[] cost) {
        long totalGain = 0;
        long totalCost = 0;
        int maxCostIndex = -1;
        int maxCostVal = -1;
        
        for (int i = 0; i < n; i++) {
            totalGain += gain[i];
            totalCost += cost[i];
            if (cost[i] > maxCostVal) {
                maxCostVal = cost[i];
                maxCostIndex = i;
            }
        }
        
        // Check if possible with coupon
        if (totalGain < totalCost - maxCostVal) {
            return -1;
        }
        
        // Standard Gas Station Greedy Logic with modified cost
        // We treat cost[maxCostIndex] as 0
        
        long currentTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            long currentCost = (i == maxCostIndex) ? 0 : cost[i];
            currentTank += gain[i] - currentCost;
            
            if (currentTank < 0) {
                // Cannot reach i+1 from current start
                // Reset start to i+1
                start = i + 1;
                currentTank = 0;
            }
        }
        
        return start;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[] gain = new int[n];
        for (int i = 0; i < n; i++) gain[i] = sc.nextInt();
        
        int[] cost = new int[n];
        for (int i = 0; i < n; i++) cost[i] = sc.nextInt();
        
        Solution solution = new Solution();
        System.out.println(solution.findStart(n, gain, cost));
        sc.close();
    }
}
```

### Python

```python
import sys

def find_start(n: int, gain: list, cost: list) -> int:
    total_gain = sum(gain)
    total_cost = sum(cost)
    max_cost = max(cost)
    
    # If even with refund we can't make it, return -1
    if total_gain < total_cost - max_cost:
        return -1
        
    # Find index of max cost to skip
    # If multiple, any will do, usually first one is fine
    max_cost_idx = cost.index(max_cost)
    
    current_tank = 0
    start = 0
    
    for i in range(n):
        current_cost = 0 if i == max_cost_idx else cost[i]
        current_tank += gain[i] - current_cost
        
        if current_tank < 0:
            start = i + 1
            current_tank = 0
            
    return start

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    
    gain = []
    for _ in range(n):
        gain.append(int(next(iterator)))
        
    cost = []
    for _ in range(n):
        cost.append(int(next(iterator)))

    result = find_start(n, gain, cost)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findStart(int n, vector<int>& gain, vector<int>& cost) {
        long long totalGain = 0;
        long long totalCost = 0;
        int maxCostVal = -1;
        int maxCostIdx = -1;
        
        for (int i = 0; i < n; i++) {
            totalGain += gain[i];
            totalCost += cost[i];
            if (cost[i] > maxCostVal) {
                maxCostVal = cost[i];
                maxCostIdx = i;
            }
        }
        
        if (totalGain < totalCost - maxCostVal) {
            return -1;
        }
        
        long long currentTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            long long currentCost = (i == maxCostIdx) ? 0 : cost[i];
            currentTank += gain[i] - currentCost;
            
            if (currentTank < 0) {
                start = i + 1;
                currentTank = 0;
            }
        }
        
        return start;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> gain(n), cost(n);
    for (int i = 0; i < n; i++) cin >> gain[i];
    for (int i = 0; i < n; i++) cin >> cost[i];

    Solution solution;
    cout << solution.findStart(n, gain, cost) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findStart(n, gain, cost) {
    let totalGain = 0;
    let totalCost = 0;
    let maxCostVal = -1;
    let maxCostIdx = -1;
    
    for (let i = 0; i < n; i++) {
      totalGain += gain[i];
      totalCost += cost[i];
      if (cost[i] > maxCostVal) {
        maxCostVal = cost[i];
        maxCostIdx = i;
      }
    }
    
    if (totalGain < totalCost - maxCostVal) {
      return -1;
    }
    
    let currentTank = 0;
    let start = 0;
    
    for (let i = 0; i < n; i++) {
      const currentCost = (i === maxCostIdx) ? 0 : cost[i];
      currentTank += gain[i] - currentCost;
      
      if (currentTank < 0) {
        start = i + 1;
        currentTank = 0;
      }
    }
    
    return start;
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
  const gain = data[ptr++].split(" ").map(Number);
  const cost = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.findStart(n, gain, cost));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
1 4 2
3 2 3
```

**Analysis:**
- Gain: `[1, 4, 2]`
- Cost: `[3, 2, 3]`
- Max Cost: 3 (indices 0 and 2). Let's pick index 0.
- Modified Cost: `[0, 2, 3]` (Cost[0] becomes 0).

**Greedy Scan:**
- `i=0`: Gain 1, Cost 0. Net +1. Tank 1.
- `i=1`: Gain 4, Cost 2. Net +2. Tank 1+2=3.
- `i=2`: Gain 2, Cost 3. Net -1. Tank 3-1=2.
- Loop ends. `start = 0`.

Let's check `start=0` manually with coupon on 0:
- Stop 0: +1. Travel 0->1 (Cost 0 w/ coupon). Tank 1.
- Stop 1: +4. Travel 1->2 (Cost 2). Tank 1+4-2 = 3.
- Stop 2: +2. Travel 2->0 (Cost 3). Tank 3+2-3 = 2.
- Valid!

The example explanation uses a different approach.
"Using coupon on the segment from stop 0 to stop 1 (cost=3)... At stop 0: fuel = 1 + 1 = 2... travel to stop 1 with coupon -> fuel = 2".
"Starting from stop 1... At stop 0: fuel = 2, travel to stop 1 costs 3 -> fuel = -1 (FAIL). Using coupon on segment 0->1... Success."
So starting at 1 works.
Starting from 0 also works according to this trace.
"Starting from stop 1 (index 1)... Output: 1".
Stop 0: Gain 1. Cost 3 (Refunded -> 0).
Tank = 1.
Stop 1: Gain 4. Cost 2.
Tank = 1 + 4 - 2 = 3.
Stop 2: Gain 2. Cost 3.
Tank = 3 + 2 - 3 = 2.
Arrive back at 0 with 2.
Both 0 and 1 are valid starting points in this case.
The "max cost" isn't unique in this example:
Cost is `[3, 2, 3]`. Indices 0 and 2 are max.
If we refund index 2 (Cost 3 -> 0):
Modified Cost: `[3, 2, 0]`.
Scan:
`i=0`: Net 1-3 = -2. Fail. Start -> 1.
`i=1`: Net 4-2 = +2. Tank 2.
`i=2`: Net 2-0 = +2. Tank 4.
Result: Start 1.

So if we pick index 2 to refund, we get start 1.
If we pick index 0 to refund, we get start 0.
Both are valid solutions?
"Find a starting stop index".
Usually implies *any* valid one.
The example output `1` suggests that maybe there's a specific tie-breaking rule or I should check both?
Or maybe the "Greedy Scan" logic guarantees finding *a* valid start, but not necessarily the *first* valid start if multiple exist?
If we modify index 0, start is 0.
If we modify index 2, start is 1.
The code implements "pick first max".
If `cost[i] > max`, update.
For `[3, 2, 3]`:
i=0: max=3, idx=0.
i=1: 2 not > 3.
i=2: 3 not > 3.
So code picks index 0. Returns 0.
The example output is 1.
This suggests the example might be using a different logic or just showing *one* valid answer.
However, for the editorial, I should clarify that multiple starts might be possible.
We stick to the algorithm that finds *a* valid start.

## ✅ Proof of Correctness

### Invariant
If `total_gain >= total_cost`, a valid start exists (Gas Station Theorem).
By reducing `total_cost` by `max_cost`, we maximize the `total_gain - total_cost` delta.
If a solution exists for the original problem (with coupon), it corresponds to a valid tour in the modified problem (where one edge is free).
Since we pick the modification that yields the best total balance, we ensure that if *any* modification works, ours works (in terms of total fuel).
Does maximizing total fuel guarantee a valid start exists? Yes, by the theorem.

## 💡 Interview Extensions

- **Extension 1:** What if we can use the coupon `k` times?
  - *Answer:* Refund the `k` most expensive edges.
- **Extension 2:** What if the coupon gives a 50% discount instead of 100%?
  - *Answer:* Same logic, reduce max cost by 50%.
- **Extension 3:** What if we want the *minimum* starting index?
  - *Answer:* We might need to check all "max cost" candidates if there are ties, or run the `O(N)` check for the valid start found.

### Common Mistakes to Avoid

1. **Not Handling Impossible Case**
   - ❌ Wrong: Assuming a solution always exists.
   - ✅ Correct: Check total sums first.

2. **Coupon Logic**
   - ❌ Wrong: Trying to use the coupon on the edge where we run out of fuel.
   - ✅ Correct: Use it on the most expensive edge globally.

3. **Index Wrap-around**
   - ❌ Wrong: Simulating the circle with modulo arithmetic in the greedy scan.
   - ✅ Correct: The linear scan `0..N-1` is sufficient to find the start if we assume a solution exists. (If the scan finishes at `start`, the valid route is `start -> ... -> N-1 -> 0 -> ... -> start`).

## Related Concepts

- **Gas Station Problem:** The base version.
- **Kadane's Algorithm:** Finding max subarray sum (related to finding deficits).
- **Greedy Choice Property:** Optimal substructure.
