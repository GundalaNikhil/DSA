---
problem_id: MTH_INVERT_VANDERMONDE__8453
display_id: MTH-013
slug: invert-vandermonde
title: "Fast Inversion of Vandermonde Matrix"
difficulty: Hard
difficulty_score: 76
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - vandermonde-matrix
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-013: Fast Inversion of Vandermonde Matrix

## Problem Statement

Given n distinct values x_i, efficiently compute the inverse of the n × n Vandermonde matrix V where V[i][j] = x_i^j. Use this to solve polynomial interpolation problems.

![Problem Illustration](../images/MTH-013/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `MOD` (prime modulus)
- Line 2: n space-separated integers representing distinct values x_0, x_1, ..., x_{n-1}

## Output Format

n lines, each containing n space-separated integers representing the inverse Vandermonde matrix modulo MOD.

## Constraints

- `1 <= n <= 2000`
- `0 <= x_i < MOD`
- All x_i are distinct
- MOD is prime

## Example

**Input:**
```
2 1000000007
1 2
```

**Output:**
```
2 1000000006
1000000006 1
```

**Explanation:**

Vandermonde matrix for [1, 2]:
V = [1  1]
    [1  2]

V^(-1) = [ 2  -1]
         [-1   1]

mod 10^9+7:
-1 ≡ 1000000006

![Example Visualization](../images/MTH-013/example-1.png)

## Notes

- Vandermonde determinant: ∏(i>j) (x_i - x_j)
- Use Lagrange basis for fast inversion
- Applications in polynomial interpolation
- Time complexity: O(n²) with FFT optimization
- More efficient than general matrix inversion

## Related Topics

vandermonde-matrix, matrix-inversion, interpolation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] invert_vandermonde(/* parameters */) {
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
def invert_vandermonde(/* parameters */) -> list[int]:
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
    vector<long long> invert_vandermonde(/* parameters */) {
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
  invert_vandermonde(/* parameters */) {
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
