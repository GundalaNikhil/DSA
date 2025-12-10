# Movie Seat Allocator

**Problem ID:** ARR-004
**Display ID:** 4
**Question Name:** Movie Seat Allocator
**Slug:** movie-seat-allocator
**Title:** Find Longest Consecutive Available Seats
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Sliding Window

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are given an array representing theater seats where 0 means available and 1 means occupied. Find the longest sequence of consecutive available seats.

## A Simple Scenario (Daily Life Usage)

You're booking movie tickets for your friend group. You want everyone to sit together. The system shows which seats are taken (1) and available (0). You need to find the longest stretch of empty seats so your group can sit together.

## Your Task

Given a binary array, find the length of the longest consecutive sequence of zeros (available seats).

## Why is it Important?

This problem teaches you:

- Consecutive sequence detection
- State tracking while iterating
- Real-world booking system logic
- Optimal subarray problems

## Examples

### Example 1:

**Input:** `seats = [1, 0, 0, 0, 1, 0, 0, 1]`
**Output:** `3`
**Explanation:** The longest sequence of available seats is from index 1-3 (3 seats).

### Example 2:

**Input:** `seats = [0, 0, 0, 0, 0]`
**Output:** `5`
**Explanation:** All seats are available.

### Example 3:

**Input:** `seats = [1, 1, 0, 1, 0, 0, 1]`
**Output:** `2`
**Explanation:** The longest sequence is at indices 4-5 (2 seats).

## Constraints

- 1 ≤ seats.length ≤ 5000
- seats[i] is either 0 or 1
- At least one seat exists in the array

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- BookMyShow
- Ticketmaster
- Fandango
- AMC Theatres

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
