# Parentheses Generator

**Problem ID:** BACK-006
**Display ID:** 65
**Question Name:** Parentheses Generator
**Slug:** parentheses-generator
**Title:** Generate Parentheses
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Backtracking, String, Dynamic Programming

## Problem Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed (valid) parentheses.

## A Simple Scenario (Daily Life Usage)

Imagine you're building a code editor that needs to auto-generate valid bracket patterns for developers. When a programmer types an opening bracket, your tool suggests all possible valid ways to complete the bracket pattern. For example, with 3 pairs of parentheses, you can create: ((())), (()()), (())(), ()(()), ()()().

This is also useful for compilers that need to validate nested structures like function calls, JSON objects, or mathematical expressions.

## Your Task

Write a function that generates all valid combinations of n pairs of parentheses. Each combination must have properly balanced and nested parentheses.

## Why is it Important?

This problem teaches you how to:

- Generate valid sequences using backtracking
- Understand constraint-based generation
- Track running state (open/close counts)
- Optimize with pruning (invalid states)
- Apply backtracking to string building

## Examples

### Example 1:

**Input:** `n = 3`
**Output:** `["((()))","(()())","(())()","()(())","()()()"]`
**Explanation:** All 5 valid combinations of 3 pairs of parentheses.

### Example 2:

**Input:** `n = 1`
**Output:** `["()"]`
**Explanation:** Only one valid combination with 1 pair.

### Example 3:

**Input:** `n = 2`
**Output:** `["(())","()()"]`
**Explanation:** Two valid combinations with 2 pairs.

### Example 4:

**Input:** `n = 4`
**Output:** `["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]`
**Explanation:** All 14 valid combinations of 4 pairs (Catalan number C₄ = 14).

## Constraints

- 1 ≤ n ≤ 8

## Asked by Companies

- Google
- Amazon
- Microsoft
- Facebook
- Bloomberg
- Uber

## Hints

1. Track the count of open and close parentheses added so far
2. Only add '(' if we haven't used all n opening parentheses
3. Only add ')' if it doesn't exceed the number of '(' used
4. When both counts reach n, add the valid combination to results
5. The number of valid combinations is the nth Catalan number: C(n) = (2n)! / ((n+1)! × n!)
6. Use backtracking to build strings incrementally
