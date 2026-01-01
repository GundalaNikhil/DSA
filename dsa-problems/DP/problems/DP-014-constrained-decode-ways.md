---
problem_id: DP_CONSTRAINED_DECODE__3012
display_id: DP-014
slug: constrained-decode-ways
title: "Constrained Decode Ways"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
  - Strings
  - Combinatorics
tags:
  - dp
  - decoding
  - strings
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-014: Constrained Decode Ways

## Problem Statement

A digit string encodes letters `1 -> A`, `2 -> B`, ..., `26 -> Z`. You must count how many distinct decodings exist under an extra rule:

- Any digit `0` is valid **only** when immediately preceded by `2`, forming the two-digit code `20`. No other placement of `0` is allowed.

Return the number of valid decodings modulo `1_000_000_007`.

![Problem Illustration](../images/DP-014/problem-illustration.png)

## Input Format

- Single line: a digit string `s` (no spaces).

## Output Format

- Single integer: number of valid decodings modulo `1_000_000_007`.

## Constraints

- `1 <= |s| <= 100000`
- `s` consists of digits `0-9`
- Leading zeros invalidate the string

## Example

**Input:**
```
2012
```

**Output:**
```
2
```

**Explanation:**

Two decodings satisfy the rule:

- `20 1 2`
- `20 12`

![Example Visualization](../images/DP-014/example-1.png)

## Notes

- The pair `10` is **invalid** because `0` must follow an even digit forming `20` only.
- Standalone `0` makes the entire string invalid.
- Use modulo arithmetic throughout to avoid overflow.

## Related Topics

Dynamic Programming, Strings, Combinatorics

---

## Solution Template

### Java


### Python


### C++


### JavaScript

