---
problem_id: GEO_WEIGHTED_UNION_AREA__5312
display_id: GEO-010
slug: weighted-union-area-rectangles
title: "Line Sweep Weighted Union Area"
difficulty: Medium
difficulty_score: 70
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
tags:
  - geometry
  - sweep-line
  - rectangles
  - medium
premium: true
subscription_tier: basic
---

# GEO-010: Line Sweep Weighted Union Area

## 📋 Problem Summary

Given `m` weighted axis-aligned rectangles and a threshold `W`, compute the total area where the cumulative weight from overlapping rectangles is **at least** `W`. Output the area.

## 🌍 Real-World Scenario

**Scenario Title:** Signal Strength Coverage**

Multiple Wi-Fi hotspots (rectangular coverage on a floor plan) each add a certain strength. Facilities need to know how much area has signal strength at or above a required threshold `W`. Overlapping regions add their strengths.

**Why This Problem Matters:**

- Extends classic union-of-rectangles to weight thresholds.
- Demonstrates sweep-line with segment tree maintaining “length with sum >= W”.
- Handles large coordinates via compression.

## ASCII Visual

```
Rect A (w=1): (0,0)-(2,2)
Rect B (w=2): (1,1)-(3,3)

Weight >= 2 area:
- Overlap 1x1 = 1 (sum=3)
- B-only region 3 (sum=2)
Total = 4
```

## Detailed Explanation

### Sweep over x

1. For each rectangle, create two events:
   - `x = x1`, add weight `w` on interval `[y1, y2)`
   - `x = x2`, add weight `-w` on interval `[y1, y2)`
2. Sort events by `x`. Between consecutive event x-values, the coverage on y is constant.

### Segment Tree on Y (with Compression)

Compress all unique `y` endpoints. The segment tree stores:

- `add`: lazy weight added to the segment.
- `maxLen`: length of y-interval where cumulative weight >= `W`.

On update over `[y1, y2)`, propagate add; recompute `maxLen` from children:
- If node’s `maxWeight` (base + add) >= `W`, set `maxLen` to full segment length; else sum children lengths.

### Area Accumulation

For each consecutive pair of events `(x_i, x_{i+1})`:
- `covered_y = tree.maxLen`
- `delta_x = x_{i+1} - x_i`
- `area += covered_y * delta_x`

### Complexity

- Sort events: `O(m log m)`
- Updates: `O(m log n)` over compressed y.
- Space: `O(n)` for segment tree (n = unique y).

## Input/Output Clarifications

- Coordinates and weights are integers; area fits in 64-bit.
- `y` intervals are half-open `[y1, y2)` to avoid double counting at edges.
- Output just the total area as integer.

## Naive Approach

**Algorithm:** Grid sweep per unique x and y ranges with prefix sums.  
**Time/Space:** `O(n^2)` on compressed grid — infeasible for `1e5`.

## Optimal Approach (Sweep + Segment Tree)

**Algorithm Steps:**

1. Collect all `y1, y2` into array; sort unique.
2. Build events `(x, y1, y2, deltaWeight)`.
3. Sort events by `x`.
4. Iterate events:
   - Update segment tree over `[y1, y2)` with `deltaWeight`.
   - Look ahead to next event’s `x_next`; add `covered_y * (x_next - x_current)` to area.
5. Return area.

**Time Complexity:** `O(m log m)` (events + updates).  
**Space Complexity:** `O(n)` for tree and coords.

## Reference Implementations

### Python

