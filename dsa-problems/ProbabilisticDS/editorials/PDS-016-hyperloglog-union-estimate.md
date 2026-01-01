---
problem_id: PDS_PROBLEM_16__7318
display_id: PDS-016
slug: hyperloglog-union-estimate
title: "HyperLogLog Union Estimate"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - HyperLogLog
  - Cardinality Estimation
tags:
  - probabilistic-ds
  - hyperloglog
  - union
  - medium
premium: true
subscription_tier: basic
---

# PDS-016: HyperLogLog Union Estimate

## 📋 Problem Summary

We need to compute the cardinality of the union of two HyperLogLog sketches.
- We are given two sketches `A` and `B`, each with `m` registers.
- The union sketch `U` is formed by taking the element-wise maximum of the registers: `U[i] = max(A[i], B[i])`.
- We then apply the standard HyperLogLog cardinality estimation formula to `U`.

## 🌍 Real-World Scenario

**Scenario Title:** Distributed Analytics Aggregation

Imagine you are analyzing logs from a cluster of 100 web servers.
- Each server maintains a HyperLogLog sketch of the unique IP addresses it has seen.
- You want to know the total number of unique IPs across *all* servers.
- Simply summing the counts from each server is wrong because the same IP might visit multiple servers (double counting).
- **HyperLogLog Union** allows you to merge the sketches from all servers into a single sketch.
- This merged sketch represents the union of all sets, and you can query it for the total unique count.
- This property makes HLL extremely powerful for distributed systems (MapReduce, Spark).

**Why This Problem Matters:**

- **Data Warehousing:** Pre-computing daily uniques and merging them to get weekly/monthly uniques.
- **Network Monitoring:** Aggregating flow counts from multiple routers.

![Real-World Application](../images/PDS-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Merging Registers

Sketch A (m=4): `[1, 5, 2, 0]`
Sketch B (m=4): `[3, 2, 2, 4]`

Union Sketch U:
- Index 0: `max(1, 3) = 3`
- Index 1: `max(5, 2) = 5`
- Index 2: `max(2, 2) = 2`
- Index 3: `max(0, 4) = 4`

Result U: `[3, 5, 2, 4]`

Now compute HLL estimate on `[3, 5, 2, 4]`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - `m`: Number of registers.
  - Registers A: List of `m` integers.
  - Registers B: List of `m` integers.
- **Output:** Estimated union cardinality.
- **Formula:** Same as PDS-006, but applied to the merged registers.

## Naive Approach

### Intuition

Merge and estimate.

### Algorithm

1. Create `U` of size `m`.
2. For each `i`: `U[i] = max(A[i], B[i])`.
3. Apply HLL formula to `U`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct implementation.

### Algorithm

1. Read inputs.
2. Compute `alpha_m` based on `m`.
3. Initialize `sum = 0`.
4. For each `i` from 0 to `m-1`:
   - `val = max(A[i], B[i])`
   - `sum += pow(2, -val)`
5. `E = alpha * m * m / sum`.
6. Print `E`.

### Time Complexity

- **O(m)**.

### Space Complexity

- **O(m)** (or O(1) if streaming inputs).

![Algorithm Visualization](../images/PDS-016/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-016/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `m=16`, A=[1...1], B=[2...2]

1. Union U = [2...2] (since `max(1, 2) = 2`).
2. `alpha_16 = 0.673`.
3. Sum: `16 x 2^-2 = 16 x 0.25 = 4.0`.
4. `E = 0.673 x 16^2 / 4.0 = 0.673 x 256 / 4 = 0.673 x 64 = 43.072`.

Output: `43.072000`. Matches example.

![Example Visualization](../images/PDS-016/example-1.png)

## ✅ Proof of Correctness

### Invariant
The max of two registers `M_A[i]` and `M_B[i]` corresponds to the register state if we had inserted all elements from both streams into a single HLL.

### Why the approach is correct
This is the standard merge operation for HyperLogLog, enabling its use in distributed systems.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Intersection?
  - *Hint:* `|A cap B| = |A| + |B| - |A cup B|`. Estimate all three and compute. Note: Error can be large if intersection is small.
- **Extension 2:** Compression?
  - *Hint:* HLL registers are small integers (0-60). Can be packed into 6 bits. Sparse representation for many zeros.

### Common Mistakes to Avoid

1. **Summing Estimates**
   - ❌ Wrong: `Estimate(A) + Estimate(B)`.
   - ✅ Correct: Merge registers, then Estimate.

## Related Concepts

- **Theta Sketch:** Better for intersection estimation.
- **Set Reconciliation:** syncing sets efficiently.
