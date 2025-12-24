# ASCII Visual References for GEO-001: Orientation of Triplets

## Overview

Images are replaced with inline ASCII art for this problem. Use the snippets below wherever a visual reference is needed.

## ASCII Snippets

### Orientation Cases
```
Counterclockwise (left turn):

    P3
     \
      \
       ● P2
      /
     /
    ● P1

Clockwise (right turn):

● P1
  \
   \
    ● P2
     \
      \
       P3

Collinear:

● P1 ----- ● P2 ----- ● P3
```

### Cross Product Sign
```
cross = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

cross > 0  => counterclockwise
cross < 0  => clockwise
cross == 0 => collinear
```
