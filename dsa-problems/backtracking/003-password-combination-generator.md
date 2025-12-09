# Password Combination Generator

**Problem ID:** BACK-003
**Display ID:** 62
**Question Name:** Password Combination Generator
**Slug:** password-combination-generator
**Title:** Permutations
**Difficulty:** Medium
**Premium:** No
**Tags:** Backtracking, Array, Recursion

## Problem Description

Given an array of distinct integers, return all possible permutations. You can return the answer in any order.

## A Simple Scenario (Daily Life Usage)

Imagine you're setting up a security system that needs to generate all possible PIN codes from a set of digits. For example, if you have the digits [1, 2, 3], you need to know all possible arrangements: 123, 132, 213, 231, 312, 321. This is useful for testing password strength, generating test cases, or understanding the total number of possible combinations.

## Your Task

Write a function that takes an array of distinct integers and returns all possible permutations of those numbers.

## Why is it Important?

This problem teaches you how to:

- Master backtracking for permutation generation
- Understand factorial time complexity
- Use swap-based or choice-based backtracking
- Handle state management in recursive solutions
- Generate all possible orderings systematically

## Examples

### Example 1:

**Input:** `nums = [1,2,3]`
**Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
**Explanation:** There are 3! = 6 permutations of three distinct numbers.

### Example 2:

**Input:** `nums = [0,1]`
**Output:** `[[0,1],[1,0]]`
**Explanation:** Two numbers have 2! = 2 permutations.

### Example 3:

**Input:** `nums = [1]`
**Output:** `[[1]]`
**Explanation:** A single number has only one permutation - itself.

### Example 4:

**Input:** `nums = [1,2,3,4]`
**Output:** `[[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1],[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]]`
**Explanation:** Four numbers have 4! = 24 permutations.

## Constraints

- 1 ≤ nums.length ≤ 6
- -10 ≤ nums[i] ≤ 10
- All the integers of nums are unique

## Asked by Companies

- Amazon
- Microsoft
- Google
- Facebook
- LinkedIn
- Apple

## Hints

1. Use backtracking to build permutations one element at a time
2. Track which elements have been used in the current permutation
3. When the current permutation length equals the input length, add it to results
4. Two approaches: swap-based (modify in place) or choice-based (build new arrays)
5. Time complexity is O(n! × n) as there are n! permutations, each taking O(n) to copy
