# Coupon Code Validator

**Problem ID:** HASH-001
**Display ID:** 36
**Question Name:** Coupon Code Validator
**Slug:** coupon-code-validator
**Title:** First Non-Repeating Character
**Difficulty:** Easy
**Premium:** No
**Tags:** Hash Table, String, Counting

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a string representing a batch of coupon codes, find the first character that appears only once. If no such character exists, return an empty string or special character.

## A Simple Scenario (Daily Life Usage)

You work at an e-commerce company processing coupon activation codes. Each code should have a unique identifier character that helps validate authenticity. When analyzing a batch of codes, you need to quickly identify the first character that appears only once - this could be the unique activation marker that prevents fraud.

## Your Task

Write a function that takes a string and returns the first non-repeating character. If all characters repeat or the string is empty, return an appropriate indicator.

## Why is it Important?

This problem teaches you:

- Hash table usage for character frequency counting
- Single-pass string traversal techniques
- Order preservation in data structures
- Real-world application in validation systems

## Examples

### Example 1:

**Input:** `codes = "discount"`
**Output:** `"d"`
**Explanation:** 'd' is the first character that appears only once.

### Example 2:

**Input:** `codes = "blackfriday"`
**Output:** `"l"`
**Explanation:** 'l' is the first non-repeating character.

### Example 3:

**Input:** `codes = "aabb"`
**Output:** `""`
**Explanation:** All characters repeat, so return empty string.

## Constraints

- 1 ≤ codes.length ≤ 100,000
- codes consists of only lowercase English letters
- Must preserve order of first occurrence

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Shopify
- eBay
- Etsy

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
