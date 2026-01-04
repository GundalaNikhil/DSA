---
problem_id: NUM_SUM_DIVISORS_RANGE__4175
display_id: NUM-010
slug: sum-divisors-range
title: "Sum of Divisors in Range"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Divisors
  - Prefix Sums
tags:
  - number-theory
  - divisors
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-010: Sum of Divisors in Range

## Problem Statement

For each integer `n`, let `sigma(n)` be the sum of its positive divisors. Given `L` and `R`, compute:

```
Sigma = sum_{n=L..R} sigma(n) mod 1000000007
```

![Problem Illustration](../images/NUM-010/problem-illustration.png)

## Input Format

- Single line: two integers `L` and `R`

## Output Format

- Single integer: the range sum modulo `1000000007`

## Constraints

- `1 <= L <= R <= 1000000`
- Modulus is fixed at `1000000007`

## Example

**Input:**

```
2 4
```

**Output:**

```
14
```

**Explanation:**

sigma(2)=3, sigma(3)=4, sigma(4)=7, total = 14.

![Example Visualization](../images/NUM-010/example-1.png)

## Notes

- Precompute sigma values using a sieve-like method
- Use prefix sums for fast range queries
- Time complexity: O(R log R)
- Space complexity: O(R)

## Related Topics

Divisor Sums, Sieve, Prefix Sums

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long sumDivisorsInRange(int l, int r) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int l = sc.nextInt();
        int r = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.sumDivisorsInRange(l, r));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def sum_divisors_in_range(self, l, r):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    l = int(input_data[0])
    r = int(input_data[1])
    sol = Solution()
    print(sol.sum_divisors_in_range(l, r))

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
    long long sumDivisorsInRange(int l, int r) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int l, r;
    if (!(cin >> l >> r)) return 0;
    Solution sol;
    cout << sol.sumDivisorsInRange(l, r) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  sumDivisorsInRange(l, r) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const l = parseInt(input[0]);
  const r = parseInt(input[1]);
  const sol = new Solution();
  console.log(sol.sumDivisorsInRange(l, r).toString());
}

solve();
```
