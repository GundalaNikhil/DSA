# Ride Share Fare Calculator

**Problem ID:** SW-006
**Display ID:** 77
**Question Name:** Ride Share Fare Calculator
**Slug:** ride-share-fare-calculator
**Title:** Max Consecutive Ones III
**Difficulty:** Medium
**Premium:** No
**Tags:** Sliding Window, Array, Two Pointers

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given a binary array representing driver availability over time slots (1 = available, 0 = unavailable) and an integer K representing the number of unavailable time slots you can convert to available through incentives. Find the maximum number of consecutive available time slots you can achieve.

## A Simple Scenario (Daily Life Usage)

Imagine you're an Uber dispatcher managing driver availability. Each hour is marked as 1 (driver available) or 0 (driver unavailable). You can offer incentives to K drivers to make them available during their off-hours. For example, with availability [1,1,0,0,1,1,1,0,1,1] and K=2 incentives, you can flip two 0s to get the longest consecutive availability period.

## Your Task

Write a function that takes a binary array and K, and returns the maximum number of consecutive 1s you can get by flipping at most K zeros to ones.

## Why is it Important?

This problem teaches you:

- Sliding window with flip/transformation constraint
- Optimizing resource allocation
- Real-world logistics and scheduling
- Maximizing service availability

## Examples

### Example 1:

**Input:** `availability = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`
**Output:** `6`
**Explanation:** Flip the two 0s at indices 9 and 10. The longest sequence of 1s is from index 4 to 10, with length 6.
Actually: [1,1,1,0,0,1,1,1,1,1,1] -> indices 5-10 gives us 6 consecutive 1s.

### Example 2:

**Input:** `availability = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]`, `k = 3`
**Output:** `10`
**Explanation:** Flip the 0s at indices 8, 9, and 10 to get 10 consecutive 1s.

### Example 3:

**Input:** `availability = [0,0,0,1,1,1,0,0]`, `k = 0`
**Output:** `3`
**Explanation:** Without any flips, the longest sequence is [1,1,1] with length 3.

### Example 4:

**Input:** `availability = [1,1,1,1]`, `k = 0`
**Output:** `4`
**Explanation:** All drivers are already available.

## Constraints

- 1 <= availability.length <= 10^5
- availability[i] is either 0 or 1
- 0 <= k <= availability.length
- Binary array represents time slot availability

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Uber
- Lyft
- DoorDash
- Instacart

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
