# ASCII Visual References for GEO-009: Half-Plane Intersection

## Overview

Use these ASCII sketches to visualize half-plane intersections.

## ASCII Snippets

### Unit square from four half-planes
```
Half-planes:
  x >= 0   ( -1*x <= 0 )
  x <= 1   (  1*x <= 1 )
  y >= 0   ( -1*y <= 0 )
  y <= 1   (  1*y <= 1 )

Intersection polygon:
 (0,1) ●------● (1,1)
        |    |
        |    |
 (0,0) ●------● (1,0)
```

### Contradictory parallels (empty)
```
Lines: x <= 0  and  x >= 1
No common region → EMPTY
```

### Slanted bounds forming a triangle
```
  x + y <= 2
  x >= 0
  y >= 0

Intersection vertices:
 (0,0), (2,0), (0,2)
```
