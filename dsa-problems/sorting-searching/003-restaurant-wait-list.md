# Restaurant Wait List

**Problem ID:** SORT-003
**Display ID:** 56
**Question Name:** Restaurant Wait List
**Slug:** restaurant-wait-list
**Title:** Kth Largest Element
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Divide and Conquer, Sorting, Heap, QuickSelect

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an unsorted array of integers, find the kth largest element. Note that it is the kth largest element in sorted order, not the kth distinct element.

## A Simple Scenario (Daily Life Usage)

You manage a restaurant's waitlist system. Throughout the day, customers have different wait times (in minutes): 45, 12, 67, 23, 89, 34, 56. Your manager wants to know the 3rd longest wait time to identify problem patterns. Instead of fully sorting all wait times, you can find just the 3rd largest value (56 minutes) more efficiently.

## Your Task

Write a function that finds the kth largest element in an unsorted array without necessarily sorting the entire array.

## Why is it Important?

This problem teaches you:

- QuickSelect algorithm (partition-based selection)
- Heap data structure usage
- Time-space complexity tradeoffs
- Partial sorting techniques

## Examples

### Example 1:

**Input:** `nums = [3, 2, 1, 5, 6, 4], k = 2`
**Output:** `5`
**Explanation:** Sorted array is [1, 2, 3, 4, 5, 6]. The 2nd largest element is 5.

### Example 2:

**Input:** `nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4`
**Output:** `4`
**Explanation:** Sorted array is [1, 2, 2, 3, 3, 4, 5, 5, 6]. The 4th largest element is 4.

### Example 3:

**Input:** `nums = [45, 12, 67, 23, 89, 34, 56], k = 3`
**Output:** `56`
**Explanation:** The 3rd longest wait time is 56 minutes.

## Constraints

- 1 ≤ k ≤ nums.length ≤ 10^4
- -10^4 ≤ nums[i] ≤ 10^4

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Facebook
- LinkedIn
- Apple

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
