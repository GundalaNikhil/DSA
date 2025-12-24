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
    public double[] absorptionStats(double[][] P, int s) {
        // Your implementation here
        return new double[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        double[][] P = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                P[i][j] = sc.nextDouble();
            }
        }

        Solution solution = new Solution();
        double[] res = solution.absorptionStats(P, s);
        if (res.length > 0) {
            System.out.printf("%.6f\n", res[0]);
            for (int i = 1; i < res.length; i++) {
                System.out.printf("%.6f", res[i]);
                if (i + 1 < res.length) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
def absorption_stats(P, s: int):
    # Your implementation here
    return []

def main():
    n, s = map(int, input().split())
    P = [list(map(float, input().split())) for _ in range(n)]
    res = absorption_stats(P, s)
    if res:
        print(f"{res[0]:.6f}")
        print(" ".join(f"{x:.6f}" for x in res[1:]))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

class Solution {
public:
    vector<double> absorptionStats(const vector<vector<double>>& P, int s) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    cin >> n >> s;
    vector<vector<double>> P(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> P[i][j];
        }
    }

    Solution solution;
    vector<double> res = solution.absorptionStats(P, s);
    if (!res.empty()) {
        cout << fixed << setprecision(6) << res[0] << "\n";
        for (int i = 1; i < (int)res.size(); i++) {
            if (i > 1) cout << " ";
            cout << fixed << setprecision(6) << res[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function absorptionStats(P, s) {
  // Your implementation here
  return [];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  if (lines.length === 0) return;
  let idx = 0;
  const first = lines[idx++].split(/\s+/).map(Number);
  const n = first[0];
  const s = first[1];
  const P = [];
  for (let i = 0; i < n; i++) {
    P.push(lines[idx++].split(/\s+/).map(Number));
  }
  const res = absorptionStats(P, s);
  if (res.length > 0) {
    console.log(res[0].toFixed(6));
    if (res.length > 1) {
      console.log(res.slice(1).map((x) => x.toFixed(6)).join(" "));
    } else {
      console.log("");
    }
  }
});
```
