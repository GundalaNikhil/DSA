---
problem_id: NUM_MODULAR_INVERSE_EXISTENCE__3507
display_id: NUM-003
slug: modular-inverse-existence
title: "Modular Inverse Existence"
difficulty: Easy
difficulty_score: 22
topics:
  - Number Theory
  - GCD
  - Modular Arithmetic
tags:
  - number-theory
  - gcd
  - modular
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-003: Modular Inverse Existence

## Problem Statement

For each query `(a, m)`, determine whether `a` has a modular inverse modulo `m`. An inverse exists if and only if `gcd(a, m) = 1`.

![Problem Illustration](../images/NUM-003/problem-illustration.png)

## Input Format

- First line: integer `q`
- Next `q` lines: two integers `a` and `m`

## Output Format

- For each query, print `true` if an inverse exists, otherwise `false`

## Constraints

- `1 <= q <= 100000`
- `1 <= a, m <= 10^9`

## Example

**Input:**

```
1
4 7
```

**Output:**

```
true
```

**Explanation:**

`gcd(4, 7) = 1`, so the inverse exists.

![Example Visualization](../images/NUM-003/example-1.png)

## Notes

- Use the Euclidean algorithm for gcd
- Time complexity: O(q log max(a,m))
- Space complexity: O(1)

## Related Topics

Modular Arithmetic, GCD, Euclid Algorithm

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean hasModularInverse(long a, long m) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int q = Integer.parseInt(line.trim());
        Solution sol = new Solution();
        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            String qLine = br.readLine();
            if (qLine == null) break;
            String[] parts = qLine.trim().split("\\s+");
            long a = Long.parseLong(parts[0]);
            long m = Long.parseLong(parts[1]);
            sb.append(sol.hasModularInverse(a, m)).append("\n");
        }
        System.out.print(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def has_modular_inverse(self, a, m):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    queries = []
    idx = 1
    for _ in range(q):
        a = int(input_data[idx])
        m = int(input_data[idx+1])
        queries.append((a, m))
        idx += 2

    sol = Solution()
    output = []
    for a, m in queries:
        output.append(str(sol.has_modular_inverse(a, m)).lower())
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    bool hasModularInverse(long long a, long long m) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (!(cin >> q)) return 0;
    Solution sol;
    while (q--) {
        long long a, m;
        cin >> a >> m;
        cout << (sol.hasModularInverse(a, m) ? "true" : "false") << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  hasModularInverse(a, m) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const q = parseInt(input[0]);
  let idx = 1;
  const sol = new Solution();
  let result = "";
  for (let i = 0; i < q; i++) {
    const a = BigInt(input[idx++]);
    const m = BigInt(input[idx++]);
    result += sol.hasModularInverse(a, m) + "\n";
  }
  process.stdout.write(result);
}

solve();
```
