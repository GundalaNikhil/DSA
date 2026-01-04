---
problem_id: PRB_MIN_CUT_RANDOM_CONTRACTION__8305
display_id: PRB-006
slug: min-cut-random-contraction
title: "Min-Cut with Randomized Contraction"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Graphs
  - Randomized Algorithms
tags:
  - probability
  - karger
  - min-cut
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-006: Min-Cut with Randomized Contraction

## Problem Statement

Karger's randomized contraction algorithm succeeds in finding the global min-cut with probability at least:

```
P_success = 2 / (n * (n - 1))
```

Given `n` and a target confidence `P`, compute the minimum number of independent trials needed so that the overall success probability is at least `P`.

![Problem Illustration](../images/PRB-006/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `P`

## Output Format

- Single integer: minimum number of trials

## Constraints

- `2 <= n <= 10^9`
- `0 < P < 1`

## Example

**Input:**

```
4 0.9
```

**Output:**

```
13
```

**Explanation:**

For n=4, P_success = 1/6. The smallest t with 1 - (1 - 1/6)^t >= 0.9 is 13.

![Example Visualization](../images/PRB-006/example-1.png)

## Notes

- Use t = ceil(log(1-P) / log(1-P_success))
- Handle floating-point precision carefully
- Time complexity: O(1)

## Related Topics

Randomized Algorithms, Min-Cut, Probability

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minTrials(long n, double p) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long n = sc.nextLong();
        double p = sc.nextDouble();
        Solution sol = new Solution();
        System.out.println(sol.minTrials(n, p));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def min_trials(self, n, p):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    p = float(input_data[1])
    sol = Solution()
    print(sol.min_trials(n, p))

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
    long long minTrials(long long n, double p) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    double p;
    if (!(cin >> n >> p)) return 0;
    Solution sol;
    cout << sol.minTrials(n, p) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minTrials(n, p) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const p = parseFloat(input[1]);
  const sol = new Solution();
  console.log(sol.minTrials(n, p));
}

solve();
```
