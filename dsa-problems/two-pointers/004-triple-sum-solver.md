# Triple Sum Solver

**Problem ID:** TP-004
**Display ID:** 69
**Question Name:** Triple Sum Solver
**Slug:** triple-sum-solver
**Title:** 3Sum
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Two Pointers, Sorting

## Problem Description

Given an array of integers, find all unique triplets in the array that sum to zero. The solution set must not contain duplicate triplets.

## A Simple Scenario (Daily Life Usage)

Three friends went on a trip and shared expenses. Now they need to settle up. If Alice spent $50 extra, Bob spent $30 less, and Charlie spent $20 less (50 + (-30) + (-20) = 0), they're perfectly balanced. You need to find all such balanced groups of three people from your friend circle.

## Your Task

Write a function that finds all unique triplets [a, b, c] in an array where a + b + c = 0. The triplets should be returned in any order, but duplicates should be avoided.

## Why is it Important?

This problem teaches you:

- Combining sorting with two-pointer technique
- Handling duplicate elements efficiently
- Reducing higher complexity problems
- Triple-loop optimization strategies

## Examples

### Example 1:

**Input:** `nums = [-1,0,1,2,-1,-4]`
**Output:** `[[-1,-1,2],[-1,0,1]]`
**Explanation:** The two unique triplets that sum to 0 are [-1,-1,2] and [-1,0,1].

### Example 2:

**Input:** `nums = [0,1,1]`
**Output:** `[]`
**Explanation:** No triplet sums to 0.

### Example 3:

**Input:** `nums = [0,0,0]`
**Output:** `[[0,0,0]]`
**Explanation:** The only triplet is [0,0,0].

## Constraints

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
- Solution set must not contain duplicate triplets
- Order of triplets in output doesn't matter

## Asked by Companies

- Amazon
- Facebook
- Microsoft
- Bloomberg
