---
problem_id: ARR_MEDIAN_COST__2918
display_id: ARR-027
slug: dynamic-median-cost-array
title: "Dynamic Median Cost Array"
difficulty: Hard
difficulty_score: 60
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - cost-minimization
  - data-structures
  - median
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-027: Dynamic Median Cost Array

## 📋 Problem Summary

For every sliding window of size `W`, calculate `Sum(|x - Median|)` for all `x` in the window.

## 🌍 Real-World Scenario

**Scenario Title:** 📡 The Stable Signal

### The Problem

You are filtering a noisy signal.
A common filter is the "Median Filter".
But you also want to know the "Deviation" or "Noise Level" of the window relative to that median.
This "Median Absolute Deviation" (scaled) is a robust measure of variability.
You need to compute this for every moment in time.

### Real-World Relevance

- **Logistics:** Placing a warehouse at the "Median" location minimizes total distance to all delivery points (1D). Moving window = changing delivery cluster.

## 🚀 Detailed Explanation

### 1. Mathematical Insight

For any set of numbers, the value `M` that minimizes `Sum(|x - M|)` IS the Median.
If we sorted the window: `x_1, x_2 ... x_k`.
Median is `x_(k/2)`.
Cost = `Sum(|x_i - Median|)`.
This splits into:
`Sum(Median - x_i)` for `x_i < Median`
`+ Sum(x_i - Median)` for `x_i > Median`.
= `(CountLeft * Median - SumLeft) + (SumRight - CountRight * Median)`.
Where `SumLeft` is sum of elements smaller than Median, etc.

### 2. Data Structure Needed

We need a structure that supports:

1. `Add(val)`
2. `Remove(val)`
3. `FindKth(k)` (To get Median value).
4. `Sum of elements < val` (To get SumLeft).
   - Actually, simpler: `Sum of first k elements` in sorted order.

A **Fenwick Tree (BIT)** or **Segment Tree** can do this efficiently.
Since values are large (`-10^9` to `10^9`), we need **Coordinate Compression** (or a dynamic segment tree).

### 3. Algorithm

1. Coordinate Compress all values in array (map to ranks 1..N).
2. Use two Fenwick Trees:
   - `CountBIT`: Stores frequency of each rank.
   - `SumBIT`: Stores sum of actual values for each rank.
3. Sliding Window:
   - Add `arr[i]`: Update BITs.
   - Remove `arr[i-W]`: Update BITs.
   - Query:
     - Find Rank of Median (k = (W+1)/2).
     - Use Binary Search on `CountBIT` prefix sums to find the index `idx` such that `Count(idx) >= k`.
     - `MedianVal` = uncompressed value of `idx`.
     - `CountSmaller` = query `CountBIT` below `idx`. `SumSmaller` = query `SumBIT` below `idx`.
     - `CountLarger`, `SumLarger` derived from Total Count/Sum.
     - Calculate Cost.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Coordinate Compress Values]
    B --> C[Init CountBIT, SumBIT]
    C --> D[Loop i from 0 to N-1]
    D --> E[Add arr[i] to BITs]
    E --> F{i >= W?}
    F -- Yes --> G[Remove arr[i-W] from BITs]
    F -- No --> H[Continue]
    G --> H
    H --> I{Window Full?}
    I -- Yes --> J[Find Median Rank]
    J --> K[Query BITs for SumLeft, SumRight]
    K --> L[Formula: Cost = (LeftCnt*Med - LeftSum) + (RightSum - RightCnt*Med)]
    L --> M[Save Result]
    M --> D
    D -- End Loop --> N[Return Results]
```

## 🧪 Edge Cases to Test

1.  **W=1:** Median is element itself. Cost 0.
2.  **Even W:** Problem says "lower middle". Formula handles this naturally if we pick the correct k-th element.
3.  **Duplicates:** Coordinate compression and BIT counts handle duplicates correctly.

## 🏃 Naive vs Optimal Approach

### Naive O(N \* W log W)

Sort window every time. Too slow.

### BIT / Segment Tree O(N log N)

- **Time:** O(N log N).
- **Space:** O(N).
  Optimal.
