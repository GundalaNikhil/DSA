---
problem_id: PRB_RANDOMIZED_MST_VERIFICATION__6089
display_id: PRB-014
slug: randomized-mst-verification
title: "Randomized MST Verification"
difficulty: Medium
difficulty_score: 56
topics:
  - Probability
  - Graphs
  - Verification
tags:
  - probability
  - mst
  - verification
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-014: Randomized MST Verification

## Problem Statement

A randomized verification algorithm detects an incorrect MST weight with probability at least `1 / n^2` per independent trial. Given `n` and a desired confidence `C`, compute the minimum number of trials needed so that the probability of detecting an incorrect MST is at least `C`.

![Problem Illustration](../images/PRB-014/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `C`

## Output Format

- Single integer: minimum number of trials

## Constraints

- `2 <= n <= 10^9`
- `0 < C < 1`

## Example

**Input:**

```
10 0.99
```

**Output:**

```
459
```

**Explanation:**

Per-trial detection probability p = 1/n^2 = 0.01. We need the smallest t with 1 - (1-p)^t >= 0.99.

![Example Visualization](../images/PRB-014/example-1.png)

## Notes

- Use t = ceil(log(1-C) / log(1-p))
- Handle floating-point precision carefully
- Time complexity: O(1)

## Related Topics

Randomized Verification, MST, Probability

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minTrials(long n, double c) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long n = sc.nextLong();
        double c = sc.nextDouble();
        Solution sol = new Solution();
        System.out.println(sol.minTrials(n, c));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def min_trials(self, n, c):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    c = float(input_data[1])
    sol = Solution()
    print(sol.min_trials(n, c))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    long long minTrials(long long n, double c) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    double c;
    if (!(cin >> n >> c)) return 0;
    Solution sol;
    cout << sol.minTrials(n, c) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minTrials(n, c) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const c = parseFloat(input[1]);
  const sol = new Solution();
  console.log(sol.minTrials(n, c));
}

solve();
```
