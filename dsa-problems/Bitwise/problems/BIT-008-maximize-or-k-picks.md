---
problem_id: BIT_MAXIMIZE_OR_K_PICKS__8408
display_id: BIT-008
slug: maximize-or-k-picks
title: "Maximize OR With K Picks"
difficulty: Medium
difficulty_score: 48
topics:
  - Bitwise Operations
  - OR
  - Greedy
  - Array
tags:
  - bitwise
  - or-operation
  - greedy
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-008: Maximize OR With K Picks

## Problem Statement

Choose exactly k elements from the array to maximize the bitwise OR of the chosen set. Return the maximum OR value.

![Problem Illustration](../images/BIT-008/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer k

## Output Format

Print the maximum possible OR value.

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`

## Example

**Input:**

```
3
1 2 4
2
```

**Output:**

```
6
```

**Explanation:**

Choosing 2 and 4 gives OR = 6, which is the maximum.

![Example Visualization](../images/BIT-008/example-1.png)

## Notes

- You must choose exactly k elements.
- The order of chosen elements does not matter.

## Related Topics

Bitwise Operations, Greedy

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maximizeOrWithK(int n, long[] a, int k) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[] a = new long[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(parts[i]);
            }
        }

        String kLine = br.readLine();
        if (kLine == null) return;
        int k = Integer.parseInt(kLine.trim());

        Solution sol = new Solution();
        System.out.println(sol.maximizeOrWithK(n, a, k));
    }
}
```

### Python

```python
import sys

class Solution:
    def maximize_or_with_k(self, n, a, k):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    if len(input_data) > n+1:
        k = int(input_data[n+1])
    else:
        k = n

    sol = Solution()
    print(sol.maximize_or_with_k(n, a, k))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maximizeOrWithK(int n, const vector<long long>& a, int k) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int k;
    cin >> k;

    Solution sol;
    cout << sol.maximizeOrWithK(n, a, k) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maximizeOrWithK(n, a, k) {
    // Implement here
    return BigInt(0);
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(BigInt(input[idx++]));
  }
  const k = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.maximizeOrWithK(n, a, k).toString());
}

solve();
```
