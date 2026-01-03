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

class Main {

static class Solution {
    private static class Pt {
        long x, y;
        Pt(long x, long y){ this.x = x; this.y = y; }
    }

    public long closestPair(long[] xs, long[] ys) {
        //Implement here
        return 0L;
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

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().closestPair(xs, ys));
    }
}
```

### Python

```python
from typing import List, Tuple

def closest_pair(xs: List[int], ys: List[int]) -> int:
    # //Implement here
    return 0
def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        n = next(it)
        xs = []
        ys = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))
        print(closest_pair(xs, ys))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;


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
    //Implement here
    return 0;
}

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
const readline = require('readline');

class Solution {
    solve(xs, ys) {
      //Implement here
      return 0;
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

