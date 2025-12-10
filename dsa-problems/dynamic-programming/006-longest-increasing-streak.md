# Longest Increasing Streak

**Problem ID:** DP-006
**Display ID:** 47
**Question Name:** Longest Increasing Streak
**Slug:** longest-increasing-streak
**Title:** Longest Increasing Subsequence
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Dynamic Programming, Binary Search, Array, Greedy, Patience Sorting

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## A Simple Scenario (Daily Life Usage)

Imagine you're building a fitness app that tracks a user's running distances over time. You want to find the longest streak of improvement - days where each run is longer than the previous one in your selected sequence. For example, if someone ran [10, 9, 2, 5, 3, 7, 101, 18] km, the longest improving trajectory is [2, 3, 7, 101] with a length of 4. This helps identify genuine progress patterns and motivate users!

## Your Task

Write a function that takes an array of integers and returns the length of the longest strictly increasing subsequence. Note that the elements don't need to be consecutive in the original array.

## Why is it Important?

This problem teaches you how to:

- Apply dynamic programming to sequence problems
- Use binary search for optimization (O(n log n) solution)
- Understand the difference between subarray and subsequence
- Implement patience sorting algorithms
- Track optimal solutions across multiple choices

## Examples

### Example 1:

**Input:** `nums = [15, 12, 4, 8, 6, 11, 150, 25]`
**Output:** `4`
**Explanation:** The longest increasing subsequence is [4, 6, 11, 150] or [4, 8, 11, 150], therefore the length is 4.

### Example 2:

**Input:** `nums = [2, 5, 2, 7, 4, 9]`
**Output:** `4`
**Explanation:** One possible longest increasing subsequence is [2, 5, 7, 9] or [2, 4, 7, 9].

### Example 3:

**Input:** `nums = [8, 8, 8, 8, 8]`
**Output:** `1`
**Explanation:** The longest increasing subsequence is just any single element [8].

### Example 4:

**Input:** `nums = [3, 6, 9, 12, 15, 7, 18, 10, 13]`
**Output:** `6`
**Explanation:** One possible longest increasing subsequence is [3, 6, 9, 12, 15, 18] with length 6.

## Constraints

- 1 ≤ nums.length ≤ 2500
- -10^4 ≤ nums[i] ≤ 10^4

## Follow-up

Can you come up with an algorithm that runs in O(n log n) time complexity?

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Microsoft
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
