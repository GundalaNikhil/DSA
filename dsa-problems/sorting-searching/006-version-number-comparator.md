# Version Number Comparator

**Problem ID:** SORT-006
**Display ID:** 59
**Question Name:** Version Number Comparator
**Slug:** version-number-comparator
**Title:** Search in Rotated Sorted Array
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Array, Binary Search

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is rotated at an unknown pivot index k such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]. Given the rotated array nums and an integer target, return the index of target if it is in nums, or -1 if it is not.

## A Simple Scenario (Daily Life Usage)

Your software maintains version numbers in a sorted list: [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]. After a system update and database rotation, the list now looks like: [3.0, 3.5, 4.0, 1.0, 1.5, 2.0, 2.5]. You need to find version 1.5 in this rotated list. A modified binary search can locate it efficiently without checking every element.

## Your Task

Write a function that searches for a target value in a rotated sorted array in O(log n) time complexity.

## Why is it Important?

This problem teaches you:

- Modified binary search techniques
- Handling rotated/shifted data
- Multiple condition checking
- Pivot point identification

## Examples

### Example 1:

**Input:** `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`
**Output:** `4`
**Explanation:** 0 is found at index 4.

### Example 2:

**Input:** `nums = [4, 5, 6, 7, 0, 1, 2], target = 3`
**Output:** `-1`
**Explanation:** 3 does not exist in the array.

### Example 3:

**Input:** `nums = [1], target = 0`
**Output:** `-1`
**Explanation:** Single element array, target not found.

## Constraints

- 1 ≤ nums.length ≤ 5000
- -10^4 ≤ nums[i] ≤ 10^4
- All values in nums are unique
- nums is rotated at some pivot
- -10^4 ≤ target ≤ 10^4
- Must achieve O(log n) time complexity

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Google
- Apple

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
