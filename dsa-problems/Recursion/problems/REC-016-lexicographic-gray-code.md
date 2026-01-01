---
problem_id: REC_LEXICOGRAPHIC_GRAY_CODE__6685
display_id: REC-016
slug: lexicographic-gray-code
title: "Lexicographic Gray Code"
difficulty: Medium
difficulty_score: 45
topics:
  - Recursion
  - Bit Manipulation
  - Gray Code
tags:
  - recursion
  - gray-code
  - bitwise
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-016: Lexicographic Gray Code

## Problem Statement

Generate an `n`-bit Gray code sequence using the standard recursive construction: prefix `0` to the previous sequence and prefix `1` to the reverse of the previous sequence.

Output the resulting sequence in order, one code per line.

![Problem Illustration](../images/REC-016/problem-illustration.png)

## Input Format

- First line: integer `n`

## Output Format

- `2^n` lines, each an `n`-bit string

## Constraints

- `1 <= n <= 12`

## Example

**Input:**

```
2
```

**Output:**

```
00
01
11
10
```

**Explanation:**

The recursive Gray code for `n=2` is `00, 01, 11, 10`.

![Example Visualization](../images/REC-016/example-1.png)

## Notes

- Base case: `n=1` yields `0, 1`
- Each consecutive pair differs by exactly one bit
- The sequence size is `2^n`
- Recursion makes the construction straightforward

## Related Topics

Gray Code, Recursion, Bit Manipulation

---

## Solution Template
### Java


### Python


### C++


### JavaScript

