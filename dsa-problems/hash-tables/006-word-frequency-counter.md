# Word Frequency Counter

**Problem ID:** HASH-006
**Display ID:** 41
**Question Name:** Word Frequency Counter
**Slug:** word-frequency-counter
**Title:** Top K Frequent Elements
**Difficulty:** Medium
**Premium:** No
**Tags:** Hash Table, Array, Sorting, Heap, Counting

## Problem Description

Given an integer array representing word IDs from blog comments, return the k most frequent word IDs. Return the answer in any order.

## A Simple Scenario (Daily Life Usage)

You're building a trending topics feature for a blogging platform. Each comment contains words that are tracked by unique IDs. You want to identify the top K most frequently mentioned topics across all comments to display as "Trending Now" on your homepage. For example, if word ID 42 (representing "technology") appears 100 times and word ID 17 (representing "coding") appears 85 times, these should be highlighted.

## Your Task

Write a function that takes an array of integers and an integer k, and returns the k most frequent elements. If there are multiple valid answers, return any of them.

## Why is it Important?

This problem teaches you:

- Frequency counting with hash tables
- Heap data structures for top-K problems
- Bucket sort optimization techniques
- Real-world trending algorithms used in social platforms

## Examples

### Example 1:

**Input:** `wordIds = [1, 1, 1, 2, 2, 3], k = 2`
**Output:** `[1, 2]`
**Explanation:** Word ID 1 appears 3 times, word ID 2 appears 2 times. These are the top 2.

### Example 2:

**Input:** `wordIds = [1], k = 1`
**Output:** `[1]`
**Explanation:** Only one unique word ID exists.

### Example 3:

**Input:** `wordIds = [4, 1, -1, 2, -1, 2, 3], k = 2`
**Output:** `[-1, 2]` or `[2, -1]`
**Explanation:** Both -1 and 2 appear twice (tied for most frequent).

## Constraints

- 1 ≤ wordIds.length ≤ 100,000
- -10,000 ≤ wordIds[i] ≤ 10,000
- k is in the range [1, number of unique elements]
- The answer is guaranteed to be unique
- Better than O(n log n) time complexity is expected

## Asked by Companies

- Reddit
- Medium
- Quora
- Stack Overflow
