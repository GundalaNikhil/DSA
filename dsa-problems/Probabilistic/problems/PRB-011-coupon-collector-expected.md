---
problem_id: PRB_COUPON_COLLECTOR_EXPECTED__1148
display_id: PRB-011
slug: coupon-collector-expected
title: "Coupon Collector Expected Trials"
difficulty: Medium
difficulty_score: 40
topics:
  - Probability
  - Expected Value
  - Harmonic Numbers
tags:
  - probability
  - expectation
  - harmonic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-011: Coupon Collector Expected Trials

## Problem Statement

With `N` equally likely coupons, compute the expected number of draws to collect all coupons:

```
E = N * (1 + 1/2 + 1/3 + ... + 1/N)
```

![Problem Illustration](../images/PRB-011/problem-illustration.png)

## Input Format

- Single line: integer `N`

## Output Format

- Single floating-point number: expected draws

## Constraints

- `1 <= N <= 10^6`

## Example

**Input:**

```
3
```

**Output:**

```
5.500000
```

**Explanation:**

E = 3 \* (1 + 1/2 + 1/3) = 5.5.

![Example Visualization](../images/PRB-011/example-1.png)

## Notes

- Compute harmonic sum with double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(N)

## Related Topics

Coupon Collector, Harmonic Numbers, Expectation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double expectedTrials(int n) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.expectedTrials(n)));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def expected_trials(self, n):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    sol = Solution()
    print(format(sol.expected_trials(n), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>

using namespace std;

class Solution {
public:
    double expectedTrials(int n) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.expectedTrials(n) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  expectedTrials(n) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const n = parseInt(input);
  const sol = new Solution();
  console.log(sol.expectedTrials(n).toFixed(6));
}

solve();
```
