---
problem_id: NUM_LATTICE_POINTS_ON_SEGMENT__6330
display_id: NUM-008
slug: lattice-points-on-segment
title: "Counting Lattice Points On Segment"
difficulty: Easy
difficulty_score: 28
topics:
  - Number Theory
  - Geometry
  - GCD
tags:
  - number-theory
  - geometry
  - gcd
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-008: Counting Lattice Points On Segment

## Problem Statement

Given two endpoints `(x1, y1)` and `(x2, y2)` with integer coordinates, count the number of integer lattice points on the closed line segment between them.

![Problem Illustration](../images/NUM-008/problem-illustration.png)

## Input Format

- Single line: four integers `x1 y1 x2 y2`

## Output Format

- Single integer: number of lattice points on the segment

## Constraints

- `|x1|, |y1|, |x2|, |y2| <= 10^9`

## Example

**Input:**

```
0 0 6 4
```

**Output:**

```
3
```

**Explanation:**

dx = 6, dy = 4, gcd(6,4) = 2, so answer = 2 + 1 = 3.

Points are (0,0), (3,2), (6,4).

![Example Visualization](../images/NUM-008/example-1.png)

## Notes

- The count equals gcd(|dx|, |dy|) + 1
- Time complexity: O(log max(|dx|,|dy|))
- Space complexity: O(1)

## Related Topics

GCD, Lattice Geometry

---

## Solution Template

### Java


### Python


### C++


### JavaScript

