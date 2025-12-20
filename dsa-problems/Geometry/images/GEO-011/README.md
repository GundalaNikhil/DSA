# ASCII Visual References for GEO-011: Maximum Overlap of Rectangles

## Overview

Plain ASCII sketches to illustrate overlap counting.

## ASCII Snippets

### Overlap of three rectangles
```
Rect A: (0,0)-(2,2)
Rect B: (1,1)-(3,3)
Rect C: (2,0)-(4,2)

Max overlap:
  A∩B region has 2
  B∩C region has 2
No triple intersection → answer 2
```

### Fully stacked rectangles
```
All rectangles identical:
max overlap = number of rectangles (all cover the same region)
```

### Disjoint rectangles
```
No overlaps:
max overlap = 1
```
