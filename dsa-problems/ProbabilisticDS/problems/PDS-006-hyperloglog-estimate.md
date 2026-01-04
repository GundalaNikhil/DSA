---
problem_id: PDS_HYPERLOGLOG_ESTIMATE__1507
display_id: PDS-006
slug: hyperloglog-estimate
title: "HyperLogLog Cardinality Estimate"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - HyperLogLog
  - Cardinality Estimation
tags:
  - probabilistic-ds
  - hyperloglog
  - cardinality
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-006: HyperLogLog Cardinality Estimate

## Problem Statement

Given `m` HyperLogLog registers (m is a power of two) and their maximum values, compute the cardinality estimate:

```
E = alpha_m * m^2 / sum(2^{-register[i]})
```

Use `alpha_m` as:

- 0.673 if m = 16
- 0.697 if m = 32
- 0.709 if m = 64
- otherwise: 0.7213 / (1 + 1.079 / m)

If `E <= 2.5 * m` and there are `V` zero registers, apply linear counting:

```
E = m * ln(m / V)
```

Output `E`.

![Problem Illustration](../images/PDS-006/problem-illustration.png)

## Input Format

- First line: integer `m`
- Second line: `m` integers (register values)

## Output Format

- Single floating-point number: estimated cardinality

## Constraints

- `m` is a power of two, `16 <= m <= 65536`
- `0 <= register[i] <= 64`

## Example

**Input:**

```
16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

**Output:**

```
21.536000
```

**Explanation:**

With all registers equal to 1, the raw estimate is 21.536.

![Example Visualization](../images/PDS-006/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(m)

## Related Topics

HyperLogLog, Cardinality Estimation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double estimateCardinality(int m, int[] registers) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        int[] registers = new int[m];
        for (int i = 0; i < m; i++) registers[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.estimateCardinality(m, registers)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def estimate_cardinality(self, m, registers):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    m = int(input_data[0])
    registers = [int(x) for x in input_data[1:1+m]]
    sol = Solution()
    print(format(sol.estimate_cardinality(m, registers), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    double estimateCardinality(int m, const vector<int>& registers) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    if (!(cin >> m)) return 0;
    vector<int> registers(m);
    for (int i = 0; i < m; i++) cin >> registers[i];
    Solution sol;
    cout << fixed << setprecision(6) << sol.estimateCardinality(m, registers) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimateCardinality(m, registers) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const m = parseInt(input[0]);
  const registers = [];
  for (let i = 0; i < m; i++) registers.push(parseInt(input[1 + i]));
  const sol = new Solution();
  console.log(sol.estimateCardinality(m, registers).toFixed(6));
}

solve();
```
