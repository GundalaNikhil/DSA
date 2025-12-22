---
problem_id: GEO_SEGMENT_INTERSECTION_COUNT__1538
display_id: GEO-003
slug: segment-intersection-count
title: "Segment Intersection Count"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Intersection
tags:
  - geometry
  - sweep-line
  - segments
  - medium
premium: true
subscription_tier: basic
---

# GEO-003: Segment Intersection Count

## 📋 Problem Summary

Given `m` non-degenerate line segments in 2D, count how many distinct pairs intersect. Intersection includes touching at endpoints and overlapping collinear segments. Output the total count.

## 🌍 Real-World Scenario

**Scenario Title:** Air-Traffic Lane Conflict Detection**

An airport models taxiway centerlines as segments. Before approving a new routing plan, the system must flag how many existing lanes would conflict (overlap or cross) with proposed detours. Counting intersecting pairs lets planners focus on the busiest conflict spots.

**Why This Problem Matters:**

- Core in CAD/GIS for overlay analysis.
- Illustrates sweep-line with ordered structure (balanced tree).
- Forces careful handling of degenerates (collinear overlaps, endpoint touches).

## ASCII Examples

```
Simple crossing:

S1: (0,0) ----\
               \
                \---- (2,2)
S2: (0,2) ----/

Count = 1

Disjoint:

S1: (0,0) ---- (2,0)
S2: (0,2) ---- (2,2)
S3: (3,0) ---- (3,2)

Count = 0

Sweep line status (ordered by y at current x):

   S_top
   S_mid   <-- only neighbors can create new intersections next
   S_bot
```

## Visual

```
S1: (0,0) to (2,2)
S2: (0,2) to (2,0)
S3: (3,0) to (3,2)

S1 and S2 intersect once (count = 1). S3 is disjoint.
```

## Detailed Explanation

Brute force `O(m^2)` checks all pairs—too slow for `m = 2e5`. A sweep line reduces it to `O(m log m)`.

### Geometry Primitives

- `orient(a,b,c)`: sign of cross `(b-a) x (c-a)` (64-bit).
- `onSegment(a,b,c)`: `orient(a,b,c) = 0` and `c` lies within bounding box of `ab`.
- `segmentsIntersect(s1,s2)`: standard predicate combining orientation tests and on-segment checks.

### Sweep-Line Outline (Bentley-Ottmann style without reporting points)

1. **Events:** For each segment, store left (min x, then min y) as `start`, right as `end`. Sort events by `x`, then type (start before end), then `y`.
2. **Status (BST ordered by y at current sweep x):** When you insert a segment, check only its neighbors for new intersections. When you remove, re-link the neighbors.
3. **Counting:** Every time `segmentsIntersect(a,b)` is true for adjacent segments in the status, increment the global count. Also, when a “start” event fires, check it against current neighbors; when an “end” event fires, check the neighbor pair that becomes adjacent.

**Why neighbors?** With a vertical sweep line, only adjacent segments in y-order can intersect next; non-adjacent would have been separated by someone else that would have intersected earlier.

### Handling Overlaps and Touching

- The intersection predicate returns true for endpoint touch and collinear overlaps.
- Because we only count per pair, even if overlapping across many x, we increment once when the pair is first detected (during insertion neighbor checks). No need to store intersection points.

### Complexity

- **Time:** `O(m log m)` from event sorting and balanced BST updates.
- **Space:** `O(m)` for events and active status.

## Naive Approach

**Intuition:** Double loop and test every pair.

**Algorithm:**  
For `i < j`, if `segmentsIntersect(i,j)` then `ans++`.

**Time Complexity:** `O(m^2)` — infeasible for `m = 2e5`.  
**Space Complexity:** `O(1)` beyond input.

## Optimal Approach (Sweep)

**Key Insight:** Only neighbor segments in the sweep order can create new intersections as x advances.

