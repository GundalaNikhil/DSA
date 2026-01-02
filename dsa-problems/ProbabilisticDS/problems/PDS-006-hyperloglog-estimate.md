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
    public double hllEstimate(int m, int[] registers) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int[] registers = new int[m];
            for (int i = 0; i < m; i++) {
                registers[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.hllEstimate(m, registers)));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def hll_estimate(m: int, registers):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    registers = list(map(int, data[1:]))
    print(f"{hll_estimate(m, registers):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double hllEstimate(int m, const vector<int>& registers) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (cin >> m) {
        vector<int> registers(m);
        for (int i = 0; i < m; i++) cin >> registers[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.hllEstimate(m, registers) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function hllEstimate(m, registers) {
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
  const registers = [];
  for (let i = 0; i < m; i++) registers.push(parseInt(data[idx++], 10));
  console.log(hllEstimate(m, registers).toFixed(6));
});
```

