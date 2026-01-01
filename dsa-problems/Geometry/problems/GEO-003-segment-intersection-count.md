---
problem_id: GEO_SEGMENT_INTERSECTION_COUNT__1538
display_id: GEO-003
slug: segment-intersection-count
title: "Segment Intersection Count"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Intersection
tags:
  - geometry
  - sweep-line
  - segments
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-003: Segment Intersection Count

## Problem Statement

You are given `m` line segments in 2D. Count how many **distinct pairs** of segments intersect (including touching at endpoints or overlapping).

Return the total number of intersecting pairs.

## ASCII Visual

```
S1: (0,0) to (2,2)
S2: (0,2) to (2,0)
S3: (3,0) to (3,2)

S1 and S2 intersect (X) once; S3 does not touch others.
```

## Input Format

- First line: integer `m` (number of segments)
- Next `m` lines: four integers `x1 y1 x2 y2` per segment

## Output Format

- Single integer: number of intersecting pairs

## Constraints

- `1 <= m <= 200000`
- `-10^9 <= coordinates <= 10^9`
- All segments are non-degenerate (endpoints are distinct)

## Example

**Input:**
```
2
0 0 2 2
0 2 2 0
```

**Output:**
```
1
```

**Explanation:**

The two segments cross once, so there is exactly one intersecting pair.

## Notes

- Touching at endpoints counts as an intersection.
- Overlapping (collinear) segments count as one intersecting pair.
- Use 64-bit arithmetic in orientation tests to avoid overflow.

## Related Topics

Computational Geometry, Sweep Line, Balanced BST

---

## Solution Template

### Java


### Python


### C++


### JavaScript

