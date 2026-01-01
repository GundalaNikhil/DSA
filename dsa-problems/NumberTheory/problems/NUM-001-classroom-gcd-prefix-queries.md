---
problem_id: NUM_CLASSROOM_GCD_PREFIX_QUERIES__4821
display_id: NUM-001
slug: classroom-gcd-prefix-queries
title: "Classroom GCD Prefix Queries"
difficulty: Easy
difficulty_score: 25
topics:
  - Number Theory
  - GCD
  - Prefix Computation
tags:
  - number-theory
  - gcd
  - prefix
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-001: Classroom GCD Prefix Queries

## Problem Statement

You are given an array `a`. For each query `r`, return the greatest common divisor of the prefix `a[0..r]` (inclusive). Preprocess once to answer all queries efficiently.

![Problem Illustration](../images/NUM-001/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a[i]`
- Next `q` lines: integer `r` (0-based index)

## Output Format

- For each query, print `gcd(a[0..r])` on its own line

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `0 <= r < n`

## Example

**Input:**

```
3 3
12 18 6
0
1
2
```

**Output:**

```
12
6
6
```

**Explanation:**

Prefix GCDs:

- r=0 -> gcd(12) = 12
- r=1 -> gcd(12,18) = 6
- r=2 -> gcd(12,18,6) = 6

![Example Visualization](../images/NUM-001/example-1.png)

## Notes

- Use absolute values when computing gcd
- Precompute prefix gcd in O(n)
- Each query is O(1)
- Space complexity: O(n)

## Related Topics

GCD, Prefix Arrays, Number Theory

---

## Solution Template

### Java


### Python


### C++


### JavaScript

