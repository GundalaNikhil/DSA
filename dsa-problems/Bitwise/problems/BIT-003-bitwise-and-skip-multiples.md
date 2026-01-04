---
problem_id: BIT_AND_SKIP_MULTIPLES__8403
display_id: BIT-003
slug: bitwise-and-skip-multiples
title: "Bitwise AND Skipping Multiples"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - AND
  - Number Theory
  - Mathematics
tags:
  - bitwise
  - and-operation
  - number-theory
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-003: Bitwise AND Skipping Multiples

## Problem Statement

Given L, R, and m, compute the bitwise AND of all numbers in [L, R] that are not divisible by m. If no numbers remain, return -1.

![Problem Illustration](../images/BIT-003/problem-illustration.png)

## Input Format

- Single line: integers L R m

## Output Format

Print the bitwise AND of all numbers in [L, R] not divisible by m, or -1.

## Constraints

- `0 <= L <= R <= 1000000000000`
- `1 <= m <= 1000000`

## Example

**Input:**

```
10 15 3
```

**Output:**

```
8
```

**Explanation:**

The numbers 10, 11, 13, 14, 15 are not divisible by 3, and their AND is 8.

![Example Visualization](../images/BIT-003/example-1.png)

## Notes

- If every number in [L, R] is divisible by m, output -1.
- Use 64-bit integers for L, R, and the result.

## Related Topics

Bitwise Operations, Math

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long bitwiseAndSkipMultiples(long l, long r, long m) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long l = sc.nextLong();
        long r = sc.nextLong();
        long m = sc.nextLong();

        Solution sol = new Solution();
        System.out.println(sol.bitwiseAndSkipMultiples(l, r, m));
    }
}
```

### Python

```python
import sys

class Solution:
    def bitwise_and_skip_multiples(self, l, r, m):
        # Implement here
        return -1

def solve():
    line = sys.stdin.readline().split()
    if not line:
        return
    l, r, m = map(int, line)

    sol = Solution()
    print(sol.bitwise_and_skip_multiples(l, r, m))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    long long bitwiseAndSkipMultiples(long long l, long long r, long long m) {
        // Implement here
        return -1;
    }
};

int main() {
    long long l, r, m;
    if (!(cin >> l >> r >> m)) return 0;

    Solution sol;
    cout << sol.bitwiseAndSkipMultiples(l, r, m) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  bitwiseAndSkipMultiples(l, r, m) {
    // Implement here
    return BigInt(-1);
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);
  if (input.length < 3) return;

  const l = BigInt(input[0]);
  const r = BigInt(input[1]);
  const m = BigInt(input[2]);

  const sol = new Solution();
  console.log(sol.bitwiseAndSkipMultiples(l, r, m).toString());
}

solve();
```
