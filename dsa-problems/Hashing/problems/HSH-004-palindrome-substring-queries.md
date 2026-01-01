---
problem_id: HSH_PALINDROME_SUBSTRING_QUERIES__2639
display_id: HSH-004
slug: palindrome-substring-queries
title: "Palindrome Substring Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Palindrome
  - String Algorithms
tags:
  - hashing
  - palindrome
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-004: Palindrome Substring Queries

## Problem Statement

Given a string `s` and `q` queries, answer whether substring `s[l..r]` is a palindrome using hash-based comparisons.

For each query `(l, r)`, determine if the substring from index `l` to `r` (inclusive, 0-indexed) reads the same forwards and backwards.

![Problem Illustration](../images/HSH-004/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of queries)
- Next `q` lines: two integers `l r` for each query

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= q <= 2*10^5`
- `0 <= l <= r < |s|`

## Example

**Input:**

```
abccba
3
0 5
1 4
2 3
```

**Output:**

```
true
false
true
```

**Explanation:**

String: "abccba"

Query 1: s[0..5] = "abccba" → palindrome → true
Query 2: s[1..4] = "bccb" → not a palindrome → false
Query 3: s[2..3] = "cc" → palindrome → true

![Example Visualization](../images/HSH-004/example-1.png)

## Notes

- Precompute forward and reverse polynomial hashes
- Compare hash of s[l..r] with hash of reverse(s[l..r])
- Use double hashing to minimize false positives
- Time complexity: O(n + q) with O(n) preprocessing
- Space complexity: O(n)

## Related Topics

Palindrome Detection, Hashing, Rolling Hash, String Reversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

