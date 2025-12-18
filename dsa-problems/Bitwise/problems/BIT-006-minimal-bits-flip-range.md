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

Given two non-negative integers `x` and `y`, find the smallest value `m` such that flipping the lowest `m` bits of `x` transforms it into `y`.

In other words, find the minimum `m` where `x XOR (2^m - 1) = y`. This means the XOR of `x` and `y` must have all 1s only in the lower `m` bits. If this is impossible, return `-1`.

```
ASCII Diagram: Bit Flipping Concept
====================================
x = 10 (binary: 1010)
y = 5  (binary: 0101)

XOR:  1010
    ^ 0101
    -------
      1111 (all 1s in lower 4 bits)

To flip lower m bits: XOR with (2^m - 1)
2^1 - 1 = 1    = 0001
2^2 - 1 = 3    = 0011
2^3 - 1 = 7    = 0111
2^4 - 1 = 15   = 1111 ← This works!

x XOR 15 = 1010 XOR 1111 = 0101 = 5 = y ✓

Answer: m = 4
```

## Input Format

- Single line: Two integers `x` and `y`

## Output Format

A single integer `m` (minimum bits to flip), or `-1` if impossible

## Constraints

- `0 <= x, y <= 10^12`
- Numbers fit in 64-bit integers

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

```
Step-by-Step Analysis:
======================
x = 10 = 1010 (binary)
y = 5  = 0101 (binary)

Compute x XOR y:
  1010
^ 0101
-------
  1111 = 15

Check if x XOR y has pattern of consecutive 1s from LSB:
1111 = 2^4 - 1 ✓

This means flipping lower 4 bits converts x to y.

Verification:
x XOR (2^4 - 1) = 10 XOR 15
  1010
^ 1111
-------
  0101 = 5 = y ✓

Answer: m = 4
```

```
ASCII Bit Position Diagram:
===========================
Bit position: 3  2  1  0
             ───────────
x (10):       1  0  1  0
y (5):        0  1  0  1
             ───────────
XOR:          1  1  1  1  ← All 1s in lower 4 bits
              └──┴──┴──┘
              Must flip all these bits

m = 4 (positions 0,1,2,3)
```

## Notes

- If `x XOR y` has all 1s only in the lower bits, answer exists
- If there are any 0s between 1s (like 10110), it's impossible
- The pattern must be: 0...0111...1 (zero or more 0s, then all 1s)
- Edge case: if `x = y`, then `m = 0` (no bits to flip)

## Related Topics

XOR Properties, Bit Manipulation, Pattern Matching, Consecutive Bits

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minimalBitsToFlip(long x, long y) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long y = sc.nextLong();

        Solution solution = new Solution();
        int result = solution.minimalBitsToFlip(x, y);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def minimal_bits_to_flip(x: int, y: int) -> int:
    # Your implementation here
    return 0

def main():
    x, y = map(int, input().split())
    result = minimal_bits_to_flip(x, y)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int minimalBitsToFlip(long long x, long long y) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x, y;
    cin >> x >> y;

    Solution solution;
    cout << solution.minimalBitsToFlip(x, y) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalBitsToFlip(x, y) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const [x, y] = data[0].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.minimalBitsToFlip(x, y));
});
```
