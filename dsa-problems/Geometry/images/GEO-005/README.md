# Emoji Visual References for GEO-005: Convex Hull with Interior Caps

## Overview

Use these emoji sketches to visualize the capped hull behavior.

## Emoji Snippets

### Square kept (theta small)
```
🟢 (0,0) ---- 🟢 (4,0)
|               |
|      ⚙️       |   theta = 60° → all 4 kept (90° ≥ 60°)
🟢 (0,4) ---- 🟢 (4,4)
```

### Triangle removed (theta large)
```
     🟢
    / \
   /   \
🟢 ----- 🟢
angles ≈ 60°, theta = 80° → all removed ⇒ k = 0
```

### Collinear case
```
🟢 --------- 🟢
All points on a line ⇒ angle = 180°; stays unless theta ≥ 180° (not allowed).
```
