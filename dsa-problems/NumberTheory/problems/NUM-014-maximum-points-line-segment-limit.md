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
    public int maxPointsOnSegment(int[][] points, int L) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int L = sc.nextInt();
        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxPointsOnSegment(points, L));
        sc.close();
    }
}
```

### Python

```python
def max_points_on_segment(points, L):
    # Your implementation here
    return 0

def main():
    n, L = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(max_points_on_segment(points, L))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxPointsOnSegment(const vector<vector<int>>& points, int L) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, L;
    cin >> n >> L;
    vector<vector<int>> points(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> points[i][0] >> points[i][1];
    }

    Solution solution;
    cout << solution.maxPointsOnSegment(points, L) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function maxPointsOnSegment(points, L) {
  // Your implementation here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const L = parseInt(data[idx++], 10);
  const points = [];
  for (let i = 0; i < n; i++) {
    const x = parseInt(data[idx++], 10);
    const y = parseInt(data[idx++], 10);
    points.push([x, y]);
  }
  console.log(maxPointsOnSegment(points, L));
});
```
