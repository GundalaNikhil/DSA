---
problem_id: BIT_MINIMIZE_MAX_PAIR_XOR__8413
display_id: BIT-013
slug: minimize-max-pair-xor
title: "Minimize Max Pair XOR"
difficulty: Medium
difficulty_score: 58
topics:
  - Bitwise Operations
  - XOR
  - Dynamic Programming
  - Pairing
tags:
  - bitwise
  - xor
  - dp
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-013: Minimize Max Pair XOR

## Problem Statement

Pair up all elements (n is even) to minimize the maximum XOR among all pairs.
Return the minimal possible maximum XOR.

![Problem Illustration](../images/BIT-013/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the minimal possible maximum XOR.

## Constraints

- `2 <= n <= 16`
- `n is even`

## Example

**Input:**
```
4
1 2 3 4
```

**Output:**
```
5
```

**Explanation:**

Pairing (1,4) and (2,3) gives XORs 5 and 1, so the maximum is 5, which is minimal.

![Example Visualization](../images/BIT-013/example-1.png)

## Notes

- n is small; exponential DP over subsets is feasible.
- All elements must be paired exactly once.

## Related Topics

Bitwise Operations, DP

---

## Solution Template

### Java



### Python



### C++



### JavaScript


