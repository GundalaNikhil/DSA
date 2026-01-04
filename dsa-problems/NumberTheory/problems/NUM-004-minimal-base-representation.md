---
problem_id: NUM_MINIMAL_BASE_REPRESENTATION__6628
display_id: NUM-004
slug: minimal-base-representation
title: "Minimal Base Representation"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Bases
  - Optimization
tags:
  - number-theory
  - bases
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-004: Minimal Base Representation

## Problem Statement

Given an integer `x` (>= 2), find the smallest base `b` (2 <= b <= 36) such that the sum of digits of `x` in base `b` is minimized. If multiple bases yield the same minimal digit sum, choose the smallest base. Output `b` and the minimal digit sum.

![Problem Illustration](../images/NUM-004/problem-illustration.png)

## Input Format

- Single line: integer `x`

## Output Format

- Two integers: `b` and `digitSum`

## Constraints

- `2 <= x <= 10^12`
- `2 <= b <= 36`

## Example

**Input:**

```
31
```

**Output:**

```
5 3
```

**Explanation:**

31 in base 5 is 111, digit sum = 3. No smaller base gives a smaller digit sum.

![Example Visualization](../images/NUM-004/example-1.png)

## Notes

- Try all bases from 2 to 36
- Convert by repeated division and sum digits
- Time complexity: O(36 \* log_b(x))
- Space complexity: O(1)

## Related Topics

Number Bases, Digit Sum, Search

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findMinimalBaseSum(long x) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x = sc.nextLong();
        Solution sol = new Solution();
        sol.findMinimalBaseSum(x);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_minimal_base_sum(self, x):
        # Implement here
        pass

def solve():
    line = sys.stdin.read().split()
    if not line:
        return
    x = int(line[0])
    sol = Solution()
    sol.find_minimal_base_sum(x)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    void findMinimalBaseSum(long long x) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long x;
    if (!(cin >> x)) return 0;
    Solution sol;
    sol.findMinimalBaseSum(x);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findMinimalBaseSum(x) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const x = BigInt(input);
  const sol = new Solution();
  sol.findMinimalBaseSum(x);
}

solve();
```
