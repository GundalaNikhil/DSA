# Meeting Room Scheduler

**Problem ID:** SORT-002
**Display ID:** 55
**Question Name:** Meeting Room Scheduler
**Slug:** meeting-room-scheduler
**Title:** Merge Intervals
**Difficulty:** Medium
**Premium:** No
**Tags:** Array, Sorting, Intervals

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

## A Simple Scenario (Daily Life Usage)

You're managing a calendar application. A user has scheduled multiple meetings: 9-11am, 10-12pm, 1-3pm, and 2-4pm. Some meetings overlap! To show clear available time blocks, you need to merge the overlapping meetings: 9-12pm (merged first two) and 1-4pm (merged last two). This gives a cleaner view of busy time blocks.

## Your Task

Write a function that takes an array of time intervals and merges all overlapping intervals into consolidated blocks.

## Why is it Important?

This problem teaches you:

- Interval manipulation techniques
- Sorting as a preprocessing step
- Merging and comparison logic
- Real-world scheduling algorithms

## Examples

### Example 1:

**Input:** `intervals = [[1,3], [2,6], [8,10], [15,18]]`
**Output:** `[[1,6], [8,10], [15,18]]`
**Explanation:** Intervals [1,3] and [2,6] overlap, so they merge into [1,6].

### Example 2:

**Input:** `intervals = [[1,4], [4,5]]`
**Output:** `[[1,5]]`
**Explanation:** Intervals [1,4] and [4,5] are considered overlapping (touching at boundary).

### Example 3:

**Input:** `intervals = [[1,4], [0,2], [3,5]]`
**Output:** `[[0,5]]`
**Explanation:** After sorting by start time: [0,2], [1,4], [3,5]. All three overlap and merge into [0,5].

## Constraints

- 1 ≤ intervals.length ≤ 10^4
- intervals[i].length == 2
- 0 ≤ start_i ≤ end_i ≤ 10^4

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google Calendar
- Microsoft Outlook
- Calendly
- Zoom

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
