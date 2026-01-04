---
problem_id: NUM_DISTINCT_PRIME_FACTORS_PREFIX__5173
display_id: NUM-006
slug: distinct-prime-factors-prefix
title: "Distinct Prime Factors Count Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Sieve
  - Prefix Sums
tags:
  - number-theory
  - sieve
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-006: Distinct Prime Factors Count Prefix

## Problem Statement

For each integer `x`, let `f(x)` be the number of distinct prime factors of `x`. Precompute `f(1..N)` and answer range sum queries:

```
sum_{x=l..r} f(x)
```

![Problem Illustration](../images/NUM-006/problem-illustration.png)

## Input Format

- First line: integers `N` and `q`
- Next `q` lines: two integers `l` and `r` (1-based, inclusive)

## Output Format

- For each query, print the range sum on its own line

## Constraints

- `1 <= N <= 1000000`
- `1 <= q <= 100000`
- `1 <= l <= r <= N`

## Example

**Input:**

```
6 1
2 5
```

**Output:**

```
4
```

**Explanation:**

f(2)=1, f(3)=1, f(4)=1, f(5)=1, sum = 4.

![Example Visualization](../images/NUM-006/example-1.png)

## Notes

- Use a modified sieve to count distinct primes
- Build a prefix sum array over f(x)
- Time complexity: O(N log log N + q)
- Space complexity: O(N)

## Related Topics

Sieve of Eratosthenes, Prefix Sums, Number Theory

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] getPrefixSumDistinctPrimes(int n) {
        // Implement here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] firstLine = line.trim().split("\\s+");
        int n = Integer.parseInt(firstLine[0]);
        int q = Integer.parseInt(firstLine[1]);

        Solution sol = new Solution();
        long[] prefixSum = sol.getPrefixSumDistinctPrimes(n);

        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            String qLine = br.readLine();
            if (qLine == null) break;
            String[] parts = qLine.trim().split("\\s+");
            int l = Integer.parseInt(parts[0]);
            int r = Integer.parseInt(parts[1]);
            sb.append(prefixSum[r] - prefixSum[l - 1]).append("\n");
        }
        System.out.print(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def get_prefix_sum_distinct_primes(self, n):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])

    sol = Solution()
    prefix_sum = sol.get_prefix_sum_distinct_primes(n)

    output = []
    idx = 2
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx+1])
        output.append(str(prefix_sum[r] - prefix_sum[l-1]))
        idx += 2
    sys.stdout.write("\n".join(output) + "\n")

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
    vector<long long> getPrefixSumDistinctPrimes(int n) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;

    Solution sol;
    vector<long long> prefixSum = sol.getPrefixSumDistinctPrimes(n);

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << prefixSum[r] - prefixSum[l - 1] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getPrefixSumDistinctPrimes(n) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const q = parseInt(input[1]);

  const sol = new Solution();
  const prefixSum = sol.getPrefixSumDistinctPrimes(n);

  let result = "";
  let idx = 2;
  for (let i = 0; i < q; i++) {
    const l = parseInt(input[idx++]);
    const r = parseInt(input[idx++]);
    result += (prefixSum[r] - prefixSum[l - 1]).toString() + "\n";
  }
  process.stdout.write(result);
}

solve();
```
