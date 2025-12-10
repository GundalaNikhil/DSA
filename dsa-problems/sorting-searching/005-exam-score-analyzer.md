# Exam Score Analyzer

**Problem ID:** SORT-005
**Display ID:** 58
**Question Name:** Exam Score Analyzer
**Slug:** exam-score-analyzer
**Title:** Sort Colors
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Two Pointers, Sorting

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an array with n objects colored red, white, or blue (represented by integers 0, 1, and 2), sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. You must solve this problem without using the library's sort function and in a single pass (one iteration through the array).

## A Simple Scenario (Daily Life Usage)

You're a teacher grading exams with three categories: Failed (0), Passed (1), and Excellent (2). Students' scores come in random order: [2,0,1,2,1,0]. You need to organize them into groups - all failures together, all passes together, all excellent together - to analyze performance. Instead of sorting with complex algorithms, you can do this in one pass using the Dutch National Flag algorithm: [0,0,1,1,2,2].

## Your Task

Write a function that sorts an array containing only 0s, 1s, and 2s in-place using a single pass through the array.

## Why is it Important?

This problem teaches you:

- Dutch National Flag algorithm
- Three-way partitioning
- In-place array manipulation
- Single-pass optimization techniques

## Examples

### Example 1:

**Input:** `nums = [2, 0, 2, 1, 1, 0]`
**Output:** `[0, 0, 1, 1, 2, 2]`
**Explanation:** All 0s first, then 1s, then 2s.

### Example 2:

**Input:** `nums = [2, 0, 1]`
**Output:** `[0, 1, 2]`
**Explanation:** Sorted in one pass.

### Example 3:

**Input:** `nums = [0]`
**Output:** `[0]`
**Explanation:** Single element, already sorted.

## Constraints

- n == nums.length
- 1 ≤ n ≤ 300
- nums[i] is either 0, 1, or 2
- Must solve in O(n) time with constant space
- Must be done in a single pass

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Bloomberg
- Amazon
- Microsoft
- Adobe

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
