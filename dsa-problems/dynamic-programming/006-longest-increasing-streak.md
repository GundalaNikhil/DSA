# Longest Increasing Streak

**Problem ID:** DP-006
**Display ID:** 47
**Question Name:** Longest Increasing Streak
**Slug:** longest-increasing-streak
**Title:** Longest Increasing Subsequence
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Dynamic Programming, Binary Search, Array, Greedy, Patience Sorting

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

**Input:** `nums = [10, 9, 2, 5, 3, 7, 101, 18]`
**Output:** `4`
**Explanation:** The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.

### Example 2:

**Input:** `nums = [0, 1, 0, 3, 2, 3]`
**Output:** `4`
**Explanation:** One possible longest increasing subsequence is [0, 1, 2, 3].

### Example 3:

**Input:** `nums = [7, 7, 7, 7, 7, 7, 7]`
**Output:** `1`
**Explanation:** The longest increasing subsequence is just any single element [7].

### Example 4:

**Input:** `nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]`
**Output:** `6`
**Explanation:** One possible longest increasing subsequence is [1, 3, 4, 5, 6] or [1, 3, 6, 7, 9, 10] - wait, that's not valid! The correct answer has length 6: [1, 3, 6, 7, 9, 10].

## Constraints

- 1 ≤ nums.length ≤ 2500
- -10^4 ≤ nums[i] ≤ 10^4

## Follow-up

Can you come up with an algorithm that runs in O(n log n) time complexity?

## Asked by Companies

- Amazon
- Google
- Microsoft
- Facebook
