---
problem_id: MTH_CONVOLUTION_MULTI_MOD_CRT__4736
display_id: MTH-012
slug: convolution-multi-mod-crt
title: "Convolution Under Multiple Mods with CRT"
difficulty: Medium
difficulty_score: 65
topics:
  - MathAdvanced
  - Convolution
tags:
  - math-advanced
  - crt
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-012: Convolution Under Multiple Mods with CRT

## Problem Statement

Compute convolution of two arrays when the final modulus is not NTT-friendly. Use Chinese Remainder Theorem (CRT) to combine results from multiple NTT-friendly primes.

![Problem Illustration](../images/MTH-012/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` and `m` (array sizes)
- Line 2: n space-separated integers representing array A
- Line 3: m space-separated integers representing array B
- Line 4: An integer `MOD` (target modulus, may not be NTT-friendly)

## Output Format

A single line containing n+m-1 space-separated integers representing the convolution modulo MOD.

## Constraints

- `1 <= n, m <= 100000`
- `0 <= A[i], B[i] <= 10^9`
- `1 <= MOD <= 10^9 + 9`
- MOD may not support NTT

## Example

**Input:**
```
2 2
1 2
3 4
1000000007
```

**Output:**
```
3 10 8
```

**Explanation:**

A = [1, 2], B = [3, 4]

Convolution:
[1*3, 1*4+2*3, 2*4] = [3, 10, 8]

All values already < 10^9+7

![Example Visualization](../images/MTH-012/example-1.png)

## Notes

- Use 2-3 NTT-friendly primes (998244353, 1004535809, 469762049)
- Compute convolution mod each prime
- Apply CRT to reconstruct result mod target
- Handles arbitrary moduli
- Time complexity: O(n log n) per prime

## Related Topics

crt, chinese-remainder-theorem, multi-modular

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] convolution_multi_mod_crt(/* parameters */) {
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
def convolution_multi_mod_crt(/* parameters */) -> list[int]:
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
    vector<long long> convolution_multi_mod_crt(/* parameters */) {
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
  convolution_multi_mod_crt(/* parameters */) {
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
