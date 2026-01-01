---
problem_id: HSH_COUNT_PAIRS_EQUAL_DOUBLE_HASH__9418
display_id: HSH-015
slug: count-pairs-equal-double-hash
title: "Count Pairs with Equal Hash Mod Two Mods"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Combinatorics
  - String Algorithms
tags:
  - hashing
  - double-hash
  - pairs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-015: Count Pairs with Equal Hash Mod Two Mods

## Problem Statement

Given a string `s` and length `L`, count the number of pairs of substrings of length `L` that have equal hash values under two different moduli (assume collisions are negligible with double hashing).

Return the count of such pairs.

![Problem Illustration](../images/HSH-015/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `L`

## Output Format

- Single integer: number of pairs with equal double hash

## Constraints

- `1 <= |s| <= 10^5`
- `1 <= L <= |s|`
- String contains only lowercase English letters

## Example

**Input:**

```
aaaa
2
```

**Output:**

```
3
```

**Explanation:**

String: "aaaa"
Length L: 2

All substrings of length 2:

- s[0..1] = "aa"
- s[1..2] = "aa"
- s[2..3] = "aa"

All three substrings are identical, so pairs with equal hash:

- (0,1), (0,2), (1,2)

Total: 3 pairs

![Example Visualization](../images/HSH-015/example-1.png)

## Notes

- Compute double hash (using two different moduli) for all substrings of length L
- Group substrings by their hash pair (hash1, hash2)
- For each group of size n, count C(n, 2) = n\*(n-1)/2 pairs
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Hashing, Double Hashing, Combinatorics, Substring Matching

---

## Solution Template

### Java


### Python


### C++


### JavaScript

