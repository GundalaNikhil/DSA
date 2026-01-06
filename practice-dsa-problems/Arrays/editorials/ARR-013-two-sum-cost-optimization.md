---
problem_id: ARR_TWO_SUM_COST__3320
display_id: ARR-013
slug: two-sum-cost-optimization
title: "Two Sum with Cost Optimization"
difficulty: Easy
difficulty_score: 25
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - optimization
  - searching
  - technical-interview-prep
  - two-pointers
  - two-sum
premium: false
subscription_tier: basic
---

# ARR-013: Two Sum with Cost Optimization

## 📋 Problem Summary

Standard Two Sum setup: Find `i, j` such that `a[i] + a[j] = T`.
Twist: Each index has an associated _cost_ `c[i]`.
Goal: Minimize the Total Cost `c[i] + c[j]`.
Tie-breaking: Minimize `i`, then `j`.

## 🌍 Real-World Scenario

**Scenario Title:** 🚚 The Cheapest Shipping Route

### The Problem

You need to transport a package across two legs of a journey to reach a total distance `T` km.

- `a[i]` is the distance of route option `i`.
- `c[i]` is the price to use route option `i`.

You must pick two distinct routes `i` and `j` whose distances add up exactly to `T`.
Among all valid pairs, you want to pay the least money.

### Real-World Relevance

- **Procurement:** Buying two components that fit together (sizes sum to T) from different vendors, minimizing total invoice price.

## 🚀 Detailed Explanation

### 1. The Challenge

Naive `O(N^2)` is too slow.
We need `O(N)`. As we iterate `j`, we want to find an `i` such that `a[i] = T - a[j]`.
But there might be _many_ such `i`'s seen so far.
Which one should we pair with?
**The one with the lowest cost!**

### 2. Map Strategy

Store in a Hash Map:
`Value -> Best Index`.
"Best" here is primarily "Lowest Cost". If costs are equal, "Smallest Index".

Algorithm:

1. Initialize `BestMap`. `GlobalBestPair = None`, `MinTotalCost = Infinity`.
2. Iterate `j` from 0 to `N`.
3. `Needed = T - a[j]`.
4. If `Needed` in `BestMap`:
   - Retrieve `i = BestMap[Needed]`.
   - Candidate pair `(i, j)` with cost `c[i] + c[j]`.
   - Compare with `GlobalBestPair`. Update if cheaper.
5. Update `BestMap` with current `a[j]`.
   - If `a[j]` not in Map, insert `j`.
   - If `a[j]` present, should we replace it?
   - Compare `c[j]` with `c[existing]`. If `c[j] < c[existing]`, update Map (we found a cheaper source for this value).
   - If `c[j] == c[existing]`, keep `existing` (because we prefer smaller index `i`, so older is better).

### 3. Tie Breaking Nuance

- Primary Goal: Min `c[i] + c[j]`.
- Secondary: Min `i`.
- Tertiary: Min `j`.

Our iteration order (j increases) naturally handles the "Min j" if we update `GlobalBest` only strictly `<`.
Does storing only the _absolute best cost_ index for a value suffice?

- Yes. If we find `a[j]`, we want the cheapest complement `a[i]`. Any other `i` with same value `a[i]` but higher cost is strictly worse for the sum.
- What if costs are same? We want smaller `i`. Our Map update logic (keep existing if costs equal) ensures we keep the smallest index.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Map: Value -> {Cost, Index}]
    B --> C[Loop j from 0 to N-1]
    C --> D[Needed = T - arr[j]]
    D --> E{Is Needed in Map?}
    E -- Yes --> F[Calculate PairCost = Map[Needed].cost + c[j]]
    F --> G[Update GlobalMin if PairCost is lower]
    E -- No --> H[Check Update Map with (arr[j], c[j])]
    G --> H
    H --> C
    C -- End Loop --> I[Return Best Pair]
```

## 🧪 Edge Cases to Test

1.  **No Solution:** Return -1.
2.  **Self Pairing:** `a=[5, 5], T=10`. Map has index 0 when processing index 1. Needs 5. Found index 0. Valid.
    - Note: Indices must be distinct (`i < j`). Map logic ensures this naturally as we look at _previous_ elements.

## 🏃 Naive vs Optimal Approach

### Naive O(N²)

Check all pairs.

### One-Pass Map O(N)

- **Time:** O(N).
- **Space:** O(N).
  Correctly keeps only the "most useful" candidate for each value.
