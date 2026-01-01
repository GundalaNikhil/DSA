---
problem_id: STK_CAMPUS_EXPRESSION_OPTIMIZER__4085
display_id: STK-012
slug: campus-expression-optimizer
title: "Campus Expression Optimizer"
difficulty: Medium
difficulty_score: 58
topics:
  - Stack
  - Parsing
  - Expressions
tags:
  - stack
  - infix
  - postfix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-012: Campus Expression Optimizer

## Problem Statement

Convert an infix expression to postfix. The expression contains single-letter operands, digits, operators `+ - * / % ^`, and parentheses.

Additionally:

- Detect syntax errors (mismatched parentheses or consecutive operators)
- Count redundant parenthesis pairs

Output the postfix expression or an error message, plus the redundant count.

![Problem Illustration](../images/STK-012/problem-illustration.png)

## Input Format

- First line: string `expr`

## Output Format

- If valid: one line `POSTFIX <postfix> <redundant_count>`
- If invalid: one line `ERROR <message> 0`

## Constraints

- `1 <= |expr| <= 10000`
- Operands are single uppercase letters or digits

## Example

**Input:**

```
A*((B+C)/D)
```

**Output:**

```
POSTFIX ABC+D/* 1
```

**Explanation:**

The outer parentheses are redundant; the postfix expression is `ABC+D/*`.

![Example Visualization](../images/STK-012/example-1.png)

## Notes

- Use operator stack with precedence and associativity
- Track previous token to detect invalid sequences
- Redundant parentheses enclose a single operand or have no effect
- Time complexity: O(n)

## Related Topics

Infix to Postfix, Stack, Parsing

---

## Solution Template
### Java


### Python


### C++


### JavaScript

