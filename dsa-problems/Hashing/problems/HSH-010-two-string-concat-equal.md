---
problem_id: HSH_TWO_STRING_CONCAT_EQUAL__4156
display_id: HSH-010
slug: two-string-concat-equal
title: "Two-String Concatenation Equal Check"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - String Algorithms
tags:
  - hashing
  - concatenation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-010: Two-String Concatenation Equal Check

## Problem Statement

Given four strings `a`, `b`, `c`, `d`, determine if `a + b == c + d` (concatenation) without explicitly creating the concatenated strings, using polynomial hashing.

![Problem Illustration](../images/HSH-010/problem-illustration.png)

## Input Format

- Four lines, each containing a string: `a`, `b`, `c`, `d`

## Output Format

- Single word: `true` or `false`

## Constraints

- `1 <= |a|, |b|, |c|, |d| <= 10^5`
- Strings contain only lowercase English letters

## Example

**Input:**

```
ab
cd
a
bcd
```

**Output:**

```
true
```

**Explanation:**

a + b = "ab" + "cd" = "abcd"
c + d = "a" + "bcd" = "abcd"

They are equal, so output is true.

![Example Visualization](../images/HSH-010/example-1.png)

## Notes

- Compute hash(a+b) as hash(a) \* B^|b| + hash(b)
- Compute hash(c+d) as hash(c) \* B^|d| + hash(d)
- Compare the two hashes
- Time complexity: O(|a| + |b| + |c| + |d|)
- Space complexity: O(1)

## Related Topics

Hashing, String Concatenation, Polynomial Hash

---

## Solution Template

### Java


### Python


### C++


### JavaScript

