---
problem_id: NUM_CRT_EXISTENCE_VALUE__5186
display_id: NUM-015
slug: crt-existence-value
title: "CRT Existence and Value"
difficulty: Medium
difficulty_score: 58
topics:
  - Number Theory
  - Chinese Remainder Theorem
  - GCD
tags:
  - number-theory
  - crt
  - gcd
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-015: CRT Existence and Value

## Problem Statement

You are given `k` congruences:

```
x ≡ a_i (mod m_i)
```

Determine if a solution exists. If it does, output the smallest non-negative solution. Moduli are not guaranteed to be coprime.

![Problem Illustration](../images/NUM-015/problem-illustration.png)

## Input Format

- First line: integer `k`
- Next `k` lines: two integers `a_i` and `m_i`

## Output Format

- If no solution exists, print `NO`
- Otherwise, print the smallest non-negative solution

## Constraints

- `1 <= k <= 10`
- `1 <= m_i <= 10^9`
- `0 <= a_i < m_i`

## Example

**Input:**

```
2
2 6
5 9
```

**Output:**

```
14
```

**Explanation:**

The smallest x such that x%6=2 and x%9=5 is 14.

![Example Visualization](../images/NUM-015/example-1.png)

## Notes

- Use generalized CRT with gcd checks
- Combine congruences iteratively
- Time complexity: O(k log M)
- Space complexity: O(1)

## Related Topics

CRT, Extended GCD, Number Theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void solveCRT(int k, long[] a, long[] m) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        long[] a = new long[k];
        long[] m = new long[k];
        for (int i = 0; i < k; i++) {
            a[i] = sc.nextLong();
            m[i] = sc.nextLong();
        }
        Solution sol = new Solution();
        sol.solveCRT(k, a, m);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def solve_crt(self, k, a, m):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    a = []
    m = []
    idx = 1
    for _ in range(k):
        a.append(int(input_data[idx]))
        m.append(int(input_data[idx+1]))
        idx += 2
    sol = Solution()
    sol.solve_crt(k, a, m)

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
    void solveCRT(int k, const vector<long long>& a, const vector<long long>& m) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    if (!(cin >> k)) return 0;
    vector<long long> a(k), m(k);
    for (int i = 0; i < k; i++) {
        cin >> a[i] >> m[i];
    }
    Solution sol;
    sol.solveCRT(k, a, m);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveCRT(k, a, m) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const k = parseInt(input[0]);
  const a = [];
  const m = [];
  let idx = 1;
  for (let i = 0; i < k; i++) {
    a.push(BigInt(input[idx++]));
    m.push(BigInt(input[idx++]));
  }
  const sol = new Solution();
  sol.solveCRT(k, a, m);
}

solve();
```
