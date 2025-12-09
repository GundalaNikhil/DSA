# Target Sum Finder

**Problem ID:** TP-003
**Display ID:** 68
**Question Name:** Target Sum Finder
**Slug:** target-sum-finder
**Title:** Two Sum II - Sorted Array
**Difficulty:** Easy
**Premium:** No
**Tags:** Array, Two Pointers, Binary Search

## Problem Description

Given a sorted array of integers and a target sum, find two numbers that add up to the target. Return the indices of these two numbers (1-indexed).

## A Simple Scenario (Daily Life Usage)

You're at lunch with a fixed budget of $15. The menu items are listed by price (sorted). You want to find two items that exactly match your budget. For example, if items cost [2, 3, 5, 7, 11], and your budget is 9, you'd pick items at positions 2 and 4 (3 + 7 = 9).

## Your Task

Write a function that takes a sorted array and a target value, then returns the 1-indexed positions of two numbers that sum to the target. You can assume exactly one solution exists.

## Why is it Important?

This problem teaches you:

- Two-pointer technique on sorted arrays
- Efficient searching without extra space
- Binary search alternatives
- Time complexity optimization

## Examples

### Example 1:

**Input:** `numbers = [2,7,11,15], target = 9`
**Output:** `[1,2]`
**Explanation:** The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2 (1-indexed).

### Example 2:

**Input:** `numbers = [2,3,4], target = 6`
**Output:** `[1,3]`
**Explanation:** The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3.

### Example 3:

**Input:** `numbers = [-1,0], target = -1`
**Output:** `[1,2]`
**Explanation:** The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2.

## Constraints

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- Exactly one solution exists

## Asked by Companies

- Amazon
- Facebook
- Microsoft
- LinkedIn
