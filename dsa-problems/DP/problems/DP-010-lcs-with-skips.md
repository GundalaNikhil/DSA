---
problem_id: DP_LCS_SKIP_BUDGET__2297
display_id: DP-010
slug: lcs-with-skips
title: "LCS With Limited Skips in A"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Strings
  - Subsequence
tags:
  - dp
  - lcs
  - strings
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-010: LCS With Limited Skips in A

## Problem Statement

You are given two lowercase strings `a` and `b`, and an integer `s`.

You may **delete** (skip) characters from `a`, but you are allowed to delete **at most `s` characters from `a`** in total. You can delete any number of characters from `b` (unlimited), as in a standard subsequence match.

Find the maximum length of a common subsequence you can obtain under this constraint. If no common subsequence satisfies the skip limit (i.e., every common subsequence would require more than `s` deletions from `a`), print `-1`.

![Problem Illustration](../images/DP-010/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`
- Third line: integer `s`

## Output Format

Print a single integer: the maximum feasible common subsequence length, or `-1` if none fits within the skip budget.

## Constraints

- `0 <= |a|, |b| <= 2000`
- `0 <= s <= |a|`
- Strings consist of lowercase English letters `a..z`

## Example

**Input:**
```
abcde
ace
2
```

**Output:**
```
3
```

**Explanation:**

- LCS is `"ace"` (length 3), which requires deleting `b` and `d` from `a` ⇒ 2 deletions
- Skip limit `s = 2` allows this, so answer is 3.

**If `s = 1` for the same strings, the best feasible length would be `-1`** because every common subsequence needs at least 2 deletions from `a`.

![Example Visualization](../images/DP-010/example-1.png)

## Notes

- Deleting characters from `b` is unrestricted (as in normal subsequence checking).
- The skip budget applies only to deletions from `a`.
- Returning `-1` indicates that even the maximum common subsequence exceeds the allowed deletions.

## Related Topics

Dynamic Programming, LCS, Strings, Subsequences

---

## Solution Template

### Java


### Python


### C++


### JavaScript


