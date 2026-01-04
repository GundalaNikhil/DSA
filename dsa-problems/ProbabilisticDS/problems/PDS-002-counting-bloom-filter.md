---
problem_id: PDS_COUNTING_BLOOM_FILTER__5830
display_id: PDS-002
slug: counting-bloom-filter
title: "Counting Bloom Filter"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Bloom Filter
  - Poisson Approximation
tags:
  - probabilistic-ds
  - bloom-filter
  - poisson
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-002: Counting Bloom Filter

## Problem Statement

A counting Bloom filter uses counters instead of bits. With `m` counters, `k` hash functions, and `n` insertions, approximate the overflow probability of a counter of `c` bits using a Poisson model.

Let `lambda = k * n / m`, and the counter maximum be `MAX = 2^c - 1`. Then:

```
P_overflow = 1 - sum_{i=0..MAX} (e^{-lambda} * lambda^i / i!)
```

Compute `P_overflow`.

![Problem Illustration](../images/PDS-002/problem-illustration.png)

## Input Format

- Single line: integers `m`, `k`, `c`, and `n`

## Output Format

- Single floating-point number: overflow probability

## Constraints

- `1 <= m <= 10^6`
- `1 <= k <= 20`
- `1 <= c <= 10`
- `1 <= n <= 10^6`

## Example

**Input:**

```
1000 3 4 500
```

**Output:**

```
0.000000000007679
```

**Explanation:**

lambda = 1.5, MAX = 15, overflow probability is about 7.679e-12.

![Example Visualization](../images/PDS-002/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-12
- Time complexity: O(2^c)

## Related Topics

Counting Bloom Filters, Poisson Approximation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double overflowProbability(int m, int k, int c, int n) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        int k = sc.nextInt();
        int c = sc.nextInt();
        int n = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.15f", sol.overflowProbability(m, k, c, n)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def overflow_probability(self, m, k, c, n):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    m = int(input_data[0])
    k = int(input_data[1])
    c = int(input_data[2])
    n = int(input_data[3])
    sol = Solution()
    print(format(sol.overflow_probability(m, k, c, n), ".15f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    double overflowProbability(int m, int k, int c, int n) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m, k, c, n;
    if (!(cin >> m >> k >> c >> n)) return 0;
    Solution sol;
    cout << fixed << setprecision(15) << sol.overflowProbability(m, k, c, n) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  overflowProbability(m, k, c, n) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 4) return;
  const m = parseInt(input[0]);
  const k = parseInt(input[1]);
  const c = parseInt(input[2]);
  const n = parseInt(input[3]);
  const sol = new Solution();
  console.log(sol.overflowProbability(m, k, c, n).toFixed(15));
}

solve();
```
