---
problem_id: BIT_COUNT_SETBITS_INDEXED_XOR__8407
display_id: BIT-007
slug: count-set-bits-indexed-xor
title: "Count Set Bits Of Indexed XOR"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - popcount
  - mathematics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-007: Count Set Bits Of Indexed XOR

## Problem Statement

Let b[i] = i XOR a[i] for i from 0 to n-1. Compute the total number of set bits across all values in b.

![Problem Illustration](../images/BIT-007/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the total count of set bits in b.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**
```
2
0 2
```

**Output:**
```
2
```

**Explanation:**

b = [0 XOR 0, 1 XOR 2] = [0, 3]. The popcounts are 0 and 2, totaling 2.

![Example Visualization](../images/BIT-007/example-1.png)

## Notes

- Indices are 0-based.
- Use 64-bit arithmetic for the total.

## Related Topics

Bitwise Operations, Counting Bits

---

## Solution Template

### Java



### Python



### C++



### JavaScript


