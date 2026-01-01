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

- With `n` up to `10^5`, `2^100000` is impossibly large. We need a more efficient approach.

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


### Python


### C++


### JavaScript


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
  - *Approach:* `dp[i][d]` = min switches ending with driver `d`. Complexity becomes `O(N * K)`.
- **Extension 2:** What if switching drivers has a cost (e.g., salary difference)?
  - *Approach:* Instead of `+1`, add `+switchCost`. The logic remains identical.
- **Extension 3:** What if drivers have multiple disjoint availability intervals?
  - *Approach:* Pre-process availability into a lookup or interval tree. The DP state might need to track *which* interval was used if it matters, but usually just "Driver ID" is enough.

### Common Mistakes to Avoid

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
