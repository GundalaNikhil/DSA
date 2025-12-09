# Water Container Maximizer

**Problem ID:** TP-001
**Display ID:** 66
**Question Name:** Water Container Maximizer
**Slug:** water-container-maximizer
**Title:** Container With Most Water
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Two Pointers, Greedy

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

**Input:** `height = [1,8,6,2,5,4,8,3,7]`
**Output:** `49`
**Explanation:** The vertical lines at index 1 (height 8) and index 8 (height 7) form a container with area = 7 * 7 = 49.

### Example 2:

**Input:** `height = [1,1]`
**Output:** `1`
**Explanation:** Only two walls available, area = 1 * 1 = 1.

### Example 3:

**Input:** `height = [4,3,2,1,4]`
**Output:** `16`
**Explanation:** The walls at index 0 (height 4) and index 4 (height 4) form area = 4 * 4 = 16.

## Constraints

- 2 <= height.length <= 10^5
- 0 <= height[i] <= 10^4
- Area calculation: width * min(height[left], height[right])

## Asked by Companies

- Amazon
- Google
- Microsoft
- Facebook
