---
problem_id: GEO_CLOSEST_PAIR_POINTS__5901
display_id: GEO-004
slug: closest-pair-points
title: "Closest Pair of Points"
difficulty: Medium
difficulty_score: 65
topics:
  - Computational Geometry
  - Divide and Conquer
  - Sorting
tags:
  - geometry
  - closest-pair
  - divide-and-conquer
  - medium
premium: true
subscription_tier: basic
---

# GEO-004: Closest Pair of Points

## 📋 Problem Summary

Given `n` points, find the minimum squared Euclidean distance between any two distinct points.

Return that squared distance.

## 🌍 Real-World Scenario

**Scenario Title:** Sensor Node Spacing Audit**

An engineer audits sensor placements on a field. The closest pair of sensors indicates the tightest spacing, which could cause interference. Computing the minimum squared distance detects whether any pair violates spacing rules.

**Why This Problem Matters:**

- Classic geometry divide-and-conquer problem with a clean `O(n log n)` solution.
- Reinforces careful sorting and strip maintenance to prune comparisons.
- Squared distance avoids precision issues and extra sqrt cost.

## ASCII Examples

```
Points:
● (0,0)   ● (3,4)
      ● (1,1)

Closest pair: (0,0) and (1,1); dist^2 = 2

Duplicate points:
● (5,5)
● (5,5)
Answer = 0
```

## Detailed Explanation

### Naive Check

Compare every pair: `O(n^2)`. Works for small `n` but too slow for `n = 2e5`.

### Optimal Divide and Conquer

1. Sort points by x (and y as tiebreaker).
2. Recursively solve left and right halves to get `d = min(d_left, d_right)`.
3. Build a **strip** of points within `sqrt(d)` of the mid x. Sort strip by y.
4. For each point in the strip (in y order), compare with next points whose y differs by less than `sqrt(d)`. A known bound shows checking up to 7 following points suffices.
5. Update `d` with any smaller squared distance found in the strip.

Return `d`.

### Why 7 Comparisons?

In the strip, packing circles of radius `sqrt(d)/2` around points limits how many points can fit in the `d x 2*sqrt(d)` rectangle without being closer than `d`. This yields a constant upper bound (often ≤ 7) on necessary forward checks.

### Duplicates

If two points are identical, answer is `0`. The recursion will find this since squared distance zero is minimal.

## Input/Output Clarifications

- Output is the **squared** distance (integer).
- Coordinates fit in 64-bit; squared distance can reach `~(2e9)^2 * 2 ≈ 8e18`, so use 128-bit where needed in C++ or long in Java.
- Points may repeat.

## Edge Cases

- Two points only.
- Duplicate points (answer 0).
- All points on a line (still works; strip check finds neighbors).
- Very large coordinates (overflow safety).

## Naive Approach

**Algorithm:**

1. For every pair `(i, j)`, compute squared distance.
2. Track the minimum.

**Time Complexity:** `O(n^2)`  
**Space Complexity:** `O(1)`

**Why It Fails Here:** Too slow for `n = 2e5`.

## Optimal Approach (Divide and Conquer)

**Algorithm:**

1. Sort points by x; keep a copy sorted by y for recursion.
2. Recurse on halves, obtaining `d`.
3. Merge y-sorted lists; build strip of points with `|x - mid_x|^2 < d`.
4. For each point in strip (y-sorted), compare to next points while `(y_next - y)^2 < d` (check up to ~7).
5. Return updated `d`.

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)` for auxiliary arrays.

## Reference Implementations

### Java

```java
import java.util.*;

class Solution {
    private static class Pt {
        long x, y;
        Pt(long x, long y){ this.x = x; this.y = y; }
    }

    public long closestPair(int[] xs, int[] ys) {
        int n = xs.length;
        Pt[] pts = new Pt[n];
        for (int i = 0; i < n; i++) pts[i] = new Pt(xs[i], ys[i]);
        Arrays.sort(pts, Comparator.comparingLong(p -> p.x));
        Pt[] tmp = new Pt[n];
        return solve(pts, 0, n, tmp);
    }

