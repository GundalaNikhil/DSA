---
problem_id: MTH_BERLEKAMP_MASSEY__5628
display_id: MTH-010
slug: berlekamp-massey
title: "Berlekamp-Massey Sequence Reconstruction"
difficulty: Hard
difficulty_score: 80
topics:
  - MathAdvanced
  - Berlekamp-Massey
tags:
  - math-advanced
  - berlekamp-massey
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-010: Berlekamp-Massey Sequence Reconstruction

## Problem Statement

Given the first 2k terms of a linearly recurrent sequence, use the Berlekamp-Massey algorithm to find the minimal recurrence relation and compute the nth term.

![Problem Illustration](../images/MTH-010/problem-illustration.png)

## Input Format

- Line 1: Two integers `m` (number of terms given) and `n` (target term)
- Line 2: m space-separated integers representing the sequence
- Line 3: An integer `MOD` (prime modulus)

## Output Format

A single integer representing the nth term of the sequence modulo MOD.

## Constraints

- `1 <= m <= 4000`
- `0 <= n <= 10^18`
- `0 <= sequence[i] < MOD`
- MOD is prime

## Example

**Input:**
```
6 10
1 1 2 3 5 8
1000000007
```

**Output:**
```
89
```

**Explanation:**

Sequence: 1, 1, 2, 3, 5, 8 (Fibonacci)

Berlekamp-Massey finds: a_n = a_{n-1} + a_{n-2}

Continuing: 13, 21, 34, 55, 89
a_10 = 89

![Example Visualization](../images/MTH-010/example-1.png)

## Notes

- Berlekamp-Massey finds minimal linear recurrence
- Works with partial sequence information
- Use matrix exponentiation for large n
- Time complexity: O(m²) for algorithm, O(k³ log n) for term
- Applications in cryptography and coding theory

## Related Topics

berlekamp-massey, linear-recurrence, sequence-reconstruction

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private long MOD;

    private long power(long base, long exp) {
        return 0;
    }

    private long modInverse(long n) {
        return 0;
    }

    // Polynomial Multiplication (Naive O(N^2))
    private long[] polyMul(long[] A, long[] B) {
        return null;
    }

    // Polynomial Modulo (Naive O(N*M))
    private long[] polyMod(long[] A, long[] Mod) {
        return null;
    }
    
    // Better Kitamasa:
    // We want x^n mod (x^L - \sum_{i=1}^L C_i x^{L-i})
    // Let Rec = [C_1, C_2, ..., C_L]
    // Multiplication: A * B. Then reduce using Rec.
    private long[] combine(long[] A, long[] B, long[] Rec) {
        return null;
    }

    public long berlekamp_massey(int m, long n, long mod, long[] S) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int m = sc.nextInt();
        long n = sc.nextLong();
        long[] S = new long[m];
        for (int i = 0; i < m; i++) S[i] = sc.nextLong();
        long MOD = sc.nextLong();
        
        Solution solution = new Solution();
        System.out.println(solution.berlekamp_massey(m, n, MOD, S));
        
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def berlekamp_massey(self, m: int, n: int, MOD: int, S: list[int]) -> int:
        return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        m = int(next(iterator))
        n = int(next(iterator))
        S = [int(next(iterator)) for _ in range(m)]
        MOD = int(next(iterator))
        
        sol = Solution()
        print(sol.berlekamp_massey(m, n, MOD, S))
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
    long long MOD;

    long long power(long long base, long long exp) {
        return 0;
    }

    long long modInverse(long long n) {
        return 0;
    }

    vector<long long> combine(const vector<long long>& A, const vector<long long>& B, const vector<long long>& Rec) {
        return {};
    }

public:
    long long berlekamp_massey(int m, long long n, long long mod, vector<long long>& S) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    long long n, MOD;
    if (!(cin >> m >> n)) return 0;
    vector<long long> S(m);
    for (int i = 0; i < m; i++) cin >> S[i];
    cin >> MOD;

    Solution solution;
    cout << solution.berlekamp_massey(m, n, MOD, S) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  berlekamp_massey(m, n, MOD, S) {
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
  
  const m = parseInt(data[ptr++]);
  const n = BigInt(data[ptr++]);
  
  const S = [];
  for(let i=0; i<m; i++) S.push(parseInt(data[ptr++]));
  
  const MOD = parseInt(data[ptr++]);
  
  const solution = new Solution();
  console.log(solution.berlekamp_massey(m, n, MOD, S));
});
```

