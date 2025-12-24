---
problem_id: NUM_DISTINCT_PRIME_FACTORS_PREFIX__5173
display_id: NUM-006
slug: distinct-prime-factors-prefix
title: "Distinct Prime Factors Count Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Sieve
  - Prefix Sums
tags:
  - number-theory
  - sieve
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-006: Distinct Prime Factors Count Prefix

## Problem Statement

For each integer `x`, let `f(x)` be the number of distinct prime factors of `x`. Precompute `f(1..N)` and answer range sum queries:

```
sum_{x=l..r} f(x)
```

![Problem Illustration](../images/NUM-006/problem-illustration.png)

## Input Format

- First line: integers `N` and `q`
- Next `q` lines: two integers `l` and `r` (1-based, inclusive)

## Output Format

- For each query, print the range sum on its own line

## Constraints

- `1 <= N <= 1000000`
- `1 <= q <= 100000`
- `1 <= l <= r <= N`

## Example

**Input:**

```
6 1
2 5
```

**Output:**

```
4
```

**Explanation:**

f(2)=1, f(3)=1, f(4)=1, f(5)=1, sum = 4.

![Example Visualization](../images/NUM-006/example-1.png)

## Notes

- Use a modified sieve to count distinct primes
- Build a prefix sum array over f(x)
- Time complexity: O(N log log N + q)
- Space complexity: O(N)

## Related Topics

Sieve of Eratosthenes, Prefix Sums, Number Theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] buildPrefixDistinct(int N) {
        // Your implementation here
        return new long[N + 1];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int q = sc.nextInt();

        Solution solution = new Solution();
        long[] pref = solution.buildPrefixDistinct(N);
        for (int i = 0; i < q; i++) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            System.out.println(pref[r] - pref[l - 1]);
        }
        sc.close();
    }
}
```

### Python

```python
def build_prefix_distinct(N: int):
    # Your implementation here
    return [0] * (N + 1)

def main():
    N, q = map(int, input().split())
    pref = build_prefix_distinct(N)
    for _ in range(q):
        l, r = map(int, input().split())
        print(pref[r] - pref[l - 1])

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
    vector<long long> buildPrefixDistinct(int N) {
        // Your implementation here
        return vector<long long>(N + 1, 0);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, q;
    cin >> N >> q;
    Solution solution;
    vector<long long> pref = solution.buildPrefixDistinct(N);
    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        cout << pref[r] - pref[l - 1] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function buildPrefixDistinct(N) {
  // Your implementation here
  return new Array(N + 1).fill(0);
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
  const N = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const pref = buildPrefixDistinct(N);
  const out = [];
  for (let i = 0; i < q; i++) {
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    out.push((pref[r] - pref[l - 1]).toString());
  }
  console.log(out.join("\n"));
});
```
