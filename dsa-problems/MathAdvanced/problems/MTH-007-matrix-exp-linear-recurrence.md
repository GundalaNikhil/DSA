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
- Line 2: k space-separated integers representing recurrence coefficients c*0 to c*{k-1}
- Line 3: k space-separated integers representing initial terms a*0 to a*{k-1}

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

Fibonacci sequence: a*n = a*{n-1} + a\_{n-2}
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
import java.io.*;

class Solution {
    public long solveRecurrence(int k, long n, long mod, long[] c, long[] a) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] firstLine = line.trim().split("\\s+");
        int k = Integer.parseInt(firstLine[0]);
        long nTerm = Long.parseLong(firstLine[1]);
        long mod = Long.parseLong(firstLine[2]);

        long[] c = new long[k];
        String[] cLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < k; i++) c[i] = Long.parseLong(cLine[i]);

        long[] a = new long[k];
        String[] aLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < k; i++) a[i] = Long.parseLong(aLine[i]);

        Solution sol = new Solution();
        System.out.println(sol.solveRecurrence(k, nTerm, mod, c, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def solve_recurrence(self, k, n, mod, c, a):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    n = int(input_data[1])
    mod = int(input_data[2])

    c = [int(val) for val in input_data[3:3+k]]
    a = [int(val) for val in input_data[3+k:3+2*k]]

    sol = Solution()
    print(sol.solve_recurrence(k, n, mod, c, a))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long solveRecurrence(int k, long long n, long long mod, const vector<long long>& c, const vector<long long>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long n, mod;
    if (!(cin >> k >> n >> mod)) return 0;

    vector<long long> c(k), a(k);
    for (int i = 0; i < k; i++) cin >> c[i];
    for (int i = 0; i < k; i++) cin >> a[i];

    Solution sol;
    cout << sol.solveRecurrence(k, n, mod, c, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveRecurrence(k, n, mod, c, a) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  const k = parseInt(input[0]);
  const n = BigInt(input[1]);
  const mod = BigInt(input[2]);

  const c = [];
  const a = [];
  let idx = 3;
  for (let i = 0; i < k; i++) c.push(BigInt(input[idx++]));
  for (let i = 0; i < k; i++) a.push(BigInt(input[idx++]));

  const sol = new Solution();
  console.log(sol.solveRecurrence(k, n, mod, c, a).toString());
}

solve();
```
