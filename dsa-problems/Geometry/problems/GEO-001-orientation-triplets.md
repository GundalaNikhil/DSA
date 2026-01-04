---
problem_id: GEO_ORIENTATION_TRIPLETS__4821
display_id: GEO-001
slug: orientation-triplets
title: "Orientation of Triplets"
difficulty: Easy
difficulty_score: 30
topics:
  - Computational Geometry
  - Cross Product
  - Orientation Test
tags:
  - geometry
  - orientation
  - cross-product
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-001: Orientation of Triplets

## Problem Statement

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539583/dsa/geometry/acrzqfh0ssjbz9sa3iyk.jpg)

Given three 2D points `P1(x1, y1)`, `P2(x2, y2)`, `P3(x3, y3)`, determine whether the ordered triplet is **clockwise**, **counterclockwise**, or **collinear**.

Print one of the words: `clockwise`, `counterclockwise`, or `collinear`.

```
P1 ●
     \
      \
       ● P2
        \
         \
          ● P3
```

The cross product of vectors `P1P2` and `P1P3` determines the turn direction.

## Input Format

- Single line with six integers: `x1 y1 x2 y2 x3 y3`

## Output Format

- Single word: `clockwise`, `counterclockwise`, or `collinear`

## Constraints

- `-10^9 <= xi, yi <= 10^9`

## Example

**Input:**

```
0 0 1 1 2 0
```

**Output:**

```
clockwise
```

**Explanation:**

`(1,1)` is above the segment `(0,0)->(2,0)`, giving a right turn.

```
P2 (1,1)
   / \
  /   \
P1-----P3
```

## Notes

- Use 64-bit arithmetic for the cross product to avoid overflow.
- The order of the points matters; swapping changes the orientation.
- Collinearity occurs when the cross product is exactly zero.

## Related Topics

Computational Geometry, Cross Product, Orientation Testing

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String getOrientation(long x1, long y1, long x2, long y2, long x3, long y3) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        if (parts.length < 6) return;

        long x1 = Long.parseLong(parts[0]);
        long y1 = Long.parseLong(parts[1]);
        long x2 = Long.parseLong(parts[2]);
        long y2 = Long.parseLong(parts[3]);
        long x3 = Long.parseLong(parts[4]);
        long y3 = Long.parseLong(parts[5]);

        Solution sol = new Solution();
        System.out.println(sol.getOrientation(x1, y1, x2, y2, x3, y3));
    }
}
```

### Python

```python
import sys

class Solution:
    def get_orientation(self, x1, y1, x2, y2, x3, y3):
        # Implement here
        return ""

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    parts = list(map(int, line.split()))
    if len(parts) < 6:
        return

    sol = Solution()
    print(sol.get_orientation(*parts))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string getOrientation(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long x1, y1, x2, y2, x3, y3;
    if (!(cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3)) return 0;

    Solution sol;
    cout << sol.getOrientation(x1, y1, x2, y2, x3, y3) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getOrientation(x1, y1, x2, y2, x3, y3) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 6) return;

  const x1 = BigInt(input[0]);
  const y1 = BigInt(input[1]);
  const x2 = BigInt(input[2]);
  const y2 = BigInt(input[3]);
  const x3 = BigInt(input[4]);
  const y3 = BigInt(input[5]);

  const sol = new Solution();
  console.log(sol.getOrientation(x1, y1, x2, y2, x3, y3));
}

solve();
```
