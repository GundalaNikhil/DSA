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


### Python


### C++


### JavaScript


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

