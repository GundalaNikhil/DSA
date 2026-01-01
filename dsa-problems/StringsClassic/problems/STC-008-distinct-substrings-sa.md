---
problem_id: STC_DISTINCT_SUBSTRINGS_SA__9517
display_id: STC-008
slug: distinct-substrings-sa
title: "Distinct Substrings Count via SA/LCP"
difficulty: Medium
difficulty_score: 46
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-008: Distinct Substrings Count via SA/LCP

## Problem Statement

Given a string `s`, compute the number of distinct substrings. Use the formula:

```
count = n*(n+1)/2 - sum(LCP)
```

where `LCP` is the array of longest common prefixes between adjacent suffixes in suffix array order.

![Problem Illustration](../images/STC-008/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single integer: number of distinct substrings

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
aaa
```

**Output:**

```
3
```

**Explanation:**

Distinct substrings are "a", "aa", "aaa".

![Example Visualization](../images/STC-008/example-1.png)

## Notes

- Build suffix array and LCP array
- Use 64-bit arithmetic for the total count
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Suffix Array, LCP, Counting

---

## Solution Template
### Java


### Python


### C++


### JavaScript

