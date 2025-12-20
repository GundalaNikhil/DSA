---
problem_id: STR_CYCLIC_SHIFT_EQUALITY_CLASSES__1015
display_id: STR-015
slug: cyclic-shift-equality-classes
title: "Cyclic Shift Equality Classes"
difficulty: Medium
difficulty_score: 40
topics:
  - String Manipulation
  - Hashing
  - Equivalence Relations
tags:
  - rotation-equivalence
  - canonical-form
  - booth-algorithm
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-015: Cyclic Shift Equality Classes

## Problem Statement

Given `n` strings, group them into equivalence classes where two strings are equivalent if one is a cyclic shift (rotation) of the other. Return the number of equivalence classes.

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5)
- Next n lines: One string per line (each length ≤ 20)

## Output Format

- A single integer representing the number of equivalence classes

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- Each string length ≤ 20

## Example 1

**Input:**

```
5
ab
ba
abc
bca
cab
```

**Output:**

```
2
```

**Explanation:**

- Class 1: {"ab", "ba"} (rotations of each other)
- Class 2: {"abc", "bca", "cab"} (rotations of each other)

## Example 2

**Input:**

```
3
aaa
aaa
bbb
```

**Output:**

```
2
```

**Explanation:**

- Class 1: {"aaa", "aaa"}
- Class 2: {"bbb"}

## Notes

- Use minimal rotation (Booth's algorithm) as canonical form
- Hash canonical forms to count unique classes
- O(n × m) time where m is max string length
