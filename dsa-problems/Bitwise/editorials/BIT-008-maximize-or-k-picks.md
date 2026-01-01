---
problem_id: BIT_MAXIMIZE_OR_K_PICKS__8408
display_id: BIT-008
slug: maximize-or-k-picks
title: "Maximize OR With K Picks"
difficulty: Medium
difficulty_score: 48
topics:
  - Bitwise Operations
  - OR
  - Greedy
  - Array
tags:
  - bitwise
  - or-operation
  - greedy
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# BIT-008: Maximize OR With K Picks

## 📋 Problem Summary

Select exactly `k` integers from an array such that their bitwise OR sum is maximized.

## 🌍 Real-World Scenario

**Scenario Title:** The Feature Bundle Optimization

You are assembling a software bundle.
- **Modules**: You have a library of `n` modules. Each module enables a specific set of features (represented by bits).
- **License**: Your license allows you to include exactly `k` modules in the standard edition.
- **Goal**: You want to offer the most feature-rich standard edition possible ( maximize the total set of unique features enabled).
- **Logic**: Since features don't conflict (OR logic), you just want to pick the `k` modules that cover the most high-value feature bits.

**Why This Problem Matters:**

- **Set Cover**: A simplified variation where "elements" (bits) have strictly hierarchical weights ($2^i$).
- **Greedy Validity**: Understanding when greedy choices are globally optimal.
- **Dimensionality**: Leveraging the small count of bits (30-60) vs large N.

![Real-World Application](../images/BIT-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Greedy Choice
```
Array: [100, 010, 001] (Binary)
K = 2

Pass 1:
- Current: 000
- Try 100 -> 100 (Gain 4)
- Try 010 -> 010 (Gain 2)
- Try 001 -> 001 (Gain 1)
- Pick 100. New Mask: 100.

Pass 2:
- Current: 100
- Try 010 -> 110 (Gain 2)
- Try 001 -> 101 (Gain 1)
- Pick 010. New Mask: 110.

Result: 110 (6).
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Integer array `a` and `k`.
- **Duplicates**: You can pick duplicates if useful (but `x | x = x`, so usually useless). Distinct indices matter.
- **Constraints**: `a[i]` up to `10^9` (30 bits).

Common interpretation mistake:

- ❌ Trying Dynamic Programming. The state space (index, currentOR) is too large.
- ✅ Using Greedy. Since bit `i` is worth more than the sum of all bits `0` to `i-1`, we always prioritize setting higher bits.

### Core Concept: Hierarchical Greedy

The value of the MSB ($2^{29}$) is greater than the sum of all lower bits ($2^{29}-1$). This simple arithmetic property means we never sacrifice a higher bit to gain lower bits.
Therefore, the strategy "Pick the number that adds the most value to the current OR" is optimal.

### Why K Threshold Matters

Since there are only ~30 bits, we can saturate the max possible OR of the array with at most 30 picks (one per bit). If `k >= 30`, we can just pick the minimal set to get `TotalOR` and fill the rest with garbage. Effectively, if `k >= 30`, answer is `OR(All)`.

## Naive Approach (Backtracking)

### Intuition

Try all combinations of size `k`.

### Algorithm

1. Recursively select element.
2. Maximize result.

### Time Complexity

- **O(C(N, K))**. Exponential.

### Space Complexity

- **O(K)** recursion.

## Optimal Approach (Greedy Scan)

### Key Insight

In each step, pick the element `x` that maximizes `CurrentOR | x`.
Repeat `k` times.

### Algorithm

1. `current_or = 0`.
2. `used = boolean array`.
3. Loop `step` from 0 to `k-1`:
   - `best_val = -1`, `best_idx = -1`.
   - Loop `i` from 0 to `n-1`:
     - If `!used[i]`:
       - `new_or = current_or | a[i]`.
       - If `new_or > best_val`: `best_val = new_or`, `best_idx = i`.
   - If `best_idx` valid:
     - `current_or = best_val`.
     - `used[best_idx] = true`.
   - Else: Break (no more numbers? Not possible if k <= n).
4. Return `current_or`.

Optimization: If `k > 30`, just return `OR` of the whole array array (linear scan), because 30 picks is enough to set all 30 bits.

### Time Complexity

- **O(min(K, 30) * N)**. Since we cap K at 30, it is **O(N)**.

### Space Complexity

- **O(N)** for used flags.

![Algorithm Visualization](../images/BIT-008/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-008/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `a=[1, 2, 4], k=2`.
1. **Pass 1**:
   - `0 | 1 = 1`
   - `0 | 2 = 2`
   - `0 | 4 = 4` -> Max. Pick 4. `current = 4`.
2. **Pass 2**:
   - `4 | 1 = 5`
   - `4 | 2 = 6` -> Max. Pick 2. `current = 6`.
Result: 6.

## ✅ Proof of Correctness

### Invariant

The greedy strategy works because the bitwise OR function with the canonical bit weights ($2^i$) satisfies the matroid property where the lexicographically largest (value-wise largest) element/set is an optimal basis. Specifically, priority to MSB is never wrong.

## 💡 Interview Extensions (High-Value Add-ons)

- **Subset Sum**: Much harder (NP-complete).
- **XOR Sum**: Requires Linear Basis (Gaussian Elimination).

## Common Mistakes to Avoid

1. **Greedy Trap**:
   - ❌ This greedy works for OR. It does NOT work for Sum or XOR generally (though XOR basis is greedy-like).
2. **Sort**:
   - ❌ Sorting array descending helps heuristic but doesn't change complexity O(NK).

## Related Concepts

- **Set Cover Problem**: General case.
- **Maximum AND**: Usually involves iterating bits from MSB.
