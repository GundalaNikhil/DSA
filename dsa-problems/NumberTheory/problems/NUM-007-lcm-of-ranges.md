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

class Solution {
    public long lcmRange(int[] a, int l, int r, long MOD) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long MOD = sc.nextLong();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution solution = new Solution();
            for (int i = 0; i < q; i++) {
                int l = sc.nextInt();
                int r = sc.nextInt();
                System.out.println(solution.lcmRange(a, l, r, MOD));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def lcm_range(a, l, r, MOD):
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        MOD = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        
        results = []
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            results.append(str(lcm_range(a, l, r, MOD)))
            
        print('\n'.join(results))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long lcmRange(const vector<int>& a, int l, int r, long long MOD) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    long long MOD;
    if (cin >> n >> q >> MOD) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution solution;
        for (int i = 0; i < q; i++) {
            int l, r;
            cin >> l >> r;
            cout << solution.lcmRange(a, l, r, MOD) << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function lcmRange(a, l, r, MOD) {
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
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const MOD = parseInt(data[idx++], 10);
  const a = [];
  for (let i = 0; i < n; i++) a.push(parseInt(data[idx++], 10));
  
  const out = [];
  for (let i = 0; i < q; i++) {
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    out.push(lcmRange(a, l, r, MOD));
  }
  console.log(out.join("\n"));
});
```

