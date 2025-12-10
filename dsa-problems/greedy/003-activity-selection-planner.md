# Non-overlapping Intervals

**Problem ID:** GRDY-003
**Display ID:** 80
**Question Name:** Activity Selection Planner
**Slug:** activity-selection-planner
**Title:** Non-overlapping Intervals
**Difficulty:** Medium
**Premium:** No
**Tags:** Greedy, Sorting, Interval, Dynamic Programming

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an array of intervals where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

## A Simple Scenario (Daily Life Usage)

Imagine you're a personal assistant managing your client's busy schedule. They've double-booked and triple-booked several appointments, and now you need to cancel the minimum number of meetings to ensure no appointments overlap. For example, if they have meetings at 9-11 AM, 10-12 PM, and 11-1 PM, you'd need to cancel at least one meeting (probably the middle one) to avoid conflicts.

## Your Task

Write a function that takes an array of intervals and returns the minimum number of intervals that need to be removed to eliminate all overlaps.

## Why is it Important?

This problem teaches you how to:

- Apply greedy algorithm strategies to interval problems
- Understand the activity selection problem pattern
- Use sorting to optimize decision-making
- Recognize when greedy choices lead to optimal solutions
- Handle edge cases with interval comparisons

## Examples

### Example 1:

**Input:** `intervals = [[1,2],[2,3],[3,4],[1,3]]`
**Output:** `1`
**Explanation:** Remove [1,3] to make the rest non-overlapping: [1,2], [2,3], [3,4].

### Example 2:

**Input:** `intervals = [[1,2],[1,2],[1,2]]`
**Output:** `2`
**Explanation:** Remove 2 intervals to keep only one [1,2].

### Example 3:

**Input:** `intervals = [[1,2],[2,3]]`
**Output:** `0`
**Explanation:** No overlaps exist, so no removal needed.

## Constraints

- 1 ≤ intervals.length ≤ 10^5
- intervals[i].length == 2
- -5 * 10^4 ≤ starti < endi ≤ 5 * 10^4

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Microsoft
- Airbnb

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
