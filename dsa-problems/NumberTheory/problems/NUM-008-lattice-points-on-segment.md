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
    private long gcd(long a, long b) {
        return 0;
    }

    public long latticePoints(long x1, long y1, long x2, long y2) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long x1 = sc.nextLong();
            long y1 = sc.nextLong();
            long x2 = sc.nextLong();
            long y2 = sc.nextLong();

            Solution solution = new Solution();
            System.out.println(solution.latticePoints(x1, y1, x2, y2));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from math import gcd

def lattice_points(x1: int, y1: int, x2: int, y2: int) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x1, y1, x2, y2 = map(int, data)
    print(lattice_points(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <numeric>
#include <cmath>

using namespace std;

class Solution {
    long long gcd(long long a, long long b) {
        return 0;
    }

public:
    long long latticePoints(long long x1, long long y1, long long x2, long long y2) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x1, y1, x2, y2;
    if (cin >> x1 >> y1 >> x2 >> y2) {
        Solution solution;
        cout << solution.latticePoints(x1, y1, x2, y2) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function gcd(a, b) {
    return 0;
  }

function latticePoints(x1, y1, x2, y2) {
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
  const x1 = parseInt(data[0], 10);
  const y1 = parseInt(data[1], 10);
  const x2 = parseInt(data[2], 10);
  const y2 = parseInt(data[3], 10);
  console.log(latticePoints(x1, y1, x2, y2));
});
```

