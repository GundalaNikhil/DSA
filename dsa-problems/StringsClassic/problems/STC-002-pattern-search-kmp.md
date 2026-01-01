---
problem_id: STC_PATTERN_SEARCH_KMP__6142
display_id: STC-002
slug: pattern-search-kmp
title: "Pattern Search With KMP"
difficulty: Easy
difficulty_score: 30
topics:
  - Strings
  - KMP
  - Pattern Matching
tags:
  - strings
  - kmp
  - pattern-search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-002: Pattern Search With KMP

## Problem Statement

Given a pattern `p` and text `t`, find all starting indices where `p` occurs in `t` using the KMP algorithm.

Indices are 0-based and should be returned in increasing order.

![Problem Illustration](../images/STC-002/problem-illustration.png)

## Input Format

- First line: pattern string `p`
- Second line: text string `t`

## Output Format

- Single line: space-separated indices of all occurrences
- If there are no occurrences, print an empty line

## Constraints

- `1 <= |p|, |t| <= 200000`
- `p` and `t` contain lowercase English letters

## Example

**Input:**

```
aba
ababa
```

**Output:**

```
0 2
```

**Explanation:**

The pattern "aba" occurs at positions 0 and 2.

![Example Visualization](../images/STC-002/example-1.png)

## Notes

- Use the prefix function for `p`
- KMP runs in O(|p| + |t|)
- Overlapping matches should be included
- Output order must be increasing

## Related Topics

KMP, Pattern Matching, Prefix Function

---

## Solution Template
### Java


### Python


### C++


### JavaScript

