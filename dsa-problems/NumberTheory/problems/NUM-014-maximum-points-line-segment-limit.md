---
problem_id: NUM_MAXIMUM_POINTS_LINE_SEGMENT_LIMIT__2904
display_id: NUM-014
slug: maximum-points-line-segment-limit
title: "Maximum Points on a Line Segment Length Limit"
difficulty: Medium
difficulty_score: 58
topics:
  - Number Theory
  - Geometry
  - Sorting
tags:
  - number-theory
  - geometry
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-014: Maximum Points on a Line Segment Length Limit

## Problem Statement

Given `n` points, find the maximum number of points that can lie on a single line segment whose length is at most `L`. The segment can be placed anywhere but must be collinear with the points it covers.

![Problem Illustration](../images/NUM-014/problem-illustration.png)

## Input Format

- First line: integers `n` and `L`
- Next `n` lines: two integers `x` and `y`

## Output Format

- Single integer: maximum count of points on any line segment of length <= L

## Constraints

- `1 <= n <= 2000`
- `1 <= L <= 10^6`
- `-10^6 <= x, y <= 10^6`

## Example

**Input:**

```
4 2
0 0
1 1
2 2
0 1
```

**Output:**

```
2
```

**Explanation:**

The points (0,0), (1,1), (2,2) are collinear, but any segment of length 2 can cover at most two of them.

![Example Visualization](../images/NUM-014/example-1.png)

## Notes

- For each anchor point, group other points by slope
- Within a slope group, sort by projection distance and use a sliding window
- Time complexity: O(n^2 log n)
- Space complexity: O(n)

## Related Topics

Geometry, Collinearity, Sliding Window

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxPoints(int n, int l, int[][] points) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int l = sc.nextInt();
        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.maxPoints(n, l, points));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def max_points(self, n, l, points):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    l = int(input_data[1])
    points = []
    idx = 2
    for _ in range(n):
        points.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
    sol = Solution()
    print(sol.max_points(n, l, points))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxPoints(int n, int l, const vector<pair<int, int>>& points) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, l;
    if (!(cin >> n >> l)) return 0;
    vector<pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }
    Solution sol;
    cout << sol.maxPoints(n, l, points) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxPoints(n, l, points) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const l = parseInt(input[1]);
  const points = [];
  let idx = 2;
  for (let i = 0; i < n; i++) {
    const x = parseInt(input[idx++]);
    const y = parseInt(input[idx++]);
    points.push([x, y]);
  }
  const sol = new Solution();
  console.log(sol.maxPoints(n, l, points).toString());
}

solve();
```
