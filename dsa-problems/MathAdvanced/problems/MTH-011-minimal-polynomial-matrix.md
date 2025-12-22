---
problem_id: MTH_MINIMAL_POLYNOMIAL_MATRIX__3891
display_id: MTH-011
slug: minimal-polynomial-matrix
title: "Minimal Polynomial of Matrix (Krylov)"
difficulty: Hard
difficulty_score: 82
topics:
  - MathAdvanced
  - Minimal
tags:
  - math-advanced
  - minimal-polynomial
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-011: Minimal Polynomial of Matrix (Krylov)

## Problem Statement

Compute the minimal polynomial of an n × n matrix using the Krylov sequence method combined with Berlekamp-Massey algorithm on the generated vector sequence.

![Problem Illustration](../images/MTH-011/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `MOD` (prime modulus)
- Next n lines: n space-separated integers representing each row of the matrix

## Output Format

First line: degree d of minimal polynomial
Second line: d+1 space-separated integers representing coefficients from constant to highest degree.

## Constraints

- `1 <= n <= 200`
- `0 <= matrix[i][j] < MOD`
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**
```
2 1000000007
1 1
0 1
```

**Output:**
```
2
1 1000000005 1
```

**Explanation:**

Matrix:
[1  1]
[0  1]

This is a Jordan block. Minimal polynomial: (x-1)²
= x² - 2x + 1

Coefficients: [1, -2, 1]
-2 mod 10^9+7 = 1000000005

![Example Visualization](../images/MTH-011/example-1.png)

## Notes

- Generate Krylov sequence: v, Av, A²v, ...
- Apply Berlekamp-Massey to find recurrence
- Minimal polynomial divides characteristic polynomial
- Time complexity: O(n³) for Krylov, O(n²) for BM
- Important in matrix theory

## Related Topics

minimal-polynomial, krylov-sequence, matrix-theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] minimal_polynomial_matrix(/* parameters */) {
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
def minimal_polynomial_matrix(/* parameters */) -> list[int]:
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
    vector<long long> minimal_polynomial_matrix(/* parameters */) {
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
  minimal_polynomial_matrix(/* parameters */) {
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
