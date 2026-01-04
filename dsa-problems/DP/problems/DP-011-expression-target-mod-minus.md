---
problem_id: DP_EXPR_MOD_MINUS__8104
display_id: DP-011
slug: expression-target-mod-minus
title: "Expression Target Modulo With Required Minus"
difficulty: Medium
difficulty_score: 60
topics:
  - Dynamic Programming
  - String
  - Modulo Arithmetic
tags:
  - dp
  - strings
  - modulo
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-011: Expression Target Modulo With Required Minus

## Problem Statement

You are given:

- a digit string `s` (length up to 12)
- an integer modulus `M`
- a target remainder `K`
- a maximum chunk length `Lmax`

You must split `s` into chunks of length `1..Lmax` (from left to right, no reordering) and insert `+` or `-` between chunks to form an expression.

Rules:

- No chunk may have leading zeros unless the chunk is exactly `"0"`.
- You must use **at least one `-` operator** in the entire expression.
- Evaluate the expression normally; let `val % M` be its remainder (negative values are taken modulo `M` as usual).

Count the number of valid expressions whose value modulo `M` equals `K`. Output the count.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513331/dsa/dp/f7zouw1gh4uotnj8nhph.jpg)

## Input Format

- First line: digit string `s`
- Second line: three integers `M`, `K`, `Lmax`

## Output Format

Print one integer: the number of valid expressions modulo `1_000_000_007`.

## Constraints

- `1 <= |s| <= 12`
- `1 <= M <= 50`
- `0 <= K < M`
- `1 <= Lmax <= |s|`

## Example

**Input:**

```
1234
7 0 2
```

**Output:**

```
5
```

**Explanation:**

With chunk length up to 2 and at least one minus, there are 5 valid expressions whose value is congruent to 0 modulo 7.

![Example Visualization](../images/DP-011/example-1.png)

## Notes

- Negative intermediate results are allowed; apply modulo normally (e.g., `(-1) % 7 = 6`).
- At least one minus is mandatory; expressions with only `+` are invalid.

## Related Topics

Dynamic Programming, Modulo Arithmetic, String Parsing

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countExpressions(String s, int m, int k, int lmax) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String secondLine = br.readLine();
        if (s == null || secondLine == null) return;

        String[] parts = secondLine.trim().split("\\s+");
        if (parts.length < 3) return;
        int m = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);
        int lmax = Integer.parseInt(parts[2]);

        Solution sol = new Solution();
        System.out.println(sol.countExpressions(s, m, k, lmax));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_expressions(self, s, m, k, lmax):
        # Implement here
        return 0

def solve():
    s = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    if not line2:
        return
    m, k, lmax = map(int, line2.split())

    sol = Solution()
    print(sol.count_expressions(s, m, k, lmax))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int countExpressions(string s, int m, int k, int lmax) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    int m, k, lmax;
    if (!(cin >> m >> k >> lmax)) return 0;

    Solution sol;
    cout << sol.countExpressions(s, m, k, lmax) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countExpressions(s, m, k, lmax) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 4) return;

  const s = input[0];
  const m = parseInt(input[1]);
  const k = parseInt(input[2]);
  const lmax = parseInt(input[3]);

  const sol = new Solution();
  console.log(sol.countExpressions(s, m, k, lmax));
}

solve();
```
