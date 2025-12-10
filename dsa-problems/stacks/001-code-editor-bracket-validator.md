# Code Editor Bracket Validator

**Problem ID:** STK-001
**Display ID:** 18
**Question Name:** Code Editor Bracket Validator
**Slug:** code-editor-bracket-validator
**Title:** Valid Parentheses Checker
**Difficulty:** Easy
**Premium:** No
**Tags:** Stack, String, Parsing

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

## A Simple Scenario (Daily Life Usage)

You're building an IDE like VS Code or IntelliJ. When a developer types code, you need to check if their brackets are properly matched. For example, if they write `function test() { return [1, 2]; }`, all brackets match correctly. But if they write `function test() { return [1, 2; }`, there's a mismatch - the square bracket was never closed!

## Your Task

Write a function that takes a string of brackets and returns true if they are valid, false otherwise.

## Why is it Important?

This problem teaches you:

- Stack data structure fundamentals
- Matching and pairing logic
- Real-world code validation
- LIFO (Last In, First Out) principle

## Examples

### Example 1:

**Input:** `s = "()"`
**Output:** `true`
**Explanation:** The parentheses open and close correctly.

### Example 2:

**Input:** `s = "()[]{}"`
**Output:** `true`
**Explanation:** All three types of brackets are properly matched.

### Example 3:

**Input:** `s = "(]"`
**Output:** `false`
**Explanation:** Opening parenthesis is closed by a square bracket - mismatch!

### Example 4:

**Input:** `s = "([)]"`
**Output:** `false`
**Explanation:** Brackets are interleaved incorrectly. The square bracket closes before the parenthesis.

### Example 5:

**Input:** `s = "{[]}"`
**Output:** `true`
**Explanation:** Properly nested brackets.

## Constraints

- 1 ≤ s.length ≤ 10,000
- s consists of parentheses only: '()[]{}'

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Microsoft (VS Code)
- JetBrains (IntelliJ IDEA)
- Sublime Text
- GitHub (Atom)

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
