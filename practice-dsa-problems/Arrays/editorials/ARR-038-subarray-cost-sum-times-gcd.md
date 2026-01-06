---
problem_id: ARR_COST_SUM_GCD__1992
display_id: ARR-038
slug: subarray-cost-sum-times-gcd
title: "Subarray Cost = sum x gcd"
difficulty: Hard
difficulty_score: 55
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - gcd
  - searching
  - segment-tree
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-038: Subarray Cost = sum x gcd

## 📋 Problem Summary

Maximize `Sum(Subarray) * GCD(Subarray)` over all contiguous subarrays.

## 🌍 Real-World Scenario

**Scenario Title:** 📦 The Batch Deal

### The Problem

You are selling a batch of items (contiguous sequence).

- The total value is the Sum of their prices.
- But the batch must be uniform. The "Uniformity Factor" is the GCD of the prices.
- The final payout is `Value * Uniformity`.
- You want to pick a batch to maximize payout.
  Example: `[6, 6, 6]`. Sum 18. GCD 6. Payout 108.
  `[6, 12, 6]`. Sum 24. GCD 6. Payout 144.

## 🚀 Detailed Explanation

### 1. Properties of GCD

As you extend a subarray, the **GCD can only decrease** (or stay same).
Crucially, it changes values at most `log(MaxElement)` times.
Why? Because every time it decreases, it loses at least one prime factor, effectively reducing to `<= GCD/2`.
So for a fixed starting index `L`, there are only `O(log V)` distinct GCD values as `R` goes from `L` to `N-1`.

### 2. Strategy: Iterate GCDs

We cannot iterate all subarrays `O(N^2)`.
But we can iterate **all possible GCD values** that appear as ranges? No, too many ranges.
We iterate over the distinct "GCD Ranges" for each `L`?
Actually, it's better to fix the **Left endpoint L** and find the few `R` points where GCD changes.

1. Start at `L`. `current_gcd = arr[L]`.
2. Find the largest `R` such that `GCD(L..R) == current_gcd`.
   - All subarrays `L..k` where `L <= k <= R` have the same GCD.
   - To maximize `Sum * GCD`, we just need to maximize `Sum`. Since numbers are positive, Max Sum is at the largest index `R`.
   - Calculate candidate cost: `Sum(L..R) * current_gcd`.
3. Update `L = R + 1`? No.
4. Move `L` to next `R+1`. Update `current_gcd = GCD(current_gcd, arr[R+1])`. Repeat.

Wait. Iterating `L` from `0` to `N-1` is `N`.
For each `L`, we jump `log V` times.
Finding "Largest R" requires Binary Search + Sparse Table (RMQ for GCD).
Total Complexity: `N * log V * log N`.
Constraints: `N=200,000`. `log V ~ 30`. `log N ~ 18`.
`2e5 * 30 * 18` approx `10^8`. A bit tight but OK for 2s.

### 3. Algorithm with Sparse Table

1. Build Sparse Table for GCD queries `O(N log N)`.
2. Prefix Sum array for O(1) sums.
3. Loop `i` from `0` to `N-1`:
   - `curr_gcd = arr[i]`. `j = i`.
   - Loop internal:
     - Binary Search `end` in `[j, N-1]` such that `query(i, end) == curr_gcd`.
     - Let this maximal index be `k`.
     - Update `Ans = max(Ans, (Prefix[k]-Prefix[i-1]) * curr_gcd)`.
     - `j = k + 1`.
     - If `j < N`: `curr_gcd = gcd(curr_gcd, arr[j])`. Else break.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Build Sparse Table for GCD]
    B --> C[Compute Prefix Sums]
    C --> D[Loop i from 0 to N-1]
    D --> E[curr_gcd = arr[i], j = i]
    E --> F[Binary Search max k >= j s.t. GCD(i..k) == curr_gcd]
    F --> G[Cost = Sum(i..k) * curr_gcd]
    G --> H[Ans = max(Ans, Cost)]
    H --> I[j = k + 1]
    I --> J{j < N?}
    J -- Yes --> K[curr_gcd = gcd(curr_gcd, arr[j])]
    K --> F
    J -- No --> D
    D -- End Loop --> L[Return Ans]
```

## 🧪 Edge Cases to Test

1.  **Single Element:** `Sum * Val`.
2.  **Primes:** GCD becomes 1 quickly.
3.  **All Same:** GCD constant. `N` iterations of BS? No, 1 iteration covering whole array. Fast.

## 🏃 Naive vs Optimal Approach

### Naive O(N^2)

Try all subarrays.

### Sparse Table + Log Jumps O(N log N log V)

- **Time:** Dominated by sparse table build and BS loops.
- **Space:** O(N log N).
  Optimal approach for this constraint class.
