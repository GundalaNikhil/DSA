---
problem_id: PDS_HYPERLOGLOG_ESTIMATE__1507
display_id: PDS-006
slug: hyperloglog-estimate
title: "HyperLogLog Cardinality Estimate"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - HyperLogLog
  - Cardinality Estimation
tags:
  - probabilistic-ds
  - hyperloglog
  - cardinality
  - medium
premium: true
subscription_tier: basic
---

# PDS-006: HyperLogLog Cardinality Estimate

## 📋 Problem Summary

We need to compute the cardinality estimate from the state of a HyperLogLog (HLL) data structure.
- HLL uses `m` registers.
- Each register stores the maximum number of leading zeros observed in the hashed values of items mapping to that register.
- The raw estimate is given by the harmonic mean of `2^register`.
- We must apply bias correction (`alpha_m`) and Linear Counting for small ranges.

## 🌍 Real-World Scenario

**Scenario Title:** Unique Visitors Analytics

Imagine you run a website like Reddit.
- You want to count "Unique Visitors" per day.
- Storing every IP address in a `Set<String>` is expensive. 100 million visitors `x` 4 bytes = 400 MB per day.
- **HyperLogLog** can estimate this count with < 2% error using only 1.5 KB of memory, regardless of how many visitors you have!
- It works by observing the "unlikeliness" of hash values. If you see a hash ending in `...00000101`, it's common. If you see `...00000000000000000001`, you've probably seen a LOT of unique items.

**Why This Problem Matters:**

- **Big Data:** Redis uses HLL for `PFCOUNT`.
- **Databases:** PostgreSQL and BigQuery use HLL for `APPROX_COUNT_DISTINCT`.

![Real-World Application](../images/PDS-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: HLL Registers

Registers (`m=4`):
`[2, 0, 5, 1]`

- Register 0 saw max leading zeros: 2 (prob `1/4`)
- Register 1 saw max leading zeros: 0 (prob `1/1`)
- Register 2 saw max leading zeros: 5 (prob `1/32`)
- Register 3 saw max leading zeros: 1 (prob `1/2`)

Harmonic Mean of probabilities:
`Sum = 2^-2 + 2^-0 + 2^-5 + 2^-1 = 0.25 + 1.0 + 0.03125 + 0.5 = 1.78125`.
Estimate `propto m^2 / Sum`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - `m`: Number of registers (power of 2).
  - Registers: Array of `m` integers.
- **Output:** Estimated cardinality.
- **Algorithm:**
  1. Calculate `alpha_m`.
  2. Calculate raw estimate `E_raw = fracalpha_m m^2sum 2^-M[j]`.
  3. If `E_raw <= 2.5m`, check for empty registers (`V`).
     - If `V > 0`, use Linear Counting: `E = m ln(m/V)`.
     - Else use `E_raw`.
  4. (Problem omits large range correction for simplicity, so just output result).

## Naive Approach

### Intuition

Just implement the formula.

### Algorithm

1. Determine `alpha_m`.
2. Sum `2^-reg`.
3. Compute `E`.
4. Check small range condition.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct implementation.

### Algorithm

1. **Alpha Calculation:**
   - Switch on `m`: 16->0.673, 32->0.697, 64->0.709.
   - Default: `0.7213 / (1 + 1.079/m)`.
2. **Raw Estimate:**
   - `sum = 0`
   - `zeros = 0`
   - For each val in registers:
     - `sum += pow(2, -val)`
     - If `val == 0`, `zeros++`
   - `E = alpha * m * m / sum`
3. **Correction:**
   - If `E <= 2.5 * m` and `zeros > 0`:
     - `E = m * log(m / zeros)`
4. Print `E`.

### Time Complexity

- **O(m)**.

### Space Complexity

- **O(1)** (ignoring input storage).

![Algorithm Visualization](../images/PDS-006/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-006/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `m=16`, `registers=[1,1,...1]` (all 1s)

1. `alpha_16 = 0.673`.
2. Sum: `16 x 2^-1 = 16 x 0.5 = 8.0`.
3. `E = 0.673 x 16^2 / 8.0 = 0.673 x 256 / 8 = 0.673 x 32 = 21.536`.
4. Check Linear Counting:
   - `2.5 x 16 = 40`.
   - `E = 21.536 <= 40`.
   - Zeros = 0.
   - Condition `zeros > 0` is false.
   - Keep `E = 21.536`.

Output: `21.536000`. Matches example.

![Example Visualization](../images/PDS-006/example-1.png)

## ✅ Proof of Correctness

### Invariant
The HyperLogLog algorithm is statistically derived.

### Why the approach is correct
We implement the standard bias-corrected formula from the Flajolet et al. paper.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Why Harmonic Mean?
  - *Hint:* It handles outliers (large values) better than arithmetic mean.
- **Extension 2:** Merging HLLs?
  - *Hint:* Take max of corresponding registers. `M_new[i] = max(M1[i], M2[i])`.
- **Extension 3:** Space complexity?
  - *Hint:* `O(m log log N)`. For `m=2^14`, registers need 5 bits (up to 32 zeros). Total `~= 12` KB.

### Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `1/m` in alpha calculation using integers.
   - ✅ Correct: `1.0/m`.
2. **Log Base**
   - ❌ Wrong: `log10` for Linear Counting.
   - ✅ Correct: `ln` (`Math.log`).

## Related Concepts

- **LogLog:** Predecessor to HLL (uses arithmetic mean).
- **MinHash:** Similarity estimation.
