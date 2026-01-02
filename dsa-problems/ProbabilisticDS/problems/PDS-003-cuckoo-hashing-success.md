---
problem_id: PDS_CUCKOO_HASHING_SUCCESS__7392
display_id: PDS-003
slug: cuckoo-hashing-success
title: "Cuckoo Hashing Success Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Hashing
  - Random Graphs
tags:
  - probabilistic-ds
  - cuckoo-hashing
  - probability
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-003: Cuckoo Hashing Success Probability

## Problem Statement

Use the following approximation for the failure probability of cuckoo hashing with two hash functions:

```
P_fail = exp(-((1 - alpha)^2 * m) / 2)
```

where `alpha` is the load factor and `m` is the table size. Compute the success probability:

```
P_success = 1 - P_fail
```

![Problem Illustration](../images/PDS-003/problem-illustration.png)

## Input Format

- Single line: integer `m` and real `alpha`

## Output Format

- Single floating-point number: `P_success`

## Constraints

- `1 <= m <= 10^6`
- `0 < alpha < 1`

## Example

**Input:**

```
50 0.8
```

**Output:**

```
0.632121
```

**Explanation:**

P_fail = exp(-1) = 0.367879, so P_success = 0.632121.

![Example Visualization](../images/PDS-003/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Cuckoo Hashing, Randomized Analysis

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double successProbability(long m, double alpha) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long m = sc.nextLong();
            double alpha = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.successProbability(m, alpha)));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def success_probability(m: int, alpha: float) -> float:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    alpha = float(data[1])
    print(f"{success_probability(m, alpha):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double successProbability(long long m, double alpha) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    double alpha;
    if (cin >> m >> alpha) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.successProbability(m, alpha) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function successProbability(m, alpha) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const m = parseInt(data[0], 10);
  const alpha = parseFloat(data[1]);
  console.log(successProbability(m, alpha).toFixed(6));
});
```

