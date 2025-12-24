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
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.expectedComparisons(n, k));
        sc.close();
    }
}
```

### Python

```python
def expected_comparisons(n: int, k: int) -> float:
    # Your implementation here
    return 0.0

def main():
    n, k = map(int, input().split())
    print(f"{expected_comparisons(n, k):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    double expectedComparisons(int n, int k) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    Solution solution;
    cout << solution.expectedComparisons(n, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function expectedComparisons(n, k) {
  // Your implementation here
  return 0.0;
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
  const k = parseInt(data[1], 10);
  console.log(expectedComparisons(n, k).toFixed(6));
});
```
