---
problem_id: GRD_FESTIVAL_STALL_PLACEMENT__7146
display_id: GRD-003
slug: festival-stall-placement
title: "Festival Stall Placement"
difficulty: Medium
difficulty_score: 45
topics:
  - Greedy Algorithms
  - Intervals
  - Activity Selection
tags:
  - greedy
  - intervals
  - scheduling
  - activity-selection
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-003: Festival Stall Placement

## Problem Statement

You are organizing a festival along a straight road and have received `n` stall placement requests. Each request specifies a start and end coordinate `[start, end]` where the vendor wants to place their stall.

However, there's a safety regulation: no two stalls can be placed within distance `d` of each other (measured by their closest points).

Your goal is to approve the maximum number of stall requests while respecting the distance constraint.

![Problem Illustration](../images/GRD-003/problem-illustration.png)

## Input Format

- First line: two integers `n d` (number of requests and minimum distance)
- Next `n` lines: two integers `start end` representing each stall's position interval

## Output Format

- Single integer: maximum number of stalls that can be placed

## Constraints

- `1 <= n <= 10^5`
- `1 <= d <= 10^9`
- `0 <= start < end <= 10^9`
- Positions are integers

## Example

**Input:**

```
3 2
0 2
1 4
5 6
```

**Output:**

```
2
```

**Explanation:**

Stall requests with minimum distance d=2:

- Stall 1: [0, 2] (ends at position 2)
- Stall 2: [1, 4] (ends at position 4)
- Stall 3: [5, 6] (ends at position 6)

Greedy approach (sort by end position, pick earliest ending):

1. Choose stall 1 ending at 2
2. Stall 2 ends at 4, but starts at 1. Distance from stall 1's end (2) to stall 2's start (1) is not valid (overlapping). Skip.
3. Stall 3 starts at 5. Distance from stall 1's end (2) to stall 3's start (5) is 3, which is >= d=2. Choose stall 3.

Total: 2 stalls

![Example Visualization](../images/GRD-003/example-1.png)

## Notes

- Sort stalls by their end position
- Greedily select stalls whose start position is at least distance `d` from the previously selected stall's end position
- This is a variant of the interval scheduling maximization problem with distance constraints
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Interval Scheduling, Activity Selection, Sorting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

