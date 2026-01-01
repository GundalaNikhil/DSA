---
problem_id: HSH_MINIMAL_ROTATION_HASH__4729
display_id: HSH-006
slug: minimal-rotation-hash
title: "Minimal Rotation via Hash Compare"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Rotation
tags:
  - hashing
  - rotation
  - lexicographic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-006: Minimal Rotation via Hash Compare

## Problem Statement

Given a string `s`, find its lexicographically smallest rotation using hashing and binary search for comparison.

A rotation of a string is obtained by moving some prefix to the end. For example, rotations of "abc" are: "abc", "bca", "cab".

![Problem Illustration](../images/HSH-006/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single line: lexicographically smallest rotation of `s`

## Constraints

- `1 <= |s| <= 2*10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
bba
```

**Output:**

```
abb
```

**Explanation:**

String: "bba"

All rotations:

- "bba" (start at index 0)
- "bab" (start at index 1)
- "abb" (start at index 2) ← lexicographically smallest

Output: "abb"

![Example Visualization](../images/HSH-006/example-1.png)

## Notes

- Concatenate s with itself to simulate all rotations
- Use hashing with binary search to compare rotations efficiently
- For each starting position, determine lexicographic order using hash comparison
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

String Rotation, Hashing, Binary Search, Lexicographic Order

---

## Solution Template

### Java


### Python


### C++


### JavaScript

