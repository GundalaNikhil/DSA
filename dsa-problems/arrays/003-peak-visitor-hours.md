# Peak Visitor Hours

**Problem ID:** ARR-003
**Display ID:** 3
**Question Name:** Peak Visitor Hours
**Slug:** peak-visitor-hours
**Title:** Find All Peak Elements in Array
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Peak Finding

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given an array representing the number of visitors to a website each hour. A "peak hour" is an hour where visitor count is greater than both the previous and next hour. Find all peak hours.

## A Simple Scenario (Daily Life Usage)

You run a coffee shop and track customers per hour. Peak hours (like 8 AM when people get morning coffee, or 3 PM during afternoon break) help you schedule more staff. If hour 5 has more customers than hours 4 and 6, it's a peak!

## Your Task

Return an array of indices representing all peak hours. The first and last hours cannot be peaks (they don't have both neighbors).

## Why is it Important?

This problem teaches you:

- Pattern recognition in data
- Boundary condition handling
- Business analytics fundamentals
- Array traversal optimization

## Examples

### Example 1:

**Input:** `visitors = [10, 25, 15, 30, 20, 35, 25, 15]`
**Output:** `[1, 3, 5]`
**Explanation:**

- Hour 1: 25 > 10 and 25 > 15 ✓
- Hour 3: 30 > 15 and 30 > 20 ✓
- Hour 5: 35 > 20 and 35 > 25 ✓

### Example 2:

**Input:** `visitors = [1, 2, 3, 4, 5]`
**Output:** `[]`
**Explanation:** The array is strictly increasing, so no peaks exist.

### Example 3:

**Input:** `visitors = [50, 100, 50, 100, 50]`
**Output:** `[1, 3]`
**Explanation:** Hours 1 and 3 have 100 visitors, which is more than their neighbors.

## Constraints

- 3 ≤ visitors.length ≤ 1000
- 0 ≤ visitors[i] ≤ 10000
- Array represents hourly data

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google Analytics
- Facebook
- LinkedIn
- Salesforce

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
