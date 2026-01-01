---
problem_id: BIT_SUBSET_AND_EQUALS_X__8410
display_id: BIT-010
slug: subset-and-equals-x
title: "Subset AND Equals X"
difficulty: Medium
difficulty_score: 52
topics:
  - Bitwise Operations
  - AND
  - Subset
  - Dynamic Programming
tags:
  - bitwise
  - and-operation
  - subset
  - dp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-010: Subset AND Equals X

## Problem Statement

Given an array of integers and a target `X`, count the number of non-empty subsets such that the bitwise AND of the subset elements is exactly `X`.

![Problem Illustration](../images/BIT-010/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer X

## Output Format

Print the number of non-empty subsets with AND equal to X.

## Constraints

- `1 <= n <= 20`
- `0 <= a[i], X <= 1000000`

## Example

**Input:**

```
3
6 4 2
2
```

**Output:**

```
2
```

**Explanation:**

The subsets [6, 2] and [2] have AND equal to 2.

![Example Visualization](../images/BIT-010/example-1.png)

## Notes

- The empty subset does not count.
- Use 64-bit integers for the count.

## Related Topics

Bitwise Operations, DP, Subsets

---

## Solution Template

### Java


### Python


### C++


### JavaScript

