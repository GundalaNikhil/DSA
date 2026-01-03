---
problem_id: HSH_LCS_HASH_TWO_STRINGS__7482
display_id: HSH-003
slug: lcs-hash-two-strings
title: "Longest Common Substring of Two Strings"
difficulty: Medium
difficulty_score: 50
topics:

- Hashing
- Binary Search
- String Algorithms
  tags:
- hashing
- binary-search
- lcs
- medium
  premium: true
  subscription_tier: basic
  time_limit: 2000
  memory_limit: 256

---

# HSH-003: Longest Common Substring of Two Strings

## Problem Statement

Given two strings `a` and `b`, find the length of their longest common substring using binary search combined with polynomial hashing.

A common substring is a contiguous sequence of characters that appears in both strings.

![Problem Illustration](../images/HSH-003/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

- Single integer: length of the longest common substring

## Constraints

- `1 <= |a|, |b| <= 10^5`
- Strings contain only lowercase English letters

## Example

**Input:**

```
abcde
cdef
```

**Output:**

```
3
```

**Explanation:**

String a: "abcde"
String b: "cdef"

Common substrings:

- "c" (length 1)
- "cd" (length 2)
- "cde" (length 3) ← longest

Output: 3

![Example Visualization](../images/HSH-003/example-1.png)

## Notes

- Use binary search on the answer (length of substring)
- For each candidate length, use hashing to check if any substring of that length appears in both strings
- Store hashes of all substrings of length L from string a in a set
- Check if any substring of length L from string b matches
- Time complexity: O((|a| + |b|) \* log(min(|a|, |b|)))
- Space complexity: O(min(|a|, |b|))

## Related Topics

Binary Search, Hashing, Rolling Hash, Longest Common Substring

---

## Solution Template

### Java

### Python

### C++

### JavaScript
