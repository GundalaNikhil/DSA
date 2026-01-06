---
problem_id: GEO_CONVEX_HULL_VERIFIED_OUTLIERS__9231
display_id: NTB-GEO-9231
slug: convex-hull-verified-outliers
title: "Convex Hull with Verified Outliers"
difficulty: Medium
difficulty_score: 50
topics:
  - Geometry
tags:
  - algorithms
  - coding-interviews
  - computational-geometry
  - convex-hull-verified-outliers
  - data-structures
  - geometry
  - spatial-reasoning
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Convex Hull with Verified Outliers

## Problem Statement

You are given `n` points in the plane. Compute the convex hull and separately identify statistical outliers based on distance from the centroid.

Outlier rule:

1. Compute the centroid `(cx, cy)` as the mean of all x-coordinates and y-coordinates.
2. For each point, compute its Euclidean distance to the centroid.
3. Let `mu` be the mean of these distances and `sigma` be the population standard deviation.
4. A point is an outlier if `distance > mu + 2 * sigma`.

You must report:

- The convex hull vertices in counterclockwise order, starting from the point with smallest x, then smallest y.
- The outlier points (by input index) without removing them from the hull computation.

## Input Format

- First line: integer `n`
- Next `n` lines: `x y`

## Output Format

- First line: integer `h` (number of hull vertices)
- Next `h` lines: hull vertices as `x y`
- Next line: integer `o` (number of outliers)
- Next `o` lines: `index x y` for each outlier, sorted by index ascending

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= x, y <= 10^9`

## Clarifying Notes

- If all points are collinear, the hull is the two endpoints in order (or one point if `n = 1`).
- Points on the boundary are part of the hull; interior collinear points are excluded.
- Outlier detection is performed on the full set of points, independent of the hull.

## Example Input

```
5
0 0
0 1
1 1
1 0
50 50
```

## Example Output

```
4
0 0
1 0
50 50
0 1
1
5 50 50
```
