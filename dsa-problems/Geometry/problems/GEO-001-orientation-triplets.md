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
import java.io.*;
import java.util.*;

class Solution {
    public String orientation(long x1, long y1, long x2, long y2, long x3, long y3) {
        //Implemention here
        return "";
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
        if (data.length < 6) return;
        int idx = 0;
        long x1 = Long.parseLong(data[idx++]);
        long y1 = Long.parseLong(data[idx++]);
        long x2 = Long.parseLong(data[idx++]);
        long y2 = Long.parseLong(data[idx++]);
        long x3 = Long.parseLong(data[idx++]);
        long y3 = Long.parseLong(data[idx++]);

        Solution solution = new Solution();
        String result = solution.orientation(x1, y1, x2, y2, x3, y3);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def orientation(x1, y1, x2, y2, x3, y3):
    # //Implemention here
    return ""

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 6:
        return
    x1, y1, x2, y2, x3, y3 = map(int, data[:6])
    result = orientation(x1, y1, x2, y2, x3, y3)
    sys.stdout.write(str(result))

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

string orientation(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    //Implemention here
    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<long long> data;
    long long val;
    while (cin >> val) {
        data.push_back(val);
    }
    if (data.size() < 6) return 0;
    long long x1 = data[0];
    long long y1 = data[1];
    long long x2 = data[2];
    long long y2 = data[3];
    long long x3 = data[4];
    long long y3 = data[5];

    cout << orientation(x1, y1, x2, y2, x3, y3);
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function orientation(x1, y1, x2, y2, x3, y3) {
  //Implemention here
  return "";
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
if (data.length < 6) {
  process.exit(0);
}
let idx = 0;
const x1 = data[idx++];
const y1 = data[idx++];
const x2 = data[idx++];
const y2 = data[idx++];
const x3 = data[idx++];
const y3 = data[idx++];

const result = orientation(x1, y1, x2, y2, x3, y3);
process.stdout.write(String(result));
```

