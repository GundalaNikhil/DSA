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
    public long[] fwht_xor_convolution(int k, long[] A, long[] B) {
        //Implement here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        int n = 1 << k;
        
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        long[] B = new long[n];
        for (int i = 0; i < n; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.fwht_xor_convolution(k, A, B);
        
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
    def fwht_xor_convolution(self, k: int, A: list[int], B: list[int]) -> list[int]:
        # //Implement here
        return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = 1 << k
        A = [int(next(iterator)) for _ in range(n)]
        B = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.fwht_xor_convolution(k, A, B)
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
    vector<long long> fwht_xor_convolution(int k, vector<long long>& A, vector<long long>& B) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    int n = 1 << k;

    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<long long> B(n);
    for (int i = 0; i < n; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.fwht_xor_convolution(k, A, B);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i < n - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  fwht_xor_convolution(k, A, B) {
    //Implement here
    return 0;
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
  const n = 1 << k;
  
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const B = [];
  for(let i=0; i<n; i++) B.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const result = solution.fwht_xor_convolution(k, A, B);
  console.log(result.join(" "));
});
```

