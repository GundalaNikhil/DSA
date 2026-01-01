---
problem_id: PRB_SKIP_LIST_EXPECTED_HEIGHT__6591
display_id: PRB-007
slug: skip-list-expected-height
title: "Skip List Expected Height"
difficulty: Medium
difficulty_score: 45
topics:
  - Probability
  - Data Structures
  - Logs
tags:
  - probability
  - skip-list
  - expectation
  - medium
premium: true
subscription_tier: basic
---

# PRB-007: Skip List Expected Height

## 📋 Problem Summary

Calculate the expected maximum height of a Skip List with n elements, where each element is promoted to the next level with probability p.

| | |
|---|---|
| **Formula** | H ≈ log₁/ₚ(n) |
| **Input** | n, p |
| **Output** | H (float) |

## 🌍 Real-World Scenario

**Scenario Title:** The Express Train System

Imagine a subway system with n stations.
- A "Level 0" train stops at every station.
- To speed up travel, you add "Level 1" express trains that skip some stations.
- You decide which stations get a Level 1 stop by flipping a coin (probability p).
- Then you add "Level 2" super-express trains that stop only at a subset of Level 1 stations (again with probability p).
- You continue adding levels until only a few major hubs remain.
- The "Height" of this system is the number of train tiers needed to ensure you can get from anywhere to anywhere efficiently (logarithmic time).
- You need to estimate this height to plan the infrastructure.

**Why This Problem Matters:**

- **Database Indexing:** Skip lists are a simpler alternative to balanced trees (used in Redis, LevelDB).
- **Network Routing:** Hierarchical routing protocols.
- **Distributed Systems:** Overlay networks like Chord use similar "finger table" concepts.

![Real-World Application](../images/PRB-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Skip List Levels

n = 10, p=0.5$.

```
Level 3: 1 -----------------------------------> NULL
Level 2: 1 ---------> 5 ----------------------> NULL
Level 1: 1 ---> 3 --> 5 -------> 9 -----------> NULL
Level 0: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> NULL
```

- Level 0 has all 10 nodes.
- Level 1 has ~5 nodes.
- Level 2 has ~2.5 nodes.
- Level 3 has ~1.25 nodes.
- Height is the number of levels.
- Expected Max Level ≈ \log_2(10) \approx 3.32$.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Formula:** H = \frac{\ln(n)}{\ln(1/p)}$.
- **Base Change:** `log_b(x) = fracln(x)ln(b)`. Here base b = 1/p.
- **Precision:** Use `double`.
- **Constraints:** n \le 10^6$. Calculation is O(1).

### Core Concept: Geometric Distribution

The height of a single element follows a Geometric distribution (number of successes before failure, or sequence of successes).
The maximum of n independent geometric variables grows logarithmically with n.
Specifically, the probability that any node reaches level L is `p^L`.
We want the level L where the expected number of nodes is roughly 1 (or small constant). n \cdot p^L \approx 1 \implies p^L \approx 1/n \implies L \ln p \approx -\ln n \implies L \approx \frac{-\ln n}{\ln p} = \frac{\ln n}{\ln(1/p)}$.

## Naive Approach

### Intuition

Simulate building a skip list many times and average the height.

### Algorithm

Monte Carlo simulation.

### Time Complexity

- **O(Trials \cdot n)**. Too slow.

## Optimal Approach

### Key Insight

Direct implementation of the logarithmic formula.

### Algorithm

1. Calculate `numerator = log(n)`.
2. Calculate `denominator = log(1.0 / p)`.
3. Return `numerator / denominator`.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-007/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `1024 0.5`.
1. `log(1024) ≈ 6.93147`.
2. `log(1/0.5) = log(2) ≈ 0.693147`.
3. `6.93147 / 0.693147 = 10.0`.
Matches example.

## ✅ Proof of Correctness

### Invariant
The formula is derived from the expected value of the maximum of n geometric random variables.

### Why the approach is correct
Standard probabilistic analysis of Skip Lists (see Pugh 1990).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Space Complexity of Skip List.
  - *Hint:* Expected total pointers is `n/(1-p)`. For p = 0.5, it's `2n`.
- **Extension 2:** Why not use p = 0.5 always?
  - *Hint:* p = 0.25 saves space (1.33 pointers/node) at cost of slightly higher height (`log_4 n`).
- **Extension 3:** Deterministic Skip Lists.
  - *Hint:* 1-2-3 Skip List (similar to B-Tree).

### Common Mistakes to Avoid

1. **Log Base**
   - ❌ Wrong: `log(n)` assuming base 10 or 2 without checking.
   - ✅ Correct: `Math.log` is natural log (e). Ratio of logs works for any base.
2. **Precision**
   - ❌ Wrong: `1/p` integer division.
   - ✅ Correct: `1.0/p`.

## Related Concepts

- **Balanced Trees:** AVL, Red-Black (deterministic guarantees).
- **Treaps:** Randomized binary search trees (similar probabilistic bounds).
