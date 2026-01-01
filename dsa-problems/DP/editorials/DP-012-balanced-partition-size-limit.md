---
problem_id: DP_BAL_PART_SIZE__5120
display_id: DP-012
slug: balanced-partition-size-limit
title: "Balanced Partition With Size Limit"
difficulty: Medium
difficulty_score: 56
topics:
  - Dynamic Programming
  - Subset Sum
  - Optimization
tags:
  - dp
  - subset-sum
  - partition
  - medium
premium: true
subscription_tier: basic
---

# DP-012: Balanced Partition With Size Limit

## 📋 Problem Summary

Partition an array into two groups so that:

- the absolute difference of group sums is at most `D`
- among all such partitions, the **larger group size** is minimized

Return the minimum possible size of the larger group, or `-1` if no valid partition exists.

## 🌍 Real-World Scenario

**Scenario Title:** Fair Lab Team Split With Budget Deviation Limit

In a lab, students have “workload scores” (positive or negative depending on prior credits). You must split the class into two teams:

- total workload difference between teams must be within `D`
- keep team sizes as balanced as possible (minimize larger team)

This models constrained fair-split problems in scheduling, load balancing, and hiring panels.

**Why This Problem Matters:**

- Combines subset-sum feasibility with a size optimization
- Requires careful DP design when values can be negative
- Shows how to derive the optimal size from reachable sums

![Real-World Application](../images/DP-012/real-world-scenario.png)

## ✅ Clarifications

- Both groups are allowed to be empty in principle; the DP will tell if that’s optimal or feasible.
- Values may be negative, so sums can be negative; we must offset indices.
- We do **not** minimize the difference (it’s constrained), we minimize `max(sizeA, sizeB)`.

## Detailed Explanation

### Reformulate the goal

Let:

- `n` = number of elements
- `total = sum(a)`
- pick a subset `S` of size `k` with sum `s`

The other group has:

- size `n-k`
- sum `total - s`

Constraint:

`| (total - s) - s | = | total - 2s | <= D`

Objective:

Minimize `max(k, n-k)` among all `(k, s)` that satisfy the constraint.

### DP over subset size and sum

Because `n <= 50` and `|a[i]| <= 500`, the total absolute sum is at most `50 * 500 = 25000`.

We can do a classic 0/1 subset DP with size:

`dp[k] = set of reachable sums using exactly k elements`

Initialize:

- `dp[0] = {0}`
- `dp[k>0] = ∅`

For each value `x`:

- iterate `k` from `n-1` down to `0`:
  - for each sum `s` in `dp[k]`, add `s+x` to `dp[k+1]`

After processing all elements, check all `(k, s)`:

- if `| total - 2s | <= D`, candidate answer = `max(k, n-k)`
- take the minimum candidate

If no candidate exists, answer = `-1`.

### Why this works

The DP enumerates all possible subset sizes and sums. The constraint only depends on `s` and `k` (through `total` and `n-k`). So scanning all reachable `(k,s)` pairs finds the optimal size.

### Complexity

- States: `O(n * number_of_sums)`; we store sets of sums per k
- Each step inserts new sums: worst-case sums count is `O(n * value_range)` which is fine for `n=50, range=25000`
- Time: roughly `O(n^2 * value_range)` but prunes well in practice at these limits
- Space: `O(n * value_range)` for reachable sums

![Algorithm Visualization](../images/DP-012/algorithm-visualization.png)
![Algorithm Steps](../images/DP-012/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
Example: `a = [3,1,4,2], D = 1`

- `total = 10`
- Pick subset `{3,2}` (k=2, sum=5): other group sum=5, diff=0 ≤ 1, larger size = 2.
- No partition can make the larger size 1 (you’d need groups of sizes 1 and 3; diff would be ≥ 3).
- So answer = 2.

![Example Visualization](../images/DP-012/example-1.png)

## ✅ Proof of Correctness

The DP enumerates all possible pairs `(k, s)`:

- `k` = number of elements chosen for group A
- `s` = sum of those elements

For each pair, group B has size `n - k` and sum `total - s`. The partition constraint holds iff `|total - 2s| <= D`. For all such feasible pairs, we compute `max(k, n-k)`. The minimum of this value is exactly the optimal larger-group size.

Since the DP includes every subset size and sum combination, it captures all possible partitions; thus the minimum found is optimal. If no feasible pair exists, answer is `-1`.

### Common Mistakes to Avoid

1. **Minimizing the sum difference instead of respecting the constraint**
2. **Forgetting negative values** (need sets/offsets; using only positive indices will break)
3. **Not using descending k in the subset loop** (would reuse an element multiple times)
4. **Stopping early after finding one feasible partition** (need the min larger size)



## Related Concepts

- Subset DP over size and sum
- Partition problems with additional objectives
- Handling negative numbers in subset sums
