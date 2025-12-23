---
problem_id: GEO_ANGLE_SORTING_POLAR__2841
display_id: GEO-014
slug: angle-sorting-polar
title: "Angle Sorting for Polar Order"
difficulty: Easy-Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Sorting
tags:
  - geometry
  - sorting
  - polar-angle
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-014: Angle Sorting for Polar Order

## Problem Statement

Given `n` points (distinct, no point at the origin), sort them by polar angle around the origin (0,0), in counterclockwise order. If two points have the same angle, the closer one (smaller distance to origin) should come first.

Output the points in the required order.

## ASCII Visual

```
   y
   ↑     ● (1,1)
   |  ● (1,0)   ● (0,1)
   |
   O------------→ x
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- `n` lines, each `x y` in the sorted order

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- No point is at the origin; points are distinct

## Example

**Input:**
```
3
1 0
1 1
0 1
```

**Output:**
```
1 0
1 1
0 1
```

**Explanation:**

Angles: (1,0) at 0°, (1,1) at 45°, (0,1) at 90°.

## Notes

- Use half-plane partition (upper vs lower) then cross product to sort without `atan2` for performance and stability.
- Tie-break by radius when cross product is zero.

## Related Topics

Sorting by Angle, Cross Product, Polar Coordinates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<long[]> sortByAngle(int[] xs, int[] ys) {
        // Your implementation here
        return Collections.emptyList();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] xs = new int[n], ys = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        List<long[]> res = sol.sortByAngle(xs, ys);
        for (long[] p : res) System.out.println(p[0] + " " + p[1]);
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def sort_by_angle(xs: List[int], ys: List[int]) -> List[Tuple[int,int]]:
    # Your implementation here
    return []

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    xs=[]; ys=[]
    for _ in range(n):
        xs.append(next(it)); ys.append(next(it))
    res = sort_by_angle(xs, ys)
    for x,y in res:
        print(x, y)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<long long,long long>> sortByAngle(const vector<long long>& xs, const vector<long long>& ys) {
    // Your implementation here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; ++i) cin >> xs[i] >> ys[i];
    auto res = sortByAngle(xs, ys);
    for (auto &p : res) cout << p.first << " " << p.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function sortByAngle(xs, ys) {
  // Your implementation here
  return [];
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const n = data[idx++];
  const xs = [], ys = [];
  for (let i = 0; i < n; i++) { xs.push(data[idx++]); ys.push(data[idx++]); }
  const res = sortByAngle(xs, ys);
  for (const [x,y] of res) console.log(``x`{y}`);
}

main();
```
