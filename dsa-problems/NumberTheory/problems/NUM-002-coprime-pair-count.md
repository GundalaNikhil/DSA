---
problem_id: NUM_COPRIME_PAIR_COUNT__7194
display_id: NUM-002
slug: coprime-pair-count
title: "Coprime Pair Count Up To N"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Euler Totient
  - Counting
tags:
  - number-theory
  - totient
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-002: Coprime Pair Count Up To N

## Problem Statement

Given an integer `N`, count the number of ordered pairs `(i, j)` such that `1 <= i < j <= N` and `gcd(i, j) = 1`.

![Problem Illustration](../images/NUM-002/problem-illustration.png)

## Input Format

- Single line: integer `N`

## Output Format

- Single integer: number of coprime pairs

## Constraints

- `1 <= N <= 100000`

## Example

**Input:**

```
5
```

**Output:**

```
9
```

**Explanation:**

The coprime pairs are:

(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4),(3,5),(4,5)

Total = 9.

![Example Visualization](../images/NUM-002/example-1.png)

## Notes

- The answer equals sum_{k=2..N} phi(k)
- Compute phi for all k with a sieve
- Time complexity: O(N log log N)
- Space complexity: O(N)

## Related Topics

Euler Totient, Counting, GCD

---

## Solution Template

### Java


### Python


### C++


### JavaScript

