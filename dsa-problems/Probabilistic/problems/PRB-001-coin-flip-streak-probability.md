---
problem_id: PRB_COIN_FLIP_STREAK_PROBABILITY__1842
display_id: PRB-001
slug: coin-flip-streak-probability
title: "Coin Flip Streak Probability"
difficulty: Medium
difficulty_score: 40
topics:
  - Probability
  - Dynamic Programming
  - Markov Chains
tags:
  - probability
  - dp
  - streaks
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-001: Coin Flip Streak Probability

## Problem Statement

A fair coin is flipped `n` times. Compute the probability of getting at least one streak of `k` consecutive heads.

![Problem Illustration](../images/PRB-001/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single floating-point number: the probability

## Constraints

- `1 <= n <= 60`
- `1 <= k <= n`

## Example

**Input:**

```
3 2
```

**Output:**

```
0.375
```

**Explanation:**

The sequences with at least one streak of two consecutive heads are HHT, HHH, and THH. Each has probability 1/8, total 3/8 = 0.375.

![Example Visualization](../images/PRB-001/example-1.png)

## Notes

- Use DP with state (position, current run of heads)
- Probability = 1 - probability of no length-k streak
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n \* k)

## Related Topics

Probability, DP, Streaks

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double streakProbability(int n, int k) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.streakProbability(n, k)));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def streak_probability(self, n, k):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    sol = Solution()
    print(format(sol.streak_probability(n, k), ".6f"))

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
    double streakProbability(int n, int k) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.streakProbability(n, k) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  streakProbability(n, k) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const sol = new Solution();
  console.log(sol.streakProbability(n, k).toFixed(6));
}

solve();
```
