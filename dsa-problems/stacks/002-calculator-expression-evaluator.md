# Calculator Expression Evaluator

**Problem ID:** STK-002
**Display ID:** 19
**Question Name:** Calculator Expression Evaluator
**Slug:** calculator-expression-evaluator
**Title:** Evaluate Reverse Polish Notation
**Difficulty:** Medium
**Premium:** No
**Tags:** Stack, Math, Expression Evaluation

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are +, -, *, and /. Each operand may be an integer or another expression. Division between two integers should truncate toward zero.

## A Simple Scenario (Daily Life Usage)

You're designing a scientific calculator like those made by Texas Instruments or HP. Many advanced calculators use RPN because it's more efficient and doesn't require parentheses. Instead of typing "3 + 4", users type "3 4 +" - numbers first, then the operation. Your calculator needs to evaluate these expressions correctly.

## Your Task

Write a function that takes an array of strings representing an RPN expression and returns the calculated result.

## Why is it Important?

This problem teaches you:

- Stack-based expression evaluation
- Postfix notation processing
- Calculator logic implementation
- Order of operations without parentheses

## Examples

### Example 1:

**Input:** `tokens = ["3", "2", "+", "4", "*"]`
**Output:** `9`
**Explanation:** ((2 + 1) * 3) = 9. First add 2 and 1 to get 3, then multiply by 3.

### Example 2:

**Input:** `tokens = ["5", "15", "3", "/", "+"]`
**Output:** `6`
**Explanation:** (4 + (13 / 5)) = 6. First divide 13 by 5 to get 2 (truncated), then add 4.

### Example 3:

**Input:** `tokens = ["12", "8", "10", "4", "+", "-15", "*", "/", "*", "20", "+", "6", "+"]`
**Output:** `22`
**Explanation:** Complex expression demonstrating multiple operations in sequence.

### Example 4:

**Input:** `tokens = ["5", "6", "+"]`
**Output:** `7`
**Explanation:** Simple addition: 3 + 4 = 7.

## Constraints

- 1 ≤ tokens.length ≤ 10,000
- tokens[i] is either an operator ("+", "-", "*", "/") or an integer in the range [-200, 200]
- The given RPN expression is always valid
- The result and all intermediate calculations fit in a 32-bit integer
- Division truncates toward zero

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Texas Instruments
- Casio
- HP Calculators
- Wolfram Alpha

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
