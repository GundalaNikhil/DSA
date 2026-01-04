---
problem_id: PRB_QUICKSELECT_EXPECTED_COMPARISONS__4028
display_id: PRB-008
slug: quickselect-expected-comparisons
title: "Randomized Quickselect Expected Comparisons"
difficulty: Medium
difficulty_score: 55
topics:
  - Probability
  - Divide and Conquer
  - Expected Value
tags:
  - probability
  - quickselect
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-008: Randomized Quickselect Expected Comparisons

## Problem Statement

For randomized Quickselect on `n` distinct elements to find the `k`-th smallest, compute the expected number of comparisons assuming the pivot is chosen uniformly at random from the current subarray.

Let `E(n, k)` be the expected comparisons. Use the recurrence:

```
E(1, k) = 0
E(n, k) = (n - 1) + (1/n) * sum_{i=1..n} E(subproblem)
```

where the subproblem depends on the pivot rank `i`.

![Problem Illustration](../images/PRB-008/problem-illustration.png)

## Input Format

- Single line: integers `n` and `k`

## Output Format

- Single floating-point number: expected comparisons

## Constraints

- `1 <= n <= 2000`
- `1 <= k <= n`

## Example

**Input:**

```
5 3
```

**Output:**

```
6.733333
```

**Explanation:**

Using the recurrence, the expected comparisons for n=5, k=3 is about 6.733333.

![Example Visualization](../images/PRB-008/example-1.png)

## Notes

- Use memoization or DP for E(n,k)
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n^2)

## Related Topics

Quickselect, Expected Value, Randomized Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double expectedComparisons(int n, int k) {
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
        System.out.println(String.format("%.6f", sol.expectedComparisons(n, k)));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def expected_comparisons(self, n, k):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    sol = Solution()
    print(format(sol.expected_comparisons(n, k), ".6f"))

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
    double expectedComparisons(int n, int k) {
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
    cout << fixed << setprecision(6) << sol.expectedComparisons(n, k) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  expectedComparisons(n, k) {
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
  console.log(sol.expectedComparisons(n, k).toFixed(6));
}

solve();
```
