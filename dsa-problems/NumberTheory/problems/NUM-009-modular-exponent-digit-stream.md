---
problem_id: NUM_MODULAR_EXPONENT_DIGIT_STREAM__9056
display_id: NUM-009
slug: modular-exponent-digit-stream
title: "Modular Exponent With Digit Stream"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Modular Exponentiation
  - Big Integers
tags:
  - number-theory
  - modular
  - exponentiation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-009: Modular Exponent With Digit Stream

## Problem Statement

Compute `a^e mod m`, where `e` is given as a decimal digit string that may be very large. You must process the exponent as a string.

![Problem Illustration](../images/NUM-009/problem-illustration.png)

## Input Format

- First line: two integers `a` and `m`
- Second line: string `e` (decimal digits)

## Output Format

- Single integer: `a^e mod m`

## Constraints

- `1 <= a, m <= 10^9`
- `1 <= |e| <= 100000`
- `e` has no leading zeros unless `e` is "0"

## Example

**Input:**

```
3 7
5
```

**Output:**

```
5
```

**Explanation:**

3^5 = 243, and 243 mod 7 = 5.

![Example Visualization](../images/NUM-009/example-1.png)

## Notes

- Process digits: result = result^10 * a^digit (mod m)
- Use fast modular exponentiation for small powers
- Time complexity: O(|e| log m)
- Space complexity: O(1)

## Related Topics

Modular Exponentiation, Big Exponents

---

## Solution Template

### Java


### Python


### C++


### JavaScript

