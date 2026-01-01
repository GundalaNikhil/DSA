---
problem_id: GRD_CAMPUS_SHUTTLE_DRIVER_SWAPS__3847
display_id: GRD-001
slug: campus-shuttle-driver-swaps
title: "Campus Shuttle Driver Swaps"
difficulty: Easy
difficulty_score: 30
topics:
  - Greedy Algorithms
  - Intervals
  - Coverage
tags:
  - greedy
  - intervals
  - scheduling
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-001: Campus Shuttle Driver Swaps

## Problem Statement

You have `n` shuttle trips that need to be covered by drivers. Each trip has a specific time interval `[start, end]`. Two drivers, A and B, are available with their own availability intervals:
- Driver A is available during interval `[A_start, A_end]`
- Driver B is available during interval `[B_start, B_end]`

Each trip must be assigned to exactly one driver who is available during that entire trip. Your goal is to minimize the number of driver switches (transitions from driver A to driver B or vice versa) while ensuring all trips are covered.

Return the minimum number of switches needed, or `-1` if it's impossible to cover all trips.

![Problem Illustration](../images/GRD-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of trips)
- Next `n` lines: two integers `start end` representing each trip's time interval
- Next line: two integers `A_start A_end` (Driver A's availability)
- Next line: two integers `B_start B_end` (Driver B's availability)

## Output Format

- Single integer: minimum number of driver switches, or `-1` if impossible

## Constraints

- `1 <= n <= 10^5`
- `1 <= start < end <= 10^9`
- `1 <= A_start < A_end <= 10^9`
- `1 <= B_start < B_end <= 10^9`
- All trips are non-overlapping (no two trips happen at the same time)

## Example

**Input:**
```
3
1 3
4 6
7 9
1 8
3 10
```

**Output:**
```
1
```

**Explanation:**

Trips:
- Trip 1: [1, 3]
- Trip 2: [4, 6]
- Trip 3: [7, 9]

Driver availabilities:
- Driver A: [1, 8]
- Driver B: [3, 10]

Optimal assignment:
- Trip 1 [1, 3]: Assign to Driver A (A is available during [1, 8])
- Trip 2 [4, 6]: Assign to Driver A (continue with same driver)
- Trip 3 [7, 9]: Assign to Driver B (A ends at 8, so switch to B)

Total switches: 1 (from A to B before trip 3)

![Example Visualization](../images/GRD-001/example-1.png)

## Notes

- A "switch" occurs when consecutive trips are assigned to different drivers
- Trips are given in chronological order (sorted by start time)
- If a trip cannot be covered by either driver, return -1
- Greedy strategy: Extend the current driver as far as possible; switch only when necessary
- Consider which driver to start with based on coverage of early trips

## Related Topics

Greedy Algorithms, Interval Scheduling, Coverage Problems, Optimization

---

## Solution Template

### Java


### Python


### C++


### JavaScript
