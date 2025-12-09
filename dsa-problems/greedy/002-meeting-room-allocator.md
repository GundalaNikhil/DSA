# Minimum Meeting Rooms

**Problem ID:** GRDY-002
**Display ID:** 79
**Question Name:** Meeting Room Allocator
**Slug:** meeting-room-allocator
**Title:** Minimum Meeting Rooms
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Greedy, Sorting, Heap, Interval

## Problem Description

Given an array of meeting time intervals where `intervals[i] = [starti, endi]`, determine the minimum number of conference rooms required to schedule all meetings without conflicts.

## A Simple Scenario (Daily Life Usage)

Imagine you're an office manager at a tech company. Your team has scheduled multiple meetings throughout the day, and each meeting has a start and end time. You need to figure out the minimum number of conference rooms required so that no two meetings overlap in the same room. For example, if one meeting is from 9-10 AM and another is from 9:30-11 AM, they need separate rooms since they overlap.

## Your Task

Write a function that takes an array of meeting intervals and returns the minimum number of conference rooms needed.

## Why is it Important?

This problem teaches you how to:

- Apply greedy algorithms to scheduling problems
- Use sorting strategically to simplify complex problems
- Work with interval overlap detection
- Implement efficient resource allocation algorithms
- Utilize priority queues (heaps) for optimal solutions

## Examples

### Example 1:

**Input:** `intervals = [[0,30],[5,10],[15,20]]`
**Output:** `2`
**Explanation:**
- Meeting 1: 0-30 needs room 1
- Meeting 2: 5-10 overlaps with meeting 1, needs room 2
- Meeting 3: 15-20 overlaps with meeting 1, can use room 2 (since meeting 2 ended at 10)
Maximum 2 rooms needed at any time.

### Example 2:

**Input:** `intervals = [[7,10],[2,4]]`
**Output:** `1`
**Explanation:** The meetings don't overlap, so only 1 room is needed.

### Example 3:

**Input:** `intervals = [[1,5],[2,6],[3,7],[4,8]]`
**Output:** `4`
**Explanation:** All four meetings overlap at time 4, so 4 rooms are needed.

## Constraints

- 1 ≤ intervals.length ≤ 10^4
- 0 ≤ starti < endi ≤ 10^6

## Asked by Companies

- Google
- Amazon
- Microsoft
- Facebook
