---
problem_id: BIT_PAIRWISE_XOR_BAND_PARITY__8404
display_id: BIT-004
slug: pairwise-xor-band-index-parity
title: "Pairwise XOR in Band With Index Parity"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Array
tags:
  - bitwise
  - xor
  - trie
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-004: Pairwise XOR in Band With Index Parity

## Problem Statement

Given an array and range `[L, U]`, count the number of index pairs `(i, j)` such that `i < j`, `i + j` is even, and the XOR sum `a[i] ^ a[j]` falls within `[L, U]`.

![Problem Illustration](../images/BIT-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integers L and U

## Output Format

Print the number of valid pairs.

## Constraints

- `1 <= n <= 100000`
- `0 <= a[i] <= 1000000000`
- `0 <= L <= U <= 1000000000`

## Example

**Input:**

```
4
2 3 1 7
1 4
```

**Output:**

```
2
```

**Explanation:**

Valid pairs are (0,2): 2 XOR 1 = 3 and (1,3): 3 XOR 7 = 4. Both have i + j even.

![Example Visualization](../images/BIT-004/example-1.png)

## Notes

- Indices are 0-based.
- Only pairs with i + j even are counted.

## Related Topics

Bitwise Operations, XOR, Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

