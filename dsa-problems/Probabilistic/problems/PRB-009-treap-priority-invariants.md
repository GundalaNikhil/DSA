---
problem_id: PRB_TREAP_PRIORITY_INVARIANTS__7410
display_id: PRB-009
slug: treap-priority-invariants
title: "Treap Priority Invariants"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Data Structures
  - Expected Value
tags:
  - probability
  - treap
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-009: Treap Priority Invariants

## Problem Statement

For a treap built from `n` distinct keys with random priorities, the expected depth analysis depends on the harmonic number. Compute:

- `H_n = 1 + 1/2 + 1/3 + ... + 1/n` (the `n`-th harmonic number)

Note: While the expected depth of a node is `E_depth = 2 * H_n - 2` and expected total path length is `E_path = 2 * (n + 1) * H_n - 4n`, for this problem we output only the harmonic sum.

![Problem Illustration](../images/PRB-009/problem-illustration.png)

## Input Format

- Single line: integer `n`

## Output Format

- Single floating-point number: `H_n` (the harmonic sum)

## Constraints

- `1 <= n <= 10^6`

## Example

**Input:**

```
4
```

**Output:**

```
2.083333
```

**Explanation:**

H_4 = 1 + 1/2 + 1/3 + 1/4 = 2.083333

![Example Visualization](../images/PRB-009/example-1.png)

## Notes

- Compute H_n as sum_{i=1..n} 1/i
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n)

## Related Topics

Treaps, Random BST, Harmonic Numbers

---

## Solution Template

### Java


### Python


### C++


### JavaScript

