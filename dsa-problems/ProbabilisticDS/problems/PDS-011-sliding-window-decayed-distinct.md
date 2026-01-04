---
problem_id: PDS_SLIDING_WINDOW_DECAYED_DISTINCT__5072
display_id: PDS-011
slug: sliding-window-decayed-distinct
title: "Sliding Window Distinct with Exponential Decay"
difficulty: Medium
difficulty_score: 56
topics:
  - Probabilistic Data Structures
  - Sliding Window
  - Decay
tags:
  - probabilistic-ds
  - sliding-window
  - decay
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-011: Sliding Window Distinct with Exponential Decay

## Problem Statement

Estimate a decayed distinct count using the last-seen time of each distinct item. Given current time `T`, decay factor `lambda`, and last-seen timestamps `t_i`, compute:

```
Estimate = sum exp(-lambda * (T - t_i))
```

![Problem Illustration](../images/PDS-011/problem-illustration.png)

## Input Format

- First line: integer `T`, real `lambda`, and integer `m`
- Second line: `m` integers (last-seen times)

## Output Format

- Single floating-point number: decayed distinct estimate

## Constraints

- `0 <= T <= 10^9`
- `0 < lambda <= 1`
- `1 <= m <= 100000`
- `0 <= t_i <= T`

## Example

**Input:**

```
10 0.1 3
10 8 5
```

**Output:**

```
2.425261
```

**Explanation:**

exp(0) + exp(-0.2) + exp(-0.5) = 2.425261.

![Example Visualization](../images/PDS-011/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(m)

## Related Topics

Exponential Decay, Sliding Window, Distinct Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double estimateDecayedDistinct(int t, double lambda, int m, int[] lastSeen) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int t = sc.nextInt();
        double lambda = sc.nextDouble();
        int m = sc.nextInt();
        int[] lastSeen = new int[m];
        for (int i = 0; i < m; i++) lastSeen[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.estimateDecayedDistinct(t, lambda, m, lastSeen)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def estimate_decayed_distinct(self, t, lam, m, last_seen):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    lam = float(input_data[1])
    m = int(input_data[2])
    last_seen = [int(x) for x in input_data[3:3+m]]
    sol = Solution()
    print(format(sol.estimate_decayed_distinct(t, lam, m, last_seen), ".6f"))

if __name__ == "__main__":
    solve()
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
    double estimateDecayedDistinct(int t, double lambda, int m, const vector<int>& lastSeen) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t, m;
    double lambda;
    if (!(cin >> t >> lambda >> m)) return 0;
    vector<int> lastSeen(m);
    for (int i = 0; i < m; i++) cin >> lastSeen[i];
    Solution sol;
    cout << fixed << setprecision(6) << sol.estimateDecayedDistinct(t, lambda, m, lastSeen) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimateDecayedDistinct(t, lambda, m, lastSeen) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const t = parseInt(input[0]);
  const lambda = parseFloat(input[1]);
  const m = parseInt(input[2]);
  const lastSeen = [];
  for (let i = 0; i < m; i++) lastSeen.push(parseInt(input[3 + i]));
  const sol = new Solution();
  console.log(sol.estimateDecayedDistinct(t, lambda, m, lastSeen).toFixed(6));
}

solve();
```
