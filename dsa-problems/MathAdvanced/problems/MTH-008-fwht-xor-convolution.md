---
problem_id: MTH_FWHT_XOR_CONVOLUTION__7451
display_id: MTH-008
slug: fwht-xor-convolution
title: "Fast Walsh-Hadamard Transform (XOR Convolution)"
difficulty: Medium
difficulty_score: 62
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - fwht
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-008: Fast Walsh-Hadamard Transform (XOR Convolution)

## Problem Statement

Given two arrays A and B of length 2^k, compute their XOR convolution using the Fast Walsh-Hadamard Transform (FWHT). The XOR convolution C is defined as: C[i⊕j] += A[i] × B[j].

![Problem Illustration](../images/MTH-008/problem-illustration.png)

## Input Format

- Line 1: An integer `k` (arrays have length 2^k)
- Line 2: 2^k space-separated integers representing array A
- Line 3: 2^k space-separated integers representing array B

## Output Format

A single line containing 2^k space-separated integers representing the XOR convolution modulo 10^9+7.

## Constraints

- `0 <= k <= 17`
- `0 <= A[i], B[i] <= 10^9`
- Array length is power of 2
- Output modulo 10^9 + 7

## Example

**Input:**
```
1
1 2
3 4
```

**Output:**
```
11 10
```

**Explanation:**

A = [1, 2], B = [3, 4]

XOR convolution:
- C[0⊕0] = A[0]*B[0] + A[1]*B[1] = 1*3 + 2*4 = 11
- C[0⊕1] = A[0]*B[1] + A[1]*B[0] = 1*4 + 2*3 = 10

Result: [11, 10]

![Example Visualization](../images/MTH-008/example-1.png)

## Notes

- FWHT is similar to FFT but for XOR operation
- Transform, pointwise multiply, inverse transform
- Time complexity: O(n log n) where n = 2^k
- Applications in subset sum problems
- Different from standard convolution

## Related Topics

fwht, xor-convolution, walsh-hadamard

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] fwht_xor_convolution(/* parameters */) {
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
def fwht_xor_convolution(/* parameters */) -> list[int]:
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
    vector<long long> fwht_xor_convolution(/* parameters */) {
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
  fwht_xor_convolution(/* parameters */) {
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
