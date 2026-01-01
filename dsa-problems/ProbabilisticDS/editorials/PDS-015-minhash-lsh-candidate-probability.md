---
problem_id: PDS_PROBLEM_15__4501
display_id: PDS-015
slug: minhash-lsh-candidate-probability
title: "MinHash LSH Candidate Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - MinHash
  - LSH
tags:
  - probabilistic-ds
  - lsh
  - minhash
  - medium
premium: true
subscription_tier: basic
---

# PDS-015: MinHash LSH Candidate Probability

## 📋 Problem Summary

We need to calculate the probability that two sets with Jaccard similarity `s` are identified as a candidate pair by the MinHash LSH algorithm.
- The LSH scheme uses `b` bands, each consisting of `r` rows.
- A pair is a candidate if they match in *at least one* band.
- Two sets match in a band if they have identical MinHash signatures in all `r` rows of that band.
- The probability of matching in one specific row is exactly `s`.

## 🌍 Real-World Scenario

**Scenario Title:** Near-Duplicate Image Search

Imagine you are Pinterest or Google Images.
- You have billions of images.
- You want to find images that are "visually similar" to a query image.
- Comparing the query against all billion images is impossible.
- **LSH (Locality Sensitive Hashing)** acts as a pre-filter.
- It groups similar items into the same buckets with high probability.
- If two images are 90% similar (`s=0.9`), we want a very high probability (`P ~= 1`) that they land in the same bucket.
- If two images are 10% similar (`s=0.1`), we want a very low probability (`P ~= 0`) that they land in the same bucket.
- The parameters `b` and `r` tune this "S-curve" to define what counts as "similar".

**Why This Problem Matters:**

- **Plagiarism Detection:** Finding documents with significant overlap.
- **Audio Fingerprinting:** Shazam-style song recognition.

![Real-World Application](../images/PDS-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: LSH Bands

Signature Matrix (`M` rows, columns are items).
Split into `b=2` bands of `r=2` rows.

```
      Item1  Item2
Row1: [ 1 ]  [ 1 ]  <- Band 1
Row2: [ 2 ]  [ 2 ]  <- Band 1 (Match! Candidate)

Row3: [ 5 ]  [ 5 ]  <- Band 2
Row4: [ 7 ]  [ 9 ]  <- Band 2 (Mismatch)
```

- Prob(Row Match) = `s`.
- Prob(Band Match) = Prob(All `r` rows match) = `s^r`.
- Prob(Band Mismatch) = `1 - s^r`.
- Prob(All `b` bands mismatch) = `(1 - s^r)^b`.
- Prob(At least one band match) = `1 - (1 - s^r)^b`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - `b`: Number of bands.
  - `r`: Rows per band.
  - `s`: Jaccard similarity (`0 <= s <= 1`).
- **Output:** Probability `P`.
- **Formula:** `1 - (1 - s^r)^b`.

## Naive Approach

### Intuition

Implement formula.

### Algorithm

1. `term1 = pow(s, r)`.
2. `term2 = pow(1 - term1, b)`.
3. `P = 1 - term2`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct calculation.

### Algorithm

1. Read `b, r, s`.
2. Compute `val = 1.0 - pow(s, r)`.
3. Compute `P = 1.0 - pow(val, b)`.
4. Print `P`.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-015/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-015/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `5 2 0.5`

1. `s=0.5, r=2`.
2. `s^r = 0.5^2 = 0.25`.
3. `1 - 0.25 = 0.75`.
4. `b=5`.
5. `0.75^5 ~= 0.237305`.
6. `1 - 0.237305 = 0.762695`.

Output: `0.762695`. Matches example.

![Example Visualization](../images/PDS-015/example-1.png)

## ✅ Proof of Correctness

### Invariant
The formula represents the probability of the union of independent events (bands matching).

### Why the approach is correct
Standard LSH probability derivation.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** How to choose `b` and `r`?
  - *Hint:* For a target threshold `t ~= (1/b)^1/r`, the curve is steepest.
- **Extension 2:** False Negatives?
  - *Hint:* Probability is `1 - P`. If `s` is high, we want this to be low.

### Common Mistakes to Avoid

1. **Order of Operations**
   - ❌ Wrong: `1 - s^(r*b)` (implies all rows must match).
   - ✅ Correct: `1 - (1 - s^r)^b`.

## Related Concepts

- **S-Curve:** The shape of the probability function `f(s) = 1-(1-s^r)^b`.
- **Cosine LSH:** Uses random hyperplanes (SimHash).
