---
problem_id: GEO_ORIENTATION_TRIPLETS__4821
display_id: GEO-001
slug: orientation-triplets
title: "Orientation of Triplets"
difficulty: Easy
difficulty_score: 30
topics:
  - Computational Geometry
  - Cross Product
  - Orientation Test
tags:
  - geometry
  - orientation
  - cross-product
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-001: Orientation of Triplets

## Problem Statement

Given three 2D points `P1(x1, y1)`, `P2(x2, y2)`, `P3(x3, y3)`, determine whether the ordered triplet is **clockwise**, **counterclockwise**, or **collinear**.

Print one of the words: `clockwise`, `counterclockwise`, or `collinear`.


```
P1 ●
     \
      \
       ● P2
        \
         \
          ● P3
```

The cross product of vectors `P1P2` and `P1P3` determines the turn direction.

## Input Format

- Single line with six integers: `x1 y1 x2 y2 x3 y3`

## Output Format

- Single word: `clockwise`, `counterclockwise`, or `collinear`

## Constraints

- `-10^9 <= xi, yi <= 10^9`

## Example

**Input:**
```
0 0 1 1 2 0
```

**Output:**
```
clockwise
```

**Explanation:**

`(1,1)` is above the segment `(0,0)->(2,0)`, giving a right turn.


```
P2 (1,1)
   / \
  /   \
P1-----P3
```

## Notes

- Use 64-bit arithmetic for the cross product to avoid overflow.
- The order of the points matters; swapping changes the orientation.
- Collinearity occurs when the cross product is exactly zero.

## Related Topics

Computational Geometry, Cross Product, Orientation Testing

---

## Solution Template

### Java


### Python


### C++


### JavaScript

