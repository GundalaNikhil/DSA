# ASCII Visual References for GEO-010: Weighted Union Area of Rectangles

## Overview

Plain ASCII sketches showing weighted overlaps and sweep concept.

## ASCII Snippets

### Two overlapping rectangles with weights
```
Rect A (w=1): (0,0)-(2,2)
Rect B (w=2): (1,1)-(3,3)

Overlap (weight sum = 3) area = 1
B-only region (weight sum = 2) area = 3
Total area where sum >= 2 is 4
```

### Sweep-line idea
```
Events at x = x1 (add w) and x = x2 (subtract w)
Between events:
  covered_y = length where weight >= W (from segment tree)
  area += covered_y * delta_x
```
