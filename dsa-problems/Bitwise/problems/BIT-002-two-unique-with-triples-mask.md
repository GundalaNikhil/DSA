---
problem_id: BIT_TWO_UNIQUE_TRIPLES__8402
display_id: BIT-002
slug: two-unique-with-triples-mask
title: "Two Unique With Triple Others Under Mask"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - bit-manipulation
  - array
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-002: Two Unique With Triple Others Under Mask

## Problem Statement

Every number appears exactly three times except two distinct numbers that appear once each. You are also given a mask M; the two uniques are guaranteed to differ in at least one bit that is set in M. Find the two unique values.

![Problem Illustration](../images/BIT-002/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer M

## Output Format

Print the two unique values in ascending order.

## Constraints

- `2 <= n <= 200000`
- `0 <= M <= 1000000000`

## Example

**Input:**
```
8
5 5 5 9 9 9 3 6
1
```

**Output:**
```
3 6
```

**Explanation:**

The only values appearing once are 3 and 6, so they are returned in ascending
order.

![Example Visualization](../images/BIT-002/example-1.png)

## Notes

- The output must be in ascending order for deterministic checking.
- The mask M guarantees a separating bit for partitioning.

## Related Topics

Bitwise Operations, Counting Bits

---

## Solution Template

### Java



### Python



### C++



### JavaScript


