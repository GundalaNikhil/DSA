---
problem_id: PRB_SKIP_LIST_EXPECTED_HEIGHT__6591
display_id: PRB-007
slug: skip-list-expected-height
title: "Skip List Expected Height"
difficulty: Medium
difficulty_score: 45
topics:
  - Probability
  - Data Structures
  - Logs
tags:
  - probability
  - skip-list
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-007: Skip List Expected Height

## Problem Statement

A skip list promotes each node to the next level independently with probability `p`. Given `n` inserted elements, approximate the expected maximum height of the skip list using:

```
H = log(n) / log(1/p)
```

Output `H`.

![Problem Illustration](../images/PRB-007/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `p`

## Output Format

- Single floating-point number: expected height

## Constraints

- `1 <= n <= 10^6`
- `0 < p < 1`

## Example

**Input:**

```
1024 0.5
```

**Output:**

```
10
```

**Explanation:**

log\_{1/p}(n) = log_2(1024) = 10.

![Example Visualization](../images/PRB-007/example-1.png)

## Notes

- Use natural logs in computation
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Skip Lists, Expected Value, Logarithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double expectedHeight(int n, double p) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        double p = sc.nextDouble();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.expectedHeight(n, p)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def expected_height(self, n, p):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    p = float(input_data[1])
    sol = Solution()
    print(format(sol.expected_height(n, p), ".6f"))

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
    double expectedHeight(int n, double p) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    double p;
    if (!(cin >> n >> p)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.expectedHeight(n, p) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  expectedHeight(n, p) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const p = parseFloat(input[1]);
  const sol = new Solution();
  console.log(sol.expectedHeight(n, p).toFixed(6));
}

solve();
```
