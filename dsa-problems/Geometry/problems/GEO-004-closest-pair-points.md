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
time_limit: 2000
memory_limit: 256
---

# GEO-004: Closest Pair of Points

## Problem Statement

Given `n` points in 2D, find the **minimum squared Euclidean distance** between any pair of distinct points.

Return that squared distance as an integer.

## ASCII Visual

```
Points:
● (0,0)   ● (3,4)
      ● (1,1)

Closest pair: (0,0) and (1,1) with dist^2 = 1^2 + 1^2 = 2
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single integer: minimum squared distance among all pairs

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`
- Points are not guaranteed distinct (distance can be 0).

## Example

**Input:**
```
3
0 0
3 4
1 1
```

**Output:**
```
2
```

**Explanation:**

Closest pair is `(0,0)` and `(1,1)` with squared distance `2`.

## Notes

- Using squared distance avoids floating-point operations.
- Divide-and-conquer with a strip check achieves `O(n log n)`.
- If duplicate points exist, answer is `0`.

## Related Topics

Computational Geometry, Sorting, Divide and Conquer

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long closestPair(long[] xs, long[] ys) {
        // Implementation here
        return 0;
    }
}

class Main {

static class Solution {
    private static class Pt {
        long x, y;
        Pt(long x, long y){ this.x = x; this.y = y; }
    }

    public long closestPair(long[] xs, long[] ys) {
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

```
// No template available
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    long long dist2(const pair<long long,long long>& a, const pair<long long,long long>& b) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    cout << closestPair(xs, ys) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(xs, ys) {
    // Implementation here
    return null;
  }
}

const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let pts = xs.map((x, i) => ({x: BigInt(x), y: BigInt(ys[i])}));
        // Sort by X
        pts.sort((a, b) => {
            if (a.x < b.x) return -1;
            if (a.x > b.x) return 1;
            return 0;
        });
        
        let unique = new Set(pts.map(p => `${p.x},${p.y}`));
        if (unique.size !== pts.length) return "0";
        
        const distSq = (a, b) => (a.x-b.x)**2n + (a.y-b.y)**2n;
        const minBig = (a, b) => (a === -1n) ? b : ((b === -1n) ? a : (a < b ? a : b));
        
        const rec = (arr) => {
            let n = arr.length;
            if (n <= 3) {
                let minD = -1n;
                for(let i=0; i<n; i++) {
                    for(let j=i+1; j<n; j++) {
                        let d = distSq(arr[i], arr[j]);
                        if (minD === -1n || d < minD) minD = d;
                    }
                }
                arr.sort((a, b) => {
                    if (a.y < b.y) return -1;
                    if (a.y > b.y) return 1;
                    return 0;
                });
                return minD === -1n ? 0n : minD; 
            }
            
            let mid = Math.floor(n / 2);
            let midX = arr[mid].x;
            let left = arr.slice(0, mid);
            let right = arr.slice(mid);
            
            let dL = rec(left);
            let dR = rec(right);
            
            let d = minBig(dL, dR);
            if (d === -1n) d = 0n;
            
            arr.sort((a, b) => {
                if (a.y < b.y) return -1;
                if (a.y > b.y) return 1;
                return 0;
            });
            
            let strip = [];
            for(let p of arr) {
                let dx = p.x - midX;
                if (d === -1n || dx*dx < d) strip.push(p);
            }
            
            for(let i=0; i<strip.length; i++) {
                for(let j=i+1; j<strip.length; j++) {
                     let dy = strip[j].y - strip[i].y;
                     if (d !== -1n && dy*dy >= d) break;
                     let currD = distSq(strip[i], strip[j]);
                     if (d === -1n || currD < d) d = currD;
                }
            }
            return d === -1n ? 0n : d;
        };
        
        return rec(pts).toString();
    }
}
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => {
    let tokens = line.match(/\S+/g) || [];
    lines.push(...tokens);
});
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => next(); 

    let n = parseInt(nextInt());
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(xs, ys));
});
```
