---
problem_id: ARR_K_MAX_SUBS__5881
display_id: ARR-029
slug: k-nonoverlapping-max-subarrays
title: "K Non-Overlapping Max Subarrays"
difficulty: Hard
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - dp-optimization
  - kadane-extension
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-029: K Non-Overlapping Max Subarrays

## 📋 Problem Summary

Choose exactly `K` disjoint contiguous subarrays to maximize total sum.

## 🌍 Real-World Scenario

**Scenario Title:** ⛏️ The Gold Veins

### The Problem

A geological scan (`arr`) shows traces of gold concentration.
You have `K` separate mining teams.
Each team can excavate one contiguous tunnel.
Teams cannot cross paths (overlap).
Where should the teams dig to get the most gold?

### Real-World Relevance

- **Advertising:** Placing `K` ads in a video stream where 'viewer attention' varies.

## 🚀 Detailed Explanation

### 1. DP State

`DP[k][i]` = Max sum using exactly `k` subarrays considering elements up to index `i`.
Transitions:
At index `i`, we can:

1. **Exclude `arr[i]`:** Score `DP[k][i-1]`. (Subarray ended earlier)
2. **Include `arr[i]` in the k-th subarray:**
   - This subarray ends at `i`.
   - It could be a single element `arr[i]` + `Max score using k-1 subarrays before it`.
   - Or it extends a subarray ending at `i-1`.
     Wait. The standard "Max Subarray" logic requires tracking whether we are currently extending or not.

Better States:

- `Global[k][i]`: Max sum using `k` subarrays in range `0..i` (ith element may or may not be used).
- `Local[k][i]`: Max sum using `k` subarrays MUST ending at `i`.

Recurrence:

- `Local[k][i] = max(Global[k-1][i-1], Local[k][i-1]) + arr[i]`.
  - Explanation:
    - Extend current k-th subarray: `Local[k][i-1] + arr[i]`.
    - Start new k-th subarray here: `Global[k-1][i-1] + arr[i]`.
- `Global[k][i] = max(Global[k][i-1], Local[k][i])`.

### 2. Space Optimization

We only need the previous column `[i-1]` to compute `[i]`.
Actually, we can optimize to `O(K)` space.
Outer loop `i` from 1 to N.
Inner loop `k` from K down to 1.
Update `Local[k]` and `Global[k]` in place.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Init Local[K], Global[K] arrays to -Inf]
    B --> C[Loop i from 0 to N-1]
    C --> D[Loop k from K down to 1]
    D --> E[Local[k] = max(Global[k-1], Local[k]) + arr[i]]
    E --> F[Global[k] = max(Global[k], Local[k])]
    F --> D
    D -- End Inner --> C
    C -- End Outer --> G[Return Global[K]]
```

## 🧪 Edge Cases to Test

1.  **K subarrays not possible:** N < K. Loop bounds handle this (or check before start).
2.  **All Negative:** Unlike standard Kadane (0 allowed), we MUST pick K subarrays.
    - DP initialization should be `-Infinity`.
    - `Local` logic will pick single negative elements if forced.
3.  **K=1:** Classic Kadane.

## 🏃 Naive vs Optimal Approach

### Naive

Recursive standard. Exponential.

### DP O(NK)

- **Time:** O(N \* K). Given N=200,000, maybe K is small?

  - Problem Constraints: `K <= N`. O(N^2) is bad.
  - Wait. If K is large (e.g. N/2), O(NK) is TLE.
  - Is there a faster way?
  - **WQS Binary Search (Alien's Trick)** allows solving this in `O(N log C)`.
  - Is this expected for "Hard" difficulty?
  - If N is large and K is large, yes.
  - If K is small constant, DP is fine.
  - For editorial purposes, O(NK) is the standard structure. However, "Alien's Trick" is the true optimal for large K.
  - Given "Hard" and modern constraints, I should mention Aliasing/WQS optimization or note that DP works for small K.
  - Let's stick to O(NK) explanation as primary, referencing Alien's Trick for advanced users.

  _Correction_: If K is large (e.g. K=100,000), O(NK) definitely TLE.
  WQS Binary Search:

  - Penalize each subarray by cost `lambda`.
  - Find max sum with unconstrained number of subarrays.
  - Check count. Adjust `lambda`.
  - This is `O(N * log(Range))`. This is required for `K ~ N`.

  I will describe the DP approach as the fundamental one, but add an "Advanced Note" about Alien's Trick.
