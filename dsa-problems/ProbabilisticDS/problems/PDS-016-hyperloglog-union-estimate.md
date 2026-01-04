---
problem_id: PDS_PROBLEM_16__7318
display_id: PDS-016
slug: hyperloglog-union-estimate
title: "HyperLogLog Union Estimate"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - HyperLogLog
  - Cardinality Estimation
tags:
  - probabilistic-ds
  - hyperloglog
  - union
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-016: HyperLogLog Union Estimate

## Problem Statement

Given two HyperLogLog sketches with the same number of registers `m`, compute the union estimate by taking register-wise maximums and then applying the HLL estimate:

```
E = alpha_m * m^2 / sum(2^{-register[i]})
```

Use `alpha_m` as:

- 0.673 if m = 16
- 0.697 if m = 32
- 0.709 if m = 64
- otherwise: 0.7213 / (1 + 1.079 / m)

Ignore small-range corrections.

![Problem Illustration](../images/PDS-016/problem-illustration.png)

## Input Format

- First line: integer `m`
- Second line: `m` integers (registers for sketch A)
- Third line: `m` integers (registers for sketch B)

## Output Format

- Single floating-point number: union cardinality estimate

## Constraints

- `m` is a power of two, `16 <= m <= 65536`
- `0 <= register[i] <= 64`

## Example

**Input:**

```
16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
```

**Output:**

```
43.072000
```

**Explanation:**

Union registers are all 2. The estimate is 43.072.

![Example Visualization](../images/PDS-016/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(m)

## Related Topics

HyperLogLog, Sketch Union

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double estimateUnionCardinality(int m, int[] regA, int[] regB) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        int[] regA = new int[m];
        for (int i = 0; i < m; i++) regA[i] = sc.nextInt();
        int[] regB = new int[m];
        for (int i = 0; i < m; i++) regB[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.estimateUnionCardinality(m, regA, regB)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def estimate_union_cardinality(self, m, reg_a, reg_b):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    m = int(input_data[0])
    reg_a = [int(x) for x in input_data[1:1+m]]
    reg_b = [int(x) for x in input_data[1+m:1+2*m]]
    sol = Solution()
    print(format(sol.estimate_union_cardinality(m, reg_a, reg_b), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double estimateUnionCardinality(int m, const vector<int>& regA, const vector<int>& regB) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    if (!(cin >> m)) return 0;
    vector<int> regA(m), regB(m);
    for (int i = 0; i < m; i++) cin >> regA[i];
    for (int i = 0; i < m; i++) cin >> regB[i];
    Solution sol;
    cout << fixed << setprecision(6) << sol.estimateUnionCardinality(m, regA, regB) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimateUnionCardinality(m, regA, regB) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const m = parseInt(input[0]);
  const regA = [];
  for (let i = 0; i < m; i++) regA.push(parseInt(input[1 + i]));
  const regB = [];
  for (let i = 0; i < m; i++) regB.push(parseInt(input[1 + m + i]));
  const sol = new Solution();
  console.log(sol.estimateUnionCardinality(m, regA, regB).toFixed(6));
}

solve();
```
