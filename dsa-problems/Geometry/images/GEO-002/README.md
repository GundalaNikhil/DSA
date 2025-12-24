# ASCII Visual References for GEO-002: Point in Polygon (Winding)

## Overview

Images are replaced with inline ASCII art for this problem. Use these snippets for quick visuals.

## ASCII Snippets

### Convex polygon, inside point
```
P4 ●-------● P3
   |       |
   |  Q ●  |   => inside
   |       |
P1 ●-------● P2
```

### Concave polygon, dented region
```
P4 ●-------● P3
   |     /
   |   ● Q    => outside (in the dent)
   |  /
P1 ●-------● P2
```

### Ray casting idea
```
Q ●-----> +x
|\
| \
|  \   edges crossing upward/downward adjust winding count
```

### Boundary check
```
Q ● on edge P1----P2   => boundary
```