**Algorithm:**
1. Build events `(x, type, id)`, where type is start/end.
2. Sort events by `(x, type, yStart)` so starts are processed before ends at same x.
3. Maintain a balanced tree keyed by the segment’s y at current sweep x (compute via interpolation).
4. On **start** of segment `s`:
   - Insert `s` into tree.
   - Let `pred` and `succ` be neighbors; if `segmentsIntersect(s, pred)` or `segmentsIntersect(s, succ)`, increment count.
5. On **end** of segment `s`:
   - Before removing, get `pred`/`succ`; after removing `s`, if both exist, test that pair and increment if intersect.
6. Output total count.

**Time Complexity:** `O(m log m)`  
**Space Complexity:** `O(m)`

## Reference Implementations

### Java

```java
import java.util.*;

class Solution {
    private static class Segment {
        long x1, y1, x2, y2;
        Segment(long a, long b, long c, long d){ x1=a; y1=b; x2=c; y2=d; }
        boolean isLeft() { return x1 < x2 || (x1 == x2 && y1 <= y2); }
    }

    private static int orient(long ax, long ay, long bx, long by, long cx, long cy) {
        long v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
        return Long.compare(v, 0);
    }

    private static boolean onSeg(long ax, long ay, long bx, long by, long cx, long cy) {
        return orient(ax, ay, bx, by, cx, cy) == 0 &&
               Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
               Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
    }

    private static boolean intersects(Segment s, Segment t) {
        int o1 = orient(s.x1, s.y1, s.x2, s.y2, t.x1, t.y1);
        int o2 = orient(s.x1, s.y1, s.x2, s.y2, t.x2, t.y2);
        int o3 = orient(t.x1, t.y1, t.x2, t.y2, s.x1, s.y1);
        int o4 = orient(t.x1, t.y1, t.x2, t.y2, s.x2, s.y2);
        if (o1 == 0 && onSeg(s.x1, s.y1, s.x2, s.y2, t.x1, t.y1)) return true;
        if (o2 == 0 && onSeg(s.x1, s.y1, s.x2, s.y2, t.x2, t.y2)) return true;
        if (o3 == 0 && onSeg(t.x1, t.y1, t.x2, t.y2, s.x1, s.y1)) return true;
        if (o4 == 0 && onSeg(t.x1, t.y1, t.x2, t.y2, s.x2, s.y2)) return true;
        return (long)o1 * o2 < 0 && (long)o3 * o4 < 0;
    }

    public long countIntersections(int[] x1, int[] y1, int[] x2, int[] y2) {
        int m = x1.length;
        Segment[] segs = new Segment[m];
        for (int i = 0; i < m; i++) segs[i] = new Segment(x1[i], y1[i], x2[i], y2[i]);

        class Event implements Comparable<Event> {
            long x; int type; int id; long y;
            Event(long x, int type, int id, long y){ this.x=x; this.type=type; this.id=id; this.y=y; }
            public int compareTo(Event o){
                if (x != o.x) return Long.compare(x, o.x);
                if (type != o.type) return Integer.compare(type, o.type); // start before end
                return Long.compare(y, o.y);
            }
        }

        List<Event> evs = new ArrayList<>(2*m);
        for (int i = 0; i < m; i++) {
            Segment s = segs[i];
            boolean left = s.isLeft();
            long sx = left ? s.x1 : s.x2;
            long sy = left ? s.y1 : s.y2;
            long ex = left ? s.x2 : s.x1;
            long ey = left ? s.y2 : s.y1;
            evs.add(new Event(sx, 0, i, sy));
            evs.add(new Event(ex, 1, i, ey));
        }
        Collections.sort(evs);

        TreeSet<Integer> status = new TreeSet<>((a,b)->{
            if (a.equals(b)) return 0;
            Segment sa=segs[a], sb=segs[b];
            // compare by y at currentX (global var)
            double ya = sa.y1 + (sa.y2 - sa.y1) * (curX - sa.x1) / (double)(sa.x2 - sa.x1);
            double yb = sb.y1 + (sb.y2 - sb.y1) * (curX - sb.x1) / (double)(sb.x2 - sb.x1);
            if (ya == yb) return Integer.compare(a,b);
            return ya < yb ? -1 : 1;
        });

        long ans = 0;
        for (Event e : evs) {
            curX = e.x;
            int id = e.id;
            if (e.type == 0) { // start
                status.add(id);
                Integer lower = status.lower(id), higher = status.higher(id);
                if (lower != null && intersects(segs[id], segs[lower])) ans++;
                if (higher != null && intersects(segs[id], segs[higher])) ans++;
            } else { // end
                Integer lower = status.lower(id), higher = status.higher(id);
                if (lower != null && higher != null && intersects(segs[lower], segs[higher])) ans++;
                status.remove(id);
            }
        }
        return ans;
    }

    private double curX = 0; // updated per event
}
```

