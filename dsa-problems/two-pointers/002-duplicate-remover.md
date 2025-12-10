# Duplicate Remover

**Problem ID:** TP-002
**Display ID:** 67
**Question Name:** Duplicate Remover
**Slug:** duplicate-remover
**Title:** Remove Duplicates from Sorted Array
**Difficulty:** Easy
**Premium:** No
**Tags:** Array, Two Pointers, In-place

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a sorted array, remove the duplicates in-place such that each unique element appears only once. Return the new length of the array. You must do this with O(1) extra space.

## A Simple Scenario (Daily Life Usage)

You're cleaning up your phone's contact list that's sorted alphabetically. You notice many duplicate entries (maybe synced from different accounts). Instead of creating a new list, you want to remove duplicates directly from the existing list to save memory.

## Your Task

Write a function that removes duplicates from a sorted array in-place and returns the count of unique elements. The relative order should be maintained.

## Why is it Important?

This problem teaches you:

- In-place array modification techniques
- Two-pointer pattern for array manipulation
- Space-efficient algorithms
- Working with sorted data structures

## Examples

### Example 1:

**Input:** `nums = [3,3,5]`
**Output:** `2, nums = [3,5,_]`
**Explanation:** Your function should return length = 2, with the first two elements being 3 and 5.

### Example 2:

**Input:** `nums = [2,2,4,4,4,6,6,8,8,9]`
**Output:** `5, nums = [2,4,6,8,9,_,_,_,_,_]`
**Explanation:** The first 5 elements contain the unique values in order.

### Example 3:

**Input:** `nums = [2,5,7]`
**Output:** `3, nums = [2,5,7]`
**Explanation:** No duplicates exist, all elements remain.

## Constraints

- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order
- You must modify the array in-place with O(1) extra space

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Google
- Adobe

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
