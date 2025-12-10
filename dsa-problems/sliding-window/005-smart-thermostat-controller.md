# Smart Thermostat Controller

**Problem ID:** SW-005
**Display ID:** 76
**Question Name:** Smart Thermostat Controller
**Slug:** smart-thermostat-controller
**Title:** Minimum Size Subarray Sum
**Difficulty:** Medium
**Premium:** No
**Tags:** Sliding Window, Array, Binary Search

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given an array of positive integers representing hourly energy consumption (in kWh) and a target value. Find the minimal length of a contiguous subarray whose sum is greater than or equal to the target. This represents the shortest time period where peak energy usage occurred.

## A Simple Scenario (Daily Life Usage)

Imagine you're designing a Google Nest thermostat that detects energy usage spikes. You need to identify the shortest consecutive time period where total energy usage exceeded a threshold, so you can alert homeowners to optimize their usage. For example, if hourly usage is [2,3,1,2,4,3] and the threshold is 7, the shortest period is [4,3] (2 hours) with a sum of 7.

## Your Task

Write a function that takes an array of energy consumption values and a target, and returns the minimal length of a subarray with sum >= target. Return 0 if no such subarray exists.

## Why is it Important?

This problem teaches you:

- Variable-size sliding window optimization
- Finding minimum/maximum window sizes
- Energy management and smart home systems
- Real-time monitoring and alerting systems

## Examples

### Example 1:

**Input:** `target = 8, consumption = [3,2,4,1,5,2]`
**Output:** `2`
**Explanation:** The subarray [4,3] has the minimal length of 2 with sum >= 7.

### Example 2:

**Input:** `target = 5, consumption = [2,3,3]`
**Output:** `1`
**Explanation:** The subarray [4] has the minimal length of 1.

### Example 3:

**Input:** `target = 12, consumption = [2,2,2,2,2,2,2,2]`
**Output:** `0`
**Explanation:** No subarray has sum >= 11.

### Example 4:

**Input:** `target = 15`, `consumption = [2,3,4,5,6]`
**Output:** `5`
**Explanation:** The entire array [1,2,3,4,5] sums to 15 with length 5.

## Constraints

- 1 <= target <= 10^9
- 1 <= consumption.length <= 10^5
- 1 <= consumption[i] <= 10^4
- All values represent energy in kWh

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google Nest
- Honeywell
- Ecobee
- Amazon

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
