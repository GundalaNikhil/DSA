---
problem_id: STK_CIRCUIT_POSTFIX_VARIABLES__7493
display_id: STK-011
slug: circuit-postfix-variables
title: "Circuit Postfix Evaluator with Variables"
difficulty: Medium
difficulty_score: 55
topics:
  - Stack
  - Expression Evaluation
  - Parsing
tags:
  - stack
  - postfix
  - parsing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-011: Circuit Postfix Evaluator with Variables

## Problem Statement

Evaluate a postfix expression with integers, operators `+ - * / %`, single-letter variables, and two extra stack operations:

- `DUP`: duplicate the top value
- `SWAP`: swap the top two values

A variable map provides values for letters. All operations are performed modulo `MOD = 1000000007`. Division uses integer division after modulo normalization.

![Problem Illustration](../images/STK-011/problem-illustration.png)

## Input Format

- First line: integer `t` (number of tokens)
- Second line: `t` space-separated tokens
- Third line: integer `m` (number of variables)
- Next `m` lines: `char value` pairs

## Output Format

- Single integer: evaluation result modulo `MOD`

## Constraints

- `1 <= t <= 10000`
- `0 <= m <= 26`
- Variable values fit in 64-bit signed integer

## Example

**Input:**

```
5
x 5 + y *
2
x 3
y 2
```

**Output:**

```
16
```

**Explanation:**

(3 + 5) * 2 = 16.

![Example Visualization](../images/STK-011/example-1.png)

## Notes

- Push numbers or variable values
- Apply modulo after each operation
- `DUP` and `SWAP` operate on the stack directly
- Assume the expression is valid

## Related Topics

Postfix Evaluation, Stack, Parsing

---

## Solution Template
### Java


### Python


### C++


### JavaScript

