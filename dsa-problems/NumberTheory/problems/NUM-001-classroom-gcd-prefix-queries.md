---
problem_id: NUM_CLASSROOM_GCD_PREFIX_QUERIES__4821
display_id: NUM-001
slug: classroom-gcd-prefix-queries
title: "Classroom GCD Prefix Queries"
difficulty: Easy
difficulty_score: 25
topics:
  - Number Theory
  - GCD
  - Prefix Computation
tags:
  - number-theory
  - gcd
  - prefix
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-001: Classroom GCD Prefix Queries

## Problem Statement

You are given an array `a`. For each query `r`, return the greatest common divisor of the prefix `a[0..r]` (inclusive). Preprocess once to answer all queries efficiently.

![Problem Illustration](../images/NUM-001/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a[i]`
- Next `q` lines: integer `r` (0-based index)

## Output Format

- For each query, print `gcd(a[0..r])` on its own line

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `0 <= r < n`

## Example

**Input:**

```
3 3
12 18 6
0
1
2
```

**Output:**

```
12
6
6
```

**Explanation:**

Prefix GCDs:

- r=0 -> gcd(12) = 12
- r=1 -> gcd(12,18) = 6
- r=2 -> gcd(12,18,6) = 6

![Example Visualization](../images/NUM-001/example-1.png)

## Notes

- Use absolute values when computing gcd
- Precompute prefix gcd in O(n)
- Each query is O(1)
- Space complexity: O(n)

## Related Topics

GCD, Prefix Arrays, Number Theory

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] getPrefixGCDs(int n, int[] a) {
        // Implement here
        return new int[0];
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

        int[] a = new int[n];
        String[] arrayLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(arrayLine[i]);
        }

        Solution sol = new Solution();
        int[] prefixGCD = sol.getPrefixGCDs(n, a);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int r = Integer.parseInt(br.readLine().trim());
            sb.append(prefixGCD[r]).append("\n");
        }
        System.out.print(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def get_prefix_gcds(self, n, a):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    a = [int(x) for x in input_data[2:2+n]]
    queries = [int(x) for x in input_data[2+n:2+n+q]]

    sol = Solution()
    prefix_gcds = sol.get_prefix_gcds(n, a)

    output = []
    for r in queries:
        output.append(str(prefix_gcds[r]))
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
    vector<int> getPrefixGCDs(int n, const vector<int>& a) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution sol;
    vector<int> prefixGCD = sol.getPrefixGCDs(n, a);

    for (int i = 0; i < q; i++) {
        int r;
        cin >> r;
        cout << prefixGCD[r] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getPrefixGCDs(n, a) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  let idx = 0;
  const n = parseInt(input[idx++]);
  const q = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) a.push(parseInt(input[idx++]));

  const sol = new Solution();
  const prefixGCD = sol.getPrefixGCDs(n, a);

  let result = "";
  for (let i = 0; i < q; i++) {
    const r = parseInt(input[idx++]);
    result += prefixGCD[r] + "\n";
  }
  process.stdout.write(result);
}

solve();
```
