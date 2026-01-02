---
problem_id: MTH_LAGRANGE_INTERPOLATION_MOD__3542
display_id: MTH-005
slug: lagrange-interpolation-mod
title: "Lagrange Interpolation Mod Prime"
difficulty: Medium
difficulty_score: 60
topics:
  - MathAdvanced
  - Lagrange
tags:
  - math-advanced
  - lagrange-interpolation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-005: Lagrange Interpolation Mod Prime

## Problem Statement

Given k points (x_i, y_i) with distinct x_i values, find the value of the unique interpolating polynomial of degree at most k-1 at a query point X, all modulo a prime.

![Problem Illustration](../images/MTH-005/problem-illustration.png)

## Input Format

- Line 1: Two integers `k` (number of points) and `X` (query point)
- Line 2: An integer `MOD` (prime modulus)
- Next k lines: Two integers `x_i` and `y_i` representing each point

## Output Format

A single integer representing P(X) modulo MOD, where P is the interpolating polynomial.

## Constraints

- `1 <= k <= 200000`
- `0 <= x_i, y_i, X < MOD`
- All x_i are distinct
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**
```
2 2
1000000007
0 1
1 3
```

**Output:**
```
5
```

**Explanation:**

Points: (0, 1) and (1, 3)

The interpolating polynomial through these points is:
P(x) = 1 + 2x

P(2) = 1 + 2(2) = 5

![Example Visualization](../images/MTH-005/example-1.png)

## Notes

- Use Lagrange interpolation formula
- Compute products efficiently
- Handle modular arithmetic carefully
- Time complexity: O(k²) naive, O(k log k) with FFT optimization
- Requires modular inverse computation

## Related Topics

lagrange-interpolation, modular-arithmetic, polynomial

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long lagrange_interpolation_mod(int k, long X, long MOD, long[][] points) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        long X = sc.nextLong();
        long MOD = sc.nextLong();
        
        long[][] points = new long[k][2];
        for (int i = 0; i < k; i++) {
            points[i][0] = sc.nextLong();
            points[i][1] = sc.nextLong();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.lagrange_interpolation_mod(k, X, MOD, points));
        
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def lagrange_interpolation_mod(self, k: int, X: int, MOD: int, points: list[list[int]]) -> int:
        # Implementation here
        return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        X = int(next(iterator))
        MOD = int(next(iterator))
        
        points = []
        for _ in range(k):
            points.append([int(next(iterator)), int(next(iterator))])
            
        sol = Solution()
        print(sol.lagrange_interpolation_mod(k, X, MOD, points))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long lagrange_interpolation_mod(int k, long long X, long long mod, vector<pair<long long, long long>>& points) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long X, MOD;
    if (!(cin >> k >> X >> MOD)) return 0;

    vector<pair<long long, long long>> points(k);
    for (int i = 0; i < k; i++) {
        cin >> points[i].first >> points[i].second;
    }

    Solution solution;
    cout << solution.lagrange_interpolation_mod(k, X, MOD, points) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  lagrange_interpolation_mod(k, X, MOD, points) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let ptr = 0;
  
  const k = parseInt(data[ptr++]);
  const X = parseInt(data[ptr++]);
  const MOD = parseInt(data[ptr++]);
  
  const points = [];
  for(let i=0; i<k; i++) {
      points.push([parseInt(data[ptr++]), parseInt(data[ptr++])]);
  }
  
  const solution = new Solution();
  console.log(solution.lagrange_interpolation_mod(k, X, MOD, points));
});
```
