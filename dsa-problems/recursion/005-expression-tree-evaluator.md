# Evaluate Mathematical Expression Tree

**Problem ID:** REC-005
**Display ID:** 106
**Question Name:** Expression Tree Evaluator
**Slug:** expression-tree-evaluator
**Title:** Evaluate Mathematical Expression Tree
**Difficulty:** Medium
**Premium:** No
**Tags:** Recursion, Tree Traversal, Math, Expression Evaluation

## Problem Description

You are building a calculator or compiler. Mathematical expressions can be represented as binary trees where leaf nodes contain numbers and internal nodes contain operators (+, -, *, /). Write a recursive function to evaluate the expression tree and return the final numeric result.

## A Simple Scenario (Daily Life Usage)

When you type "3 + 5 * 2" into a calculator, it doesn't just compute left to right. It builds an expression tree respecting operator precedence: the multiplication happens first (5 * 2 = 10), then the addition (3 + 10 = 13). Compilers and advanced calculators (like Wolfram Alpha, MATLAB, or even spreadsheet formulas in Excel) use expression trees to correctly evaluate complex mathematical expressions.

## Your Task

Write a recursive function that takes an expression tree and returns the evaluated result. Each node is either:
- A **leaf node** with a `value` property (number)
- An **operator node** with an `operator` property (+, -, *, /) and `left` and `right` child nodes

Evaluate the tree using post-order traversal: recursively evaluate left subtree, then right subtree, then apply the operator.

## Why is it Important?

This problem teaches you how to:

- Apply recursion to evaluate expressions
- Use post-order tree traversal
- Build calculators and expression parsers
- Understand how compilers process mathematical operations

## Examples

### Example 1:

**Input:**
```javascript
{
  operator: '+',
  left: { value: 3 },
  right: {
    operator: '*',
    left: { value: 5 },
    right: { value: 2 }
  }
}
```
**Output:** `13`
**Explanation:**
- Evaluate left: 3
- Evaluate right: 5 * 2 = 10
- Apply operator: 3 + 10 = 13
- This represents: 3 + (5 * 2)

### Example 2:

**Input:**
```javascript
{
  operator: '-',
  left: {
    operator: '*',
    left: { value: 10 },
    right: { value: 2 }
  },
  right: { value: 5 }
}
```
**Output:** `15`
**Explanation:**
- Left subtree: 10 * 2 = 20
- Right subtree: 5
- Apply operator: 20 - 5 = 15
- This represents: (10 * 2) - 5

### Example 3:

**Input:**
```javascript
{
  operator: '/',
  left: {
    operator: '+',
    left: { value: 20 },
    right: { value: 10 }
  },
  right: { value: 5 }
}
```
**Output:** `6`
**Explanation:**
- Left: 20 + 10 = 30
- Right: 5
- Result: 30 / 5 = 6
- This represents: (20 + 10) / 5

### Example 4:

**Input:**
```javascript
{ value: 42 }
```
**Output:** `42`
**Explanation:** Single leaf node just returns its value.

### Example 5:

**Input:**
```javascript
{
  operator: '*',
  left: {
    operator: '+',
    left: { value: 2 },
    right: { value: 3 }
  },
  right: {
    operator: '-',
    left: { value: 10 },
    right: { value: 4 }
  }
}
```
**Output:** `30`
**Explanation:**
- Left: 2 + 3 = 5
- Right: 10 - 4 = 6
- Result: 5 * 6 = 30
- This represents: (2 + 3) * (10 - 4)

## Constraints

- 1 ≤ total nodes in tree ≤ 1,000
- -1000 ≤ leaf node values ≤ 1000
- Operators: +, -, *, / only
- Division is integer division (truncate toward zero)
- No division by zero in test cases
- Tree depth ≤ 20 levels

## Asked by Companies

- Wolfram (Mathematica)
- MathWorks (MATLAB)
- Desmos
- Symbolab
- Khan Academy
- Google (Calculator)
- Microsoft (Excel)
