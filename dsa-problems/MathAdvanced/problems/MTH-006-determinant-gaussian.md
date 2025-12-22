---
problem_id: MTH_DETERMINANT_GAUSSIAN__4917
display_id: MTH-006
slug: determinant-gaussian
title: "Determinant via Gaussian Elimination"
difficulty: Medium
difficulty_score: 55
topics:
  - MathAdvanced
  - Determinant
tags:
  - math-advanced
  - determinant
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-006: Determinant via Gaussian Elimination

## Problem Statement

Compute the determinant of an n × n matrix modulo a prime using Gaussian elimination with partial pivoting. Track row swaps to maintain correct sign.

![Problem Illustration](../images/MTH-006/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `MOD` (prime modulus)
- Next n lines: n space-separated integers representing each row of the matrix

## Output Format

A single integer representing the determinant modulo MOD.

## Constraints

- `1 <= n <= 1000`
- `0 <= matrix[i][j] < MOD`
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**
```
2 1000000007
1 2
3 4
```

**Output:**
```
1000000005
```

**Explanation:**

Matrix:
[1  2]
[3  4]

Determinant = 1*4 - 2*3 = 4 - 6 = -2

-2 mod 10^9+7 = 10^9+7-2 = 1000000005

![Example Visualization](../images/MTH-006/example-1.png)

## Notes

- Use Gaussian elimination to convert to upper triangular form
- Track number of row swaps (affects sign)
- Use modular inverse for division
- Det = (-1)^swaps × product of diagonal elements
- Time complexity: O(n³)

## Related Topics

determinant, gaussian-elimination, linear-algebra

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long determinant_gaussian(/* parameters */) {
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
def determinant_gaussian(/* parameters */) -> int:
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
    long long determinant_gaussian(/* parameters */) {
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
  determinant_gaussian(/* parameters */) {
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
