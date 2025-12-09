# Stock Trading Optimizer

**Problem ID:** DP-004
**Display ID:** 45
**Question Name:** Stock Trading Optimizer
**Slug:** stock-trading-optimizer
**Title:** Best Time to Buy and Sell Stock
**Difficulty:** Easy
**Premium:** No
**Tags:** Array, Dynamic Programming, Greedy, Kadane's Algorithm

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

**Input:** `prices = [7, 1, 5, 3, 6, 4]`
**Output:** `5`
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2:

**Input:** `prices = [7, 6, 4, 3, 1]`
**Output:** `0`
**Explanation:** In this case, no transactions are done and the max profit = 0.

### Example 3:

**Input:** `prices = [2, 4, 1, 7, 5, 11]`
**Output:** `10`
**Explanation:** Buy on day 3 (price = 1) and sell on day 6 (price = 11), profit = 11 - 1 = 10.

## Constraints

- 1 ≤ prices.length ≤ 10^5
- 0 ≤ prices[i] ≤ 10^4

## Asked by Companies

- Amazon
- Microsoft
- Google
- Facebook
