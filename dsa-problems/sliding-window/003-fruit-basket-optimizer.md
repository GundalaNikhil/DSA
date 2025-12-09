# Fruit Basket Optimizer

**Problem ID:** SW-003
**Display ID:** 74
**Question Name:** Fruit Basket Optimizer
**Slug:** fruit-basket-optimizer
**Title:** Fruits Into Baskets
**Difficulty:** Medium
**Premium:** No
**Tags:** Sliding Window, Hash Table, Array

## Problem Description

You are in an orchard with a row of fruit trees. Each tree produces one type of fruit. You have two baskets, and each basket can only hold one type of fruit. Starting from any tree, you want to collect as many fruits as possible. Find the maximum number of fruits you can collect with your two baskets.

## A Simple Scenario (Daily Life Usage)

Imagine you're working for a fruit harvest company like Instacart planning an orchard pick. You have two baskets, and each can only hold one fruit type (apples or oranges, for example). If you see trees with fruits [1,2,1,2,3,1,1], you can start at position 0 and collect fruits from trees with types 1 and 2, getting [1,2,1,2] for a total of 4 fruits before you hit type 3.

## Your Task

Write a function that takes an array where each element represents a fruit type, and returns the maximum number of fruits you can collect into two baskets.

## Why is it Important?

This problem teaches you:

- Sliding window with constraint (at most 2 types)
- Hash map for counting frequency
- Optimizing harvest and collection operations
- Real-world logistics and planning

## Examples

### Example 1:

**Input:** `fruits = [1,2,1]`
**Output:** `3`
**Explanation:** We can collect all three fruits into two baskets (type 1 and type 2).

### Example 2:

**Input:** `fruits = [0,1,2,2]`
**Output:** `3`
**Explanation:** We can collect [1,2,2]. If we start at index 0, we would only get [0,1].

### Example 3:

**Input:** `fruits = [1,2,3,2,2]`
**Output:** `4`
**Explanation:** We can collect [2,3,2,2], the longest subarray with at most 2 different types.

### Example 4:

**Input:** `fruits = [3,3,3,1,2,1,1,2,3,3,4]`
**Output:** `5`
**Explanation:** We can collect [1,2,1,1,2], which has 5 fruits with only 2 types.

## Constraints

- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
- Each integer represents a different fruit type

## Asked by Companies

- Amazon
- Google
- Facebook
- Instacart
