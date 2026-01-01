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
---

# NUM-014: Maximum Points on a Line Segment Length Limit

## 📋 Problem Summary

Given `n` points on a 2D plane and a maximum length `L`, find the maximum number of collinear points that can be covered by a single line segment of length at most `L`.
- Input: Points `(x_i, y_i)`, Length `L`.
- Output: Max count.

## 🌍 Real-World Scenario

**Scenario Title:** The Sensor Alignment

You are deploying a linear sensor array (like a LIDAR strip or a directional antenna) that has a physical length limit `L`.
- You have a map of potential signal sources (points).
- To maximize signal reception, you want to align your sensor array such that it covers the maximum number of sources simultaneously.
- The sources must lie on the line defined by the sensor, and the distance between the first and last covered source must not exceed `L`.

**Why This Problem Matters:**

- **Computational Geometry:** Finding patterns in spatial data.
- **Computer Vision:** Line detection (Hough Transform variants).
- **Data Mining:** Finding linear clusters with density constraints.

![Real-World Application](../images/NUM-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window

Points: A(0,0), B(1,1), C(2,2), D(3,3). `L=2`.
All are collinear on `y=x`.
Distances from A:
A: 0
B: `sqrt2 ~= 1.41`
C: `2sqrt2 ~= 2.82`
D: `3sqrt2 ~= 4.24`

Window `[0, 2]`:
- A (0), B (1.41). Count 2.
- C is at 2.82 > 2. Not included.

Window shifts:
- B (1.41), C (2.82). Dist `2.82 - 1.41 = 1.41 <= 2`. Count 2.
- C (2.82), D (4.24). Dist `1.41 <= 2`. Count 2.

`2.82 > 2`. So A and C cannot be covered together.
Correct.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `n <= 2000`. `O(n^2 log n)` is acceptable.
- **Collinearity:** Three points are collinear if slopes match.
- **Length:** Euclidean distance.
- **Single Point:** A segment of length 0 covers 1 point. Max is at least 1.

### Core Concept: Slope Grouping & Sliding Window

1. **Fix an anchor point `P_i`.**
2. Calculate the slope from `P_i` to every other point `P_j`.
3. Group points by slope.
4. For each group (points collinear with `P_i`), sort them by distance from `P_i`.
5. Use a **sliding window** on the sorted distances to find the max subset with range `<= L`.

## Naive Approach

### Intuition

For every pair of points, define a line. Project all points onto this line. Sort and slide window.

### Algorithm

- Iterate all pairs `(i, j)`.
- Define line.
- Check all `k`.
- `O(n^3)`. Too slow.

## Optimal Approach

### Key Insight

Instead of checking all lines, iterate each point as a "center" or "anchor".
For a fixed anchor `i`, any line passing through `i` is determined by its angle/slope.
We collect all `j` relative to `i`, store as `(slope, distance)`.
Sort by slope. Points with same slope are collinear with `i`.
Process each slope group: sort by distance, then sliding window.

### Algorithm

1. `max_points = 1`.
2. For each point `i` from 0 to `n-1`:
   - Create a list of `(dx, dy, dist)` for all `j != i`.
   - Simplify `(dx, dy)` by dividing by `gcd(|dx|, |dy|)` to represent slope uniquely.
   - Sort the list by `(dx, dy)`.
   - Group by `(dx, dy)`.
   - For each group:
     - We have a list of distances from `i`. Note: `i` itself is at distance 0.
     - Add 0 to the list (representing `i`).
     - Sort distances.
     - Sliding window: `left = 0`. For `right` from 0 to `size-1`:
       - While `dists[right] - dists[left] > L`: `left++`.
       - `max_points = max(max_points, right - left + 1)`.
3. Return `max_points`.

### Time Complexity

- **O(n^2 \log n)** due to sorting.
- `2000^2 x 11 ~= 4.4 * 10^7` ops. Fits in 2s.

### Space Complexity

- **O(n)**.

![Algorithm Visualization](../images/NUM-014/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-014/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `(0,0), (1,1), (2,2), (0,1)`, `L=2`.
1. Anchor `(0,0)`:
   - `(1,1)`: Slope `(1,1)`, Dist `1.41`.
   - `(2,2)`: Slope `(1,1)`, Dist `2.82`.
   - `(0,1)`: Slope `(0,1)`, Dist `1.0`.
   - Group `(1,1)`: `[0, 1.41, 2.82]`.
     - Window `[0, 1.41]`: Len 1.41 <= 2. Count 2.
     - Window `[1.41, 2.82]`: Len 1.41 <= 2. Count 2.
     - Window `[0, 2.82]`: Len 2.82 > 2.
   - Group `(0,1)`: `[0, 1.0]`. Count 2.
2. Max 2.

## ✅ Proof of Correctness

### Invariant
By iterating every point as an anchor, we consider every possible line.
By sorting signed distances, we correctly handle points on both sides of the anchor.
Sliding window finds the optimal segment on that line.

### Why the approach is correct
Exhaustive coverage of all lines defined by pairs of points.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Max points on ANY line (no length limit).
  - *Hint:* Just max group size.
- **Extension 2:** Circle of radius R.
  - *Hint:* Angular sweep.
- **Extension 3:** 3D Points.
  - *Hint:* Slope becomes `(dx, dy, dz) / gcd`.

### Common Mistakes to Avoid

1. **Slope Representation**
   - ❌ Wrong: Using `double` slope (precision issues).
   - ✅ Correct: Use reduced fraction `(dx, dy)`.
2. **Line Direction**
   - ❌ Wrong: Treating `(1,1)` and `(-1,-1)` as different lines.
   - ✅ Correct: Normalize to canonical form.

## Related Concepts

- **Hough Transform:** Line detection.
- **Angular Sweep:** Processing points by angle.
