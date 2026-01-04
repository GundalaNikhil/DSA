---
problem_id: BIT_MINIMAL_BITS_FLIP_RANGE__8406
display_id: BIT-006
slug: minimal-bits-flip-range
title: "Minimal Bits to Flip Range"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Bit Manipulation
tags:
  - bitwise
  - xor
  - bit-flipping
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-006: Minimal Bits to Flip Range

## Problem Statement

Given two integers `x` and `y`, determine if `x` can be converted to `y` by flipping the **lowest** `m` bits (for some integer `m >= 0`). If possible, return the smallest `m`. Otherwise, return `-1`.

![Problem Illustration](../images/BIT-006/problem-illustration.png)

## Input Format

- Single line: integers x y

## Output Format

Print the smallest m, or -1 if impossible.

## Constraints

- `0 <= x, y <= 1000000000000`

## Example

**Input:**

```
10 5
```

**Output:**

```
4
```

**Explanation:**

10 XOR 5 = 15, which is 2^4 - 1, so flipping the lowest 4 bits works.

![Example Visualization](../images/BIT-006/example-1.png)

## Notes

- Flipping the lowest m bits means toggling every bit position 0..m-1.
- If x == y, the smallest m is 0.

## Related Topics

Bitwise Operations, Math

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int minimalBitsToFlip(long x, long y) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x = sc.nextLong();
        long y = sc.nextLong();

        Solution sol = new Solution();
        System.out.println(sol.minimalBitsToFlip(x, y));
    }
}
```

### Python

```python
import sys

class Solution:
    def minimal_bits_to_flip(self, x, y):
        # Implement here
        return -1

def solve():
    line = sys.stdin.readline().split()
    if not line:
        return
    x, y = map(int, line)

    sol = Solution()
    print(sol.minimal_bits_to_flip(x, y))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    int minimalBitsToFlip(long long x, long long y) {
        // Implement here
        return -1;
    }
};

int main() {
    long long x, y;
    if (!(cin >> x >> y)) return 0;

    Solution sol;
    cout << sol.minimalBitsToFlip(x, y) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minimalBitsToFlip(x, y) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);
  if (input.length < 2) return;

  const x = BigInt(input[0]);
  const y = BigInt(input[1]);

  const sol = new Solution();
  console.log(sol.minimalBitsToFlip(x, y));
}

solve();
```
