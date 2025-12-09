# Non-overlapping Intervals

**Problem ID:** GRDY-003
**Display ID:** 80
**Question Name:** Activity Selection Planner
**Slug:** activity-selection-planner
**Title:** Non-overlapping Intervals
**Difficulty:** Medium
**Premium:** No
**Tags:** Greedy, Sorting, Interval, Dynamic Programming

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

- Amazon
- Google
- Microsoft
- Airbnb
