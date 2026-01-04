---
problem_id: NUM_MODULAR_EXPONENT_DIGIT_STREAM__9056
display_id: NUM-009
slug: modular-exponent-digit-stream
title: "Modular Exponent With Digit Stream"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Modular Exponentiation
  - Big Integers
tags:
  - number-theory
  - modular
  - exponentiation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-009: Modular Exponent With Digit Stream

## Problem Statement

Compute `a^e mod m`, where `e` is given as a decimal digit string that may be very large. You must process the exponent as a string.

![Problem Illustration](../images/NUM-009/problem-illustration.png)

## Input Format

- First line: two integers `a` and `m`
- Second line: string `e` (decimal digits)

## Output Format

- Single integer: `a^e mod m`

## Constraints

- `1 <= a, m <= 10^9`
- `1 <= |e| <= 100000`
- `e` has no leading zeros unless `e` is "0"

## Example

**Input:**

```
3 7
5
```

**Output:**

```
5
```

**Explanation:**

3^5 = 243, and 243 mod 7 = 5.

![Example Visualization](../images/NUM-009/example-1.png)

## Notes

- Process digits: result = result^10 \* a^digit (mod m)
- Use fast modular exponentiation for small powers
- Time complexity: O(|e| log m)
- Space complexity: O(1)

## Related Topics

Modular Exponentiation, Big Exponents

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long modularExponent(long a, String e, long m) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long a = sc.nextLong();
        long m = sc.nextLong();
        String e = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.modularExponent(a, e, m));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def modular_exponent(self, a, e, m):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    m = int(input_data[1])
    e = input_data[2]
    sol = Solution()
    print(sol.modular_exponent(a, e, m))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    long long modularExponent(long long a, string e, long long m) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, m;
    string e;
    if (!(cin >> a >> m >> e)) return 0;
    Solution sol;
    cout << sol.modularExponent(a, e, m) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  modularExponent(a, e, m) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const a = BigInt(input[0]);
  const m = BigInt(input[1]);
  const e = input[2];
  const sol = new Solution();
  console.log(sol.modularExponent(a, e, m).toString());
}

solve();
```
