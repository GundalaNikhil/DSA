# ASCII Visual References for GEO-013: Point-Line Distance

## Overview

Plain ASCII sketches to visualize the closest-point cases.

## ASCII Snippets

### Perpendicular drop inside the segment
```
A ●------------------● B
         |
         |
         ● P
Closest point is vertical projection onto AB; distance is that segment.
```

### Projection beyond endpoint
```
A ●------● B          P ●

Projection falls beyond B, so closest point is B; distance = |P - B|.
```

### Vertical segment
```
A ●
|
|
● B
P ●---- horizontal distance to segment (clamped between A,B)
```
