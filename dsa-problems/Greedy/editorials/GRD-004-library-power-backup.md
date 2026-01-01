---
problem_id: GRD_LIBRARY_POWER_BACKUP__4928
display_id: GRD-004
slug: library-power-backup
title: "Library Power Backup"
difficulty: Medium
difficulty_score: 40
topics:
  - Greedy Algorithms
  - Sorting
  - Optimization
tags:
  - greedy
  - sorting
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# GRD-004: Library Power Backup

## 📋 Problem Summary

You need to power a server for `T` hours using a set of `n` batteries, each with a specific capacity. You can only use one battery at a time. When one runs out, you must switch to another. Your goal is to minimize the number of switches required to keep the server running for the full duration.

## 🌍 Real-World Scenario

**Scenario Title:** Emergency Generator Management

During a blackout, a hospital needs to keep its life-support systems running for 24 hours. They have a collection of fuel canisters of various sizes (5 gallons, 2 gallons, 10 gallons, etc.).

Switching canisters requires a brief manual intervention or "swap." To minimize the workload on the staff and reduce the risk of power interruption during a swap, the hospital manager wants to use the fewest number of canisters possible to cover the 24-hour period.

**Why This Problem Matters:**

- **Reliability:** Fewer components/steps usually mean higher reliability.
- **Efficiency:** Minimizing active interventions saves labor and time.
- **Resource Management:** Using the most potent resources first is a common heuristic in logistics.

![Real-World Application](../images/GRD-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Stacking Capacities

Target `T = 10`

Batteries: `[2, 5, 3, 1]`

**Option A (Random):**
Use 2, then 1, then 3... Sum = 6. Still need 4. Use 5.
Total used: 4 batteries. Swaps: 3.

**Option B (Greedy - Largest First):**
1. Use 5. Remaining needed: 5.
2. Use 3. Remaining needed: 2.
3. Use 2. Remaining needed: 0.
Total used: 3 batteries. Swaps: 2.

```text
Target Height: |==========| (10)

Greedy Stack:
[ 5 ] + [ 3 ] + [ 2 ] = 10 (Matches target)
  ^       ^       ^
  1       2       3  (Batteries used)
  
Swaps = (Batteries Used) - 1 = 2
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Swaps vs. Count:** The problem asks for *swaps*. If you use 1 battery, that's 0 swaps. If you use `k` batteries, that's `k-1` swaps.
- **Impossible Case:** If the sum of all battery capacities is less than `T`, return -1.
- **Exact vs. Excess:** It's okay to have more capacity than `T`. You just stop when you reach or exceed `T`.

## Naive Approach

### Intuition

Try every combination of batteries to see which ones sum up to at least `T`. Among those valid combinations, find the one with the fewest elements.

### Algorithm

1. Generate all subsets of batteries.
2. Filter for subsets where `sum(subset) >= T`.
3. Find the subset with minimum size `k`.
4. Return `k-1`.

### Time Complexity

- **O(2^n)**: Checking all subsets.

### Space Complexity

- **O(n)**: Recursion stack.

### Limitations

- With `n=10^5`, `2^100000` is way too large.

## Optimal Approach

### Key Insight

To minimize the number of batteries used, we should get as much "value" (capacity) as possible from each individual pick. This implies we should always choose the largest available battery.

This is a classic **Greedy Strategy**:
- Sort the batteries in descending order.
- Pick them one by one until the total capacity `>= T`.

### Algorithm

1. **Sum Check:** Calculate total capacity of all batteries. If `total < T`, return -1.
2. **Sort:** Sort the `capacities` array in descending order.
3. **Iterate:**
   - Initialize `currentSum = 0`, `count = 0`.
   - Loop through sorted batteries:
     - Add capacity to `currentSum`.
     - Increment `count`.
     - If `currentSum >= T`, break.
4. **Result:** Return `count - 1`.

### Time Complexity

- **O(N log N)**: Due to sorting. The iteration is O(N).

### Space Complexity

- **O(1)**: Or O(N) for sorting depending on language/implementation.

### Why This Is Optimal

Suppose an optimal solution uses a set of `k` batteries `S_opt = b_1, b_2, ..., b_k` where `b_1 >= b_2 >= ... >= b_k`.
Suppose our greedy solution picks the `k` largest batteries `S_greedy = g_1, g_2, ..., g_k`.
By definition, `g_i` is the `i`-th largest battery available, so `g_i >= b_i` for all `i`.
Therefore, `sum S_greedy >= sum S_opt`.
If `S_opt` is sufficient to cover `T`, then `S_greedy` is also sufficient (and potentially overkill).
Thus, we never need *more* batteries than the optimal solution.

![Algorithm Visualization](../images/GRD-004/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 7
3 5 2
```

**Execution:**
1. **Total Check:** `3+5+2 = 10 >= 7`. Possible.
2. **Sort:** `[5, 3, 2]`
3. **Iteration:**
   - Pick 5. `currentSum = 5`. `count = 1`. `5 < 7`, continue.
   - Pick 3. `currentSum = 8`. `count = 2`. `8 >= 7`, break.
4. **Result:** `count - 1` = `2 - 1` = `1`.

**Output:** `1`

![Example Visualization](../images/GRD-004/example-1.png)

## ✅ Proof of Correctness

### Invariant
At any step `k`, the greedy strategy has selected the set of `k` batteries with the maximum possible total capacity.

### Why the approach is correct
Since we want to reach threshold `T` with minimum `k`, we want to maximize the sum for any fixed `k`.
The sum of the largest `k` elements is always `>=` the sum of any other `k` elements.
Thus, if there exists a solution with `k` batteries, the greedy solution will also find a solution with `k` (or fewer) batteries.

## 💡 Interview Extensions

- **Extension 1:** What if we need to minimize the *total capacity used* instead of the count?
  - *Answer:* Then sort ascending (smallest first) until sum >= T.
- **Extension 2:** What if we can't switch batteries instantly (switching takes time)?
  - *Answer:* The problem changes; we might need to account for downtime or overlap.
- **Extension 3:** What if batteries have weights and we want to minimize total weight for capacity `T`?
  - *Answer:* This is the **Knapsack Problem** (specifically Unbounded or 0/1 depending on supply). Greedy fails; use DP.

### Common Mistakes to Avoid

1. **Sorting Ascending**
   - ❌ Wrong: Using smallest batteries first maximizes the count (worst case).
   - ✅ Correct: Sort descending.

2. **Off-by-one Error**
   - ❌ Wrong: Returning `count`.
   - ✅ Correct: Problem asks for *swaps*, which is `count - 1`.

3. **Integer Overflow**
   - ❌ Wrong: Using 32-bit int for `currentSum` if `T` or total capacity is large.
   - ✅ Correct: Use `long` (Java/C++) or Python (auto-bigint).

## Related Concepts

- **Greedy Algorithms:** Making the locally optimal choice.
- **Knapsack Problem:** Related optimization problem (though this is a simpler variant).
- **Sorting:** Essential preprocessing step.