*(Status comparator uses a `curX` field updated per event; in production, guard against vertical segments and identical y by tie-breaking on id.)*

### Python

```python
from typing import List, Tuple
import bisect

def count_intersections(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    m = len(x1)
    segs = [(x1[i], y1[i], x2[i], y2[i]) for i in range(m)]

    def orient(ax, ay, bx, by, cx, cy):
        v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
        return (v > 0) - (v < 0)

    def on_seg(ax, ay, bx, by, cx, cy):
        return orient(ax, ay, bx, by, cx, cy) == 0 and min(ax, bx) <= cx <= max(ax, bx) and min(ay, by) <= cy <= max(ay, by)

    def inter(s, t):
        ax, ay, bx, by = s
        cx, cy, dx, dy = t
        o1 = orient(ax, ay, bx, by, cx, cy)
        o2 = orient(ax, ay, bx, by, dx, dy)
        o3 = orient(cx, cy, dx, dy, ax, ay)
        o4 = orient(cx, cy, dx, dy, bx, by)
        if o1 == 0 and on_seg(ax, ay, bx, by, cx, cy): return True
        if o2 == 0 and on_seg(ax, ay, bx, by, dx, dy): return True
        if o3 == 0 and on_seg(cx, cy, dx, dy, ax, ay): return True
        if o4 == 0 and on_seg(cx, cy, dx, dy, bx, by): return True
        return o1 * o2 < 0 and o3 * o4 < 0

    events = []
    for i,(ax,ay,bx,by) in enumerate(segs):
        if (ax,ay) > (bx,by):
            ax,ay,bx,by = bx,by,ax,ay
        events.append((ax, 0, ay, i))
        events.append((bx, 1, by, i))
        segs[i] = (ax,ay,bx,by)
    events.sort()

    def y_at(seg, x):
        ax,ay,bx,by = seg
        if ax == bx: return min(ay, by)  # vertical; tie-break by lower y
        return ay + (by - ay) * (x - ax) / (bx - ax)

    status = []  # list of (y, id), kept sorted by y
    ans = 0
    for x, typ, y, idx in events:
        if typ == 0:
            ycur = y_at(segs[idx], x)
            pos = bisect.bisect_left(status, (ycur, idx))
            # check neighbors
            if pos > 0 and inter(segs[idx], segs[status[pos-1][1]]): ans += 1
            if pos < len(status) and inter(segs[idx], segs[status[pos][1]]): ans += 1
            status.insert(pos, (ycur, idx))
        else:
            ycur = y_at(segs[idx], x)
            pos = bisect.bisect_left(status, (ycur, idx))
            if 0 <= pos < len(status) and status[pos][1] == idx:
                left = status[pos-1][1] if pos-1 >= 0 else None
                right = status[pos+1][1] if pos+1 < len(status) else None
                if left is not None and right is not None and inter(segs[left], segs[right]): ans += 1
                status.pop(pos)
    return ans
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Seg { long long x1,y1,x2,y2; };

int orient(const Seg& s, long long cx, long long cy) {
    long long v = (s.x2 - s.x1) * (cy - s.y1) - (s.y2 - s.y1) * (cx - s.x1);
    return (v>0) - (v<0);
}

bool onSeg(const Seg& s, long long cx, long long cy) {
    return orient(s, cx, cy) == 0 && min(s.x1, s.x2) <= cx && cx <= max(s.x1, s.x2)
                                && min(s.y1, s.y2) <= cy && cy <= max(s.y1, s.y2);
}

bool inter(const Seg& a, const Seg& b) {
    int o1 = orient(a, b.x1, b.y1), o2 = orient(a, b.x2, b.y2);
    int o3 = orient(b, a.x1, a.y1), o4 = orient(b, a.x2, a.y2);
    if (o1 == 0 && onSeg(a, b.x1, b.y1)) return true;
    if (o2 == 0 && onSeg(a, b.x2, b.y2)) return true;
    if (o3 == 0 && onSeg(b, a.x1, a.y1)) return true;
    if (o4 == 0 && onSeg(b, a.x2, a.y2)) return true;
    return (long long)o1 * o2 < 0 && (long long)o3 * o4 < 0;
}

long long countIntersections(const vector<long long>& x1, const vector<long long>& y1,
                             const vector<long long>& x2, const vector<long long>& y2) {
    int m = x1.size();
    vector<Seg> segs(m);
    for (int i = 0; i < m; ++i) {
        segs[i] = {x1[i], y1[i], x2[i], y2[i]};
        if (make_pair(segs[i].x1, segs[i].y1) > make_pair(segs[i].x2, segs[i].y2))
            swap(segs[i].x1, segs[i].x2), swap(segs[i].y1, segs[i].y2);
    }
    struct Event { long long x; int type; int id; long long y; };
    vector<Event> evs; evs.reserve(2*m);
    for (int i = 0; i < m; ++i) {
        evs.push_back({segs[i].x1, 0, i, segs[i].y1});
        evs.push_back({segs[i].x2, 1, i, segs[i].y2});
    }
    sort(evs.begin(), evs.end(), [](const Event& a, const Event& b){
        if (a.x != b.x) return a.x < b.x;
        if (a.type != b.type) return a.type < b.type;
        return a.y < b.y;
    });

    auto yAt = [&](const Seg& s, long long x)->long double{
        if (s.x1 == s.x2) return min(s.y1, s.y2);
        return s.y1 + (long double)(s.y2 - s.y1) * (x - s.x1) / (long double)(s.x2 - s.x1);
    };

    long double curX = 0;
    struct Cmp {
        vector<Seg>* ps; long double* cx;
        bool operator()(int a, int b) const {
            if (a == b) return false;
            auto& sa = (*ps)[a]; auto& sb = (*ps)[b];
            long double ya = sa.x1==sa.x2 ? min(sa.y1, sa.y2) : sa.y1 + (long double)(sa.y2-sa.y1)*((*cx)-sa.x1)/(sa.x2-sa.x1);
            long double yb = sb.x1==sb.x2 ? min(sb.y1, sb.y2) : sb.y1 + (long double)(sb.y2-sb.y1)*((*cx)-sb.x1)/(sb.x2-sb.x1);
            if (ya == yb) return a < b;
            return ya < yb;
        }
    } cmp{&segs, &curX};

    set<int, Cmp> status(cmp);
    long long ans = 0;
    for (auto &e : evs) {
        curX = e.x;
        int id = e.id;
        if (e.type == 0) {
            auto it = status.insert(id).first;
            auto prev = it, next = it;
            if (it != status.begin()) { --prev; if (inter(segs[*prev], segs[id])) ans++; }
            ++next;
            if (next != status.end() && inter(segs[*next], segs[id])) ans++;
        } else {
            auto it = status.find(id);
            if (it != status.end()) {
                auto prev = it, next = it;
                bool hasPrev = (it != status.begin());
                if (hasPrev) --prev;
                ++next;
                if (hasPrev && next != status.end() && inter(segs[*prev], segs[*next])) ans++;
                status.erase(it);
            }
        }
    }
    return ans;
}
```

