# Streaming Service Buffer

**Problem ID:** SW-001
**Display ID:** 72
**Question Name:** Streaming Service Buffer
**Slug:** streaming-service-buffer
**Title:** Maximum Sum Subarray of Size K
**Difficulty:** Easy
**Premium:** No
**Tags:** Sliding Window, Array

## Problem Description

You are given an array of integers representing video chunk sizes (in KB) and a buffer size K. Find the maximum total size of K consecutive video chunks that can be loaded into the buffer.

## A Simple Scenario (Daily Life Usage)

Imagine you're Netflix optimizing video streaming. Your buffer can hold K chunks at a time, and you want to maximize the amount of data loaded to ensure smooth playback without buffering. If your buffer holds 3 chunks and you have chunk sizes [5, 10, 3, 20, 15], the best 3 consecutive chunks are [3, 20, 15] with a total of 38 KB.

## Your Task

Write a function that takes an array of chunk sizes and a buffer size K, and returns the maximum sum of K consecutive chunks.

## Why is it Important?

This problem teaches you:

- The sliding window technique for fixed-size windows
- Efficient array traversal with O(n) time complexity
- Optimizing streaming performance
- Understanding buffer management in video players

## Examples

### Example 1:

**Input:** `chunks = [2, 1, 5, 1, 3, 2]`, `k = 3`
**Output:** `9`
**Explanation:** The subarray [5, 1, 3] has the maximum sum of 9.

### Example 2:

**Input:** `chunks = [100, 200, 300, 400]`, `k = 2`
**Output:** `700`
**Explanation:** The subarray [300, 400] has the maximum sum of 700.

### Example 3:

**Input:** `chunks = [1, 4, 2, 10, 23, 3, 1, 0, 20]`, `k = 4`
**Output:** `39`
**Explanation:** The subarray [4, 2, 10, 23] has the maximum sum of 39.

## Constraints

- 1 <= chunks.length <= 10^5
- 1 <= k <= chunks.length
- -10^4 <= chunks[i] <= 10^4
- All chunk sizes are in KB

## Asked by Companies

- Netflix
- YouTube
- Hulu
- Disney+
