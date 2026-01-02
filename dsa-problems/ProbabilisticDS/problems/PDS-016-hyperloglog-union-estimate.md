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
    public double hllUnionEstimate(int m, int[] a, int[] b) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int[] a = new int[m];
            int[] b = new int[m];
            for (int i = 0; i < m; i++) a[i] = sc.nextInt();
            for (int i = 0; i < m; i++) b[i] = sc.nextInt();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.hllUnionEstimate(m, a, b)));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def hll_union_estimate(m: int, a, b):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    # The next m integers are A
    a = []
    idx = 1
    for _ in range(m):
        a.append(int(data[idx]))
        idx += 1
    # The next m integers are B
    b = []
    for _ in range(m):
        b.append(int(data[idx]))
        idx += 1
        
    print(f"{hll_union_estimate(m, a, b):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

class Solution {
public:
    double hllUnionEstimate(int m, const vector<int>& a, const vector<int>& b) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (cin >> m) {
        vector<int> a(m), b(m);
        for (int i = 0; i < m; i++) cin >> a[i];
        for (int i = 0; i < m; i++) cin >> b[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.hllUnionEstimate(m, a, b) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function hllUnionEstimate(m, a, b) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const m = parseInt(data[idx++], 10);
  const a = [];
  const b = [];
  for (let i = 0; i < m; i++) a.push(parseInt(data[idx++], 10));
  for (let i = 0; i < m; i++) b.push(parseInt(data[idx++], 10));
  console.log(hllUnionEstimate(m, a, b).toFixed(6));
});
```

