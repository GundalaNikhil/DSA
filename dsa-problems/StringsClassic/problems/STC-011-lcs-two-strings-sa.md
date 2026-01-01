---
problem_id: STC_LCS_TWO_STRINGS_SA__4927
display_id: STC-011
slug: lcs-two-strings-sa
title: "Longest Common Substring of Two Strings (SA)"
difficulty: Medium
difficulty_score: 56
topics:
  - Strings
  - Suffix Array
  - LCP
tags:
  - strings
  - suffix-array
  - lcp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-011: Longest Common Substring of Two Strings (SA)

## Problem Statement

Given two strings `a` and `b`, find the length of their longest common substring. A substring is a contiguous segment of a string.

![Problem Illustration](../images/STC-011/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

- Single integer: length of the longest common substring

## Constraints

- `1 <= |a|, |b| <= 100000`
- `|a| + |b| <= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
abcd
bc
```

**Output:**

```
2
```

**Explanation:**

The longest common substring is "bc" with length 2.

![Example Visualization](../images/STC-011/example-1.png)

## Notes

- Build a suffix array for `a + '#' + b` with a separator not in the alphabet.
- The answer is the maximum LCP of adjacent suffixes from different strings.
- Time complexity: O(n log n) with suffix array + LCP.
- Space complexity: O(n).

## Related Topics

Suffix Array, LCP, Longest Common Substring

---

## Solution Template

### Java


### Python


### C++


### JavaScript

