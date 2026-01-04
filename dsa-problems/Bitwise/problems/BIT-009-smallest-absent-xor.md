---
problem_id: BIT_SMALLEST_ABSENT_XOR__8409
display_id: BIT-009
slug: smallest-absent-xor
title: "Smallest Absent XOR"
difficulty: Medium
difficulty_score: 60
topics:
  - Bitwise Operations
  - XOR
  - XOR Basis
  - Linear Algebra
tags:
  - bitwise
  - xor
  - xor-basis
  - hard
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-009: Smallest Absent XOR

## Problem Statement

Find the smallest non-negative integer x that cannot be represented as the XOR of any subset of the array (including the empty subset).

![Problem Illustration](../images/BIT-009/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the smallest absent XOR value.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
3
1 2 3
```

**Output:**

```
4
```

**Explanation:**

The reachable subset XOR values are {0, 1, 2, 3}. The smallest non-negative integer
not in the set is 4.

![Example Visualization](../images/BIT-009/example-1.png)

## Notes

- The empty subset is allowed and contributes XOR 0.
- Use a linear basis to characterize reachable XOR values.

## Related Topics

Bitwise Operations, Linear Basis

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long findSmallestAbsentXor(int n, long[] a) {
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

        Solution sol = new Solution();
        System.out.println(sol.findSmallestAbsentXor(n, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_smallest_absent_xor(self, n, a):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))

    sol = Solution()
    print(sol.find_smallest_absent_xor(n, a))

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
    long long findSmallestAbsentXor(int n, const vector<long long>& a) {
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

    Solution sol;
    cout << sol.findSmallestAbsentXor(n, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findSmallestAbsentXor(n, a) {
    // Implement here
    return BigInt(0);
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(BigInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.findSmallestAbsentXor(n, a).toString());
}

solve();
```
