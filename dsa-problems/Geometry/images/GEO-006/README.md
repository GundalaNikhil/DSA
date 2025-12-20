# Emoji Visual References for GEO-006: Polygon Area (Shoelace)

## Overview

Use these emoji sketches to visualize area computation.

## Emoji Snippets

### Square
```
🟢 (0,0) ---- 🟢 (2,0)
|               |
|               |
🟢 (0,2) ---- 🟢 (2,2)
Area = 4
```

### Triangle
```
    🟢 (0,3)
   / \
  /   \
🟢-----🟢
(0,0)  (4,0)
Area = 6
```

### Shoelace notion
```
Sum xi*y(i+1) ↘
Sum yi*x(i+1) ↗
area = |sum1 - sum2| / 2
```
