---
problem_id: NUM_COPRIME_PAIR_COUNT__7194
display_id: NUM-002
slug: coprime-pair-count
title: "Coprime Pair Count Up To N"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Euler Totient
  - Counting
tags:
  - number-theory
  - totient
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-002: Coprime Pair Count Up To N

## Problem Statement

Given an integer `N`, count the number of ordered pairs `(i, j)` such that `1 <= i < j <= N` and `gcd(i, j) = 1`.

![Problem Illustration](../images/NUM-002/problem-illustration.png)

## Input Format

- Single line: integer `N`

## Output Format

- Single integer: number of coprime pairs

## Constraints

- `1 <= N <= 100000`

## Example

**Input:**

```
5
```

**Output:**

```
9
```

**Explanation:**

The coprime pairs are:

(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4),(3,5),(4,5)

Total = 9.

![Example Visualization](../images/NUM-002/example-1.png)

## Notes

- The answer equals sum\_{k=2..N} phi(k)
- Compute phi for all k with a sieve
- Time complexity: O(N log log N)
- Space complexity: O(N)

## Related Topics

Euler Totient, Counting, GCD

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countCoprimePairs(int n) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countCoprimePairs(n));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_coprime_pairs(self, n):
        # Implement here
        return 0

def solve():
    line = sys.stdin.read().split()
    if not line:
        return
    n = int(line[0])
    sol = Solution()
    print(sol.count_coprime_pairs(n))

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
    long long countCoprimePairs(int n) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    Solution sol;
    cout << sol.countCoprimePairs(n) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countCoprimePairs(n) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const n = parseInt(input);
  const sol = new Solution();
  console.log(sol.countCoprimePairs(n).toString());
}

solve();
```
