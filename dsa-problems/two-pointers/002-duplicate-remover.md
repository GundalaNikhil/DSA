# Duplicate Remover

**Problem ID:** TP-002
**Display ID:** 67
**Question Name:** Duplicate Remover
**Slug:** duplicate-remover
**Title:** Remove Duplicates from Sorted Array
**Difficulty:** Easy
**Premium:** No
**Tags:** Array, Two Pointers, In-place

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

**Input:** `nums = [1,1,2]`
**Output:** `2, nums = [1,2,_]`
**Explanation:** Your function should return length = 2, with the first two elements being 1 and 2.

### Example 2:

**Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`
**Output:** `5, nums = [0,1,2,3,4,_,_,_,_,_]`
**Explanation:** The first 5 elements contain the unique values in order.

### Example 3:

**Input:** `nums = [1,2,3]`
**Output:** `3, nums = [1,2,3]`
**Explanation:** No duplicates exist, all elements remain.

## Constraints

- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order
- You must modify the array in-place with O(1) extra space

## Asked by Companies

- Amazon
- Microsoft
- Google
- Adobe
