# Temperature Fluctuation Analyzer

**Problem ID:** ARR-001
**Display ID:** 1
**Question Name:** Temperature Fluctuation Analyzer
**Slug:** temperature-fluctuation-analyzer
**Title:** Find Maximum Temperature Drop
**Difficulty:** Easy
**Premium:** No
**Tags:** Array, Simulation, Math

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given an array of integers representing daily temperatures (in Celsius) for a week. Find the maximum temperature drop between any two consecutive days.

## A Simple Scenario (Daily Life Usage)

Imagine you're a weather forecaster planning outdoor events. You need to warn people about sudden temperature drops so they can dress appropriately. For example, if Monday was 25°C and Tuesday is 15°C, that's a 10-degree drop - people should bring warmer clothes!

## Your Task

Write a function that takes an array of temperatures and returns the maximum drop between consecutive days. If temperatures only increase or stay the same, return 0.

## Why is it Important?

This problem teaches you how to:

- Iterate through arrays efficiently
- Track running comparisons
- Handle edge cases in data analysis
- Apply algorithmic thinking to real-world weather patterns

## Examples

### Example 1:

**Input:** `temperatures = [22, 25, 19, 15, 20, 18, 21]`
**Output:** `6`
**Explanation:** The maximum drop occurs from day 2 (25°C) to day 3 (19°C), which is a drop of 6°C.

### Example 2:

**Input:** `temperatures = [15, 18, 20, 23, 26]`
**Output:** `0`
**Explanation:** Temperatures only increase, so there's no drop.

### Example 3:

**Input:** `temperatures = [30, 30, 28, 28, 25]`
**Output:** `3`
**Explanation:** The maximum drop is from 28°C to 25°C, which is 3 degrees.

## Constraints

- 2 ≤ temperatures.length ≤ 365
- -50 ≤ temperatures[i] ≤ 50
- All temperatures are in Celsius

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Weather.com
- AccuWeather
- IBM Watson
- Google Cloud

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
