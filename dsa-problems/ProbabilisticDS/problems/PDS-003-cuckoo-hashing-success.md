---
problem_id: PDS_CUCKOO_HASHING_SUCCESS__7392
display_id: PDS-003
slug: cuckoo-hashing-success
title: "Cuckoo Hashing Success Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Hashing
  - Random Graphs
tags:
  - probabilistic-ds
  - cuckoo-hashing
  - probability
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-003: Cuckoo Hashing Success Probability

## Problem Statement

Use the following approximation for the failure probability of cuckoo hashing with two hash functions:

```
P_fail = exp(-((1 - alpha)^2 * m) / 2)
```

where `alpha` is the load factor and `m` is the table size. Compute the success probability:

```
P_success = 1 - P_fail
```

![Problem Illustration](../images/PDS-003/problem-illustration.png)

## Input Format

- Single line: integer `m` and real `alpha`

## Output Format

- Single floating-point number: `P_success`

## Constraints

- `1 <= m <= 10^6`
- `0 < alpha < 1`

## Example

**Input:**

```
50 0.8
```

**Output:**

```
0.632121
```

**Explanation:**

P_fail = exp(-1) = 0.367879, so P_success = 0.632121.

![Example Visualization](../images/PDS-003/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Cuckoo Hashing, Randomized Analysis

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double successProbability(int m, double alpha) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        double alpha = sc.nextDouble();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.successProbability(m, alpha)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def success_probability(self, m, alpha):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    m = int(input_data[0])
    alpha = float(input_data[1])
    sol = Solution()
    print(format(sol.success_probability(m, alpha), ".6f"))

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
    double successProbability(int m, double alpha) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    double alpha;
    if (!(cin >> m >> alpha)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.successProbability(m, alpha) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  successProbability(m, alpha) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const m = parseInt(input[0]);
  const alpha = parseFloat(input[1]);
  const sol = new Solution();
  console.log(sol.successProbability(m, alpha).toFixed(6));
}

solve();
```
