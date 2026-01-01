---
problem_id: STK_LAB_MIXED_BRACKET_REPAIR__7391
display_id: STK-002
slug: lab-mixed-bracket-repair
title: "Lab Mixed Bracket Repair"
difficulty: Easy
difficulty_score: 34
topics:
  - Stack
  - Brackets
  - Greedy
tags:
  - stack
  - brackets
  - greedy
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-002: Lab Mixed Bracket Repair

## Problem Statement

A string contains brackets from `()[]{}` and wildcards `?`. Each `?` can be replaced by any single bracket character. Determine if there exists a replacement so that the final string is balanced and well-nested.

Output `true` if possible, otherwise `false`.

![Problem Illustration](../images/STK-002/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `true` or `false`

## Constraints

- `1 <= |s| <= 100000`
- `s` contains only `()[]{}` and `?`

## Example

**Input:**

```
(?[?])??
```

**Output:**

```
true
```

**Explanation:**

One valid replacement is `([[]])()`, which is balanced and well-nested.

![Example Visualization](../images/STK-002/example-1.png)

## Notes

- Use a stack to match bracket types
- Treat `?` as flexible to fix mismatches greedily
- The final string length must be even
- Time complexity: O(n)

## Related Topics

Stack, Bracket Matching, Greedy

---

## Solution Template
### Java


### Python


### C++


### JavaScript

