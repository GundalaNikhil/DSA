---
problem_id: GEO_CONVEX_HULL_CAPPED__2407
display_id: GEO-005
slug: convex-hull-capped
title: "Convex Hull with Interior Caps"
difficulty: Medium
difficulty_score: 65
topics:
  - Computational Geometry
  - Convex Hull
  - Geometry Filtering
tags:
  - geometry
  - convex-hull
  - filtering
  - medium
premium: true
subscription_tier: basic
---

# GEO-005: Convex Hull with Interior Caps

## 📋 Problem Summary

Build the convex hull of `n` points, then drop any hull vertex whose interior angle is **strictly less than** `theta` (degrees). Output the remaining vertices in CCW order; if none remain, output `0`.

## 🌍 Real-World Scenario

**Scenario Title:** Drone Flight Path Smoothing**

Before publishing a polygonal flight boundary, operations wants to remove “too sharp” hull corners (below `theta`) to ensure smooth turns. The capped hull represents the smoothed boundary the drone can follow safely.

**Why This Problem Matters:**

- Extends convex hull by post-processing with angle-based pruning.
- Reinforces robust hull construction and angle checks without floating error.
- Practical for simplifying polygons under turning constraints.

## Emoji Visuals

```
🟩 Square hull, theta = 60°
  🟢 (0,0) ---- 🟢 (4,0)
  |              |
  |      ⚙️      |   => all 4 kept (90° ≥ 60°)
  🟢 (0,4) ---- 🟢 (4,4)

🔺 Triangle hull, theta = 80°
        🟢
       / \
      /   \
   🟢 ----- 🟢
   angles 60° < 80° ⇒ all capped away ⇒ k = 0
```

## Detailed Explanation

### Step 1: Convex Hull

Use a standard hull algorithm (Andrew’s monotone chain). Keep the hull in CCW order. Interior angles on a convex hull lie in `(0, 180]`.

### Step 2: Interior Angle Test

For consecutive hull vertices `(prev, curr, next)`, compute:

- `dot = (prev - curr) · (next - curr)`
- `cross = (prev - curr) x (next - curr)`

Interior angle `α` satisfies `cos α = -dot / (|prev-curr| * |next-curr|)` and `sin α = |cross| / (|prev-curr| * |next-curr|)`. To avoid trig, compare using cosine threshold:

- We need `α < theta` to discard.
- Compute `cos α = -dot / (|u||v|)`.
- Precompute `cos(theta)` once (in double) and discard if `cos α > cos(theta)` **and** `cross != 0` (since cos decreases as angle grows in `[0, π]`).

Alternatively, compare using tan/side-lengths with squared lengths to stay integer-heavy; a single cosine comparison is fine with doubles because we only need a strict inequality.

### Corner Cases

- **Collinear hull edges:** angle is 180°; never discarded unless `theta > 180` (impossible here), so they stay.
- **All removed:** output `0`.
- **Duplicate points:** hull algorithm ignores them; duplicates can cause 0 distance edges; ensure you skip zero-length vectors when computing angle.

## Input/Output Clarifications

- Output first the count `k`, then the `k` vertices CCW.
- If `k = 0`, print just `0`.
- `theta` is in degrees; convert to radians for cosine if needed.

## Naive Approach

**Algorithm:**
1. Compute hull.
2. For each hull vertex, compute actual angle via `acos` and compare with `theta`.

**Time:** `O(n log n)` for hull, `O(h)` for angles.  
**Space:** `O(h)`.

**Limitations:** Uses `acos` per vertex; slower and less stable than cosine comparison.

## Optimal Approach

**Key Insight:** You can compare angles without computing them explicitly.

**Algorithm:**
1. Build hull `H` in CCW via monotone chain. Let `h = |H|`.
2. Precompute `cosT = cos(theta)` in radians.
3. For each `i` in `H`, let `prev = H[(i-1+h)%h]`, `curr = H[i]`, `next = H[(i+1)%h]`.
4. Compute vectors `u = prev - curr`, `v = next - curr`.
5. If either `u` or `v` is zero-length, skip discarding.
6. Compute `dot = u.x*v.x + u.y*v.y`, `lenU = |u|`, `lenV = |v|`, `cosA = -dot / (lenU*lenV)`.
7. If `cosA > cosT` (i.e., angle smaller than `theta`), discard `curr`; otherwise keep it.
8. Output kept vertices.

**Time Complexity:** `O(n log n)` (hull dominates).  
**Space Complexity:** `O(n)` for hull arrays.

## Reference Implementations

### Python


### Java


### C++


### JavaScript


### Common Mistakes to Avoid

1. **Using `acos` per vertex.**  
   Compare cosines; it’s faster and avoids precision pitfalls.

2. **Dropping collinear edges incorrectly.**  
   Collinear angles are 180° and should not be removed for `theta < 180`.

3. **Losing hull order.**  
   Ensure the hull remains CCW after building; the filtering must preserve order.

4. **Zero-length edges.**  
   Duplicates can create zero-length vectors; guard against division by zero.

### Complexity Analysis

- **Time:** `O(n log n)` (hull) + `O(h)` (filter).  
- **Space:** `O(n)` for hull buffers.

## Testing Strategy

- Square with small `theta` (keep all).
- Square with `theta > 90` (discard all).
- Triangle with `theta` below/above 60°.
- Collinear points (degenerate hull of 2 points).
- Large coordinates to ensure 64-bit safety.

## Applications

- Simplifying polygons under turn constraints.
- Smoothing navigation boundaries.
- Filtering noisy hulls before rendering.

## Emoji Recap

```
🟢 Hull built (CCW) ➜ 🪓 Remove sharp corners (< theta) ➜ ✅ Output capped hull
```
