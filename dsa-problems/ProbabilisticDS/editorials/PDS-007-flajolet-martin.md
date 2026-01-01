---
problem_id: PDS_FLAJOLET_MARTIN__2749
display_id: PDS-007
slug: flajolet-martin
title: "Flajolet-Martin Bit Pattern"
difficulty: Medium
difficulty_score: 48
topics:
  - Probabilistic Data Structures
  - Flajolet-Martin
  - Distinct Count
tags:
  - probabilistic-ds
  - flajolet-martin
  - distinct-count
  - medium
premium: true
subscription_tier: basic
---

# PDS-007: Flajolet-Martin Bit Pattern

## 📋 Problem Summary

We need to estimate the number of distinct elements in a stream based on the maximum number of trailing zeros (`R`) observed in their hash values.
- The formula is `E = 2^R / phi`.
- `phi ~= 0.77351`.

## 🌍 Real-World Scenario

**Scenario Title:** Database Query Optimization

Database optimizers need to know how many distinct values are in a column to choose the best query plan.
- `SELECT COUNT(DISTINCT user_id) FROM clicks`
- Exact counting requires sorting or hashing all values, which is `O(N)` memory.
- **Flajolet-Martin** (and its successor HyperLogLog) allows estimating this count using `O(log N)` bits.
- If the max trailing zeros seen is 10, it means we likely saw around `2^10` distinct items.
- Why? Because getting 10 zeros in a row is a `1/1024` probability event. You expect to see it once after `~= 1024` trials.

**Why This Problem Matters:**

- **Streaming Analytics:** Counting unique users in real-time.
- **Network Monitoring:** Counting distinct flows.

![Real-World Application](../images/PDS-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Trailing Zeros

Hashes (binary):
`...10110` (1 zero)
`...00100` (2 zeros)
`...11000` (3 zeros) -> Max so far `R=3`.
`...00001` (0 zeros)

If `R=3`, estimate `~= 2^3 = 8`.
Correction factor `phi` accounts for statistical bias.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Integer `R` (max trailing zeros).
- **Output:** Estimated count.
- **Formula:** `2^R / 0.77351`.

## Naive Approach

### Intuition

Implement formula.

### Algorithm

1. Compute `2^R`.
2. Divide by `0.77351`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct formula.

### Algorithm

1. Read `R`.
2. Compute `pow(2, R) / 0.77351`.
3. Print result.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-007/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `4`

1. `2^4 = 16`.
2. `16 / 0.77351 ~= 20.68493`.

Output: `20.684930`. Matches example.

![Example Visualization](../images/PDS-007/example-1.png)

## ✅ Proof of Correctness

### Invariant
The probability of observing `R` trailing zeros is roughly `2^-R`.

### Why the approach is correct
Flajolet and Martin proved that `R` is an estimator for `log_2(phi N)`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** High variance?
  - *Hint:* A single estimate has huge variance. Use multiple hash functions and average (Stochastic Averaging).
- **Extension 2:** HyperLogLog?
  - *Hint:* Uses harmonic mean of `2^R` across buckets to reduce variance.

### Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: `1 << R` if `R > 31` (in Java/C++ int).
   - ✅ Correct: `pow(2, R)` or `1L << R`.

## Related Concepts

- **HyperLogLog:** Improved version.
- **MinCount:** Another estimator.
