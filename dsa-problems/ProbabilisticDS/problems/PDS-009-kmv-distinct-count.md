---
problem_id: PDS_KMV_DISTINCT_COUNT__9186
display_id: PDS-009
slug: kmv-distinct-count
title: "k-Minimum Values (KMV) Distinct Count"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - KMV
  - Distinct Count
tags:
  - probabilistic-ds
  - kmv
  - distinct-count
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-009: k-Minimum Values (KMV) Distinct Count

## Problem Statement

You are given the `k` smallest hash values in (0,1) for a set. Estimate the number of distinct elements using:

```
Estimate = (k - 1) / h_k
```

where `h_k` is the k-th smallest hash value.

![Problem Illustration](../images/PDS-009/problem-illustration.png)

## Input Format

- First line: integer `k`
- Second line: `k` floating-point numbers in ascending order

## Output Format

- Single floating-point number: estimated distinct count

## Constraints

- `2 <= k <= 100000`
- `0 < h_k < 1`

## Example

**Input:**

```
3
0.1 0.2 0.4
```

**Output:**

```
5.0
```

**Explanation:**

Estimate = (3-1) / 0.4 = 5.

![Example Visualization](../images/PDS-009/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

KMV, Sketches, Distinct Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double estimateDistinctCount(int k, double[] h) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        double[] h = new double[k];
        for (int i = 0; i < k; i++) h[i] = sc.nextDouble();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.estimateDistinctCount(k, h)));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def estimate_distinct_count(self, k, h):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    h = [float(x) for x in input_data[1:1+k]]
    sol = Solution()
    print(format(sol.estimate_distinct_count(k, h), ".6f"))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double estimateDistinctCount(int k, const vector<double>& h) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    if (!(cin >> k)) return 0;
    vector<double> h(k);
    for (int i = 0; i < k; i++) cin >> h[i];
    Solution sol;
    cout << fixed << setprecision(6) << sol.estimateDistinctCount(k, h) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimateDistinctCount(k, h) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const k = parseInt(input[0]);
  const h = [];
  for (let i = 0; i < k; i++) h.push(parseFloat(input[1 + i]));
  const sol = new Solution();
  console.log(sol.estimateDistinctCount(k, h).toFixed(6));
}

solve();
```
