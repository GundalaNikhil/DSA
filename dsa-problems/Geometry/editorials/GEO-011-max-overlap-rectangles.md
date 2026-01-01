---
problem_id: GEO_MAX_OVERLAP_RECTS__6720
display_id: GEO-011
slug: max-overlap-rectangles
title: "Maximum Overlap of Rectangles"
difficulty: Medium
difficulty_score: 55
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
tags:
  - geometry
  - rectangles
  - sweep-line
  - overlap
  - medium
premium: true
subscription_tier: basic
---

# GEO-011: Maximum Overlap of Rectangles

## 📋 Problem Summary

Given `m` axis-aligned rectangles, find the maximum number of rectangles covering any single point (edges count as covered). Output that maximum overlap count.

## 🌍 Real-World Scenario

**Scenario Title:** Hotspot Density Check**

On a floor plan, each Wi-Fi router covers a rectangle. The networking team wants to know the highest number of routers covering any location to tune channel assignments and avoid interference.

**Why This Problem Matters:**

- Classic sweep-line plus segment tree problem.
- Reinforces interval updates with max tracking.
- Useful for density/coverage analytics in GIS and facility planning.

## ASCII Visual

```
Rect A: (0,0)-(2,2)
Rect B: (1,1)-(3,3)
Rect C: (2,0)-(4,2)

Max overlap = 2 (A∩B and B∩C touch, but no point has all 3)
```

## Detailed Explanation

We need the highest cumulative count of overlapping rectangles.

### Sweep over x

Create events for each rectangle:
- At `x1`: add +1 to interval `[y1, y2)`.
- At `x2`: add -1 to interval `[y1, y2)`.

Sort events by `x`. Between consecutive x-values, the y-coverage counts are constant. We only need the maximum count, not area.

### Segment Tree on Y (Coordinate Compressed)

Compress all unique `y` endpoints. Segment tree nodes store:
- `add`: lazy delta applied to the node interval.
- `mx`: maximum coverage in that interval.

Update `[y1, y2)` with `+1` or `-1`. After each update, the root `mx` gives the current max overlap at this sweep position. Track the overall maximum as we process events in order.

### Complexity

- Sort events: `O(m log m)`
- Updates: `O(m log n)` where `n` is number of unique y’s.
- Space: `O(n)` for segment tree.

## Input/Output Clarifications

- Rectangles are closed, but using half-open intervals `[y1, y2)` avoids double counting edges; max count remains correct.
- Coordinates fit in 64-bit; max overlap fits in `m`.

## Naive Approach

**Algorithm:** Check all rectangle pairs or grid by all unique x,y lines and count crossings.

**Time:** `O(m^2)` or `O(n^2)` grid—too slow for `1e5`.

## Optimal Approach (Sweep + Segment Tree)

**Algorithm Steps:**
1. Collect all `y1, y2`; sort unique for compression.
2. Build events `(x, type, y1_idx, y2_idx)` with `type = +1` for entering, `-1` for leaving.
3. Sort events by `x`.
4. Initialize segment tree arrays `add` and `mx`.
5. For each event in order:
   - Update tree on `[y1_idx, y2_idx)` with `type`.
   - Update answer with `mx[1]`.
6. Output answer.

**Time Complexity:** `O(m log m)`  
**Space Complexity:** `O(n)`

## Reference Implementations

### Python


### Java (outline)


### C++ (outline)


### JavaScript


### Common Mistakes to Avoid

1. **Missing coordinate compression.** Direct y range up to 1e9 is infeasible.
2. **Off-by-one on intervals.** Use `[y1, y2)` consistently.
3. **Forgetting to propagate add into mx.** Root mx must include lazy value.
4. **Sorting events incorrectly.** Same x can process in any order here; if ties matter, process all at x before moving.

### Complexity Analysis

- **Time:** `O(m log m)`  
- **Space:** `O(m)` for events + tree.

## Testing Strategy

- Single rectangle (answer 1).
- Two disjoint rectangles (answer 1).
- Fully overlapping stack (answer = m).
- Chain overlaps where max is smaller than m.
- Large coordinates with small count.

## ASCII Recap

```
Events along x:
  add +1 on entering edge
  add -1 on leaving edge
Segment tree keeps max overlap on y.
Track global max after each event.
```
