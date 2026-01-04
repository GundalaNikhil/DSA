---
problem_id: PDS_COUNT_MIN_SKETCH__4815
display_id: PDS-004
slug: count-min-sketch
title: "Count-Min Sketch Error Bound"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Sketches
  - Error Bounds
tags:
  - probabilistic-ds
  - sketch
  - error-bound
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-004: Count-Min Sketch Error Bound

## Problem Statement

Given desired error `epsilon` and failure probability `delta`, compute parameters for a Count-Min Sketch:

```
w = ceil(e / epsilon)
d = ceil(ln(1 / delta))
```

Output `w` and `d`.

![Problem Illustration](../images/PDS-004/problem-illustration.png)

## Input Format

- Single line: real `epsilon` and real `delta`

## Output Format

- Two integers: `w` and `d`

## Constraints

- `0 < epsilon < 1`
- `0 < delta < 1`

## Example

**Input:**

```
0.01 0.01
```

**Output:**

```
272 5
```

**Explanation:**

w = ceil(e / 0.01) = 272, d = ceil(ln(100)) = 5.

![Example Visualization](../images/PDS-004/example-1.png)

## Notes

- Use natural log
- Time complexity: O(1)

## Related Topics

Count-Min Sketch, Approximate Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void computeParameters(double epsilon, double delta) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextDouble()) return;
        double epsilon = sc.nextDouble();
        double delta = sc.nextDouble();
        Solution sol = new Solution();
        sol.computeParameters(epsilon, delta);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def compute_parameters(self, epsilon, delta):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    epsilon = float(input_data[0])
    delta = float(input_data[1])
    sol = Solution()
    sol.compute_parameters(epsilon, delta)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    void computeParameters(double epsilon, double delta) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    double epsilon, delta;
    if (!(cin >> epsilon >> delta)) return 0;
    Solution sol;
    sol.computeParameters(epsilon, delta);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  computeParameters(epsilon, delta) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const epsilon = parseFloat(input[0]);
  const delta = parseFloat(input[1]);
  const sol = new Solution();
  sol.computeParameters(epsilon, delta);
}

solve();
```
