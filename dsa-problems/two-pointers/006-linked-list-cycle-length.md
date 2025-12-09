# Happy Number

**Problem ID:** TP-006
**Display ID:** 71
**Question Name:** Happy Number
**Slug:** happy-number
**Title:** Happy Number
**Difficulty:** Easy
**Premium:** No
**Tags:** Math, Two Pointers, Hash Table

## Problem Description

Write an algorithm to determine if a number is "happy". A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the process until the number equals 1 (happy), or it loops endlessly in a cycle (not happy).

## A Simple Scenario (Daily Life Usage)

Think of this like a math game you play while waiting. You take a number, square each digit and add them up. For example, with 19: 1^2 + 9^2 = 82. Then 8^2 + 2^2 = 68. Keep going until you either reach 1 (you win!) or start seeing the same numbers repeat (you're stuck in a loop).

## Your Task

Write a function that determines if a number is happy. Return true if it reaches 1, false if it gets stuck in a cycle.

## Why is it Important?

This problem teaches you:

- Cycle detection using two pointers (Floyd's algorithm)
- Mathematical sequence analysis
- Efficient loop detection without extra space
- Pattern recognition in number sequences

## Examples

### Example 1:

**Input:** `n = 19`
**Output:** `true`
**Explanation:**
- 1^2 + 9^2 = 82
- 8^2 + 2^2 = 68
- 6^2 + 8^2 = 100
- 1^2 + 0^2 + 0^2 = 1 (Happy!)

### Example 2:

**Input:** `n = 2`
**Output:** `false`
**Explanation:** The sequence enters a cycle and never reaches 1.

### Example 3:

**Input:** `n = 7`
**Output:** `true`
**Explanation:**
- 7^2 = 49
- 4^2 + 9^2 = 97
- 9^2 + 7^2 = 130
- Eventually reaches 1.

## Constraints

- 1 <= n <= 2^31 - 1
- Must detect cycles efficiently
- Can use either hash set or two-pointer approach
- Process continues until reaching 1 or detecting a cycle

## Asked by Companies

- Amazon
- Google
- Microsoft
- Facebook
