# Merge Sorted Data Streams

**Problem ID:** HEAP-006
**Display ID:** 89
**Question Name:** Merge Sorted Data Streams
**Slug:** merge-sorted-data-streams
**Title:** Merge K Sorted Log Files
**Difficulty:** Hard
**Premium:** No
**Tags:** Heap, Merge Sort, Divide and Conquer, Array

## Problem Description

You are building a log aggregation system for a distributed application running across multiple servers. Each server produces its own log file with entries sorted by timestamp. You need to merge K sorted log files into a single sorted timeline of events.

Each log file is represented as a sorted array of integers (timestamps in seconds). Merge all log files into one sorted array efficiently.

## A Simple Scenario (Daily Life Usage)

Imagine you're debugging a distributed system with 5 microservices. Each service writes logs with timestamps:

- Auth Service: [100, 150, 200, 300]
- Payment Service: [120, 180, 250]
- Database Service: [110, 140, 190, 220]
- API Gateway: [105, 160]
- Cache Service: [130, 170, 210]

To understand the sequence of events during an incident, you need to merge all logs into one timeline: [100, 105, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 250, 300]. This helps you trace the root cause by seeing events in chronological order across all services.

## Your Task

Write a function that takes an array of K sorted arrays (log files) and merges them into a single sorted array.

Each array represents logs from one server, already sorted by timestamp. Return a single array with all timestamps in sorted order.

## Why is it Important?

This problem teaches you:

- Using min heaps to efficiently merge multiple sorted sequences
- Understanding the classic K-way merge algorithm
- Optimizing from O(nk log nk) to O(nk log k) time complexity
- Real-world distributed systems and observability
- Trade-offs between different merge strategies

## Examples

### Example 1:

**Input:**
```
logFiles = [
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]
```

**Output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

**Explanation:** Merge all three log files in sorted order.

### Example 2:

**Input:**
```
logFiles = [
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
```

**Output:** `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

**Explanation:** The third log file has the earliest timestamp (0) and the latest timestamps (8-11).

### Example 3:

**Input:**
```
logFiles = [
  [10, 20, 30],
  [15, 25, 35],
  [5, 40, 50]
]
```

**Output:** `[5, 10, 15, 20, 25, 30, 35, 40, 50]`

**Explanation:** Even though each file is internally sorted, the merged result needs proper ordering.

### Example 4:

**Input:**
```
logFiles = [
  [1],
  [0]
]
```

**Output:** `[0, 1]`

**Explanation:** Two single-element log files merged.

### Example 5:

**Input:**
```
logFiles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
```

**Output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Explanation:** Only one log file, return it as is.

## Constraints

- 1 ≤ k ≤ 10^4 (number of log files)
- 0 ≤ logFiles[i].length ≤ 500
- 0 ≤ logFiles[i][j] ≤ 10^9
- logFiles[i] is sorted in ascending order
- Total number of log entries ≤ 10^4

## Follow-up Questions

1. Can you solve it with O(nk log k) time complexity where n is average length and k is number of files?
2. How would you handle this if log files are too large to fit in memory?
3. What if new log entries are continuously streaming in?

## Asked by Companies

- Splunk
- Datadog
- New Relic
- Elastic
