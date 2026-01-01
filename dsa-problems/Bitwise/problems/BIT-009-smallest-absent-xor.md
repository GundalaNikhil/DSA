---
problem_id: BIT_SMALLEST_ABSENT_XOR__8409
display_id: BIT-009
slug: smallest-absent-xor
title: "Smallest Absent XOR"
difficulty: Medium
difficulty_score: 60
topics:
  - Bitwise Operations
  - XOR
  - XOR Basis
  - Linear Algebra
tags:
  - bitwise
  - xor
  - xor-basis
  - hard
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-009: Smallest Absent XOR

## Problem Statement

Find the smallest non-negative integer x that cannot be represented as the XOR of any subset of the array (including the empty subset).

![Problem Illustration](../images/BIT-009/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the smallest absent XOR value.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**
```
3
1 2 3
```

**Output:**
```
4
```

**Explanation:**

The reachable subset XOR values are {0, 1, 2, 3}. The smallest non-negative integer
not in the set is 4.

![Example Visualization](../images/BIT-009/example-1.png)

## Notes

- The empty subset is allowed and contributes XOR 0.
- Use a linear basis to characterize reachable XOR values.

## Related Topics

Bitwise Operations, Linear Basis

---

## Solution Template

### Java



### Python



### C++



### JavaScript


