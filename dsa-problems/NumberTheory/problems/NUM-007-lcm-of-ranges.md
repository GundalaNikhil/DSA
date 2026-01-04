---
problem_id: NUM_LCM_OF_RANGES__8402
display_id: NUM-007
slug: lcm-of-ranges
title: "LCM of Ranges"
difficulty: Medium
difficulty_score: 52
topics:
  - Number Theory
  - LCM
  - Prime Factorization
tags:
  - number-theory
  - lcm
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-007: LCM of Ranges

## Problem Statement

Given an array `a`, answer queries asking for `lcm(a[l..r])` modulo `MOD`. Each query has `r - l <= 20`, so ranges are short.

![Problem Illustration](../images/NUM-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `q`, and `MOD`
- Second line: `n` integers `a[i]`
- Next `q` lines: two integers `l` and `r` (0-based, inclusive)

## Output Format

- For each query, print `lcm(a[l..r]) mod MOD`

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 100000`
- `1 <= a[i] <= 10^9`
- `1 <= MOD <= 10^9+7`
- `0 <= l <= r < n`, and `r - l <= 20`

## Example

**Input:**

```
3 1 1000000007
2 6 3
0 1
```

**Output:**

```
6
```

**Explanation:**

lcm(2, 6) = 6.

![Example Visualization](../images/NUM-007/example-1.png)

## Notes

- Factorize numbers in the short range
- Track max exponent per prime for the LCM
- Time complexity per query: O((r-l+1) log a[i])
- Space complexity: O(number of primes in range)

## Related Topics

LCM, Prime Factorization, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public void solveLCMQueries(int n, int q, int mod, int[] a, int[][] queries) {
        // Implement here
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
        int mod = Integer.parseInt(firstLine[2]);

        int[] a = new int[n];
        String[] arrayLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(arrayLine[i]);

        int[][] queries = new int[q][2];
        for (int i = 0; i < q; i++) {
            String qLine = br.readLine();
            if (qLine == null) break;
            String[] parts = qLine.trim().split("\\s+");
            queries[i][0] = Integer.parseInt(parts[0]);
            queries[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        sol.solveLCMQueries(n, q, mod, a, queries);
    }
}
```

### Python

```python
import sys

class Solution:
    def solve_lcm_queries(self, n, q, mod, a, queries):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    mod = int(input_data[2])
    a = [int(x) for x in input_data[3:3+n]]
    queries = []
    idx = 3 + n
    for _ in range(q):
        queries.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    sol = Solution()
    sol.solve_lcm_queries(n, q, mod, a, queries)

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
    void solveLCMQueries(int n, int q, int mod, const vector<int>& a, const vector<pair<int, int>>& queries) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q, mod;
    if (!(cin >> n >> q >> mod)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vector<pair<int, int>> queries(q);
    for (int i = 0; i < q; i++) cin >> queries[i].first >> queries[i].second;

    Solution sol;
    sol.solveLCMQueries(n, q, mod, a, queries);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveLCMQueries(n, q, mod, a, queries) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const n = parseInt(input[0]);
  const q = parseInt(input[1]);
  const mod = parseInt(input[2]);
  const a = [];
  let idx = 3;
  for (let i = 0; i < n; i++) a.push(parseInt(input[idx++]));
  const queries = [];
  for (let i = 0; i < q; i++) {
    const l = parseInt(input[idx++]);
    const r = parseInt(input[idx++]);
    queries.push([l, r]);
  }

  const sol = new Solution();
  sol.solveLCMQueries(n, q, mod, a, queries);
}

solve();
```
