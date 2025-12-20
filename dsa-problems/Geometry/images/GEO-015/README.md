# ASCII Visual References for GEO-015: Segment-Rectangle Intersection

## Overview

Plain ASCII sketches showing intersection cases.

## ASCII Snippets

### Crossing the rectangle
```
●---------●
|   /     |
|  /      |
●-/-------●

Segment crosses left edge → true
```

### Inside the rectangle
```
●-----------●
|   ●---●   |
|           |
●-----------●
Entire segment inside → true
```

### Outside and disjoint
```
●-----------●
|           |
|           |
●-----------●      ●------●

Segment far right, no touch → false
```
