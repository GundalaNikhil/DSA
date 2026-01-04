---
problem_id: PRB_TREAP_PRIORITY_INVARIANTS__7410
display_id: PRB-009
slug: treap-priority-invariants
title: "Treap Priority Invariants"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Data Structures
  - Expected Value
tags:
  - probability
  - treap
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-009: Treap Priority Invariants

## Problem Statement

For a treap built from `n` distinct keys with random priorities, the expected depth analysis depends on the harmonic number. Compute:

- `H_n = 1 + 1/2 + 1/3 + ... + 1/n` (the `n`-th harmonic number)

Note: While the expected depth of a node is `E_depth = 2 * H_n - 2` and expected total path length is `E_path = 2 * (n + 1) * H_n - 4n`, for this problem we output only the harmonic sum.

![Problem Illustration](../images/PRB-009/problem-illustration.png)

## Input Format

- Single line: integer `n`

## Output Format

- Single floating-point number: `H_n` (the harmonic sum)

## Constraints

- `1 <= n <= 10^6`

## Example

**Input:**

```
4
```

**Output:**

```
2.083333
```

**Explanation:**

H_4 = 1 + 1/2 + 1/3 + 1/4 = 2.083333

![Example Visualization](../images/PRB-009/example-1.png)

## Notes

- Compute H*n as sum*{i=1..n} 1/i
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n)

## Related Topics

Treaps, Random BST, Harmonic Numbers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double harmonicSum(int n) {
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
        System.out.println(String.format("%.6f", sol.harmonicSum(n)));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def harmonic_sum(self, n):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    sol = Solution()
    print(format(sol.harmonic_sum(n), ".6f"))

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
    double harmonicSum(int n) {
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
    cout << fixed << setprecision(6) << sol.harmonicSum(n) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  harmonicSum(n) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const n = parseInt(input);
  const sol = new Solution();
  console.log(sol.harmonicSum(n).toFixed(6));
}

solve();
```
