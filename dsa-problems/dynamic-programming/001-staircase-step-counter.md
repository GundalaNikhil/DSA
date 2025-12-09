# Staircase Step Counter

**Problem ID:** DP-001
**Display ID:** 42
**Question Name:** Staircase Step Counter
**Slug:** staircase-step-counter
**Title:** Climbing Stairs
**Difficulty:** Easy
**Premium:** No
**Tags:** Dynamic Programming, Math, Memoization, Fibonacci

## Problem Description

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## A Simple Scenario (Daily Life Usage)

Imagine you're climbing the stairs to your bedroom every night. You can either take one step at a time or skip a step and take two at once. How many different ways can you reach your bedroom if there are n stairs? For example, with 3 stairs, you could go: (1+1+1), (1+2), or (2+1) - that's 3 different ways!

## Your Task

Write a function that takes a positive integer n representing the number of stairs and returns the number of distinct ways to climb to the top.

## Why is it Important?

This problem teaches you how to:

- Recognize and apply dynamic programming patterns
- Understand the relationship between Fibonacci sequences and real-world problems
- Optimize recursive solutions with memoization
- Break down complex problems into smaller subproblems
- Apply mathematical thinking to combinatorial problems

## Examples

### Example 1:

**Input:** `n = 2`
**Output:** `2`
**Explanation:** There are two ways to climb to the top:
1. 1 step + 1 step
2. 2 steps

### Example 2:

**Input:** `n = 3`
**Output:** `3`
**Explanation:** There are three ways to climb to the top:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

### Example 3:

**Input:** `n = 5`
**Output:** `8`
**Explanation:** There are eight distinct ways to climb 5 stairs using combinations of 1 and 2 steps.

## Constraints

- 1 ≤ n ≤ 45
- The answer is guaranteed to fit in a 32-bit integer

## Asked by Companies

- Google
- Amazon
- Adobe
- Apple
