# Lottery Probability Calculator

**Problem ID:** MATH-001
**Display ID:** 108
**Question Name:** Lottery Probability Calculator
**Slug:** lottery-probability-calculator
**Title:** Calculate Lottery Winning Odds
**Difficulty:** Easy
**Premium:** No
**Tags:** Math, Combinations, Probability, Number Theory

## Problem Description

You are building a lottery odds calculator that determines the probability of winning based on the total number of balls and how many need to be selected. Given `n` total balls and `k` balls to pick, calculate the number of possible combinations using the combination formula: C(n,k) = n! / (k! * (n-k)!)

## A Simple Scenario (Daily Life Usage)

Imagine you're at a convenience store deciding whether to buy a lottery ticket. The lottery requires picking 6 numbers from 1 to 49. Before spending your money, you want to know your actual odds. Your calculator will show you there are 13,983,816 possible combinations - helping you make an informed decision about whether the $2 ticket is worth it!

## Your Task

Write a function that takes the total number of balls `n` and the number of selections `k`, then returns the total number of possible combinations. Implement the combination formula efficiently without causing integer overflow.

## Why is it Important?

This problem teaches you how to:

- Implement mathematical combinations efficiently
- Handle large factorials without overflow
- Understand probability theory fundamentals
- Optimize calculations by canceling terms early
- Apply number theory to real-world gambling scenarios

## Examples

### Example 1:

**Input:** `n = 5, k = 3`
**Output:** `10`
**Explanation:** Selecting 3 balls from 5 gives us: C(5,3) = 5!/(3!*2!) = 120/(6*2) = 10 possible combinations.

### Example 2:

**Input:** `n = 49, k = 6`
**Output:** `13983816`
**Explanation:** This is the classic lottery format. C(49,6) = 13,983,816 possible combinations. Odds of winning: 1 in 13,983,816!

### Example 3:

**Input:** `n = 10, k = 2`
**Output:** `45`
**Explanation:** Picking 2 from 10: C(10,2) = 10!/(2!*8!) = (10*9)/(2*1) = 45 combinations.

### Example 4:

**Input:** `n = 7, k = 7`
**Output:** `1`
**Explanation:** Only one way to select all 7 balls from 7 total.

## Constraints

- 1 ≤ k ≤ n ≤ 60
- Result will fit in a 64-bit integer
- Do not use built-in combination functions

## Asked by Companies

- Scientific Games
- IGT (International Game Technology)
- FanDuel
- DraftKings
- Camelot Group
- Lottery.com
