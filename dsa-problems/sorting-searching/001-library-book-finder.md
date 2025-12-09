# Library Book Finder

**Problem ID:** SORT-001
**Display ID:** 54
**Question Name:** Library Book Finder
**Slug:** library-book-finder
**Title:** Binary Search
**Difficulty:** Easy
**Premium:** No
**Tags:** Binary Search, Array, Search

## Problem Description

Given a sorted array of integers and a target value, return the index of the target if it exists, otherwise return -1. Implement the solution using binary search algorithm.

## A Simple Scenario (Daily Life Usage)

You're working at a library where books are organized by ID numbers in ascending order. A patron asks for book ID 4523. Instead of checking every book one by one, you open the catalog in the middle. If the middle book's ID is higher than 4523, you know to check the left half; if lower, check the right half. You keep dividing until you find the exact book or determine it doesn't exist.

## Your Task

Write a function that takes a sorted array and a target value, and returns the index of the target using binary search. If the target is not found, return -1.

## Why is it Important?

This problem teaches you:

- Binary search algorithm fundamentals
- Logarithmic time complexity (O(log n))
- Efficient searching in sorted data
- Index manipulation and boundary conditions

## Examples

### Example 1:

**Input:** `nums = [-1, 0, 3, 5, 9, 12], target = 9`
**Output:** `4`
**Explanation:** 9 exists in the array at index 4.

### Example 2:

**Input:** `nums = [-1, 0, 3, 5, 9, 12], target = 2`
**Output:** `-1`
**Explanation:** 2 does not exist in the array.

### Example 3:

**Input:** `nums = [5], target = 5`
**Output:** `0`
**Explanation:** Single element array, target found at index 0.

## Constraints

- 1 ≤ nums.length ≤ 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are unique
- nums is sorted in ascending order

## Asked by Companies

- Google
- Amazon
- Microsoft
- Facebook
