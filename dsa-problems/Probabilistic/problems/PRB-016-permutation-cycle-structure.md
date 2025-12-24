---
problem_id: PRB_PERMUTATION_CYCLE_STRUCTURE__9150
display_id: PRB-016
slug: permutation-cycle-structure
title: "Random Permutation Cycle Structure"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Combinatorics
  - Expectations
tags:
  - probability
  - permutations
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-016: Random Permutation Cycle Structure

## Problem Statement

For a uniformly random permutation of `n` elements:

- The expected number of cycles of length exactly `k` is `1/k`
- The expected length of the longest cycle is approximately `0.624330 * n`

Given `n` and `k`, output both values.

![Problem Illustration](../images/PRB-016/problem-illustration.png)

## Input Format

- Single line: integers `n` and `k`

## Output Format

- Two floating-point numbers: expected cycles of length `k`, and expected longest cycle length

## Constraints

- `1 <= k <= n <= 100000`

## Example

**Input:**

```
5 2
```

**Output:**

```
0.500000 3.121650
```

**Explanation:**

Expected cycles of length 2 is 1/2. Expected longest cycle length ≈ 0.624330 * 5.

![Example Visualization](../images/PRB-016/example-1.png)

## Notes

- Use the constant 0.624330 for the longest cycle approximation
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Random Permutations, Cycle Decomposition, Expectations

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double[] cycleExpectations(int n, int k) {
        // Your implementation here
        return new double[]{0.0, 0.0};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        double[] res = solution.cycleExpectations(n, k);
        System.out.printf("%.6f %.6f\n", res[0], res[1]);
        sc.close();
    }
}
```

### Python

```python
def cycle_expectations(n: int, k: int):
    # Your implementation here
    return 0.0, 0.0

def main():
    n, k = map(int, input().split())
    a, b = cycle_expectations(n, k)
    print(f"{a:.6f} {b:.6f}")

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
    pair<double, double> cycleExpectations(int n, int k) {
        // Your implementation here
        return {0.0, 0.0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    Solution solution;
    auto res = solution.cycleExpectations(n, k);
    cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function cycleExpectations(n, k) {
  // Your implementation here
  return [0.0, 0.0];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  const res = cycleExpectations(n, k);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
```
