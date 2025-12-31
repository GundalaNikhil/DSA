---
problem_id: GEO_POLYGON_AREA_SHOELACE__7719
display_id: GEO-006
slug: polygon-area-shoelace
title: "Polygon Area (Shoelace)"
difficulty: Easy-Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Polygon
  - Shoelace Formula
tags:
  - geometry
  - area
  - shoelace
  - easy-medium
premium: true
subscription_tier: basic
---

# GEO-006: Polygon Area (Shoelace)

## 📋 Problem Summary

Given `n` vertices of a simple polygon (in order, CW or CCW), compute its area using the shoelace formula. Output the absolute area as an integer.

## 🌍 Real-World Scenario

**Scenario Title:** Parcel Footprint Calculation**

A GIS analyst needs parcel areas from boundary coordinates. The shoelace formula yields exact polygon areas without triangulating or using floating point, making it ideal for large batches of parcels.

**Why This Problem Matters:**

- Fundamental polygon area computation in graphics, GIS, and simulations.
- Demonstrates cross-product accumulation and sign handling (CW vs CCW).
- Avoids floating-point drift by using integer arithmetic.

## Emoji Visual

```
⬛ Square:
🟢 (0,0) ---- 🟢 (2,0)
|               |
|               |
🟢 (0,2) ---- 🟢 (2,2)
Area = 4
```

## Detailed Explanation

### Shoelace Formula

For vertices `(xi, yi)` with `i = 0..n-1` and `i+1` wrapped modulo `n`:

```
twice_area = Σ (xi * y{i+1} - x{i+1} * yi)
area = |twice_area| / 2
```

The sign of `twice_area` indicates orientation (positive for CCW). Taking the absolute value handles both CW and CCW input; divide by `2` (integer division) to get the area.

### Why It Works

The sum aggregates the signed areas of trapezoids formed with the x-axis. Algebraically, it matches the polygon’s signed area from Green’s theorem.

### Overflow Safety

`xi, yi` up to `1e9`; each product up to `1e18`; summing `1e5` terms fits in 128-bit. In Java use `long`; in C++ use `long long` (and `__int128` internally if paranoid).

## Input/Output Clarifications

- Vertices are in order; polygon is simple (no self-intersections).
- Output is the absolute area (no “.0”).
- If the polygon degenerates (not in constraints), shoelace still computes signed area; constraints guarantee simplicity.

## Naive Approach

**Algorithm:** Triangulate from a root and sum triangle areas via cross products.

**Time:** `O(n)`  
**Space:** `O(1)`

**Limitations:** More bookkeeping; shoelace is simpler and equivalent.

## Optimal Approach (Shoelace)

**Algorithm:**
1. Initialize `sum = 0`.
2. For each `i` from `0` to `n-1` (with `j = (i+1) % n`), add `(xi * yj - xj * yi)` to `sum`.
3. `area = abs(sum) // 2`.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

## Reference Implementations

### Python

```python
from typing import List

def polygon_area(xs: List[int], ys: List[int]) -> int:
    n = len(xs)
    total = 0
    for i in range(n):
        j = (i + 1) % n
        total += xs[i] * ys[j] - xs[j] * ys[i]
    return abs(total) // 2


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
```

### Java

```java
class Solution {
    public long polygonArea(int[] xs, int[] ys) {
        int n = xs.length;
        long sum = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            sum += 1L * xs[i] * ys[j] - 1L * xs[j] * ys[i];
        }
        return Math.abs(sum) / 2;
    }
}
```

### C++

```cpp
long long polygonArea(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        sum += xs[i] * ys[j] - xs[j] * ys[i];
    }
    return llabs(sum) / 2;
}
```

### JavaScript

```javascript
function polygonArea(xs, ys) {
  const n = xs.length;
  let sum = 0n;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n;
    sum += BigInt(xs[i]) * BigInt(ys[j]) - BigInt(xs[j]) * BigInt(ys[i]);
  }
  const absSum = sum < 0n ? -sum : sum;
  return absSum / 2n;
}
```

### Common Mistakes to Avoid

1. **Forgetting to wrap the last vertex to the first.**
2. **Missing absolute value.** Clockwise input yields negative signed area.
3. **Using floating point unnecessarily.** Stick to integer arithmetic.
4. **Overflow on products.** Cast to 64-bit before multiplying.

### Complexity Analysis

- **Time:** `O(n)`  
- **Space:** `O(1)`

## Testing Strategy

- Axis-aligned square (area 4).
- Triangle with known area (e.g., base*height/2).
- Concave simple polygon.
- Large coordinates to stress overflow.
- Clockwise vs CCW input should produce same absolute area.

## Applications

- GIS parcel areas.
- Graphics fill computations.
- Physics: polygon mass properties (area as a first step).

## Emoji Recap

```
🧮 Sum cross terms ➕ wrap around ➡️ take |sum| ➗ 2 ➡️ 📐 area
```