    private long dist2(Pt a, Pt b) {
        long dx = a.x - b.x, dy = a.y - b.y;
        return dx*dx + dy*dy;
    }

    private long solve(Pt[] a, int l, int r, Pt[] tmp) {
        int n = r - l;
        if (n <= 3) {
            long best = Long.MAX_VALUE;
            for (int i = l; i < r; i++)
                for (int j = i+1; j < r; j++)
                    best = Math.min(best, dist2(a[i], a[j]));
            Arrays.sort(a, l, r, Comparator.comparingLong(p -> p.y));
            return best;
        }
        int mid = (l + r) >>> 1;
        long midx = a[mid].x;
        long dl = solve(a, l, mid, tmp);
        long dr = solve(a, mid, r, tmp);
        long d = Math.min(dl, dr);

        // merge by y
        int i=l, j=mid, k=0;
        while (i<mid && j<r) tmp[k++] = (a[i].y <= a[j].y) ? a[i++] : a[j++];
        while (i<mid) tmp[k++] = a[i++];
        while (j<r) tmp[k++] = a[j++];
        System.arraycopy(tmp, 0, a, l, k);

        List<Pt> strip = new ArrayList<>();
        for (int t = l; t < r; t++) {
            long dx = a[t].x - midx;
            if (dx*dx < d) strip.add(a[t]);
        }
        for (int s = 0; s < strip.size(); s++) {
            for (int t = s+1; t < strip.size(); t++) {
                long dy = strip.get(t).y - strip.get(s).y;
                if (dy*dy >= d) break;
                d = Math.min(d, dist2(strip.get(s), strip.get(t)));
            }
        }
        return d;
    }
}
```

### Python

```python
from typing import List, Tuple

def closest_pair(xs: List[int], ys: List[int]) -> int:
    pts = sorted(zip(xs, ys))

    def dist2(a: Tuple[int,int], b: Tuple[int,int]) -> int:
        dx = a[0]-b[0]; dy = a[1]-b[1]
        return dx*dx + dy*dy

    def solve(arr: List[Tuple[int,int]]) -> int:
        n = len(arr)
        if n <= 3:
            best = min(dist2(arr[i], arr[j]) for i in range(n) for j in range(i+1, n))
            arr.sort(key=lambda p: p[1])
            return best
        mid = n//2
        midx = arr[mid][0]
        left = arr[:mid]
        right = arr[mid:]
        d = min(solve(left), solve(right))
        merged = []
        i=j=0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                merged.append(left[i]); i+=1
            else:
                merged.append(right[j]); j+=1
        merged.extend(left[i:]); merged.extend(right[j:])
        arr[:] = merged
        strip = [p for p in arr if (p[0]-midx)**2 < d]
        for i in range(len(strip)):
            for j in range(i+1, min(i+8, len(strip))):
                dy = strip[j][1] - strip[i][1]
                if dy*dy >= d: break
                d = min(d, dist2(strip[i], strip[j]))
        return d

    if len(pts) != len(set(pts)):
        return 0
    return solve(pts)
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long dist2(const pair<long long,long long>& a, const pair<long long,long long>& b) {
    long long dx = a.first - b.first, dy = a.second - b.second;
    return dx*dx + dy*dy;
}

long long solve(vector<pair<long long,long long>>& pts) {
    int n = pts.size();
    if (n <= 3) {
        long long best = LLONG_MAX;
        for (int i = 0; i < n; ++i)
            for (int j = i+1; j < n; ++j)
                best = min(best, dist2(pts[i], pts[j]));
        sort(pts.begin(), pts.end(), [](auto &a, auto &b){ return a.second < b.second; });
        return best;
    }
    int mid = n/2;
    long long midx = pts[mid].first;
    vector<pair<long long,long long>> left(pts.begin(), pts.begin()+mid);
    vector<pair<long long,long long>> right(pts.begin()+mid, pts.end());
    long long d = min(solve(left), solve(right));
    merge(left.begin(), left.end(), right.begin(), right.end(), pts.begin(),
          [](auto &a, auto &b){ return a.second < b.second; });
    vector<pair<long long,long long>> strip;
    for (auto &p : pts) {
        long long dx = p.first - midx;
        if (dx*dx < d) strip.push_back(p);
    }
    for (int i = 0; i < (int)strip.size(); ++i) {
        for (int j = i+1; j < (int)strip.size() && j <= i+7; ++j) {
            long long dy = strip[j].second - strip[i].second;
            if (dy*dy >= d) break;
            d = min(d, dist2(strip[i], strip[j]));
        }
    }
    return d;
}

