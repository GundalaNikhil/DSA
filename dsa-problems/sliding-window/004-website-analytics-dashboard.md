# Website Analytics Dashboard

**Problem ID:** SW-004
**Display ID:** 75
**Question Name:** Website Analytics Dashboard
**Slug:** website-analytics-dashboard
**Title:** Minimum Window Substring
**Difficulty:** Hard
**Premium:** Yes
**Tags:** Sliding Window, Hash Table, String

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

**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`
**Output:** `"BANC"`
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

### Example 2:

**Input:** `s = "a"`, `t = "a"`
**Output:** `"a"`
**Explanation:** The entire string s is the minimum window.

### Example 3:

**Input:** `s = "a"`, `t = "aa"`
**Output:** `""`
**Explanation:** Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.

### Example 4:

**Input:** `s = "ADOBECODEBANCABC"`, `t = "AABC"`
**Output:** `"BANCA"`
**Explanation:** The minimum window must contain two 'A's, one 'B', and one 'C'.

## Constraints

- 1 <= s.length, t.length <= 10^5
- s and t consist of uppercase and lowercase English letters
- A valid answer is guaranteed to be unique
- Follow up: Can you find an algorithm that runs in O(m + n) time?

## Asked by Companies

- Google Analytics
- Mixpanel
- Amplitude
- Segment
