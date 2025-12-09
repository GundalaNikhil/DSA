# Package Delivery Tracker

**Problem ID:** SORT-004
**Display ID:** 57
**Question Name:** Package Delivery Tracker
**Slug:** package-delivery-tracker
**Title:** First Bad Version
**Difficulty:** Easy
**Premium:** No
**Tags:** Binary Search, Interactive

## Problem Description

You are a product manager and currently leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Given n versions [1, 2, ..., n], find the first bad version that caused all the following ones to be bad. You have access to an API `isBadVersion(version)` which returns whether version is bad.

## A Simple Scenario (Daily Life Usage)

Your company ships packages in batches numbered 1 to 1000. Quality control discovers that starting from a certain batch, all packages are defective due to a machine malfunction. Batch 1-456 are good, but batch 457 onwards are all bad. Instead of checking every single batch sequentially, you can use binary search: check batch 500 (bad), then 250 (good), then 375 (good), then 437 (good), then 468 (bad), and so on, until you pinpoint batch 457 as the first bad one.

## Your Task

Write a function to find the first bad version. Minimize the number of API calls to `isBadVersion`.

## Why is it Important?

This problem teaches you:

- Binary search on abstract problems
- API call optimization
- Minimizing expensive operations
- Real-world debugging scenarios

## Examples

### Example 1:

**Input:** `n = 5, bad = 4`
**Output:** `4`
**Explanation:**
```
Call isBadVersion(3) -> false
Call isBadVersion(5) -> true
Call isBadVersion(4) -> true
Therefore, 4 is the first bad version.
```

### Example 2:

**Input:** `n = 1, bad = 1`
**Output:** `1`
**Explanation:** Only one version exists and it's bad.

### Example 3:

**Input:** `n = 1000, bad = 457`
**Output:** `457`
**Explanation:** Binary search finds the first defective batch efficiently.

## Constraints

- 1 ≤ bad ≤ n ≤ 2^31 - 1
- Minimize calls to isBadVersion API

## Asked by Companies

- Google
- Amazon
- Microsoft
- Facebook
