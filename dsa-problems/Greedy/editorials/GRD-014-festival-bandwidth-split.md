---
problem_id: GRD_FESTIVAL_BANDWIDTH_SPLIT__9163
display_id: GRD-014
slug: festival-bandwidth-split
title: "Festival Bandwidth Split"
difficulty: Medium
difficulty_score: 45
topics:
  - Greedy Algorithms
  - Knapsack
  - Optimization
tags:
  - greedy
  - knapsack
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# GRD-014: Festival Bandwidth Split

## 📋 Problem Summary

You have `n` stages, each requiring a minimum bandwidth `b[i]`. You have a total bandwidth budget `B`. You want to maximize the **count** of stages that can run. As a secondary goal, minimize wasted bandwidth.

## 🌍 Real-World Scenario

**Scenario Title:** Packing a Lunchbox

Imagine you have a small lunchbox (Capacity `B`) and many different snacks (Items).
- Each snack has a size `b[i]`.
- You want to fit as many *different* snacks as possible into the box to have variety.
- You don't care about the total calories (sum of sizes), just the *number* of items.
- If you have space left over, you'd prefer to fill it tightly, but your main goal is "More Items".

To fit the most items, you should obviously pack the smallest ones first! Putting a giant watermelon in the box takes up space that could hold 10 grapes.

**Why This Problem Matters:**

- **Resource Allocation:** Maximizing the number of customers served (throughput) when resources are limited.
- **Budgeting:** Buying as many items as possible with a fixed amount of money.

![Real-World Application](../images/GRD-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Greedy Choice

Items: [5, 2, 4]. Budget: 7.

Sorted: [2, 4, 5].

```text
Step 1: Pick smallest (2).
   Remaining Budget: 7 - 2 = 5.
   Count: 1.

Step 2: Pick next smallest (4).
   Remaining Budget: 5 - 4 = 1.
   Count: 2.

Step 3: Pick next smallest (5).
   Remaining Budget: 1 - 5 = -4 (Impossible).
   Stop.

Result: 2 items.
```

If we picked 5 first:
   Remaining: 2.
   Pick 2: Remaining 0. Count 2.
   Pick 4: Impossible.
   Result: 2 items.

Both give 2 items. But picking smallest first guarantees we never "block" a future small item with a large one unnecessarily.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Maximize Count:** This is the primary objective.
- **Does Greedy Minimize Waste?**
  - The problem asks to minimize waste among solutions with maximum stages.
  - For maximizing count, the greedy strategy of picking smallest items first is optimal.
  - For the secondary goal (minimizing waste), the simple greedy may not always find the optimal solution within the same count tier, as this becomes a subset sum problem.
  - The output format requests only the count of stages, not the waste or specific set.
  - Both strategies yielding the same count satisfy the primary objective.
  - Given constraints (N up to 10^5), solving subset sum is computationally infeasible.
  - The simple greedy approach (smallest first) is the standard and correct solution for maximizing count.

## Naive Approach

### Intuition

Try all subsets.

### Algorithm

1. Generate `2^N` subsets.
2. Filter those with Sum `<= B`.
3. Pick max size.

### Time Complexity

- **O(2^N)**: Impossible.

## Optimal Approach

### Key Insight

To maximize the *number* of items with a fixed budget, we should always buy the cheapest items.
Proof: Suppose an optimal solution `S` does not include the smallest item `x`, but includes a larger item `y`. We can swap `y` for `x`. The count remains the same, but the total sum decreases (or stays same), so the budget constraint is still satisfied. We can repeat this until `S` consists of the `k` smallest items.

### Algorithm

1. Sort `bandwidths` in ascending order.
2. Iterate and sum up values.
3. Stop when `current_sum + next_val > B`.
4. Return the count.

### Time Complexity

- **O(N log N)**: Sorting.

### Space Complexity

- **O(1)**: (ignoring sort space).

![Algorithm Visualization](../images/GRD-014/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 7
5 2 4
```

**Step 1:** Sort `[2, 4, 5]`.
**Step 2:**
- Pick 2. Sum 2. Count 1.
- Pick 4. Sum 6. Count 2.
- Pick 5. Sum 6+5=11 > 7. Break.

**Result:** 2.

![Example Visualization](../images/GRD-014/example-1.png)

## ✅ Proof of Correctness

### Invariant
The set of `k` smallest elements has the minimum possible sum of any subset of size `k`.
Therefore, if any subset of size `k` fits in budget `B`, the subset of the `k` smallest elements also fits.
This implies that we can simply check sizes `k=1, 2, ...` using the smallest elements until we fail.

## 💡 Interview Extensions

- **Extension 1:** What if we want to maximize the *total bandwidth used* (Knapsack)?
  - *Answer:* This is 0/1 Knapsack (NP-Hard). Solvable with DP if `B` is small.
- **Extension 2:** What if we can use fractions of a stage?
  - *Answer:* Fractional Knapsack (Greedy by value/weight ratio). Here value=1, weight=b. Ratio = `1/b`. Best ratio = smallest `b`. Same logic.

### Common Mistakes to Avoid

1. **Sorting Strings**
   - ❌ Wrong: In JS, `sort()` sorts alphabetically ("10" < "2").
   - ✅ Correct: `sort((a,b) => a-b)`.

2. **Integer Overflow**
   - ❌ Wrong: Using `int` for sum if `B` is large (`10^12`).
   - ✅ Correct: Use `long` / `long long`.

## Related Concepts

- **Knapsack Problem:** The general family.
- **Sorting:** The key operation.
