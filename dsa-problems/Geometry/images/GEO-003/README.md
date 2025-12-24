# ASCII Visual References for GEO-003: Segment Intersection Count

## Overview

Images are replaced with inline ASCII art for this problem. Use these snippets for quick visuals.

## ASCII Snippets

### Simple crossing
```
S1: (0,0) ----\
               \
                \---- (2,2)
S2: (0,2) ----/

S1 and S2 intersect once.
```

### Disjoint segments
```
S1: (0,0) ---- (2,0)
S2: (0,2) ---- (2,2)
S3: (3,0) ---- (3,2)

No pairs intersect.
```

### Overlapping collinear
```
S1: (0,0) --------- (4,0)
S2:       (2,0) --------- (6,0)
Overlap counts as an intersection for the pair (S1, S2).
```

### Sweep-line concept
```
sweep x -> increasing
status (ordered by y at current x):
   S_top
   S_mid   <-- only neighbors can create new intersections next
   S_bot
```
