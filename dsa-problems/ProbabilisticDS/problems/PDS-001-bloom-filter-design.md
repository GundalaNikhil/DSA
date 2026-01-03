---
problem_id: PDS_BLOOM_FILTER_DESIGN__4217
display_id: PDS-001
slug: bloom-filter-design
title: "Bloom Filter Design"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Bloom Filter
  - Optimization
tags:
  - probabilistic-ds
  - bloom-filter
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-001: Bloom Filter Design

## Problem Statement

Given an expected number of items `n` and a target false positive rate `f`, choose the Bloom filter parameters:

```
m = ceil(-(n * ln f) / (ln 2)^2)
k = round((m / n) * ln 2)
```

Then compute the expected false positive rate using:

```
FPR = (1 - exp(-k * n / m))^k
```

Output `m`, `k`, and `FPR`.

![Problem Illustration](../images/PDS-001/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `f`

## Output Format

- Three values: `m` (integer), `k` (integer), `FPR` (floating-point)

## Constraints

- `1 <= n <= 10^6`
- `0 < f < 1`

## Example

**Input:**

```
1000 0.01
```

**Output:**

```
9586 7 0.010035
```

**Explanation:**

m = 9586, k = 7, FPR ≈ 0.010035.

![Example Visualization](../images/PDS-001/example-1.png)

## Notes

- Use natural logarithms
- Print FPR with at least 6 decimal digits
- Accept answers with absolute error <= 1e-6

## Related Topics

Bloom Filters, Parameter Optimization, False Positives

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public Object[] designBloom(long n, double f) {
        //Implement here
        return new Object[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            double f = sc.nextDouble();

            Solution solution = new Solution();
            Object[] res = solution.designBloom(n, f);
            System.out.println(res[0] + " " + res[1] + " " + String.format("%.6f", (double)res[2]));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def design_bloom(n: int, f: float):
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    f = float(data[1])
    m, k, fpr = design_bloom(n, f)
    print(f"{m} {k} {fpr:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
#include <tuple>

using namespace std;

class Solution {
public:
    tuple<long long, long long, double> designBloom(long long n, double f) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    double f;
    if (cin >> n >> f) {
        Solution solution;
        auto res = solution.designBloom(n, f);
        cout << get<0>(res) << " " << get<1>(res) << " " << fixed << setprecision(6) << get<2>(res) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function designBloom(n, f) {
  //Implement here
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
  const n = parseInt(data[0], 10);
  const f = parseFloat(data[1]);
  const res = designBloom(n, f);
  console.log(res[0] + " " + res[1] + " " + res[2].toFixed(6));
});
```

