---
problem_id: BIT_MINIMAL_BITS_FLIP_RANGE__8406
display_id: BIT-006
slug: minimal-bits-flip-range
title: "Minimal Bits to Flip Range"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Bit Manipulation
tags:
  - bitwise
  - xor
  - bit-flipping
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-006: Minimal Bits to Flip Range

## Problem Statement

Given two integers `x` and `y`, determine if `x` can be converted to `y` by flipping the **lowest** `m` bits (for some integer `m >= 0`). If possible, return the smallest `m`. Otherwise, return `-1`.

![Problem Illustration](../images/BIT-006/problem-illustration.png)

## Input Format

- Single line: integers x y

## Output Format

Print the smallest m, or -1 if impossible.

## Constraints

- `0 <= x, y <= 1000000000000`

## Example

**Input:**

```
10 5
```

**Output:**

```
4
```

**Explanation:**

10 XOR 5 = 15, which is 2^4 - 1, so flipping the lowest 4 bits works.

![Example Visualization](../images/BIT-006/example-1.png)

## Notes

- Flipping the lowest m bits means toggling every bit position 0..m-1.
- If x == y, the smallest m is 0.

## Related Topics

Bitwise Operations, Math

---

## Solution Template

### Java


### Python


### C++


### JavaScript

