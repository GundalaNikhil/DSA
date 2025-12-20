---
problem_id: STR_CAMPUS_BADGE_NORMALIZE__1001
display_id: STR-001
slug: campus-badge-normalize
title: "Campus Badge Normalize"
difficulty: Easy
difficulty_score: 25
topics:
  - String Manipulation
  - State Machine
tags:
  - string-processing
  - normalization
  - single-pass
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-001: Campus Badge Normalize

## Problem Statement

You are given a string `s` containing alphanumeric characters, spaces, and special characters. Your task is to normalize it according to these rules:

1. Convert all uppercase letters to lowercase
2. Replace any sequence of non-alphanumeric characters with a single hyphen (`-`)
3. Remove leading and trailing hyphens from the result

The normalized string should be suitable for use as a URL slug or identifier.

## Input Format

- A single string `s` (1 ≤ |s| ≤ 2 × 10^5)

## Output Format

- A single string representing the normalized version of `s`

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- Input may contain uppercase letters, lowercase letters, digits, spaces, and special characters

## Example 1

**Input:**
```
Hello__World!!
```

**Output:**
```
hello-world
```

**Explanation:**
- "Hello" → "hello" (lowercase)
- "__" → "-" (collapse to single hyphen)
- "World" → "world" (lowercase)
- "!!" → "-" (collapse, but trailing so removed)
- Final: "hello-world"

## Example 2

**Input:**
```
  Test@123#Code  
```

**Output:**
```
test-123-code
```

**Explanation:**
- Leading spaces removed
- "@" and "#" replaced with "-"
- Trailing spaces removed

## Notes

- Use a state machine or single-pass algorithm for optimal O(n) time complexity
- Be careful with edge cases: all non-alphanumeric, empty result, etc.
