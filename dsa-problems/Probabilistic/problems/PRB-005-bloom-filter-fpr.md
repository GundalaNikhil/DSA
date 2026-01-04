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
    public double bloomFilterFPR(int m, int k, int n) {
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
        int n = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.bloomFilterFPR(m, k, n)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def bloom_filter_fpr(self, m, k, n):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    m = int(input_data[0])
    k = int(input_data[1])
    n = int(input_data[2])
    sol = Solution()
    print(format(sol.bloom_filter_fpr(m, k, n), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    double bloomFilterFPR(int m, int k, int n) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m, k, n;
    if (!(cin >> m >> k >> n)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.bloomFilterFPR(m, k, n) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  bloomFilterFPR(m, k, n) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const m = parseInt(input[0]);
  const k = parseInt(input[1]);
  const n = parseInt(input[2]);
  const sol = new Solution();
  console.log(sol.bloomFilterFPR(m, k, n).toFixed(6));
}

solve();
```
