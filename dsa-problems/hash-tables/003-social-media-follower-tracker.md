# Social Media Follower Tracker

**Problem ID:** HASH-003
**Display ID:** 38
**Question Name:** Social Media Follower Tracker
**Slug:** social-media-follower-tracker
**Title:** Intersection of Two Arrays
**Difficulty:** Easy
**Premium:** No
**Tags:** Hash Table, Array, Two Pointers, Sorting

## Problem Description

Given two arrays of user IDs, find all users who appear in both arrays. Return the result as an array of unique user IDs.

## A Simple Scenario (Daily Life Usage)

You're building a social media analytics tool. You have two lists: users who follow Account A and users who follow Account B. You want to find all users who follow both accounts - these are highly engaged users who might be interested in collaborative content or cross-promotions.

## Your Task

Write a function that takes two arrays of integers and returns an array containing all elements that appear in both arrays. Each element in the result should be unique.

## Why is it Important?

This problem teaches you:

- Hash set operations for efficient lookups
- Array intersection algorithms
- Duplicate handling in results
- Cross-reference data analysis techniques

## Examples

### Example 1:

**Input:** `followersA = [1, 2, 2, 1], followersB = [2, 2]`
**Output:** `[2]`
**Explanation:** User 2 follows both accounts.

### Example 2:

**Input:** `followersA = [4, 9, 5], followersB = [9, 4, 9, 8, 4]`
**Output:** `[9, 4]` or `[4, 9]`
**Explanation:** Users 4 and 9 follow both accounts. Order doesn't matter.

### Example 3:

**Input:** `followersA = [1, 2, 3], followersB = [4, 5, 6]`
**Output:** `[]`
**Explanation:** No common followers between the accounts.

## Constraints

- 1 ≤ followersA.length, followersB.length ≤ 1000
- 0 ≤ followersA[i], followersB[i] ≤ 1000
- Each array may contain duplicates
- Result should contain unique elements only

## Asked by Companies

- Twitter
- Instagram
- TikTok
- YouTube