### JavaScript

```javascript
function orient(ax, ay, bx, by, cx, cy) {
  const v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
  return v === 0 ? 0 : v > 0 ? 1 : -1;
}

function onSeg(ax, ay, bx, by, cx, cy) {
  return orient(ax, ay, bx, by, cx, cy) === 0 &&
    Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
    Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
}

function inter(a, b) {
  const [ax, ay, bx, by] = a;
  const [cx, cy, dx, dy] = b;
  const o1 = orient(ax, ay, bx, by, cx, cy);
  const o2 = orient(ax, ay, bx, by, dx, dy);
  const o3 = orient(cx, cy, dx, dy, ax, ay);
  const o4 = orient(cx, cy, dx, dy, bx, by);
  if (o1 === 0 && onSeg(ax, ay, bx, by, cx, cy)) return true;
  if (o2 === 0 && onSeg(ax, ay, bx, by, dx, dy)) return true;
  if (o3 === 0 && onSeg(cx, cy, dx, dy, ax, ay)) return true;
  if (o4 === 0 && onSeg(cx, cy, dx, dy, bx, by)) return true;
  return o1 * o2 < 0 && o3 * o4 < 0;
}

function countIntersections(x1, y1, x2, y2) {
  const m = x1.length;
  const segs = [];
  const events = [];
  for (let i = 0; i < m; i++) {
    let ax = x1[i], ay = y1[i], bx = x2[i], by = y2[i];
    if (ax > bx || (ax === bx && ay > by)) [ax, ay, bx, by] = [bx, by, ax, ay];
    segs.push([ax, ay, bx, by]);
    events.push([ax, 0, ay, i]);
    events.push([bx, 1, by, i]);
  }
  events.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[3] - b[3]);

  const yAt = (s, x) => {
    const [ax, ay, bx, by] = s;
    if (ax === bx) return Math.min(ay, by);
    return ay + (by - ay) * (x - ax) / (bx - ax);
  };

  let ans = 0;
  const status = [];
  for (const [x, typ, y, id] of events) {
    if (typ === 0) {
      const ycur = yAt(segs[id], x);
      let pos = status.findIndex(pair => yAt(segs[pair[1]], x) > ycur || (yAt(segs[pair[1]], x) === ycur && pair[1] > id));
      if (pos === -1) pos = status.length;
      if (pos > 0 && inter(segs[id], segs[status[pos-1][1]])) ans++;
      if (pos < status.length && inter(segs[id], segs[status[pos][1]])) ans++;
      status.splice(pos, 0, [ycur, id]);
    } else {
      const ycur = yAt(segs[id], x);
      const pos = status.findIndex(pair => pair[1] === id);
      if (pos !== -1) {
        const left = pos > 0 ? status[pos-1][1] : null;
        const right = pos+1 < status.length ? status[pos+1][1] : null;
        if (left !== null && right !== null && inter(segs[left], segs[right])) ans++;
        status.splice(pos, 1);
      }
    }
  }
  return ans;
}
```

### Common Mistakes to Avoid

1. **Using even–odd for segments:** This is for point-in-polygon; use segment intersection predicates instead.
2. **Ignoring overlaps:** Collinear overlapping segments must count as intersecting.
3. **Overflow in orientation:** Use 64-bit arithmetic for cross products.
4. **Duplicate counting:** Only count a pair once; neighbor-check patterns above prevent double increments.
5. **Vertex double-hit:** Endpoint touching counts once; avoid counting at both insert and delete without checks.

## Testing Strategy

- Simple cross, simple disjoint, pure overlap.
- Grid of vertical + horizontal lines (many crossings).
- Nested sub-segments on the same line.
- Triangles (each edge shares endpoints with others).
- Stress with `±1e9` coordinates.

## Applications

- Map overlay operations.
- Detecting wire crossings in circuit layout.
- Preprocessing in planar graph construction.

## ASCII Recap

```
Sweep line moving -> increasing x

status (ordered by y at current x):
   S_top
   S_mid   <-- only neighbors can create new intersections next
   S_bot

Events: segment starts/ends adjust status and neighbor checks increment count.
```
