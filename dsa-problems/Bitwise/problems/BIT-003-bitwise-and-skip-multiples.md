---
problem_id: BIT_AND_SKIP_MULTIPLES__8403
display_id: BIT-003
slug: bitwise-and-skip-multiples
title: "Bitwise AND Skipping Multiples"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - AND
  - Number Theory
  - Mathematics
tags:
  - bitwise
  - and-operation
  - number-theory
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-003: Bitwise AND Skipping Multiples

## Problem Statement

Given L, R, and m, compute the bitwise AND of all numbers in [L, R] that are not divisible by m. If no numbers remain, return -1.

![Problem Illustration](../images/BIT-003/problem-illustration.png)

## Input Format

- Single line: integers L R m

## Output Format

Print the bitwise AND of all numbers in [L, R] not divisible by m, or -1.

## Constraints

- `0 <= L <= R <= 1000000000000`
- `1 <= m <= 1000000`

## Example

**Input:**
```
10 15 3
```

**Output:**
```
8
```

**Explanation:**

The numbers 10, 11, 13, 14, 15 are not divisible by 3, and their AND is 8.

![Example Visualization](../images/BIT-003/example-1.png)

## Notes

- If every number in [L, R] is divisible by m, output -1.
- Use 64-bit integers for L, R, and the result.

## Related Topics

Bitwise Operations, Math

---

## Solution Template

### Java



### Python



### C++



### JavaScript


