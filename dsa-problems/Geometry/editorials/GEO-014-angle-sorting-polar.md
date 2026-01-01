---
problem_id: GEO_ANGLE_SORTING_POLAR__2841
display_id: GEO-014
slug: angle-sorting-polar
title: "Angle Sorting for Polar Order"
difficulty: Easy-Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Sorting
tags:
  - geometry
  - sorting
  - polar-angle
  - easy-medium
premium: true
subscription_tier: basic
---

# GEO-014: Angle Sorting for Polar Order

## 📋 Problem Summary

Given `n` points (none at the origin), output them sorted by polar angle around the origin in counterclockwise order. Ties (same angle) are broken by distance to the origin (closer first).

## 🌍 Real-World Scenario

**Scenario Title:** Radar Target Sweep**

A radar marks targets relative to its origin. To render them in sweep order, targets are sorted by angle. If two align on the same bearing, the closer appears first.

**Why This Problem Matters:**

- Polar sorting underpins convex hull algorithms and angular sweeps.
- Shows how to avoid `atan2` by using half-plane partition + cross product for speed and stability.

## ASCII Visual

```
   y
   ↑     ● (1,1)
   |  ● (1,0)   ● (0,1)
   |
   O------------→ x
```

Order: (1,0) → (1,1) → (0,1) → ... continuing CCW.

## Detailed Explanation

### Half-Plane Partition

Classify a point `(x,y)` as:
- Upper half: `y > 0` or `y == 0 && x > 0`
- Lower half: otherwise

When sorting:
1. Points in the upper half come before points in the lower half.
2. If two points are in the same half, order by cross product sign:
   - For `a` then `b`, `cross(a, b) > 0` ⇒ `a` before `b` (CCW).
   - If `cross == 0`, tie-break by radius `r^2 = x^2 + y^2` (smaller first).

This avoids computing angles explicitly.

### Cross Product

`cross(a, b) = a.x * b.y - a.y * b.x`  
Positive => `b` is CCW from `a`.

### Why This Works

Sorting by half then cross product matches the order of `atan2(y,x)`:
- Half determines whether angle is in `[0, π)` or `[π, 2π)`.
- Cross product compares angles within the same half.

## Input/Output Clarifications

- No point equals (0,0).
- Points are distinct.
- Output exactly the points in sorted order, one per line.

## Naive Approach

**Algorithm:** Compute `atan2(y,x)` for each point; sort by angle then radius.

**Limitations:** Uses floating point angles; slower and subject to precision issues.

## Optimal Approach (Half-Plane + Cross)

**Algorithm:**
1. Define `half(p)` as above.
2. Sort points with comparator:
   - If `half(a) != half(b)`, `half(a) < half(b)` first.
   - Else, if `cross(a, b) != 0`, order by cross sign.
   - Else, order by squared radius.
3. Output sorted list.

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(1)` beyond storage.

## Reference Implementations

### Python





### Java


### C++


### JavaScript


### Common Mistakes to Avoid

1. **Using `atan2` everywhere.** Slower and can misorder near 180° vs -180°; half+cross avoids that.
2. **Origin point present.** The problem forbids it; if present, handle separately.
3. **Wrong tie-break for same angle.** Must use radius to order closer first.
4. **Half-plane definition errors.** Ensure `(y > 0) or (y == 0 and x > 0)` defines the upper half.

### Complexity Analysis

- **Time:** `O(n log n)`  
- **Space:** `O(1)` beyond input storage.

## Testing Strategy

- Points in all four quadrants.
- Collinear with origin (same angle) to test radius tie-break.
- Only upper-half or only lower-half points.
- Large coordinate magnitudes (cross fits in 128-bit if needed).

## ASCII Recap

```
Half = upper? else lower
Sort by (half, cross>0?, radius)
```
