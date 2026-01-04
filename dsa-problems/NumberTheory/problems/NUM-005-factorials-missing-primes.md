---
problem_id: NUM_FACTORIALS_MISSING_PRIMES__2941
display_id: NUM-005
slug: factorials-missing-primes
title: "Factorials With Missing Primes"
difficulty: Medium
difficulty_score: 55
topics:
  - Number Theory
  - Modular Arithmetic
  - Factorials
tags:
  - number-theory
  - factorial
  - modular
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-005: Factorials With Missing Primes

## Problem Statement

Given `n` and a prime `p`, compute:

```
product of all integers in [1..n] that are NOT divisible by p, modulo p
```

Return the result modulo `p`.

![Problem Illustration](../images/NUM-005/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `p`

## Output Format

- Single integer: the product modulo `p`

## Constraints

- `1 <= n <= 10^12`
- `2 <= p <= 10^6` and `p` is prime

## Example

**Input:**

```
6 5
```

**Output:**

```
4
```

**Explanation:**

Numbers from 1 to 6 not divisible by 5 are 1,2,3,4,6.

Product = 144, and 144 mod 5 = 4.

![Example Visualization](../images/NUM-005/example-1.png)

## Notes

- Use the periodicity of residues modulo p
- Avoid multiplying values divisible by p
- Time complexity: depends on p, typically O(p log_p n)
- Space complexity: O(p)

## Related Topics

Factorials Modulo Prime, Number Theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long productMissingPrimes(long n, int p) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long n = sc.nextLong();
        int p = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.productMissingPrimes(n, p));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def product_missing_primes(self, n, p):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    p = int(input_data[1])
    sol = Solution()
    print(sol.product_missing_primes(n, p))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    long long productMissingPrimes(long long n, int p) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    int p;
    if (!(cin >> n >> p)) return 0;
    Solution sol;
    cout << sol.productMissingPrimes(n, p) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  productMissingPrimes(n, p) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = BigInt(input[0]);
  const p = parseInt(input[1]);
  const sol = new Solution();
  console.log(sol.productMissingPrimes(n, p).toString());
}

solve();
```
