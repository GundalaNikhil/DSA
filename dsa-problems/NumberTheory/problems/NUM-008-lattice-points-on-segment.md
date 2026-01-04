---
problem_id: NUM_LATTICE_POINTS_ON_SEGMENT__6330
display_id: NUM-008
slug: lattice-points-on-segment
title: "Counting Lattice Points On Segment"
difficulty: Easy
difficulty_score: 28
topics:
  - Number Theory
  - Geometry
  - GCD
tags:
  - number-theory
  - geometry
  - gcd
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-008: Counting Lattice Points On Segment

## Problem Statement

Given two endpoints `(x1, y1)` and `(x2, y2)` with integer coordinates, count the number of integer lattice points on the closed line segment between them.

![Problem Illustration](../images/NUM-008/problem-illustration.png)

## Input Format

- Single line: four integers `x1 y1 x2 y2`

## Output Format

- Single integer: number of lattice points on the segment

## Constraints

- `|x1|, |y1|, |x2|, |y2| <= 10^9`

## Example

**Input:**

```
0 0 6 4
```

**Output:**

```
3
```

**Explanation:**

dx = 6, dy = 4, gcd(6,4) = 2, so answer = 2 + 1 = 3.

Points are (0,0), (3,2), (6,4).

![Example Visualization](../images/NUM-008/example-1.png)

## Notes

- The count equals gcd(|dx|, |dy|) + 1
- Time complexity: O(log max(|dx|,|dy|))
- Space complexity: O(1)

## Related Topics

GCD, Lattice Geometry

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countLatticePoints(long x1, long y1, long x2, long y2) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x1 = sc.nextLong();
        long y1 = sc.nextLong();
        long x2 = sc.nextLong();
        long y2 = sc.nextLong();
        Solution sol = new Solution();
        System.out.println(sol.countLatticePoints(x1, y1, x2, y2));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_lattice_points(self, x1, y1, x2, y2):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x1 = int(input_data[0])
    y1 = int(input_data[1])
    x2 = int(input_data[2])
    y2 = int(input_data[3])
    sol = Solution()
    print(sol.count_lattice_points(x1, y1, x2, y2))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    long long countLatticePoints(long long x1, long long y1, long long x2, long long y2) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long x1, y1, x2, y2;
    if (!(cin >> x1 >> y1 >> x2 >> y2)) return 0;
    Solution sol;
    cout << sol.countLatticePoints(x1, y1, x2, y2) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countLatticePoints(x1, y1, x2, y2) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 4) return;
  const x1 = BigInt(input[0]);
  const y1 = BigInt(input[1]);
  const x2 = BigInt(input[2]);
  const y2 = BigInt(input[3]);
  const sol = new Solution();
  console.log(sol.countLatticePoints(x1, y1, x2, y2).toString());
}

solve();
```
