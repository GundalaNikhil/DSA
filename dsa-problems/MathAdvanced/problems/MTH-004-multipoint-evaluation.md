---
problem_id: MTH_MULTIPOINT_EVALUATION__8129
display_id: MTH-004
slug: multipoint-evaluation
title: "Multipoint Evaluation"
difficulty: Hard
difficulty_score: 75
topics:
  - MathAdvanced
  - Multipoint
tags:
  - math-advanced
  - polynomial-evaluation
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-004: Multipoint Evaluation

## Problem Statement

Given a polynomial P(x) and a set of points x_i, compute P(x_i) for all points using divide-and-conquer with product tree and remainder tree.

![Problem Illustration](../images/MTH-004/problem-illustration.png)

## Input Format

- Line 1: Two integers `d` (degree of P) and `n` (number of points)
- Line 2: `d+1` space-separated integers representing coefficients of P(x)
- Line 3: `n` space-separated integers representing evaluation points x_i

## Output Format

A single line containing `n` space-separated integers representing P(x_i) for each point, modulo 10^9+7.

## Constraints

- `0 <= d <= 100000`
- `1 <= n <= 100000`
- `-10^9 <= coefficients, x_i <= 10^9`
- All outputs modulo 10^9 + 7

## Example

**Input:**
```
2 3
1 0 1
0 1 2
```

**Output:**
```
1 2 5
```

**Explanation:**

P(x) = 1 + 0x + x² = 1 + x²

Evaluations:
- P(0) = 1 + 0² = 1
- P(1) = 1 + 1² = 2
- P(2) = 1 + 2² = 5

![Example Visualization](../images/MTH-004/example-1.png)

## Notes

- Use divide-and-conquer approach with product tree and remainder tree
- Product tree: Build tree of products of (x - x_i)
- Remainder tree: Compute remainders top-down
- Time complexity: O(n log² n) using FFT/NTT
- Faster than evaluating each point independently

## Related Topics

polynomial-evaluation, divide-and-conquer, product-tree

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] multipoint_evaluation(long[] coeffs, long[] points) {
        // Implementation here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int d = sc.nextInt();
        int n = sc.nextInt();
        
        long[] coeffs = new long[d + 1];
        for (int i = 0; i < d + 1; i++) coeffs[i] = sc.nextLong();
        
        long[] points = new long[n];
        for (int i = 0; i < n; i++) points[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.multipoint_evaluation(coeffs, points);
        
        for (int i = 0; i < n; i++) {
            System.out.print(res[i] + (i < n - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def multipoint_evaluation(self, coeffs: list[int], points: list[int]) -> list[int]:
        # Implementation here
        return []

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        d = int(next(iterator))
        n = int(next(iterator))
        coeffs = [int(next(iterator)) for _ in range(d + 1)]
        points = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.multipoint_evaluation(coeffs, points)
        print(*(res))
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
    vector<long long> multipoint_evaluation(vector<long long>& coeffs, vector<long long>& points) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int d, n;
    if (!(cin >> d >> n)) return 0;
    
    vector<long long> coeffs(d + 1);
    for (int i = 0; i < d + 1; i++) cin >> coeffs[i];
    
    vector<long long> points(n);
    for (int i = 0; i < n; i++) cin >> points[i];
    
    Solution solution;
    vector<long long> res = solution.multipoint_evaluation(coeffs, points);
    
    for (int i = 0; i < n; i++) {
        cout << res[i] << (i < n - 1 ? " " : "");
    }
    cout << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  multipoint_evaluation(coeffs, points) {
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
  
  const d = parseInt(data[ptr++]);
  const n = parseInt(data[ptr++]);
  
  const coeffs = [];
  for(let i=0; i<=d; i++) coeffs.push(parseInt(data[ptr++]));
  
  const points = [];
  for(let i=0; i<n; i++) points.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const result = solution.multipoint_evaluation(coeffs, points);
  console.log(result.join(" "));
});
```
