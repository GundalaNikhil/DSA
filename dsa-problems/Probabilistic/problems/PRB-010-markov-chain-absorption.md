---
problem_id: PRB_MARKOV_CHAIN_ABSORPTION__9031
display_id: PRB-010
slug: markov-chain-absorption
title: "Markov Chain Absorption"
difficulty: Medium
difficulty_score: 55
topics:
  - Probability
  - Markov Chains
  - Linear Algebra
tags:
  - probability
  - markov
  - absorption
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-010: Markov Chain Absorption

## Problem Statement

You are given a Markov chain with some absorbing states (a state with probability 1 of staying in itself). From a given start state, compute:

- Expected number of steps to absorption
- Absorption probabilities for each absorbing state

![Problem Illustration](../images/PRB-010/problem-illustration.png)

## Input Format

- First line: integer `n` and integer `s` (start state, 0-based)
- Next `n` lines: `n` real numbers (transition matrix rows)

## Output Format

- First line: expected steps to absorption
- Second line: absorption probabilities for absorbing states in increasing index order

## Constraints

- `1 <= n <= 20`
- Matrix rows sum to 1

## Example

**Input:**

```
3 0
0.5 0.5 0
0 0.5 0.5
0 0 1
```

**Output:**

```
4.000000
1.000000
```

**Explanation:**

State 2 is absorbing. Starting at 0, absorption is certain and expected steps are 4.

![Example Visualization](../images/PRB-010/example-1.png)

## Notes

- Use standard absorbing Markov chain formulas with (I-Q)^{-1}
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n^3)

## Related Topics

Markov Chains, Linear Algebra, Absorption

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void absorptionAnalysis(int n, int s, double[][] transition) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int s = sc.nextInt();
        double[][] transition = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                transition[i][j] = sc.nextDouble();
            }
        }
        Solution sol = new Solution();
        sol.absorptionAnalysis(n, s, transition);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def absorption_analysis(self, n, s, transition):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    s = int(input_data[1])
    transition = []
    idx = 2
    for i in range(n):
        row = [float(x) for x in input_data[idx:idx+n]]
        transition.append(row)
        idx += n
    sol = Solution()
    sol.absorption_analysis(n, s, transition)

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
    void absorptionAnalysis(int n, int s, const vector<vector<double>>& transition) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, s;
    if (!(cin >> n >> s)) return 0;
    vector<vector<double>> transition(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> transition[i][j];
        }
    }
    Solution sol;
    sol.absorptionAnalysis(n, s, transition);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  absorptionAnalysis(n, s, transition) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const s = parseInt(input[1]);
  const transition = [];
  let idx = 2;
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(parseFloat(input[idx++]));
    }
    transition.push(row);
  }
  const sol = new Solution();
  sol.absorptionAnalysis(n, s, transition);
}

solve();
```
