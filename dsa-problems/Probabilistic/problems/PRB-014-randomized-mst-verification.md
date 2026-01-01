---
problem_id: PRB_RANDOMIZED_MST_VERIFICATION__6089
display_id: PRB-014
slug: randomized-mst-verification
title: "Randomized MST Verification"
difficulty: Medium
difficulty_score: 56
topics:
  - Probability
  - Graphs
  - Verification
tags:
  - probability
  - mst
  - verification
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-014: Randomized MST Verification

## Problem Statement

A randomized verification algorithm detects an incorrect MST weight with probability at least `1 / n^2` per independent trial. Given `n` and a desired confidence `C`, compute the minimum number of trials needed so that the probability of detecting an incorrect MST is at least `C`.

![Problem Illustration](../images/PRB-014/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `C`

## Output Format

- Single integer: minimum number of trials

## Constraints

- `2 <= n <= 10^9`
- `0 < C < 1`

## Example

**Input:**

```
10 0.99
```

**Output:**

```
459
```

**Explanation:**

Per-trial detection probability p = 1/n^2 = 0.01. We need the smallest t with 1 - (1-p)^t >= 0.99.

![Example Visualization](../images/PRB-014/example-1.png)

## Notes

- Use t = ceil(log(1-C) / log(1-p))
- Handle floating-point precision carefully
- Time complexity: O(1)

## Related Topics

Randomized Verification, MST, Probability

---

## Solution Template

### Java


### Python


### C++


### JavaScript

