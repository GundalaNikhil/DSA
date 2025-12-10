# Stock Portfolio Rebalancer

**Problem ID:** ARR-005
**Display ID:** 5
**Question Name:** Stock Portfolio Rebalancer
**Slug:** stock-portfolio-rebalancer
**Title:** Rotate Array for Portfolio Adjustment
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Array, In-place Algorithm

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an array representing your stock portfolio positions and a number k, rotate the array to the right by k positions. This represents rebalancing your portfolio.

## A Simple Scenario (Daily Life Usage)

Imagine your investment portfolio as a circular list. Each month, you want to shift focus to different sectors (rotate). If you have [Tech, Healthcare, Energy, Finance] and rotate by 2, it becomes [Energy, Finance, Tech, Healthcare] - your new priority order!

## Your Task

Rotate the array in-place (using O(1) extra space) to the right by k steps.

## Why is it Important?

This problem teaches you:

- In-place array manipulation
- Modular arithmetic
- Space optimization techniques
- Reversal algorithms

## Examples

### Example 1:

**Input:** `portfolio = [100, 200, 300, 400, 500], k = 2`
**Output:** `[400, 500, 100, 200, 300]`
**Explanation:**

- Rotate 1 step right: [500, 100, 200, 300, 400]
- Rotate 2 steps right: [400, 500, 100, 200, 300]

### Example 2:

**Input:** `portfolio = [10, 20, 30], k = 4`
**Output:** `[30, 10, 20]`
**Explanation:** k = 4 is same as k = 1 (since 4 % 3 = 1)

### Example 3:

**Input:** `portfolio = [1], k = 0`
**Output:** `[1]`
**Explanation:** No rotation needed.

## Constraints

- 1 ≤ portfolio.length ≤ 10^5
- -10^6 ≤ portfolio[i] ≤ 10^6
- 0 ≤ k ≤ 10^5
- Must solve in O(1) extra space

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Goldman Sachs
- Morgan Stanley
- Bloomberg
- Charles Schwab

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
