---
problem_id: HEP_MEETING_ROOMS_MIN_IDLE_SETUP__3108
display_id: HEP-005
slug: meeting-rooms-min-idle-setup
title: "Meeting Rooms Min Idle with Setup Time"
difficulty: Medium
difficulty_score: 54
topics:
  - Heaps
  - Scheduling
  - Intervals
tags:
  - heaps
  - scheduling
  - intervals
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-005: Meeting Rooms Min Idle with Setup Time

## Problem Statement

You must assign meetings to `k` rooms. Each meeting is a time interval `[start, end]`. After a meeting ends, the room requires `s` units of setup time before it can host the next meeting. If two meetings `i` and `j` are in the same room, then:

```
end_i + s <= start_j
```

The slack between consecutive meetings in a room is:

```
start_j - (end_i + s)
```

Minimize the total slack across all rooms. Input guarantees that a valid schedule exists.

![Problem Illustration](../images/HEP-005/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `s`
- Next `n` lines: two integers `start` and `end`

## Output Format

- Single integer: minimum total slack

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- `0 <= s <= 10^6`
- `0 <= start <= end <= 10^9`

## Example

**Input:**

```
3 2 1
0 10
5 8
13 20
```

**Output:**

```
2
```

**Explanation:**

Assign meetings as:

- Room 1: [0,10] then [13,20] -> slack = 13 - (10 + 1) = 2
- Room 2: [5,8] -> no slack

Total slack = 2.

![Example Visualization](../images/HEP-005/example-1.png)

## Notes

- Sort meetings by start time
- Use a heap of room availability times
- Choose the room that becomes available latest but still <= start
- Time complexity: O(n log k)
- Space complexity: O(k)

## Related Topics

Heaps, Scheduling, Interval Partitioning, Greedy

---

## Solution Template

### Java


### Python


### C++


### JavaScript

