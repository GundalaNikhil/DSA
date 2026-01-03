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
import java.io.*;
import java.util.*;

class Solution {
    public List<long[]> sortByAngle(long[] xs, long[] ys) {
        //Implemention here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        int n = Integer.parseInt(data[idx++]);
        if (data.length < 1 + 2 * n) return;
        long[] xs = new long[n];
        long[] ys = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Long.parseLong(data[idx++]);
            ys[i] = Long.parseLong(data[idx++]);
        }

        Solution solution = new Solution();
        List<long[]> result = solution.sortByAngle(xs, ys);
        StringBuilder out = new StringBuilder();
        for (long[] p : result) {
            out.append(p[0]).append(' ').append(p[1]).append('\n');
        }
        System.out.print(out.toString());
    }
}
```

### Python

```python
import sys

def sort_by_angle(xs, ys):
    # //Implemention here
    return []

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]);
    idx += 1
    if len(data) < 1 + 2 * n:
        return
    xs = []
    ys = []
    for _ in range(n):
        xs.append(int(data[idx]));
        ys.append(int(data[idx + 1]));
        idx += 2
    result = sort_by_angle(xs, ys)
    out_lines = []
    for x, y in result:
        out_lines.append(f"{x} {y}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

vector<pair<long long, long long>> sort_by_angle(const vector<long long>& xs, const vector<long long>& ys) {
    //Implemention here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (long long i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i];
    }

    vector<pair<long long, long long>> result = sort_by_angle(xs, ys);
    for (const auto& p : result) {
        cout << p.first << " " << p.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function sortByAngle(xs, ys) {
  //Implemention here
  return [];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
let idx = 0;
const n = data[idx++];
if (!Number.isFinite(n) || data.length < 1 + 2 * n) {
  process.exit(0);
}
const xs = [];
const ys = [];
for (let i = 0; i < n; i++) {
  xs.push(data[idx++]);
  ys.push(data[idx++]);
}

const result = sortByAngle(xs, ys);
let out = [];
for (const p of result) {
  out.push(p[0] + " " + p[1]);
}
process.stdout.write(out.join("\n"));
```

