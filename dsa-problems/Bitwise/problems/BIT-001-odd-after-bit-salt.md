---
problem_id: BIT_XOR_ODD_OCCURRENCE__8401
display_id: BIT-001
slug: odd-after-bit-salt
title: "Odd After Bit Salt"
difficulty: Easy
difficulty_score: 30
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Mathematics
tags:
  - bitwise
  - xor
  - array
  - mathematics
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-001: Odd After Bit Salt

## Problem Statement

Each array element x is transformed to x XOR salt, where salt is the same for all elements. In the transformed multiset, exactly one value appears an odd number of times and all others appear an even number of times.
Find that odd-occurring value without explicitly building the transformed array.

![Problem Illustration](../images/BIT-001/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer salt

## Output Format

Print the transformed value that appears an odd number of times.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`
- `-1000000000 <= salt <= 1000000000`

## Example

**Input:**

```
7
4 1 2 1 2 4 7
3
```

**Output:**

```
4
```

**Explanation:**

XOR all values with salt and use XOR aggregation; the odd-occurring transformed
value is 4.

![Example Visualization](../images/BIT-001/example-1.png)

## Notes

- XOR is associative and cancels even counts.
- You do not need to materialize the transformed array.

## Related Topics

Bitwise Operations, XOR, Arrays

---

## Solution Template

### Java


### Python


### C++


### JavaScript

