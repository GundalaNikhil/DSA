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
import java.math.BigInteger;

class Solution {
    public String crtSolve(long[] a, long[] m) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            long[] a = new long[k];
            long[] m = new long[k];
            for (int i = 0; i < k; i++) {
                a[i] = sc.nextLong();
                m[i] = sc.nextLong();
            }

            Solution solution = new Solution();
            String res = solution.crtSolve(a, m);
            if (res == null) {
                System.out.println("NO");
            } else {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def crt_solve(a, m):
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    try:
        k = int(next(iterator))
        a = []
        m = []
        for _ in range(k):
            a.append(int(next(iterator)))
            m.append(int(next(iterator)))
            
        res = crt_solve(a, m)
        print("NO" if res is None else res)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef __int128_t int128;

string int128ToString(int128 n) {
    if (n == 0) return "0";
    string s = "";
    while (n > 0) {
        s += (char)('0' + (n % 10));
        n /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

class Solution {
public:
    string crtSolve(const vector<long long>& a, const vector<long long>& m) {
        //Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<long long> a(k), m(k);
        for (int i = 0; i < k; i++) {
            cin >> a[i] >> m[i];
        }

        Solution solution;
        string result = solution.crtSolve(a, m);
        cout << result << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function crtSolve(a, m) {
  //Implement here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) data.push(parts[i]);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const k = parseInt(data[idx++], 10);
  const a = [];
  const m = [];
  for (let i = 0; i < k; i++) {
    a.push(parseInt(data[idx++], 10));
    m.push(parseInt(data[idx++], 10));
  }
  const res = crtSolve(a, m);
  console.log(res === null ? "NO" : res.toString());
});
```

