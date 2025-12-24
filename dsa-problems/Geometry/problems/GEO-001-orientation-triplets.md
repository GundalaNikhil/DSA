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

class Solution {
    public String orientation(long x1, long y1, long x2, long y2, long x3, long y3) {
        // Your implementation here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x1 = sc.nextLong(), y1 = sc.nextLong();
        long x2 = sc.nextLong(), y2 = sc.nextLong();
        long x3 = sc.nextLong(), y3 = sc.nextLong();
        Solution sol = new Solution();
        System.out.println(sol.orientation(x1, y1, x2, y2, x3, y3));
        sc.close();
    }
}
```

### Python

```python
def orientation(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> str:
    # Your implementation here
    return ""

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) != 6:
        return
    x1, y1, x2, y2, x3, y3 = data
    print(orientation(x1, y1, x2, y2, x3, y3))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

string orientation(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    // Your implementation here
    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long x1, y1, x2, y2, x3, y3;
    if (!(cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3)) return 0;
    cout << orientation(x1, y1, x2, y2, x3, y3) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function orientation(x1, y1, x2, y2, x3, y3) {
  // Your implementation here
  return "";
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
  if (data.length !== 6) return;
  const [x1, y1, x2, y2, x3, y3] = data;
  console.log(orientation(x1, y1, x2, y2, x3, y3));
}

main();
```
