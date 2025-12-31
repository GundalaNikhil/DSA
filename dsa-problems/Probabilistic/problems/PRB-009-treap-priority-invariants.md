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

- Compute H_n as sum_{i=1..n} 1/i
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
    public double[] treapExpectations(int n) {
        // Your implementation here
        return new double[]{0.0, 0.0};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Solution solution = new Solution();
        double[] res = solution.treapExpectations(n);
        System.out.printf("%.6f %.6f\n", res[0], res[1]);
        sc.close();
    }
}
```

### Python

```python
def treap_expectations(n: int):
    # Your implementation here
    return 0.0, 0.0

def main():
    n = int(input())
    d, p = treap_expectations(n)
    print(f"{d:.6f} {p:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

class Solution {
public:
    pair<double, double> treapExpectations(int n) {
        // Your implementation here
        return {0.0, 0.0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    Solution solution;
    auto res = solution.treapExpectations(n);
    cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function treapExpectations(n) {
  // Your implementation here
  return [0.0, 0.0];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const res = treapExpectations(n);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
```
