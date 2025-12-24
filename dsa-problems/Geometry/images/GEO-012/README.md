# ASCII Visual References for GEO-012: Largest Empty Circle Inside Rectangle

## Overview

Plain ASCII sketches showing where the largest empty circle sits.

## ASCII Snippets

### Simple example
```
Rect: (0,0) to (4,4)
Points: (1,1), (3,1)

   y=4  ----------------
         |            |
         |     ○      |  center (2,3), r=1
         |            |
   y=0  ----------------
```

### Two points forcing center between them
```
Points: (0,0) and (0,2) on left edge
Best center near right edge, limited by distance to points and edge.
```

### No points
```
Largest circle is centered in the rectangle center with radius = min distance to edges.
```
