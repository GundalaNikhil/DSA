---
problem_id: PRB_MIN_CUT_RANDOM_CONTRACTION__8305
display_id: PRB-006
slug: min-cut-random-contraction
title: "Min-Cut with Randomized Contraction"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Graphs
  - Randomized Algorithms
tags:
  - probability
  - karger
  - min-cut
  - medium
premium: true
subscription_tier: basic
---

# PRB-006: Min-Cut with Randomized Contraction

## 📋 Problem Summary

Karger's algorithm finds the global min-cut of a graph with n vertices with probability `p_success >= frac2n(n-1)`.
Given n and a desired confidence level P (e.g., 0.99), calculate the minimum number of independent trials t required to ensure the probability of finding the min-cut is at least P.

| | |
|---|---|
| **Input** | n, P |
| **Output** | Integer t |

## 🌍 Real-World Scenario

**Scenario Title:** The Network Vulnerability Scan

You are a security analyst testing a communication network for bottlenecks.
- The "Global Min-Cut" represents the smallest set of links whose removal would disconnect the network into two pieces.
- Finding this exactly is computationally expensive for massive networks.
- You run a fast randomized algorithm (Karger's) that might miss the true min-cut.
- To be 99.9% sure you've found the actual weakest point, you need to run the simulation multiple times.
- You need to calculate exactly how many times to run it to meet your safety certification standards.

**Why This Problem Matters:**

- **Network Reliability:** Assessing robustness against link failures.
- **Image Segmentation:** Graph cuts are used to separate objects from backgrounds.
- **Clustering:** Identifying tightly connected communities.

![Real-World Application](../images/PRB-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Probability Amplification

Single Trial:
Success (S) prob p. Failure (F) prob 1-p.

t Trials:
All Fail: `(1-p)^t`.
At least one Success: `1 - (1-p)^t`.

We want `1 - (1-p)^t >= P`.
`(1-p)^t <= 1 - P`. t \ln(1-p) \le \ln(1-P)$.
Since `ln(1-p)` is negative, dividing flips the inequality: t \ge \frac{\ln(1-P)}{\ln(1-p)}$.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Formula:** `p_success = frac2n(n-1)`.
- **Logarithms:** Use natural log (`Math.log` in Java/JS, `math.log` in Python, `log` in C++).
- **Rounding:** Since t must be an integer, take the ceiling.
- **Constraints:** n up to 10⁹. `p_success` can be very small.
  - If p is very small, `ln(1-p) ~= -p`.
  - t \approx \frac{\ln(1-P)}{-p} = \frac{-\ln(1-P)}{p}$.
  - This approximation is useful for mental checks but use exact log for code.

### Core Concept: Bernoulli Trials

We are repeating a Bernoulli trial until "at least one success".
This is related to the Geometric distribution (waiting time), but here we fix the number of trials to guarantee a cumulative probability.

## Naive Approach

### Intuition

Loop t = 1, 2, \dots`until`1 - (1-p)^t \ge P$.

### Algorithm

While loop.

### Time Complexity

- **O(t)**. If p is small (10⁻¹⁸), t can be huge (`10^18`). Loop is too slow.

## Optimal Approach

### Key Insight

Use the closed-form logarithmic formula derived above.

### Algorithm

1. Calculate `p_success = 2.0 / (n * (n - 1))`.
2. Calculate numerator = `ln(1 - P)`.
3. Calculate denominator = `ln(1 - p_success)`.
4. Calculate t = \text{ceil}(\text{numerator} / \text{denominator})$.
5. Print t.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-006/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-006/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `4 0.9`.
1. `p_success = 2 / (4 x 3) = 2/12 = 1/6 ~= 0.1667`.
2. `ln(1 - 0.9) = ln(0.1) ~= -2.3026`.
3. `ln(1 - 0.1667) = ln(0.8333) ~= -0.1823`.
4. Ratio: `-2.3026 / -0.1823 ~= 12.63`.
5. Ceil: 13.
Matches example.

## ✅ Proof of Correctness

### Invariant
The formula directly solves the inequality for cumulative probability.

### Why the approach is correct
Standard probability theory.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Karger-Stein Algorithm.
  - *Hint:* Recursive contraction improves success probability to `1/log n`.
- **Extension 2:** Parallel trials.
  - *Hint:* Run trials on multiple cores to reduce wall-clock time.
- **Extension 3:** Weighted Graphs.
  - *Hint:* Karger's works for weighted graphs too (probabilities proportional to weights).

### Common Mistakes to Avoid

1. **Precision Loss**
   - ❌ Wrong: `1.0 - P` when P is very close to 1.
   - ✅ Correct: Use `log1p(-P)` if available for better precision, though standard `log` is usually fine for P < 1 - 10^{-15}$.
2. **Integer Division**
   - ❌ Wrong: `2 / (n * (n-1))` in integer arithmetic.
   - ✅ Correct: `2.0 / ...`.

## Related Concepts

- **Monte Carlo Algorithms:** Always fast, sometimes wrong (but error bounded).
- **Las Vegas Algorithms:** Always correct, sometimes slow. Karger's is Monte Carlo.