long long closestPair(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    vector<pair<long long,long long>> pts(n);
    for (int i = 0; i < n; ++i) pts[i] = {xs[i], ys[i]};
    sort(pts.begin(), pts.end());
    if (adjacent_find(pts.begin(), pts.end()) != pts.end()) return 0;
    return solve(pts);
}
```

### JavaScript

```javascript
function closestPair(xs, ys) {
  const n = xs.length;
  const pts = Array.from({ length: n }, (_, i) => [xs[i], ys[i]]);
  pts.sort((a, b) => (a[0] - b[0]) || (a[1] - b[1]));
  for (let i = 1; i < n; i++) {
    if (pts[i][0] === pts[i-1][0] && pts[i][1] === pts[i-1][1]) return 0;
  }
  const dist2 = (a, b) => {
    const dx = a[0] - b[0], dy = a[1] - b[1];
    return dx*dx + dy*dy;
  };
  function solve(arr) {
    const len = arr.length;
    if (len <= 3) {
      let best = Number.MAX_SAFE_INTEGER;
      for (let i = 0; i < len; i++)
        for (let j = i+1; j < len; j++)
          best = Math.min(best, dist2(arr[i], arr[j]));
      arr.sort((a,b)=>a[1]-b[1]);
      return best;
    }
    const mid = len >> 1;
    const midx = arr[mid][0];
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);
    let d = Math.min(solve(left), solve(right));
    const merged = [];
    let i=0,j=0;
    while (i<left.length && j<right.length) {
      if (left[i][1] <= right[j][1]) merged.push(left[i++]); else merged.push(right[j++]);
    }
    while (i<left.length) merged.push(left[i++]);
    while (j<right.length) merged.push(right[j++]);
    arr.splice(0, arr.length, ...merged);
    const strip = [];
    for (const p of arr) {
      const dx = p[0] - midx;
      if (dx*dx < d) strip.push(p);
    }
    for (let s = 0; s < strip.length; s++) {
      for (let t = s+1; t < strip.length && t <= s+7; t++) {
        const dy = strip[t][1] - strip[s][1];
        if (dy*dy >= d) break;
        d = Math.min(d, dist2(strip[s], strip[t]));
      }
    }
    return d;
  }
  return solve(pts);
}
```

### C++ommon Mistakes to Avoid

1. **Taking square roots.**  
   Work with squared distances to avoid precision issues and extra cost.

2. **Not sorting by y in merge.**  
   The strip step relies on y-sorted order; ensure you merge by y after recursion.

3. **Checking too many strip points.**  
   Limiting comparisons to nearby y (≈7 ahead) keeps the algorithm `O(n log n)`.

4. **Overflow in `dx*dx + dy*dy`.**  
   Use 64-bit (or bigger) for squared distances.

5. **Ignoring duplicates.**  
   Early return 0 if two identical points exist.

### C++omplexity Analysis

- **Time:** `O(n log n)`  
- **Space:** `O(n)` auxiliary for merges and strip.

## Testing Strategy

- Minimal `n=2` (distance straightforward).
- Duplicate points (expect 0).
- Points on a line equally spaced.
- Random large coordinates (check overflow safety).
- Clustered points vs. far apart to exercise strip logic.

## Applications

- Sensor/antenna spacing checks.
- Nearest neighbor preprocessing.
- Graphics collision broad-phase heuristics.

## ASCII Recap

```
Divide:
Left half | Right half

Strip around mid:
         |<---- 2*sqrt(d) ---->|
   points within dx^2 < d are checked in y-order (few comparisons)
```
