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
---

# BIT-006: Minimal Bits to Flip Range

## 📋 Problem Summary

Given two integers `x` and `y`, determine if `x` can be converted to `y` by flipping the **lowest** `m` bits (for some integer `m >= 0`). If possible, return the smallest `m`. Otherwise, return `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** The Hardware Reset Sequence

You are debugging a circuit board.
- **State**: The registers hold coordinates, currently `x`.
- **Target**: You need to reset the state to `y`.
- **Mechanism**: The board has a special "Hard Reset" dial. Turning the dial to setting `m` instantly toggles the power state (0 to 1, 1 to 0) of the first `m` pins.
- **Constraint**: You cannot toggle pins individually or arbitrarily. You can only flip a contiguous block starting from pin 0.
- **Goal**: Find the setting `m` to achieve the target state `y`.

**Why This Problem Matters:**

- **Mask Generation**: Understanding properties of masks like `(1 << m) - 1`.
- **XOR Differences**: Identifying which bits differ between two numbers.
- **Constraint Validation**: Checking if a number conforms to a specific binary pattern (all 1s).

![Real-World Application](../images/BIT-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Toggle Mask
```
X = 10 (1010)
Y = 5  (0101)

Diff = 10 ^ 5 = 15 (1111)
Is 1111 a valid low-bits mask?
Yes, it's 2^4 - 1.
So m = 4.

X = 10 (1010)
Y = 4  (0100)
Diff = 14 (1110)
Is 1110 a valid low-bits mask?
No, bit 0 is 0 but bit 1 is 1. Not a contiguous block from 0.
Return -1.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Inputs**: 64-bit integers.
- **m=0**: If `x == y`, return 0.
- **Order**: Can be `x > y` or `y > x`. The XOR difference is symmetric.

Common interpretation mistake:

- ❌ Thinking `flip` means "set to 1". Flip means toggle (XOR with 1).
- ✅ Checking if `X ^ Y` is of the form `00...011...1`.

### Core Concept: XOR and Masks

`Flip(x, m)` means `x ^ Mask`, where `Mask` has the lowest `m` bits as 1.
We need `x ^ Mask = y`.
XORing both sides by `x`: `Mask = x ^ y`.
So the problem reduces to: Is `diff = x ^ y` a valid mask of form `2^m - 1`?

### Why Naive Approach is too slow

Looping `m` from 0 to 62 and checking `(1<<m) - 1 == diff` is generally fast enough (O(60)).
However, checking directly using bit properties is O(1).

## Naive Approach (Iterate m)

### Intuition

Try every possible `m`.

### Algorithm

1. `diff = x ^ y`.
2. Loop `m` from 0 to 62:
   - `mask = (1 << m) - 1`
   - If `mask == diff`: return `m`.
3. Return -1.

### Time Complexity

- **O(64)** -> O(1).

### Space Complexity

- **O(1)**.

## Optimal Approach (Bit Tricks)

### Key Insight

A number `n` is of the form `2^m - 1` (binary `11...1`) if and only if `n + 1` is a power of 2.
Power of 2 check: `(k & (k - 1)) == 0` for `k > 0`.
So, `((diff + 1) & diff) == 0`.

### Algorithm

1. `diff = x ^ y`.
2. If `diff == 0` return 0.
3. If `(diff & (diff + 1)) == 0`:
   - Return number of set bits in `diff` (Or bit length).
4. Else return -1.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-006/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-006/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long minimalBitsFlipRange(long x, long y) {
        long diff = x ^ y;
        if (diff == 0) return 0;
        
        // Check if diff is of form 111...1
        // If so, diff + 1 is a power of 2 (100...0)
        // ANDing them should be 0.
        // Also ensure diff > 0, which is handled by diff==0 check.
        // Edge case: if diff is Long.MAX_VALUE (all 1s except sign?), 
        // Logic holds for unsigned interpretation but Java uses signed.
        // For inputs up to 10^12, we are well within 63 bits, so no overflow issues.
        
        if ((diff & (diff + 1)) == 0) {
            // Count bits. Since it's all 1s, count is just population count.
            return Long.bitCount(diff);
        }
        
        return -1;
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
    diff = x ^ y
    if diff == 0: return 0
    
    # Check if diff is 2^m - 1
    if (diff & (diff + 1)) == 0:
        return diff.bit_length()
        
    return -1

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
        unsigned long long diff = x ^ y;
        if (diff == 0) return 0;
        
        if ((diff & (diff + 1)) == 0) {
            // Number of set bits.
            // For example 111 (7) -> 3.
            return __builtin_popcountll(diff);
        }
        
        return -1;
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
    let diff = x ^ y;
    if (diff === 0n) return 0;
    
    // Check (diff & (diff + 1)) == 0
    if ((diff & (diff + 1n)) === 0n) {
      // Find bit length.
      return diff.toString(2).length;
    }
    
    return -1;
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

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `x=10, y=5`.
1. Diff = `1010 ^ 0101 = 1111` (15).
2. `15 & 16 = 0`. Valid.
3. Bits in 15 = 4. Return 4.

**Input**: `x=10, y=4`.
1. Diff = `1010 ^ 0100 = 1110` (14).
2. `14 & 15 = 14`. Not 0.
3. Return -1.

## ✅ Proof of Correctness

### Invariant

We seek `m` such that `x ^ ((1<<m)-1) == y`. This implies `x ^ y == (1<<m)-1`.
The number `(1<<m)-1` is the unique positive integer with exactly `m` lowest bits set to 1 and all others 0. The check `(diff & (diff+1)) == 0` is the standard condition for numbers of the form `2^k - 1` (Mersenne numbers).

## 💡 Interview Extensions (High-Value Add-ons)

- **Range Flip**: What if we flip range `[i, j]`? Then `diff` looks like `0011100`. Shift right until bit 0 is 1, then check same property.
- **Min Flips**: Standard BFS if multiple operations allowed.

## Common Mistakes to Avoid

1. **Shift Overflow**:
   - ❌ `1 << 60` with 32-bit int.
   - ✅ Use `1L` in C++/Java.
2. **Precedence**:
   - ❌ `diff & diff + 1` evaluates as `diff & (diff + 1)` in C++, but safe to parenthesize.

## Related Concepts

- **Power of 2 Check**: `k & (k-1) == 0`.
- **Lowest Set Bit**: `k & -k`.
