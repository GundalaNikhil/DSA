---
problem_id: BIT_SWAP_ADJACENT_2BIT_BLOCKS__8415
display_id: BIT-015
slug: swap-adjacent-2bit-blocks
title: "Swap Adjacent 2-Bit Blocks"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Bitwise Operations
  - Bit Manipulation
  - Masking
tags:
  - bitwise
  - bit-swapping
  - masking
  - easy
premium: true
subscription_tier: basic
---

# BIT-015: Swap Adjacent 2-Bit Blocks

## 📋 Problem Summary

Given a 32-bit integer `x`, swap every adjacent pair of 2-bit blocks. Specifically, swap bits `[0, 1]` with `[2, 3]`, bits `[4, 5]` with `[6, 7]`, and so on.

## 🌍 Real-World Scenario

**Scenario Title:** The Byte-Order Correction (Endianness Variant)

You are processing a raw data stream from a legacy hardware device.
- **Protocol**: The device transmits data in "nibble-swapped" chunks, but with a twist: it swaps 2-bit sub-nibbles instead of full 4-bit nibbles.
- **Goal**: You need to efficiently normalize the data stream by restoring the correct 2-bit block ordering.
- **Constraints**: This operation runs on a high-throughput router, so you cannot iterate bits. You need a constant-time bitwise solution (O(1)).

**Why This Problem Matters:**

- **Parallel Bit Ops**: Demonstrates how to operate on multiple data chunks simultaneously (SIMD-like logic using standard registers).
- **Masking**: Fundamental skill for isolating specific bit patterns (`0x33333333`).
- **Binary Arithmetic**: Understanding how shifting affects positions.

