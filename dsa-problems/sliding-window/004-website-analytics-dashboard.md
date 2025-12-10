# Website Analytics Dashboard

**Problem ID:** SW-004
**Display ID:** 75
**Question Name:** Website Analytics Dashboard
**Slug:** website-analytics-dashboard
**Title:** Minimum Window Substring
**Difficulty:** Hard
**Premium:** Yes
**Tags:** Sliding Window, Hash Table, String

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are analyzing user journey paths on a website. Given a string representing all page visits and a target pattern of required pages, find the minimum window in the visit sequence that contains all pages from the target pattern.

## A Simple Scenario (Daily Life Usage)

Imagine you're a Google Analytics engineer tracking user behavior. You need to find the shortest path where a user visited all critical pages (like "home", "product", "cart", "checkout"). If the user path is "homeaboutproductblogcartcontactcheckout" and you need ["home", "product", "cart", "checkout"], you want to find the shortest substring containing all these page visits.

## Your Task

Write a function that takes a string S (page visits) and a string T (required pages), and returns the minimum window substring of S that contains all characters of T. If no such window exists, return an empty string.

## Why is it Important?

This problem teaches you:

- Advanced sliding window with two pointers
- Hash table for character frequency matching
- Optimizing user experience analysis
- Understanding conversion funnel optimization

## Examples

### Example 1:

**Input:** `s = "HOMEPRODUCTCARTCHECKOUT"`, `t = "HPC"`
**Output:** `"HOMEPRODUCTC"`
**Explanation:** The minimum window substring "HOMEPRODUCTC" includes 'H', 'P', and 'C' from the required pages.

### Example 2:

**Input:** `s = "LANDINGPAGE"`, `t = "LG"`
**Output:** `"LANDINAG"`
**Explanation:** The minimum window contains both required page identifiers 'L' and 'G'.

### Example 3:

**Input:** `s = "ABOUTBLOG"`, `t = "AAB"`
**Output:** `""`
**Explanation:** Two 'A's are required but the string only has one 'A', so return empty string.

### Example 4:

**Input:** `s = "SEARCHFILTERPRODUCTSEARCH"`, `t = "SSPF"`
**Output:** `"SEARCHFILTERPRODUCTS"`
**Explanation:** The minimum window must contain two 'S's, one 'P', and one 'F'.

## Constraints

- 1 <= s.length, t.length <= 10^5
- s and t consist of uppercase and lowercase English letters
- A valid answer is guaranteed to be unique
- Follow up: Can you find an algorithm that runs in O(m + n) time?

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google Analytics
- Mixpanel
- Amplitude
- Segment

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
