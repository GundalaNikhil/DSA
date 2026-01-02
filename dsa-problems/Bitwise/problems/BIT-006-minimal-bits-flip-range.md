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

class Solution {
    public long minimalBitsFlipRange(long x, long y) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x = sc.nextLong();
        long y = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.minimalBitsFlipRange(x, y));
        sc.close();
    }
}
```

### Python

```python
import sys

def minimal_bits_flip_range(x: int, y: int) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    x = int(data[0])
    y = int(data[1])
    
    result = minimal_bits_flip_range(x, y)
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
    long long minimalBitsFlipRange(long long x, long long y) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x, y;
    if (!(cin >> x >> y)) return 0;

    Solution solution;
    cout << solution.minimalBitsFlipRange(x, y) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalBitsFlipRange(x, y) {
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
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    const x = BigInt(tokens[0]);
    const y = BigInt(tokens[1]);
    
    const solution = new Solution();
    console.log(String(solution.minimalBitsFlipRange(x, y)));
});
```

