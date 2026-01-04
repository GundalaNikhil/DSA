---
problem_id: PDS_FLAJOLET_MARTIN__2749
display_id: PDS-007
slug: flajolet-martin
title: "Flajolet-Martin Bit Pattern"
difficulty: Medium
difficulty_score: 48
topics:
  - Probabilistic Data Structures
  - Flajolet-Martin
  - Distinct Count
tags:
  - probabilistic-ds
  - flajolet-martin
  - distinct-count
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-007: Flajolet-Martin Bit Pattern

## Problem Statement

Given the maximum number of trailing zeros `R` observed in hashed stream items, estimate the number of distinct elements using:

```
Estimate = 2^R / phi
```

where `phi = 0.77351`.

![Problem Illustration](../images/PDS-007/problem-illustration.png)

## Input Format

- Single line: integer `R`

## Output Format

- Single floating-point number: estimated distinct count

## Constraints

- `0 <= R <= 60`

## Example

**Input:**

```
4
```

**Output:**

```
20.684930
```

**Explanation:**

Estimate = 16 / 0.77351 = 20.68493.

![Example Visualization](../images/PDS-007/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Flajolet-Martin, Distinct Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double estimateDistinctCount(int r) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int r = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(String.format("%.6f", sol.estimateDistinctCount(r)));
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def estimate_distinct_count(self, r):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    r = int(input_data[0])
    sol = Solution()
    print(format(sol.estimate_distinct_count(r), ".6f"))

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
    double estimateDistinctCount(int r) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r;
    if (!(cin >> r)) return 0;
    Solution sol;
    cout << fixed << setprecision(6) << sol.estimateDistinctCount(r) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimateDistinctCount(r) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const r = parseInt(input);
  const sol = new Solution();
  console.log(sol.estimateDistinctCount(r).toFixed(6));
}

solve();
```
