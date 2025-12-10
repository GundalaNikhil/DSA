# Coin Change Machine

**Problem ID:** DP-003
**Display ID:** 44
**Question Name:** Coin Change Machine
**Slug:** coin-change-machine
**Title:** Coin Change
**Difficulty:** Medium
**Premium:** No
**Tags:** Dynamic Programming, Array, Breadth-First Search, Greedy

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## A Simple Scenario (Daily Life Usage)

Imagine you're programming a vending machine that needs to dispense change. You want to give customers the minimum number of coins possible. For example, if someone needs 11 cents back and you have pennies (1¢), nickels (5¢), and dimes (10¢), the optimal way is to give 1 dime and 1 penny (2 coins) instead of 11 pennies. This keeps your coin hopper from running out and makes transactions faster!

## Your Task

Write a function that takes an array of coin denominations and a target amount, then returns the minimum number of coins needed to make that amount. If it's impossible, return -1.

## Why is it Important?

This problem teaches you how to:

- Apply dynamic programming to combinatorial problems
- Understand the difference between greedy and optimal solutions
- Build solutions from smaller subproblems
- Optimize for minimum resource usage
- Handle edge cases where no solution exists

## Examples

### Example 1:

**Input:** `coins = [2, 3, 7], amount = 13`
**Output:** `3`
**Explanation:** 11 = 5 + 5 + 1 (3 coins)

### Example 2:

**Input:** `coins = [3\], amount = 5`
**Output:** `-1`
**Explanation:** Amount 3 cannot be made up with only coins of denomination 2.

### Example 3:

**Input:** `coins = [1\], amount = 0`
**Output:** `0`
**Explanation:** No coins are needed to make amount 0.

### Example 4:

**Input:** `coins = [1, 5, 10, 25], amount = 63`
**Output:** `6`
**Explanation:** 63 = 25 + 25 + 10 + 1 + 1 + 1 (6 coins)

## Constraints

- 1 ≤ coins.length ≤ 12
- 1 ≤ coins[i] ≤ 2^31 - 1
- 0 ≤ amount ≤ 10^4

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Coinbase
- Square
- PayPal
- Stripe

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
