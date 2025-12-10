# Train Platform Scheduling

**Problem ID:** GRDY-004
**Display ID:** 81
**Question Name:** Minimum Platform Problem
**Slug:** minimum-platform-problem
**Title:** Train Platform Scheduling
**Difficulty:** Medium
**Premium:** No
**Tags:** Greedy, Sorting, Two Pointers, Array

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits. You are given two arrays: `arrival[i]` represents the arrival time of the ith train, and `departure[i]` represents the departure time of the ith train.

## A Simple Scenario (Daily Life Usage)

Imagine you're managing a busy railway station. Throughout the day, multiple trains arrive and depart. Each train needs a platform while it's at the station (from arrival to departure). You need to determine the minimum number of platforms required so that no train has to wait for a platform. For example, if one train is at platform 1 from 9:00-9:15 and another arrives at 9:10 and leaves at 9:30, you need a second platform since they overlap.

## Your Task

Write a function that takes two arrays representing arrival and departure times and returns the minimum number of platforms required.

## Why is it Important?

This problem teaches you how to:

- Apply greedy algorithms to real-world scheduling problems
- Use sorting and two-pointer techniques effectively
- Handle overlapping interval optimization
- Solve resource allocation problems efficiently
- Understand the relationship between events and resource usage

## Examples

### Example 1:

**Input:** `arrival = [900, 940, 950, 1100, 1500, 1800]`, `departure = [910, 1200, 1120, 1130, 1900, 2000]`
**Output:** `3`
**Explanation:**
- At 900: train 1 arrives (1 platform needed)
- At 910: train 1 departs (0 platforms needed)
- At 940: train 2 arrives (1 platform needed)
- At 950: train 3 arrives (2 platforms needed)
- At 1100: train 4 arrives (3 platforms needed) ← Maximum
- At 1120: train 3 departs (2 platforms needed)
- At 1130: train 4 departs (1 platform needed)
Maximum 3 platforms needed simultaneously.

### Example 2:

**Input:** `arrival = [900, 1100, 1235]`, `departure = [1000, 1200, 1240]`
**Output:** `1`
**Explanation:** All trains arrive and depart without overlap, so only 1 platform is needed.

### Example 3:

**Input:** `arrival = [100, 200, 300]`, `departure = [200, 300, 400]`
**Output:** `1`
**Explanation:** Each train departs exactly when the next arrives, so 1 platform can be reused.

## Constraints

- 1 ≤ n ≤ 50000
- 0 ≤ arrival[i] < departure[i] ≤ 2359
- Times are in 24-hour format (HHMM)

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Indian Railways
- Amtrak
- Uber
- Google

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
