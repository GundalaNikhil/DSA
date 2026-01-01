---
problem_id: PDS_KMV_DISTINCT_COUNT__9186
display_id: PDS-009
slug: kmv-distinct-count
title: "k-Minimum Values (KMV) Distinct Count"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - KMV
  - Distinct Count
tags:
  - probabilistic-ds
  - kmv
  - distinct-count
  - medium
premium: true
subscription_tier: basic
---

# PDS-009: k-Minimum Values (KMV) Distinct Count

## 📋 Problem Summary

We are given the `k` smallest hash values from a set of items, where hash values are uniformly distributed in `(0, 1)`. We need to estimate the total number of distinct elements in the original set using the KMV estimator: `Estimate = frack-1h_k`, where `h_k` is the `k`-th smallest hash value.

## 🌍 Real-World Scenario

**Scenario Title:** Distributed Database Query Optimization

Imagine a distributed database like Cassandra or DynamoDB.
- Data is sharded across hundreds of nodes.
- You want to run `SELECT COUNT(DISTINCT user_id) FROM users`.
- Querying every shard and merging full sets of user IDs is extremely slow and network-heavy.
- **KMV Solution:** Each shard maintains just the `k` smallest hash values of the user IDs it sees.
- The coordinator node collects these small lists, merges them to find the global `k` smallest hashes, and applies the KMV formula.
- This allows estimating the global distinct count with minimal data transfer.

**Why This Problem Matters:**

- **Set Operations:** KMV sketches allow estimating intersection and union sizes (Jaccard similarity).
- **Data Warehousing:** Pre-computing statistics for query planning.

![Real-World Application](../images/PDS-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Hash Space

Hash values are points on the line `(0, 1)`.
If we have `N` distinct items, their hashes will be roughly evenly spaced with gap `1/N`.
The `k`-th smallest hash `h_k` should be roughly at position `k/N`.

```
0.0   h1    h2        h3 (k=3)                                  1.0
|-----|-----|---------|------------------------------------------|
      ^     ^         ^
    Items mapped to (0,1)
```

If `h_k ~= k/N`, then `N ~= k/h_k`.
The unbiased estimator uses `k-1` instead of `k`: `N ~= (k-1)/h_k`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - `k`: Number of smallest hashes provided.
  - Hashes: List of `k` floats, sorted.
- **Output:** Estimated count.
- **Formula:** `(k-1) / hashes[k-1]`. (Note: 0-based index of `k`-th item is `k-1`).

## Naive Approach

### Intuition

Implement formula.

### Algorithm

1. Get `h_k` (last element of input).
2. Compute `(k-1) / h_k`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct formula.

### Algorithm

1. Read `k` and hashes.
2. `h_k = hashes[k-1]`.
3. Result = `(k-1) / h_k`.
4. Print result.

### Time Complexity

- **O(1)** (after reading input).

### Space Complexity

- **O(1)** (ignoring input storage).

![Algorithm Visualization](../images/PDS-009/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-009/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input:
`3`
`0.1 0.2 0.4`

1. `k=3`.
2. `h_k = 0.4`.
3. Estimate = `(3-1) / 0.4 = 2 / 0.4 = 5.0`.

Output: `5.0`. Matches example.

![Example Visualization](../images/PDS-009/example-1.png)

## ✅ Proof of Correctness

### Invariant
The `k`-th order statistic of `N` uniform random variables on `(0,1)` follows a Beta distribution with expected value `k/(N+1)`.
So `E[h_k] ~= k/N implies N ~= k/h_k`.
The bias-corrected version is `(k-1)/h_k`.

### Why the approach is correct
Standard KMV estimator.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Merging KMV sketches?
  - *Hint:* Take the union of the two lists of hashes, sort them, and keep the smallest `k`.
- **Extension 2:** Jaccard Similarity?
  - *Hint:* `|A cap B| / |A cup B| ~= frac|S_A cap S_B||S_A cup S_B|` where `S` are the KMV sets.

### Common Mistakes to Avoid

1. **Index Error**
   - ❌ Wrong: Using `hashes[k]` (out of bounds).
   - ✅ Correct: `hashes[k-1]`.
2. **Formula Error**
   - ❌ Wrong: `k / hk` (biased).
   - ✅ Correct: `(k-1) / hk`.

## Related Concepts

- **HyperLogLog:** Another distinct count estimator (more space efficient).
- **Order Statistics:** Statistical properties of sorted random samples.
