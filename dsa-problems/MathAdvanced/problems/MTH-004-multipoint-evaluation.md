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
    public long[] multipoint_evaluation(/* parameters */) {
        // Your implementation here
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Read input
        
        Solution solution = new Solution();
        // Call method and print result
        
        sc.close();
    }
}
```

### Python

```python
def multipoint_evaluation(/* parameters */) -> list[int]:
    # Your implementation here
    return None

def main():
    # Read input
    
    # Call function and print result
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
    vector<long long> multipoint_evaluation(/* parameters */) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // Read input
    
    Solution solution;
    // Call method and print result
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  multipoint_evaluation(/* parameters */) {
    // Your implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  // Parse input
  
  const solution = new Solution();
  // Call method and print result
});
```
