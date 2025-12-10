# Stock Trading Optimizer

**Problem ID:** DP-004
**Display ID:** 45
**Question Name:** Stock Trading Optimizer
**Slug:** stock-trading-optimizer
**Title:** Best Time to Buy and Sell Stock
**Difficulty:** Easy
**Premium:** No
**Tags:** Array, Dynamic Programming, Greedy, Kadane's Algorithm

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## A Simple Scenario (Daily Life Usage)

Imagine you have a time machine that shows you all the stock prices for a company over several days. You can buy the stock once and sell it once at a later date. What's the best profit you can make? For example, if the prices are [7, 1, 5, 3, 6, 4], you'd buy when the price is 1 and sell when it's 6, making a profit of 5. This is like finding the best timing for any buy-low-sell-high scenario!

## Your Task

Write a function that takes an array of stock prices (one per day) and returns the maximum profit you can achieve by buying once and selling once. You must buy before you sell, and if no profit is possible, return 0.

## Why is it Important?

This problem teaches you how to:

- Track minimum and maximum values efficiently
- Apply dynamic programming and greedy approaches
- Understand Kadane's algorithm for maximum subarray problems
- Make optimal decisions with temporal constraints
- Optimize single-pass array algorithms

## Examples

### Example 1:

**Input:** `prices = [9, 2, 6, 4, 8, 5]`
**Output:** `6`
**Explanation:** Buy on day 2 (price = 2) and sell on day 5 (price = 8), profit = 8 - 2 = 6.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2:

**Input:** `prices = [10, 8, 6, 4, 2]`
**Output:** `0`
**Explanation:** Prices only decrease, so no profitable transactions are possible. Max profit = 0.

### Example 3:

**Input:** `prices = [3, 5, 2, 9, 6, 12]`
**Output:** `10`
**Explanation:** Buy on day 3 (price = 2) and sell on day 6 (price = 12), profit = 12 - 2 = 10.

## Constraints

- 1 ≤ prices.length ≤ 10^5
- 0 ≤ prices[i] ≤ 10^4

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Google
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
