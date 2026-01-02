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
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().closestPair(xs, ys));
        sc.close();
    }
}
```

### Python

```python
def closest_pair(xs: list, ys: list) -> int:
    # Implementation here
    return 0

def main():
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

using namespace std;

class Solution {
public:
    long long closestPair(const vector<long long>& xs, const vector<long long>& ys) {
        // Implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i];
    }

    Solution sol;
    cout << sol.closestPair(xs, ys) << "\n";

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
