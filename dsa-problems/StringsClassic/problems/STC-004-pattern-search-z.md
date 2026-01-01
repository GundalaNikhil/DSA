---
problem_id: STC_PATTERN_SEARCH_Z__4681
display_id: STC-004
slug: pattern-search-z
title: "Pattern Search With Z-Function"
difficulty: Easy
difficulty_score: 32
topics:
  - Strings
  - Z-Algorithm
  - Pattern Matching
tags:
  - strings
  - z-function
  - pattern-search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-004: Pattern Search With Z-Function

## Problem Statement

Given a pattern `p` and text `t`, find all starting indices where `p` occurs in `t` using the Z-function on `p + '#' + t`.

Indices are 0-based and should be output in increasing order.

![Problem Illustration](../images/STC-004/problem-illustration.png)

## Input Format

- First line: pattern string `p`
- Second line: text string `t`

## Output Format

- Single line: space-separated indices of all occurrences
- If there are no occurrences, print an empty line

## Constraints

- `1 <= |p|, |t| <= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
aa
aaa
```

**Output:**

```
0 1
```

**Explanation:**

The pattern "aa" occurs at indices 0 and 1.

![Example Visualization](../images/STC-004/example-1.png)

## Notes

- Use a delimiter `#` not appearing in the strings
- Compute Z on the concatenated string
- Match positions where `Z[i] == |p|`
- Time complexity: O(|p| + |t|)

## Related Topics

Z-Algorithm, Pattern Matching, String Search

---

## Solution Template
### Java


### Python


### C++


### JavaScript