```python
from typing import List, Tuple

def weighted_area(x1: List[int], y1: List[int], x2: List[int], y2: List[int], w: List[int], W: int) -> int:
    n = len(x1)
    ys = sorted(set(y1 + y2))
    idx = {v:i for i,v in enumerate(ys)}
    events = []
    for i in range(n):
        events.append((x1[i], 1, idx[y1[i]], idx[y2[i]], w[i]))
        events.append((x2[i], -1, idx[y1[i]], idx[y2[i]], w[i]))
    events.sort()

    segN = len(ys) - 1
    add = [0]*(4*segN)
    lenCovered = [0]*(4*segN)

    def pull(node, l, r):
        if add[node] >= W:
            lenCovered[node] = ys[r] - ys[l]
        elif r - l == 1:
            lenCovered[node] = 0
        else:
            lenCovered[node] = lenCovered[node*2] + lenCovered[node*2+1]

    def update(node, l, r, ql, qr, val):
        if qr <= l or r <= ql: return
        if ql <= l and r <= qr:
            add[node] += val
            pull(node, l, r)
            return
        mid = (l + r)//2
        update(node*2, l, mid, ql, qr, val)
        update(node*2+1, mid, r, ql, qr, val)
        pull(node, l, r)

    prevX = events[0][0]
    area = 0
    for i, (x, typ, l, r, wt) in enumerate(events):
        dx = x - prevX
        area += lenCovered[1] * dx
        update(1, 0, segN, l, r, wt if typ==1 else -wt)
        prevX = x
    return area


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
```

### Java (outline)

```java
// Implement sweep with events and a lazy segment tree storing covered length when sum>=W.
```

### C++ (outline)

```cpp
// Same sweep; compress ys; segment tree with add[] and len[] storing length where sum>=W.
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedArea(x1, y1, x2, y2, w, W) {
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
      events.push({ x: x1[i], type: 1, l: yMap.get(y1[i]), r: yMap.get(y2[i]), wt: w[i] });
      events.push({ x: x2[i], type: -1, l: yMap.get(y1[i]), r: yMap.get(y2[i]), wt: w[i] });
    }
    
    events.sort((a, b) => a.x - b.x);
    
    const segN = sortedYs.length - 1;
    if (segN <= 0) return 0;
    
    const add = new Int32Array(4 * segN).fill(0);
    const lenCovered = new Int32Array(4 * segN).fill(0);
    
    const pull = (node, l, r) => {
      if (add[node] >= W) {
        lenCovered[node] = sortedYs[r] - sortedYs[l];
      } else if (r - l === 1) {
        lenCovered[node] = 0;
      } else {
        lenCovered[node] = lenCovered[node * 2] + lenCovered[node * 2 + 1];
      }
    };
    
    const update = (node, l, r, ql, qr, val) => {
      if (qr <= l || r <= ql) return;
      if (ql <= l && r <= qr) {
        add[node] += val;
        pull(node, l, r);
        return;
      }
      const mid = Math.floor((l + r) / 2);
      update(node * 2, l, mid, ql, qr, val);
      update(node * 2 + 1, mid, r, ql, qr, val);
      pull(node, l, r);
    };
    
    let prevX = events[0].x;
    let area = 0n;
    
    for (const e of events) {
      const dx = BigInt(e.x - prevX);
      area += BigInt(lenCovered[1]) * dx;
      update(1, 0, segN, e.l, e.r, e.type === 1 ? e.wt : -e.wt);
      prevX = e.x;
    }
    
    return area.toString();
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
  
  const x1 = [], y1 = [], x2 = [], y2 = [], w = [];
  for (let i = 0; i < n; i++) x1.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) y1.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) x2.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) y2.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) w.push(parseInt(data[ptr++], 10));
  
  const W = parseInt(data[ptr++], 10);
  
  const solution = new Solution();
  console.log(solution.weightedArea(x1, y1, x2, y2, w, W));
});
```

### Common Mistakes to Avoid

1. **Forgetting half-open intervals:** Use `[y1, y2)` to avoid double counting edges.
2. **Not compressing y:** Direct coordinate range up to 1e9 is impossible for arrays.
3. **Sign errors on events:** Add weight on entering edge, subtract on leaving.
4. **Wrong covered length logic:** A node is fully covered if its lazy sum >= W.
5. **Overflow in area:** Use 64-bit for `covered_y * dx`.

### Complexity Analysis

- **Time:** `O(m log m)`  
- **Space:** `O(m)` for events + segment tree.

## Testing Strategy

- Single rectangle, weight above/below W.
- Two overlapping rectangles with different weights.
- Negative weights canceling positives.
- Large coordinates with small count.
- Multiple stacked rectangles achieving threshold only in overlap.

## ASCII Recap

```
Events sorted by x:
  at x: update y-interval weights
  area += covered_y_len * delta_x

Segment tree node:
  add = current weight sum on interval
  lenCovered = interval length where add+children >= W
```
