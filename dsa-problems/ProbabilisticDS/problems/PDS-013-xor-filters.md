---
problem_id: PDS_XOR_FILTERS__7789
display_id: PDS-013
slug: xor-filters
title: "XOR Filters"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - XOR Filters
  - False Positives
tags:
  - probabilistic-ds
  - xor-filter
  - false-positives
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-013: XOR Filters

## Problem Statement

An XOR filter stores fingerprints of `b` bits. The false positive rate is approximately:

```
FPR = 2^{-b}
```

Assume the filter uses `ceil(1.23 * n)` cells. Given `n` and `b`, compute:

- Total memory bits: `ceil(1.23 * n) * b`
- False positive rate `FPR`

![Problem Illustration](../images/PDS-013/problem-illustration.png)

## Input Format

- Single line: integers `n` and `b`

## Output Format

- Two values: `memory_bits` and `FPR`

## Constraints

- `1 <= n <= 10^6`
- `1 <= b <= 16`

## Example

**Input:**

```
1000 8
```

**Output:**

```
9840 0.003906
```

**Explanation:**

Cells = ceil(1.23 * 1000) = 1230. Memory = 1230 * 8 = 9840 bits. FPR = 1/256.

![Example Visualization](../images/PDS-013/example-1.png)

## Notes

- Use double precision for FPR
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

XOR Filters, Fingerprints, Approximate Membership

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void computeMetrics(int n, int b) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int b = sc.nextInt();
        Solution sol = new Solution();
        sol.computeMetrics(n, b);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def compute_metrics(self, n, b):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    b = int(input_data[1])
    sol = Solution()
    sol.compute_metrics(n, b)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    void computeMetrics(int n, int b) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, b;
    if (!(cin >> n >> b)) return 0;
    Solution sol;
    sol.computeMetrics(n, b);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  computeMetrics(n, b) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const b = parseInt(input[1]);
  const sol = new Solution();
  sol.computeMetrics(n, b);
}

solve();
```
