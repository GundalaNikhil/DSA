# Water Container Maximizer

**Problem ID:** TP-001
**Display ID:** 66
**Question Name:** Water Container Maximizer
**Slug:** water-container-maximizer
**Title:** Container With Most Water
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Two Pointers, Greedy

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given an array of integers where each value represents the height of a vertical line at that position. Find two lines that together with the x-axis form a container that can hold the most water.

## A Simple Scenario (Daily Life Usage)

Imagine you're designing a water tank for a building. You have vertical walls of different heights, and you need to find which two walls would create the largest water storage capacity. The width between the walls and the height of the shorter wall determine how much water you can store.

## Your Task

Write a function that takes an array of heights and returns the maximum area of water that can be contained between any two walls.

## Why is it Important?

This problem teaches you:

- Two-pointer technique for optimization
- Greedy algorithm principles
- Area calculation and maximization
- Efficient space-time tradeoffs

## Examples

### Example 1:

**Input:** `height = [3, 9, 4, 2, 6, 5, 9, 2, 8]`
**Output:** `56`
**Explanation:** The walls at index 1 (height 9) and index 8 (height 8) form a container with area = 7 * 8 = 56.

### Example 2:

**Input:** `height = [2, 2]`
**Output:** `2`
**Explanation:** Only two walls available, area = 1 * 2 = 2.

### Example 3:

**Input:** `height = [6, 4, 3, 2, 1, 5]`
**Output:** `25`
**Explanation:** The walls at index 0 (height 6) and index 5 (height 5) form area = 5 * 5 = 25.

## Constraints

- 2 <= height.length <= 10^5
- 0 <= height[i] <= 10^4
- Area calculation: width * min(height[left], height[right])

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Microsoft
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
