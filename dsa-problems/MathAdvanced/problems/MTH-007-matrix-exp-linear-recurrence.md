---
problem_id: MTH_MATRIX_EXP_LINEAR_RECURRENCE__6283
display_id: MTH-007
slug: matrix-exp-linear-recurrence
title: "Matrix Exponentiation for Linear Recurrence"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Matrix
tags:
  - math-advanced
  - matrix-exponentiation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-007: Matrix Exponentiation for Linear Recurrence

## Problem Statement

Given a linear recurrence relation of order k with coefficients and initial terms, compute the nth term modulo a prime using matrix exponentiation.

![Problem Illustration](../images/MTH-007/problem-illustration.png)

## Input Format

- Line 1: Three integers `k` (recurrence order), `n` (target term), and `MOD` (modulus)
- Line 2: k space-separated integers representing recurrence coefficients c_0 to c_{k-1}
- Line 3: k space-separated integers representing initial terms a_0 to a_{k-1}

## Output Format

A single integer representing the nth term of the sequence modulo MOD.

## Constraints

- `1 <= k <= 50`
- `0 <= n <= 10^18`
- `0 <= c_i, a_i < MOD`
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**
```
2 5 1000000007
1 1
0 1
```

**Output:**
```
5
```

**Explanation:**

Fibonacci sequence: a_n = a_{n-1} + a_{n-2}
Coefficients: [1, 1]
Initial: [0, 1]

Sequence: 0, 1, 1, 2, 3, 5, ...
a_5 = 5

![Example Visualization](../images/MTH-007/example-1.png)

## Notes

- Build k×k transition matrix
- Use fast matrix exponentiation: O(k³ log n)
- Handles very large n efficiently
- Common for Fibonacci-like sequences
- Can solve any linear recurrence

## Related Topics

matrix-exponentiation, linear-recurrence, fast-exponentiation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] matrix_exp_linear_recurrence(/* parameters */) {
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
def matrix_exp_linear_recurrence(/* parameters */) -> list[int]:
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
    vector<long long> matrix_exp_linear_recurrence(/* parameters */) {
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
  matrix_exp_linear_recurrence(/* parameters */) {
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
