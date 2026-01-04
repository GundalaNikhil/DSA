---
problem_id: PRB_MONTE_CARLO_PI__2365
display_id: PRB-004
slug: monte-carlo-pi
title: "Monte Carlo Estimation of Pi"
difficulty: Easy
difficulty_score: 30
topics:
  - Probability
  - Statistics
  - Monte Carlo
tags:
  - probability
  - monte-carlo
  - statistics
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-004: Monte Carlo Estimation of Pi

## Problem Statement

You sampled `N` random points in the unit square and counted how many fell inside the quarter circle of radius 1. Given `N` and `C` (count inside), compute:

- The estimate of π: `pi_hat = 4 * C / N`
- A 95% confidence half-width: `err = 1.96 * sqrt(p*(1-p)/N) * 4` where `p = C/N`

![Problem Illustration](../images/PRB-004/problem-illustration.png)

## Input Format

- Single line: integers `N` and `C`

## Output Format

- Two floating-point numbers: `pi_hat` and `err`

## Constraints

- `1 <= N <= 10^6`
- `0 <= C <= N`

## Example

**Input:**

```
10000 7854
```

**Output:**

```
3.141600 0.032187
```

**Explanation:**

p = 0.7854, pi_hat = 3.1416. The error half-width is about 0.032187.

![Example Visualization](../images/PRB-004/example-1.png)

## Notes

- Print values with at least 6 decimal digits
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Monte Carlo, Confidence Intervals, Estimation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void estimatePi(int n, int c) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int c = sc.nextInt();
        Solution sol = new Solution();
        sol.estimatePi(n, c);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def estimate_pi(self, n, c):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    c = int(input_data[1])
    sol = Solution()
    sol.estimate_pi(n, c)

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
    void estimatePi(int n, int c) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, c;
    if (!(cin >> n >> c)) return 0;
    Solution sol;
    sol.estimatePi(n, c);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimatePi(n, c) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const c = parseInt(input[1]);
  const sol = new Solution();
  sol.estimatePi(n, c);
}

solve();
```
