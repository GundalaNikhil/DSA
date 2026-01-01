---
problem_id: REC_EXPRESSION_TARGET_ONE_FLIP__9316
display_id: REC-009
slug: expression-target-one-flip
title: "Expression Target With One Negation Flip"
difficulty: Medium
difficulty_score: 57
topics:
  - Recursion
  - Backtracking
  - Expressions
tags:
  - recursion
  - backtracking
  - expressions
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-009: Expression Target With One Negation Flip

## Problem Statement

Given a digit string `s`, insert `+` or `-` operators between digits or concatenate digits to form an expression that evaluates to `T`.

You may also apply a unary negation to at most one operand chunk (write it with a leading `-` without adding an operator). Use at most `c` binary operators in total.

Return all valid expressions in lexicographic order. If none exist, output `NONE`.

![Problem Illustration](../images/REC-009/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `T`
- Third line: integer `c`

## Output Format

- Each valid expression on its own line, in lexicographic order
- Output `NONE` if no expression matches

## Constraints

- `1 <= |s| <= 10`
- `0 <= c <= 9`
- `-10^9 <= T <= 10^9`
- No chunk may have leading zeros unless the chunk is exactly `"0"`

## Example

**Input:**

```
1203
-202
2
```

**Output:**

```
1+-203
```

**Explanation:**

Split into `1` and `203`, insert `+`, and apply the unary flip to `203`: `1 + (-203) = -202`.

![Example Visualization](../images/REC-009/example-1.png)

## Notes

- Track current value, previous operator count, and whether a flip has been used
- Avoid leading-zero chunks
- The unary flip applies to a chosen chunk only once
- Backtracking is required to explore all splits

## Related Topics

Backtracking, Expression Evaluation, Recursion

---

## Solution Template
### Java


### Python


### C++


### JavaScript

