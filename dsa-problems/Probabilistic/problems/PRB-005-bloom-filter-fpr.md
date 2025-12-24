---
problem_id: PRB_BLOOM_FILTER_FPR__4972
display_id: PRB-005
slug: bloom-filter-fpr
title: "Bloom Filter False Positive Rate"
difficulty: Medium
difficulty_score: 48
topics:
  - Probability
  - Data Structures
  - Hashing
tags:
  - probability
  - bloom-filter
  - hashing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-005: Bloom Filter False Positive Rate

## Problem Statement

Given a Bloom filter with `m` bits, `k` hash functions, and `n` inserted items, compute the false positive probability using the standard approximation:

```
P = (1 - exp(-k * n / m))^k
```

![Problem Illustration](../images/PRB-005/problem-illustration.png)

## Input Format

- Single line: integers `m`, `k`, `n`

## Output Format

- Single floating-point number: false positive probability

## Constraints

- `1 <= m, n <= 10^6`
- `1 <= k <= 20`

## Example

**Input:**

```
1000 3 100
```

**Output:**

```
0.017411
```

**Explanation:**

Using the approximation, the false positive rate is about 0.01741.

![Example Visualization](../images/PRB-005/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Bloom Filters, False Positives, Probabilistic Data Structures

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double bloomFpr(double m, double k, double n) {
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double m = sc.nextDouble();
        double k = sc.nextDouble();
        double n = sc.nextDouble();

        Solution solution = new Solution();
        System.out.println(solution.bloomFpr(m, k, n));
        sc.close();
    }
}
```

### Python

```python
import math

def bloom_fpr(m: float, k: float, n: float) -> float:
    # Your implementation here
    return 0.0

def main():
    m, k, n = map(float, input().split())
    print(f"{bloom_fpr(m, k, n):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    double bloomFpr(double m, double k, double n) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double m, k, n;
    cin >> m >> k >> n;
    Solution solution;
    cout << solution.bloomFpr(m, k, n) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function bloomFpr(m, k, n) {
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
  const m = parseFloat(data[0]);
  const k = parseFloat(data[1]);
  const n = parseFloat(data[2]);
  console.log(bloomFpr(m, k, n).toFixed(6));
});
```
