---
problem_id: PDS_BLOOM_FILTER_DESIGN__4217
display_id: PDS-001
slug: bloom-filter-design
title: "Bloom Filter Design"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Bloom Filter
  - Optimization
tags:
  - probabilistic-ds
  - bloom-filter
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-001: Bloom Filter Design

## Problem Statement

Given an expected number of items `n` and a target false positive rate `f`, choose the Bloom filter parameters:

```
m = ceil(-(n * ln f) / (ln 2)^2)
k = round((m / n) * ln 2)
```

Then compute the expected false positive rate using:

```
FPR = (1 - exp(-k * n / m))^k
```

Output `m`, `k`, and `FPR`.

![Problem Illustration](../images/PDS-001/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `f`

## Output Format

- Three values: `m` (integer), `k` (integer), `FPR` (floating-point)

## Constraints

- `1 <= n <= 10^6`
- `0 < f < 1`

## Example

**Input:**

```
1000 0.01
```

**Output:**

```
9586 7 0.010035
```

**Explanation:**

m = 9586, k = 7, FPR ≈ 0.010035.

![Example Visualization](../images/PDS-001/example-1.png)

## Notes

- Use natural logarithms
- Print FPR with at least 6 decimal digits
- Accept answers with absolute error <= 1e-6

## Related Topics

Bloom Filters, Parameter Optimization, False Positives

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void computeParams(long n, double f) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long n = sc.nextLong();
        double f = sc.nextDouble();
        Solution sol = new Solution();
        sol.computeParams(n, f);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def compute_params(self, n, f):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    f = float(input_data[1])
    sol = Solution()
    sol.compute_params(n, f)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    void computeParams(long long n, double f) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    double f;
    if (!(cin >> n >> f)) return 0;
    Solution sol;
    sol.computeParams(n, f);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  computeParams(n, f) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = BigInt(input[0]);
  const f = parseFloat(input[1]);
  const sol = new Solution();
  sol.computeParams(n, f);
}

solve();
```
