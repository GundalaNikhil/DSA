---
problem_id: GEO_MAX_OVERLAP_RECTS__6720
display_id: GEO-011
slug: max-overlap-rectangles
title: "Maximum Overlap of Rectangles"
difficulty: Medium
difficulty_score: 55
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
tags:
  - geometry
  - rectangles
  - sweep-line
  - overlap
  - medium
premium: true
subscription_tier: basic
---

# GEO-011: Maximum Overlap of Rectangles

## 📋 Problem Summary

Given `m` axis-aligned rectangles, find the maximum number of rectangles covering any single point (edges count as covered). Output that maximum overlap count.

## 🌍 Real-World Scenario

**Scenario Title:** Hotspot Density Check**

On a floor plan, each Wi-Fi router covers a rectangle. The networking team wants to know the highest number of routers covering any location to tune channel assignments and avoid interference.

**Why This Problem Matters:**

- Classic sweep-line plus segment tree problem.
- Reinforces interval updates with max tracking.
- Useful for density/coverage analytics in GIS and facility planning.

## ASCII Visual

```
Rect A: (0,0)-(2,2)
Rect B: (1,1)-(3,3)
Rect C: (2,0)-(4,2)

Max overlap = 2 (A∩B and B∩C touch, but no point has all 3)
```

## Detailed Explanation

We need the highest cumulative count of overlapping rectangles.

### Sweep over x

Create events for each rectangle:
- At `x1`: add +1 to interval `[y1, y2)`.
- At `x2`: add -1 to interval `[y1, y2)`.

Sort events by `x`. Between consecutive x-values, the y-coverage counts are constant. We only need the maximum count, not area.

### Segment Tree on Y (Coordinate Compressed)

Compress all unique `y` endpoints. Segment tree nodes store:
- `add`: lazy delta applied to the node interval.
- `mx`: maximum coverage in that interval.

Update `[y1, y2)` with `+1` or `-1`. After each update, the root `mx` gives the current max overlap at this sweep position. Track the overall maximum as we process events in order.

### Complexity

- Sort events: `O(m log m)`
- Updates: `O(m log n)` where `n` is number of unique y’s.
- Space: `O(n)` for segment tree.

## Input/Output Clarifications

- Rectangles are closed, but using half-open intervals `[y1, y2)` avoids double counting edges; max count remains correct.
- Coordinates fit in 64-bit; max overlap fits in `m`.

## Naive Approach

**Algorithm:** Check all rectangle pairs or grid by all unique x,y lines and count crossings.

**Time:** `O(m^2)` or `O(n^2)` grid—too slow for `1e5`.

## Optimal Approach (Sweep + Segment Tree)

**Algorithm Steps:**
1. Collect all `y1, y2`; sort unique for compression.
2. Build events `(x, type, y1_idx, y2_idx)` with `type = +1` for entering, `-1` for leaving.
3. Sort events by `x`.
4. Initialize segment tree arrays `add` and `mx`.
5. For each event in order:
   - Update tree on `[y1_idx, y2_idx)` with `type`.
   - Update answer with `mx[1]`.
6. Output answer.

**Time Complexity:** `O(m log m)`  
**Space Complexity:** `O(n)`

## Reference Implementations

### Python

```python
from typing import List

def max_overlap(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    n = len(x1)
    ys = sorted(set(y1 + y2))
    idx = {v:i for i,v in enumerate(ys)}
    events = []
    for i in range(n):
        events.append((x1[i], 1, idx[y1[i]], idx[y2[i]]))
        events.append((x2[i], -1, idx[y1[i]], idx[y2[i]]))
    events.sort()

    m = len(ys) - 1
    add = [0]*(4*m)
    mx = [0]*(4*m)

    def pull(node):
        mx[node] = add[node] + max(mx[node*2], mx[node*2+1])

    def update(node, l, r, ql, qr, val):
        if qr <= l or r <= ql: return
        if ql <= l and r <= qr:
            add[node] += val
            mx[node] += val
            return
        mid = (l + r)//2
        update(node*2, l, mid, ql, qr, val)
        update(node*2+1, mid, r, ql, qr, val)
        mx[node] = add[node] + max(mx[node*2], mx[node*2+1])

    ans = 0
    for x, typ, l, r in events:
        update(1, 0, m, l, r, typ)
        ans = max(ans, mx[1])
    return ans
```

### Java (outline)

```java
// Sweep events sorted by x; segment tree with add[] and mx[] storing max coverage.
```

### C++ (outline)

```cpp
// Same sweep; compress ys; segment tree supports range add and tracks max at root.
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxOverlap(x1, y1, x2, y2) {
    const n = x1.length;
    let ys = new Set();
    for (let i = 0; i < n; i++) {
      ys.add(y1[i]);
      ys.add(y2[i]);
    }
    const sortedYs = Array.from(ys).sort((a, b) => a - b);
    const yMap = new Map();
    for (let i = 0; i < sortedYs.length; i++) {
      yMap.set(sortedYs[i], i);
    }
    
    const events = [];
    for (let i = 0; i < n; i++) {
      events.push({ x: x1[i], type: 1, l: yMap.get(y1[i]), r: yMap.get(y2[i]) });
      events.push({ x: x2[i], type: -1, l: yMap.get(y1[i]), r: yMap.get(y2[i]) });
    }
    
    events.sort((a, b) => a.x - b.x);
    
    const segN = sortedYs.length - 1;
    if (segN <= 0) return 0;
    
    const add = new Int32Array(4 * segN).fill(0);
    const mx = new Int32Array(4 * segN).fill(0);
    
    const update = (node, l, r, ql, qr, val) => {
      if (qr <= l || r <= ql) return;
      if (ql <= l && r <= qr) {
        add[node] += val;
        mx[node] += val;
        return;
      }
      const mid = Math.floor((l + r) / 2);
      update(node * 2, l, mid, ql, qr, val);
      update(node * 2 + 1, mid, r, ql, qr, val);
      mx[node] = add[node] + Math.max(mx[node * 2], mx[node * 2 + 1]);
    };
    
    let ans = 0;
    for (const e of events) {
      update(1, 0, segN, e.l, e.r, e.type);
      ans = Math.max(ans, mx[1]);
    }
    
    return ans;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  
  const x1 = [], y1 = [], x2 = [], y2 = [];
  for (let i = 0; i < n; i++) x1.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) y1.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) x2.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) y2.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  console.log(solution.maxOverlap(x1, y1, x2, y2));
});
```

### Common Mistakes to Avoid

1. **Missing coordinate compression.** Direct y range up to 1e9 is infeasible.
2. **Off-by-one on intervals.** Use `[y1, y2)` consistently.
3. **Forgetting to propagate add into mx.** Root mx must include lazy value.
4. **Sorting events incorrectly.** Same x can process in any order here; if ties matter, process all at x before moving.

### Complexity Analysis

- **Time:** `O(m log m)`  
- **Space:** `O(m)` for events + tree.

## Testing Strategy

- Single rectangle (answer 1).
- Two disjoint rectangles (answer 1).
- Fully overlapping stack (answer = m).
- Chain overlaps where max is smaller than m.
- Large coordinates with small count.

## ASCII Recap

```
Events along x:
  add +1 on entering edge
  add -1 on leaving edge
Segment tree keeps max overlap on y.
Track global max after each event.
```
