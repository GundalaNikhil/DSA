# Calendar Day Finder

**Problem ID:** MATH-003
**Display ID:** 110
**Question Name:** Calendar Day Finder
**Slug:** calendar-day-finder
**Title:** Find Day of Week for Any Date
**Difficulty:** Medium
**Premium:** No
**Tags:** Math, Number Theory, Modular Arithmetic, Calendar Algorithms

## Problem Description

You are implementing a calendar feature that needs to determine what day of the week any given date falls on. Given a date in the format (year, month, day), use Zeller's Congruence algorithm to calculate the day of week. Return the day as a string: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or "Saturday".

Zeller's Formula (simplified):
h = (day + ⌊13(month+1)/5⌋ + year + ⌊year/4⌋ - ⌊year/100⌋ + ⌊year/400⌋) mod 7

Where h=0 is Saturday, h=1 is Sunday, etc.
Note: January and February are counted as months 13 and 14 of the previous year.

## A Simple Scenario (Daily Life Usage)

Imagine you're building a meeting scheduler app like Calendly. When someone tries to book a meeting for "March 15, 2024", your app needs to automatically show that it's a Friday. This helps users avoid accidentally scheduling important meetings on weekends. A project manager scheduling a team standup would see that March 15, 2024 is Friday and know it's a valid workday.

## Your Task

Write a function that takes year, month (1-12), and day (1-31) as integers and returns the day of the week as a string. Implement Zeller's Congruence algorithm correctly, handling the special cases for January and February.

## Why is it Important?

This problem teaches you how to:

- Implement mathematical algorithms for date calculations
- Work with modular arithmetic in practical applications
- Handle edge cases with month numbering
- Understand the mathematics behind calendar systems
- Optimize integer division operations

## Examples

### Example 1:

**Input:** `year = 2024, month = 3, day = 15`
**Output:** `"Friday"`
**Explanation:** March 15, 2024 falls on a Friday. Using Zeller's formula confirms this.

### Example 2:

**Input:** `year = 2000, month = 1, day = 1`
**Output:** `"Saturday"`
**Explanation:** January 1, 2000 was a Saturday (Y2K day!). Remember: January counts as month 13 of 1999 in Zeller's formula.

### Example 3:

**Input:** `year = 1995, month = 8, day = 15`
**Output:** `"Tuesday"`
**Explanation:** August 15, 1995 fell on a Tuesday.

### Example 4:

**Input:** `year = 2025, month = 12, day = 25`
**Output:** `"Thursday"`
**Explanation:** Christmas Day 2025 will be a Thursday.

## Constraints

- 1600 ≤ year ≤ 9999 (Gregorian calendar era)
- 1 ≤ month ≤ 12
- 1 ≤ day ≤ 31
- Assume all input dates are valid (no February 30, etc.)
- Must use integer arithmetic only (no date libraries)

## Follow-up

Can you modify your solution to also handle dates before year 1600? What changes would you need to make for the Julian calendar?

## Asked by Companies

- Google Calendar
- Apple Calendar
- Microsoft Outlook
- Calendly
- Doodle
- When I Work
