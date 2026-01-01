---
problem_id: GEO_LARGEST_EMPTY_CIRCLE__9186
display_id: GEO-012
slug: the-quiet-zone-problem
title: "The Quiet Zone Problem (Largest Empty Circle Among Disks)"
difficulty: Medium
difficulty_score: 65
topics:
  - Computational Geometry
  - Voronoi
  - Optimization
tags:
  - geometry
  - circle
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# GEO-012: The Quiet Zone Problem

## 📋 Problem Summary

You are given a rectangular field and a set of noise sources, each represented by a point $(x_i, y_i)$ and a noise radius $r_i$. You need to find the largest possible "Quiet Circle" that stays entirely inside the rectangle and does not intersect any of the noise disks.

## 🌍 Real-World Scenario

**Scenario: Designing a Silent Park Section**

Imagine a city park where several loud exhaust fans or heavy machinery are placed. Each machine has a specific noise range. To build a relaxation area (the Quiet Circle), you must find a spot that is far enough from all noise sources and stays within the park's boundaries.

## 🛠️ Detailed Explanation

### The Geometry of the Quiet Zone

The problem asks to find a center $C(x,y)$ that maximizes $R$ subject to:
1.  **Boundary Constraint**: The circle must stay inside $[xL, xR] \times [yB, yT]$.
    This means $R \le \min(x - xL, xR - x, y - yB, yT - y)$.
2.  **Noise Constraint**: For each source $P_i$ with radius $r_i$, the distance between $C$ and $P_i$ must be at least $R + r_i$.
    This means $R \le dist(C, P_i) - r_i$.

Combining these, for any point $(x,y)$, the maximum possible radius is:
$$f(x,y) = \min \left( \text{dist to boundaries}, \min_{i} (dist(C, P_i) - r_i) \right)$$

This is a **global optimization problem** over the rectangle.

### Why Optimization?

While a pure geometric approach (Voronoi Diagram of Sites and Disks) exists, it is complex to implement. Given the constraints ($n \le 1000$), a **Sampling + Search** approach is highly effective.

1.  **Dense Sampling (Grid Search)**: First, we sample the function $f(x,y)$ on a dense $100 \times 100$ grid. This identifies "peaks" or candidate regions for the global maximum.
2.  **Refined Search (Hill Climbing)**: From the best candidates found on the grid, we perform Hill Climbing. We take small steps in 8 directions, gradually decreasing the step size to "climb" to the local peak with high precision.

### ASCII Visual

```
 Park Boundary: [0, 10] x [0, 10]
 Noise Source: (5, 5), Range = 0
 
 Maximum R occurs when circle touches boundary AND noise disk.
 If center is at C(x, x):
 dist(C, Boundary) = x
 dist(C, Noise Edge) = dist(C, (5,5)) - 0
 
 Setting x = sqrt((5-x)^2 + (5-x)^2)
 x = sqrt(2)*(5-x)
 x(1+sqrt(2)) = 5*sqrt(2)
 x approx 2.928932, R approx 2.928932
```

## 💡 Key Implementation Details

- **Distance Pruning**: If a noise disk completely covers the rectangle center or the rectangle itself, $R$ will be $0$.
- **Precision**: Hill Climbing should continue until the step size is extremely small (e.g., $10^{-11}$) to satisfy the $6$ decimal requirement.
- **Robustness**: Always check the rectangle midpoint if no candidates are found.

## 🚀 Complexity Analysis

- **Time Complexity**: $O(G^2 \cdot N + K \cdot S \cdot N)$, where $G$ is the grid resolution ($100$), $K$ is the number of hill-climbing restarts ($20$), and $S$ is the number of steps ($\approx 40$). With $N=1000$, this is roughly $10^7$ operations, well within 2 seconds.
- **Space Complexity**: $O(N)$ to store noise source coordinates and radii.

## Reference Implementation (Python)

```python
from typing import List
import math

def largest_quiet_circle(xL: int, yB: int, xR: int, yT: int, xs: List[int], ys: List[int], rs: List[int]) -> float:
    n = len(xs)
    
    def get_radius(x, y):
        # Distance to borders
        r = min(x - xL, xR - x, y - yB, yT - y)
        if r <= 0: return 0.0
        
        # Distance to each noise disk
        for i in range(n):
            d = math.sqrt((x - xs[i])**2 + (y - ys[i])**2)
            r = min(r, d - rs[i])
            if r <= 0: return 0.0
        return r

    best_r = 0.0
    cands = []
    
    # 1. 100x100 grid starts for robust global coverage
    grid_res = 100
    for i in range(grid_res + 1):
        cx = xL + (xR - xL) * i / float(grid_res)
        for j in range(grid_res + 1):
            cy = yB + (yT - yB) * j / float(grid_res)
            r = get_radius(cx, cy)
            if r > 0:
                cands.append((r, cx, cy))
    
    if not cands:
        mid_x, mid_y = (xL + xR) / 2.0, (yB + yT) / 2.0
        best_r = max(best_r, get_radius(mid_x, mid_y))
    else:
        cands.sort(reverse=True)
        # 2. Hill Climbing from top candidates
        for _, sx, sy in cands[:20]:
            curr_x, curr_y = sx, sy
            curr_r = get_radius(curr_x, curr_y)
            
            step = max(xR - xL, yT - yB) / float(grid_res)
            while step > 1e-11:
                improved = False
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0), (0.7,0.7), (0.7,-0.7), (-0.7,0.7), (-0.7,-0.7)]:
                    nx, ny = curr_x + dx * step, curr_y + dy * step
                    if xL <= nx <= xR and yB <= ny <= yT:
                        nr = get_radius(nx, ny)
                        if nr > curr_r:
                            curr_r = nr
                            curr_x, curr_y = nx, ny
                            improved = True
                            break
                if not improved:
                    step *= 0.5
            best_r = max(best_r, curr_r)
            
    return max(0.0, best_r)
```
