---
problem_id: PRB_COUPON_COLLECTOR_EXPECTED__1148
display_id: PRB-011
slug: coupon-collector-expected
title: "Coupon Collector Expected Trials"
difficulty: Medium
difficulty_score: 40
topics:
  - Probability
  - Expected Value
  - Harmonic Numbers
tags:
  - probability
  - expectation
  - harmonic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-011: Coupon Collector Expected Trials

## Problem Statement

With `N` equally likely coupons, compute the expected number of draws to collect all coupons:

```
E = N * (1 + 1/2 + 1/3 + ... + 1/N)
```

![Problem Illustration](../images/PRB-011/problem-illustration.png)

## Input Format

- Single line: integer `N`

## Output Format

- Single floating-point number: expected draws

## Constraints

- `1 <= N <= 10^6`

## Example

**Input:**

```
3
```

**Output:**

```
5.500000
```

**Explanation:**

E = 3 * (1 + 1/2 + 1/3) = 5.5.

![Example Visualization](../images/PRB-011/example-1.png)

## Notes

- Compute harmonic sum with double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(N)

## Related Topics

Coupon Collector, Harmonic Numbers, Expectation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double expectedDraws(int N) {
        //Implement here
        return 0.0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            int N = (int) sc.nextLong();
            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.expectedDraws(N));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def expected_draws(N: int) -> float:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    print(f"{expected_draws(N):.6f}")

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
    double expectedDraws(int N) {
        //Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (cin >> N) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.expectedDraws(N) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function expectedDraws(N) {
  //Implement here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  console.log(expectedDraws(N).toFixed(6));
});
```

