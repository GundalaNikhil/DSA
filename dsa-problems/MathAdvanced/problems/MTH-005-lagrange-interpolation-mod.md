---
problem_id: MTH_LAGRANGE_INTERPOLATION_MOD__3542
display_id: MTH-005
slug: lagrange-interpolation-mod
title: "Lagrange Interpolation Mod Prime"
difficulty: Medium
difficulty_score: 60
topics:
  - MathAdvanced
  - Lagrange
tags:
  - math-advanced
  - lagrange-interpolation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-005: Lagrange Interpolation Mod Prime

## Problem Statement

Given k points (x_i, y_i) with distinct x_i values, find the value of the unique interpolating polynomial of degree at most k-1 at a query point X, all modulo a prime.

![Problem Illustration](../images/MTH-005/problem-illustration.png)

## Input Format

- Line 1: Two integers `k` (number of points) and `X` (query point)
- Line 2: An integer `MOD` (prime modulus)
- Next k lines: Two integers `x_i` and `y_i` representing each point

## Output Format

A single integer representing P(X) modulo MOD, where P is the interpolating polynomial.

## Constraints

- `1 <= k <= 200000`
- `0 <= x_i, y_i, X < MOD`
- All x_i are distinct
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**

```
2 2
1000000007
0 1
1 3
```

**Output:**

```
5
```

**Explanation:**

Points: (0, 1) and (1, 3)

The interpolating polynomial through these points is:
P(x) = 1 + 2x

P(2) = 1 + 2(2) = 5

![Example Visualization](../images/MTH-005/example-1.png)

## Notes

- Use Lagrange interpolation formula
- Compute products efficiently
- Handle modular arithmetic carefully
- Time complexity: O(k²) naive, O(k log k) with FFT optimization
- Requires modular inverse computation

## Related Topics

lagrange-interpolation, modular-arithmetic, polynomial

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long interpolate(int k, long xQuery, long mod, long[][] points) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] firstLine = line.trim().split("\\s+");
        int k = Integer.parseInt(firstLine[0]);
        long xQuery = Long.parseLong(firstLine[1]);

        long mod = Long.parseLong(br.readLine().trim());

        long[][] points = new long[k][2];
        for (int i = 0; i < k; i++) {
            String[] pLine = br.readLine().trim().split("\\s+");
            points[i][0] = Long.parseLong(pLine[0]);
            points[i][1] = Long.parseLong(pLine[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.interpolate(k, xQuery, mod, points));
    }
}
```

### Python

```python
import sys

class Solution:
    def interpolate(self, k, x_query, mod, points):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    x_query = int(input_data[1])
    mod = int(input_data[2])

    points = []
    idx = 3
    for _ in range(k):
        points.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    sol = Solution()
    print(sol.interpolate(k, x_query, mod, points))

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
    long long interpolate(int k, long long X, long long MOD, const vector<pair<long long, long long>>& points) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long X, MOD;
    if (!(cin >> k >> X >> MOD)) return 0;

    vector<pair<long long, long long>> points(k);
    for (int i = 0; i < k; i++) {
        cin >> points[i].first >> points[i].second;
    }

    Solution sol;
    cout << sol.interpolate(k, X, MOD, points) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  interpolate(k, xQuery, mod, points) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  const k = parseInt(input[0]);
  const xQuery = BigInt(input[1]);
  const mod = BigInt(input[2]);

  const points = [];
  let idx = 3;
  for (let i = 0; i < k; i++) {
    const x = BigInt(input[idx++]);
    const y = BigInt(input[idx++]);
    points.push([x, y]);
  }

  const sol = new Solution();
  console.log(sol.interpolate(k, xQuery, mod, points).toString());
}

solve();
```
