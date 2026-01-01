---
problem_id: BIT_MAX_SUBARRAY_XOR_START__8405
display_id: BIT-005
slug: max-subarray-xor-with-start
title: "Max Subarray XOR With Start"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Prefix Sum
tags:
  - bitwise
  - xor
  - trie
  - prefix-xor
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-005: Max Subarray XOR With Start

## Problem Statement

Given an array of integers and a fixed starting index `s`, find the subarray `a[s...k]` (where `k >= s`) that has the maximum XOR sum.

![Problem Illustration](../images/BIT-005/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer s (0-based)

## Output Format

Print the maximum XOR of a subarray starting at s.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
4
3 8 2 6
1
```

**Output:**

```
12
```

**Explanation:**

The subarray [8, 2, 6] has XOR 12, which is the maximum among subarrays starting at 1.

![Example Visualization](../images/BIT-005/example-1.png)

## Notes

- Index s is 0-based.
- The subarray must start at s but can end at any index >= s.

## Related Topics

Bitwise Operations, XOR, Trie

---

## Solution Template

### Java


### Python


### C++


### JavaScript

