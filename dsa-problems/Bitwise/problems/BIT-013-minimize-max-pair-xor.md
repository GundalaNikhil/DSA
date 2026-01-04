---
problem_id: BIT_MINIMIZE_MAX_PAIR_XOR__8413
display_id: BIT-013
slug: minimize-max-pair-xor
title: "Minimize Max Pair XOR"
difficulty: Medium
difficulty_score: 58
topics:
  - Bitwise Operations
  - XOR
  - Dynamic Programming
  - Pairing
tags:
  - bitwise
  - xor
  - dp
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-013: Minimize Max Pair XOR

## Problem Statement

Pair up all elements (n is even) to minimize the maximum XOR among all pairs.
Return the minimal possible maximum XOR.

![Problem Illustration](../images/BIT-013/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the minimal possible maximum XOR.

## Constraints

- `2 <= n <= 16`
- `n is even`

## Example

**Input:**

```
4
1 2 3 4
```

**Output:**

```
5
```

**Explanation:**

Pairing (1,4) and (2,3) gives XORs 5 and 1, so the maximum is 5, which is minimal.

![Example Visualization](../images/BIT-013/example-1.png)

## Notes

- n is small; exponential DP over subsets is feasible.
- All elements must be paired exactly once.

## Related Topics

Bitwise Operations, DP

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int minimizeMaxPairXor(int n, int[] a) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution sol = new Solution();
        System.out.println(sol.minimizeMaxPairXor(n, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def minimize_max_pair_xor(self, n, a):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))

    sol = Solution()
    print(sol.minimize_max_pair_xor(n, a))

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
    int minimizeMaxPairXor(int n, const vector<int>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution sol;
    cout << sol.minimizeMaxPairXor(n, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minimizeMaxPairXor(n, a) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.minimizeMaxPairXor(n, a));
}

solve();
```
