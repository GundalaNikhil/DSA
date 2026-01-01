---
problem_id: HSH_SUBSTRING_EQUALITY_QUERIES__5917
display_id: HSH-002
slug: substring-equality-queries
title: "Substring Equality Queries"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - Rolling Hash
  - String Matching
tags:
  - hashing
  - rolling-hash
  - substring
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-002: Substring Equality Queries

## Problem Statement

Given a string `s` and `q` queries, each query asks whether two substrings of `s` are equal.

Each query is specified as `(l1, r1, l2, r2)` where:

- First substring: `s[l1..r1]` (inclusive, 0-indexed)
- Second substring: `s[l2..r2]` (inclusive, 0-indexed)

For each query, output `true` if the two substrings are equal, `false` otherwise.

Use polynomial hashing with double hashing (two different moduli) to minimize collision probability.

![Problem Illustration](../images/HSH-002/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of queries)
- Next `q` lines: four integers `l1 r1 l2 r2` for each query

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= q <= 2*10^5`
- `0 <= l1 <= r1 < |s|`
- `0 <= l2 <= r2 < |s|`
- `r1 - l1 == r2 - l2` (substring lengths must match)

## Example

**Input:**

```
ababa
3
0 1 2 3
0 2 2 4
1 1 3 3
```

**Output:**

```
true
true
true
```

**Explanation:**

String: "ababa"

Query 1: s[0..1] = "ab", s[2..3] = "ab" → true
Query 2: s[0..2] = "aba", s[2..4] = "aba" → true
Query 3: s[1..1] = "b", s[3..3] = "b" → true

![Example Visualization](../images/HSH-002/example-1.png)

## Notes

- Precompute prefix hashes during initialization
- Use two different moduli for double hashing to reduce collision probability
- Hash comparison: O(1) per query after O(n) preprocessing
- Time complexity: O(n + q)
- Space complexity: O(n)

## Related Topics

Rolling Hash, String Matching, Substring Comparison, Double Hashing

---

## Solution Template

### Java


### Python


### C++


### JavaScript

