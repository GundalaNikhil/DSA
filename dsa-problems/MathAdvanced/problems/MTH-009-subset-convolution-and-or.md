---
problem_id: MTH_SUBSET_CONVOLUTION_AND_OR__9174
display_id: MTH-009
slug: subset-convolution-and-or
title: "Subset Convolution (AND/OR)"
difficulty: Hard
difficulty_score: 78
topics:
  - MathAdvanced
  - Subset
tags:
  - math-advanced
  - subset-convolution
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-009: Subset Convolution (AND/OR)

## Problem Statement

Perform subset convolution under bitwise AND or OR operations using zeta and Möbius transforms on the subset lattice.

![Problem Illustration](../images/MTH-009/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (bit size) and `op` (0 for AND, 1 for OR)
- Line 2: 2^n space-separated integers representing array A
- Line 3: 2^n space-separated integers representing array B

## Output Format

A single line containing 2^n space-separated integers representing the subset convolution modulo 10^9+7.

## Constraints

- `1 <= n <= 20`
- `0 <= A[i], B[i] <= 10^9`
- op = 0 (AND) or 1 (OR)
- Output modulo 10^9 + 7

## Example

**Input:**
```
2 1
1 1 0 0
0 1 1 0
```

**Output:**
```
0 1 1 2
```

**Explanation:**

n=2, so we have 4 subsets: {}, {0}, {1}, {0,1}
A = [1, 1, 0, 0]
B = [0, 1, 1, 0]

OR convolution computes sum over subsets.

![Example Visualization](../images/MTH-009/example-1.png)

## Notes

- Use ranked zeta/Möbius transforms
- Subset convolution: C[S] = Σ(T⊆S) A[T] × B[S\T]
- Time complexity: O(2^n × n²)
- Applications in DP on subsets
- More complex than FWHT

## Related Topics

subset-convolution, zeta-transform, mobius-transform

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] subset_convolution_and_or(int n, int op, long[] A, long[] B) {
        // Implementation here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int op = sc.nextInt();
        int size = 1 << n;
        
        long[] A = new long[size];
        for (int i = 0; i < size; i++) A[i] = sc.nextLong();
        
        long[] B = new long[size];
        for (int i = 0; i < size; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.subset_convolution_and_or(n, op, A, B);
        
        for (int i = 0; i < size; i++) {
            System.out.print(res[i] + (i < size - 1 ? " " : ""));
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
    def subset_convolution_and_or(self, n: int, op: int, A: list[int], B: list[int]) -> list[int]:
        # Implementation here
        return []

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        op = int(next(iterator))
        size = 1 << n
        
        A = [int(next(iterator)) for _ in range(size)]
        B = [int(next(iterator)) for _ in range(size)]
        
        sol = Solution()
        res = sol.subset_convolution_and_or(n, op, A, B)
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
    vector<long long> subset_convolution_and_or(int n, int op, vector<long long>& A, vector<long long>& B) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, op;
    if (!(cin >> n >> op)) return 0;
    int size = 1 << n;

    vector<long long> A(size);
    for (int i = 0; i < size; i++) cin >> A[i];

    vector<long long> B(size);
    for (int i = 0; i < size; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.subset_convolution_and_or(n, op, A, B);

    for (int i = 0; i < size; i++) {
        cout << result[i] << (i < size - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  subset_convolution_and_or(n, op, A, B) {
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
  
  const n = parseInt(data[ptr++]);
  const op = parseInt(data[ptr++]);
  const size = 1 << n;
  
  const A = [];
  for(let i=0; i<size; i++) A.push(parseInt(data[ptr++]));
  
  const B = [];
  for(let i=0; i<size; i++) B.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const result = solution.subset_convolution_and_or(n, op, A, B);
  console.log(result.join(" "));
});
```
