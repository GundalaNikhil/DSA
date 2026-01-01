---
problem_id: HSH_DETECT_PERIOD_STRING__6183
display_id: HSH-007
slug: detect-period-string
title: "Detect Period of String"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - String Algorithms
  - Periodicity
tags:
  - hashing
  - period
  - pattern
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-007: Detect Period of String

## Problem Statement

Determine the smallest period `p` of string `s`. The period is the smallest positive integer `p` such that `s` can be represented as the repetition of a substring of length `p`.

If no such period exists (i.e., the string cannot be formed by repeating a substring), return the length of the string.

![Problem Illustration](../images/HSH-007/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single integer: smallest period of the string

## Constraints

- `1 <= |s| <= 2*10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
ababab
```

**Output:**

```
2
```

**Explanation:**

String: "ababab"

The string can be formed by repeating "ab" (length 2) three times.
Periods to check:

- Period 1: "a" repeated → "aaaaaa" ≠ "ababab"
- Period 2: "ab" repeated → "ababab" ✓

Smallest period: 2

![Example Visualization](../images/HSH-007/example-1.png)

## Notes

- Check divisors of string length as potential periods
- Use hashing to verify if s equals concatenation of s[0..p-1] repeated
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

String Period, Pattern Matching, Hashing, KMP Failure Function

---

## Solution Template

### Java


### Python


### C++


### JavaScript

