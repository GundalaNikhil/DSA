---
problem_id: PRB_MARKOV_CHAIN_ABSORPTION__9031
display_id: PRB-010
slug: markov-chain-absorption
title: "Markov Chain Absorption"
difficulty: Medium
difficulty_score: 55
topics:
  - Probability
  - Markov Chains
  - Linear Algebra
tags:
  - probability
  - markov
  - absorption
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-010: Markov Chain Absorption

## Problem Statement

You are given a Markov chain with some absorbing states (a state with probability 1 of staying in itself). From a given start state, compute:

- Expected number of steps to absorption
- Absorption probabilities for each absorbing state

![Problem Illustration](../images/PRB-010/problem-illustration.png)

## Input Format

- First line: integer `n` and integer `s` (start state, 0-based)
- Next `n` lines: `n` real numbers (transition matrix rows)

## Output Format

- First line: expected steps to absorption
- Second line: absorption probabilities for absorbing states in increasing index order

## Constraints

- `1 <= n <= 20`
- Matrix rows sum to 1

## Example

**Input:**

```
3 0
0.5 0.5 0
0 0.5 0.5
0 0 1
```

**Output:**

```
4.000000
1.000000
```

**Explanation:**

State 2 is absorbing. Starting at 0, absorption is certain and expected steps are 4.

![Example Visualization](../images/PRB-010/example-1.png)

## Notes

- Use standard absorbing Markov chain formulas with (I-Q)^{-1}
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n^3)

## Related Topics

Markov Chains, Linear Algebra, Absorption

---

## Solution Template

### Java


### Python


### C++


### JavaScript