![Real-World Application](../images/BIT-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Swapping Logic
```
Value: 6 (00 00 ... 01 10)
Block Indices: ... 1  0
Bits:          ... 32 10

Block 0 (Bits 0-1): 10 (2)
Block 1 (Bits 2-3): 01 (1)

Swap:
Block 0 moves to Block 1 position.
Block 1 moves to Block 0 position.

Result:
New Block 0: 01 (1)
New Block 1: 10 (2)
Value: ... 10 01 = 9.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Integer `x` (32-bit).
- **Behavior**: Swap `Block[2k]` with `Block[2k+1]`.
- **Masks**: Use hex constants for clarity. `3` is `0011`. `C` is `1100`.

Common interpretation mistake:

- ❌ Swapping bit `i` with `i+1`. (That is swapping adjacent bits, `0x5555...`).
- ✅ Swapping blocks of size 2. Mask is `0011 0011...` (`0x3333...`).

### Core Concept: Parallel Swapping

Instead of iterating, we process all "even blocks" and "odd blocks" in parallel.
1. **Isolate Even Blocks**: `x & 00110011...` (Blocks 0, 2, 4...)
2. **Isolate Odd Blocks**: `x & 11001100...` (Blocks 1, 3, 5...)
3. **Shift**: Move Even blocks LEFT by 2 positions. Move Odd blocks RIGHT by 2 positions.
4. **Combine**: OR the results.

### Why Naive Approach is too slow

Looping through 8 pairs of blocks is O(1) effectively (constant 8 loops), but bitwise parallelization is much faster and cleaner (no branching).

## Naive Approach (Iterate Blocks)

### Intuition

Extract bits manually, reconstruct.

### Algorithm

1. `res = 0`.
2. Loop `i` from 0 to 7:
   - Extract block `2i` and `2i+1`.
   - Place them in swapped positions in `res`.

### Time Complexity

- **O(1)** (8 iterations).

### Space Complexity

- **O(1)**.

## Optimal Approach (Mask & Shift)

### Key Insight

Use magic masks `0x33333333` and `0xCCCCCCCC`.

### Algorithm

1. `even_mask = 0x33333333`
2. `odd_mask = 0xCCCCCCCC`
3. `even_parts = (x & even_mask)`
4. `odd_parts = (x & odd_mask)`
5. `return (even_parts << 2) | (odd_parts >>> 2)`

### Time Complexity

- **O(1)**. Few instructions.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-015/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-015/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long swapAdjacent2BitBlocks(int x) {
        // Use logical right shift >>> to handle sign bit correctly for 32-bit int
        // Mask 0x33333333 gets blocks 0, 2, 4... (0011 0011 ...)
        // Mask 0xCCCCCCCC gets blocks 1, 3, 5... (1100 1100 ...)
        
        int evenBlocks = x & 0x33333333;
        int oddBlocks = x & 0xCCCCCCCC;
        
        // Move even blocks LEFT to odd positions
        // Move odd blocks RIGHT to even positions
        int res = (evenBlocks << 2) | (oddBlocks >>> 2);
        
        // Return as long to treat as unsigned value if necessary, though problem implies 32-bit swap
        return Integer.toUnsignedLong(res);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int x = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.swapAdjacent2BitBlocks(x));
        sc.close();
    }
}
```

### Python

```python
import sys

def swap_adjacent_2bit_blocks(x: int) -> int:
    # Python ints are arbitrary precision. Use 32-bit mask.
    MASK_32 = 0xFFFFFFFF
    x &= MASK_32
    
    even_mask = 0x33333333
    odd_mask = 0xCCCCCCCC
    
    even_blocks = x & even_mask
    odd_blocks = x & odd_mask
    
    # Even blocks move left (<< 2)
    # Odd blocks move right (>> 2)
    res = (even_blocks << 2) | (odd_blocks >> 2)
    
    return res & MASK_32

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    x = int(data[0])
    
    result = swap_adjacent_2bit_blocks(x)
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
    long long swapAdjacent2BitBlocks(int x) {
        // Cast to unsigned to ensure logical shift
        unsigned int ux = (unsigned int)x;
        
        unsigned int evenMask = 0x33333333;
        unsigned int oddMask = 0xCCCCCCCC;
        
        unsigned int evenBlocks = ux & evenMask;
        unsigned int oddBlocks = ux & oddMask;
        
        return (evenBlocks << 2) | (oddBlocks >> 2);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x;
    if (!(cin >> x)) return 0;

    Solution solution;
    cout << solution.swapAdjacent2BitBlocks(x) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  swapAdjacent2BitBlocks(x) {
    // JS bitwise operators work on 32-bit signed ints
    // Use >>> for unsigned shift
    const evenMask = 0x33333333;
    const oddMask = 0xCCCCCCCC; // This will be negative in signed 32-bit context
    
    // x & oddMask might fail if oddMask reads as negative? 
    // JS treats constants as double until bitwise op.
    // 0xCCCCCCCC is 3435973836 (unsigned) or -858993460 (signed).
    // It works correctly for bitwise AND.
    
    const evenBlocks = x & evenMask;
    const oddBlocks = x & oddMask; // Will preserve bits
    
    // Note: oddBlocks is signed. >>> 2 treats it as unsigned.
    const res = (evenBlocks << 2) | (oddBlocks >>> 2);
    
    // Ensure result is unsigned 32-bit
    return (res >>> 0).toString();
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
    
    const x = Number(tokens[0]);
    
    const solution = new Solution();
    console.log(solution.swapAdjacent2BitBlocks(x));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `6` (`...00 01 10`).
Even Mask (`...00 11 00`): Keeps `00`. `0`?
No, `0x33` is `00110011`.
Positions: 76 54 32 10
Even: Keeps 10 (Bits 0-1) and 54 (Bits 4-5).
Odd: Keeps 32 (Bits 2-3) and 76 (Bits 6-7).
So `6` (`00 01 10`):
Bits 0-1 (`10`): Kept in Even. (`000010`).
Bits 2-3 (`01`): Kept in Odd. (`000100`).
Even << 2: `00001000` (8).
Odd >> 2: `00000001` (1).
Result: 9.

## ✅ Proof of Correctness

### Invariant

The operation is a bijection on the 32-bit space. By masking and shifting, we move bits exactly 2 positions (block size) in opposite directions, effectively swapping the blocks without collision (since we mask disjoint sets).

## 💡 Interview Extensions (High-Value Add-ons)

- **Generalize**: Swap blocks of size 4 (`0x0F0F0F0F`), size 1 (`0x55555555`), size 8 (`0x00FF00FF`).
- **Reverse Bits**: Combining swap 1, 2, 4, 8, 16 reverses all bits in O(log bits).

## Common Mistakes to Avoid

1. **Mask Values**:
   - ❌ `0x55555555` is for 1-bit swap.
   - ✅ `0x33333333` is for 2-bit swap.
2. **Shift Direction**:
   - ❌ Shifting Even (Low) Right falls off edge.
   - ✅ Even (Low) needs to go High (Left). Odd (High) needs to go Low (Right).

## Related Concepts

- **SWAR**: SIMD Within A Register.
- **Bit Reversal**: Divide and conquer approach.
