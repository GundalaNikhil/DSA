# Shopping Cart Merger

**Problem ID:** ARR-002
**Display ID:** 2
**Question Name:** Shopping Cart Merger
**Slug:** shopping-cart-merger
**Title:** Merge Two Sorted Shopping Lists
**Difficulty:** Easy
**Premium:** No
**Tags:** Array, Two Pointers, Sorting

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You have two shopping lists, each sorted by item price (ascending order). Merge them into one sorted list maintaining the price order.

## A Simple Scenario (Daily Life Usage)

You and your roommate both created shopping lists on different apps. Both lists show items from cheapest to most expensive. Now you want to combine them into one master list that's still sorted by price so you can budget effectively.

## Your Task

Given two sorted arrays representing item prices, merge them into a single sorted array without using built-in sort functions.

## Why is it Important?

This problem teaches you:

- Two-pointer technique
- Merging sorted data efficiently
- Understanding merge sort fundamentals
- Optimizing space and time complexity

## Examples

### Example 1:

**Input:**

```
list1 = [1.99, 3.50, 5.99, 8.99]
list2 = [2.50, 4.99, 7.25]
```

**Output:** `[1.99, 2.50, 3.50, 4.99, 5.99, 7.25, 8.99]`
**Explanation:** All items are merged and sorted by price.

### Example 2:

**Input:**

```
list1 = []
list2 = [10.99, 15.99]
```

**Output:** `[10.99, 15.99]`
**Explanation:** If one list is empty, return the other list.

### Example 3:

**Input:**

```
list1 = [5.00, 10.00, 15.00]
list2 = [6.00, 11.00, 16.00]
```

**Output:** `[5.00, 6.00, 10.00, 11.00, 15.00, 16.00]`
**Explanation:** Items are interleaved while maintaining sorted order.

## Constraints

- 0 ≤ list1.length, list2.length ≤ 500
- 0.01 ≤ list1[i], list2[i] ≤ 1000.00
- list1 and list2 are sorted in ascending order
- Prices are rounded to 2 decimal places

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Walmart Labs
- Instacart
- Shopify

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
