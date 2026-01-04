---
problem_id: PRB_RANDOM_WALK_HITTING_PROB_2D__5274
display_id: PRB-013
slug: random-walk-hitting-prob-2d
title: "Random Walk Hitting Probability 2D"
difficulty: Hard
difficulty_score: 70
topics:
  - Probability
  - Random Walk
  - Dynamic Programming
tags:
  - probability
  - random-walk
  - dp
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-013: Random Walk Hitting Probability 2D

## Problem Statement

A simple symmetric random walk starts at `(0,0)` on the 2D integer grid. At each step, it moves one unit north, south, east, or west with equal probability.

Given a target `(a, b)` and a time horizon `T`, compute the probability that the walk hits `(a, b)` at least once within `T` steps.

![Problem Illustration](../images/PRB-013/problem-illustration.png)

## Input Format

- Single line: integers `a`, `b`, and `T`

## Output Format

- Single floating-point number: probability of hitting within `T` steps

## Constraints

- `|a|, |b| <= 10`
- `1 <= T <= 500`

## Example

**Input:**

```
1 0 1
```

**Output:**

```
0.250000
```

**Explanation:**

The walk reaches (1,0) in one step only if it moves east, which has probability 1/4.

![Example Visualization](../images/PRB-013/example-1.png)

## Notes

- Use DP over steps and bounded positions
- Track probability of first hit or use complement of never hitting
- Accept answers with absolute error <= 1e-6
- Time complexity: O(T * bound^2)

## Related Topics

Random Walks, DP, Probability

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double hittingProbability(int a, int b, int t) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int a = sc.nextInt();
        int b = sc.nextInt();
        int t = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.hittingProbability(a, b, t)));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def hitting_probability(self, a, b, t):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    t = int(input_data[2])
    sol = Solution()
    print(format(sol.hitting_probability(a, b, t), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

class Solution {
public:
    double hittingProbability(int a, int b, int t) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int a, b, t;
    if (!(cin >> a >> b >> t)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.hittingProbability(a, b, t) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  hittingProbability(a, b, t) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const a = parseInt(input[0]);
  const b = parseInt(input[1]);
  const t = parseInt(input[2]);
  const sol = new Solution();
  console.log(sol.hittingProbability(a, b, t).toFixed(6));
}

solve();
```
