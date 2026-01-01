---
problem_id: BIT_DISTINCT_SUBARRAY_XORS__8412
display_id: BIT-012
slug: distinct-subarray-xors
title: "Distinct Subarray XORs"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Subarray
  - Trie
tags:
  - bitwise
  - xor
  - subarray
  - trie
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-012: Distinct Subarray XORs

## Problem Statement

Count the number of **distinct** values obtained by XORing elements of all possible subarrays of `a`.

![Problem Illustration](../images/BIT-012/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the number of distinct subarray XOR values.

## Constraints

- `1 <= n <= 10000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
3
1 2 3
```

**Output:**

```
4
```

**Explanation:**

The distinct XORs across all subarrays are {0, 1, 2, 3}.

![Example Visualization](../images/BIT-012/example-1.png)

## Notes

- The total number of subarrays is n \* (n + 1) / 2.
- Use a set to track distinct XOR results.

## Related Topics

Bitwise Operations, Prefix XOR

---

## Solution Template

### Java


### Python


### C++


### JavaScript

