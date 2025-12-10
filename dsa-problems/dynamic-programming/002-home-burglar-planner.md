# Home Burglar Planner

**Problem ID:** DP-002
**Display ID:** 43
**Question Name:** Home Burglar Planner
**Slug:** home-burglar-planner
**Title:** House Robber
**Difficulty:** Medium
**Premium:** No
**Tags:** Dynamic Programming, Array, Optimization, Decision Making

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a row. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money at each house, return the maximum amount of money you can rob tonight without alerting the police.

## A Simple Scenario (Daily Life Usage)

Think of this as an optimal decision-making puzzle rather than actual robbery! Imagine you're collecting prizes along a game board where you can't pick two adjacent prizes. Or think of it as scheduling tasks where you can't do consecutive ones - what's the maximum value you can achieve? For example, with prizes [2, 7, 9, 3, 1], you'd pick 7 and 9 and 1 (skipping adjacent ones) for a total of 12.

## Your Task

Write a function that takes an array of non-negative integers representing the value at each house and returns the maximum amount you can rob without robbing two adjacent houses.

## Why is it Important?

This problem teaches you how to:

- Apply dynamic programming to optimization problems
- Make optimal decisions with constraints
- Understand the concept of state transitions
- Balance greedy vs. optimal solutions
- Solve problems with dependency constraints

## Examples

### Example 1:

**Input:** `nums = [3, 5, 2, 8]`
**Output:** `11`
**Explanation:** Rob house 1 (money = 3) and then rob house 4 (money = 8). Total amount = 3 + 8 = 11.

### Example 2:

**Input:** `nums = [4, 8, 12, 6, 3]`
**Output:** `19`
**Explanation:** Rob house 2 (money = 8), rob house 4 (money = 6) and rob house 5 (money = 3). Total amount = 8 + 6 + 3 = 17. Actually, rob house 1 (4) and house 3 (12) and house 5 (3) = 19.

### Example 3:

**Input:** `nums = [5, 3, 4, 11, 2]`
**Output:** `16`
**Explanation:** Rob house 1 (money = 5) and house 4 (money = 11). Total amount = 5 + 11 = 16.

## Constraints

- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 400

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Facebook
- Bloomberg

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
