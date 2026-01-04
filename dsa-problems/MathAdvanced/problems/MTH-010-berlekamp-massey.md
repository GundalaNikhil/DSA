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

Berlekamp-Massey finds: a*n = a*{n-1} + a\_{n-2}

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
import java.io.*;

class Solution {
    public long findNthTerm(int m, long n, long[] seq, long mod) {
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
        int m = Integer.parseInt(firstLine[0]);
        long nTerm = Long.parseLong(firstLine[1]);

        long[] seq = new long[m];
        String[] sLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < m; i++) seq[i] = Long.parseLong(sLine[i]);

        long mod = Long.parseLong(br.readLine().trim());

        Solution sol = new Solution();
        System.out.println(sol.findNthTerm(m, nTerm, seq, mod));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_nth_term(self, m, n, seq, mod):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    n = int(input_data[1])
    seq = [int(val) for val in input_data[2:2+m]]
    mod = int(input_data[2+m])

    sol = Solution()
    print(sol.find_nth_term(m, n, seq, mod))

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
    long long findNthTerm(int m, long long n, const vector<long long>& seq, long long mod) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    long long n, mod;
    if (!(cin >> m >> n)) return 0;

    vector<long long> seq(m);
    for (int i = 0; i < m; i++) cin >> seq[i];
    cin >> mod;

    Solution sol;
    cout << sol.findNthTerm(m, n, seq, mod) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findNthTerm(m, n, seq, mod) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const m = parseInt(input[0]);
  const n = BigInt(input[1]);
  const seq = [];
  for (let i = 0; i < m; i++) seq.push(BigInt(input[2 + i]));
  const mod = BigInt(input[2 + m]);

  const sol = new Solution();
  console.log(sol.findNthTerm(m, n, seq, mod).toString());
}

solve();
```
