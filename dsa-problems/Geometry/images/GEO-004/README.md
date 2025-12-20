# ASCII Visual References for GEO-004: Closest Pair of Points

## Overview

Images are replaced with inline ASCII art for this problem. Use these snippets for quick visuals.

## ASCII Snippets

### Simple set with closest pair
```
● (0,0)   ● (3,4)
      ● (1,1)

Closest pair: (0,0) and (1,1) with dist^2 = 2
```

### Duplicate points
```
● (5,5)
● (5,5)   => distance = 0
```

### Strip idea in divide-and-conquer
```
Left half | Right half
mid x = xm

Points within |x - xm| < sqrt(d):
        |<------- 2*sqrt(d) ------->|

Check only nearby points in y-order (few comparisons).
```
