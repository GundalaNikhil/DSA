---
problem_id: NUM_MAXIMUM_POINTS_LINE_SEGMENT_LIMIT__2904
display_id: NUM-014
slug: maximum-points-line-segment-limit
title: "Maximum Points on a Line Segment Length Limit"
difficulty: Medium
difficulty_score: 58
topics:
  - Number Theory
  - Geometry
  - Sorting
tags:
  - number-theory
  - geometry
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-014: Maximum Points on a Line Segment Length Limit

## Problem Statement

Given `n` points, find the maximum number of points that can lie on a single line segment whose length is at most `L`. The segment can be placed anywhere but must be collinear with the points it covers.

![Problem Illustration](../images/NUM-014/problem-illustration.png)

## Input Format

- First line: integers `n` and `L`
- Next `n` lines: two integers `x` and `y`

## Output Format

- Single integer: maximum count of points on any line segment of length <= L

## Constraints

- `1 <= n <= 2000`
- `1 <= L <= 10^6`
- `-10^6 <= x, y <= 10^6`

## Example

**Input:**

```
4 2
0 0
1 1
2 2
0 1
```

**Output:**

```
2
```

**Explanation:**

The points (0,0), (1,1), (2,2) are collinear, but any segment of length 2 can cover at most two of them.

![Example Visualization](../images/NUM-014/example-1.png)

## Notes

- For each anchor point, group other points by slope
- Within a slope group, sort by projection distance and use a sliding window
- Time complexity: O(n^2 log n)
- Space complexity: O(n)

## Related Topics

Geometry, Collinearity, Sliding Window

---

## Solution Template

### Java


### Python


### C++


### JavaScript

