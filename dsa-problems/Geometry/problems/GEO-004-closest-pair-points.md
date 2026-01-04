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
    public long findClosestPairSquaredDistance(int n, long[][] points) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[][] points = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] p = br.readLine().trim().split("\\s+");
            points[i][0] = Long.parseLong(p[0]);
            points[i][1] = Long.parseLong(p[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.findClosestPairSquaredDistance(n, points));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_closest_pair_squared_distance(self, n, points):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1
    points = []
    for _ in range(n):
        points.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    sol = Solution()
    print(sol.find_closest_pair_squared_distance(n, points))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long findClosestPairSquaredDistance(int n, vector<pair<long long, long long>>& points) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }

    Solution sol;
    cout << sol.findClosestPairSquaredDistance(n, points) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findClosestPairSquaredDistance(n, points) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const points = [];
  for (let i = 0; i < n; i++) {
    points.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.findClosestPairSquaredDistance(n, points).toString());
}

solve();
```
