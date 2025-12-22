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
    public Long crtSolve(long[] a, long[] m) {
        // Your implementation here
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        long[] a = new long[k];
        long[] m = new long[k];
        for (int i = 0; i < k; i++) {
            a[i] = sc.nextLong();
            m[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        Long res = solution.crtSolve(a, m);
        if (res == null) {
            System.out.println("NO");
        } else {
            System.out.println(res);
        }
        sc.close();
    }
}
```

### Python

```python
def crt_solve(a, m):
    # Your implementation here
    return None

def main():
    k = int(input())
    a = []
    m = []
    for _ in range(k):
        ai, mi = map(int, input().split())
        a.append(ai)
        m.append(mi)
    res = crt_solve(a, m)
    print("NO" if res is None else res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool crtSolve(const vector<long long>& a, const vector<long long>& m, long long& result) {
        // Your implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    cin >> k;
    vector<long long> a(k), m(k);
    for (int i = 0; i < k; i++) {
        cin >> a[i] >> m[i];
    }

    Solution solution;
    long long result;
    if (!solution.crtSolve(a, m, result)) {
        cout << "NO\n";
    } else {
        cout << result << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function crtSolve(a, m) {
  // Your implementation here
  return null;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
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
