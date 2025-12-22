---
problem_id: BIT_SWAP_ADJACENT_2BIT_BLOCKS__8415
display_id: BIT-015
slug: swap-adjacent-2bit-blocks
title: "Swap Adjacent 2-Bit Blocks"
difficulty: Easy
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

Given a 32-bit integer, treat it as 16 pairs of 2-bit blocks and swap each pair of adjacent blocks. This elegant bit manipulation problem tests your understanding of bit masking and shifting operations—fundamental techniques in low-level programming and systems design.

## 🌍 Real-World Scenario

**Scenario Title:** GPU Texture Compression and Pixel Format Conversion

Imagine you're working on a graphics driver team at NVIDIA or AMD, developing optimized texture compression algorithms for modern GPUs. Graphics cards store pixel data in various formats, and one common optimization involves swapping adjacent 2-bit blocks to convert between different color channel orderings (like RGBA to BGRA or transforming compressed texture formats).

In GPU texture units, pixels are often packed into 32-bit words where each 2-bit segment might represent a color channel component or alpha transparency value. When rendering textures, the GPU needs to rapidly convert between different pixel formats to match what shaders expect. A common operation is swapping adjacent 2-bit blocks across the entire 32-bit word—exactly what this problem solves.

For example, DirectX and OpenGL sometimes need different pixel orderings. A game might load a texture in one format but need to render it in another. Instead of reprocessing entire texture files, the GPU can perform bit-swapping operations in parallel across millions of pixels using specialized hardware instructions. This single operation can save gigabytes of texture memory and milliseconds per frame.

The technique also appears in network protocol implementations (reordering packet header fields), cryptographic algorithms (bit permutations in ciphers), and data compression (transforming bit patterns for better compression ratios).

**Why This Problem Matters:**

- **Performance-Critical:** Used in GPU drivers processing billions of pixels per second
- **Memory Bandwidth:** Reduces texture memory transfers by enabling format conversion in registers
- **Hardware Support:** Modern CPUs have SIMD instructions (like PSHUFB) that can perform similar operations in parallel

```
ASCII Diagram: GPU Pixel Format Conversion
===========================================
Original 32-bit pixel (RGBA format):
R0 R1 | G0 G1 | B0 B1 | A0 A1 | ... (16 pairs)
 [A]     [B]     [C]     [D]

After swapping adjacent 2-bit blocks:
G0 G1 | R0 R1 | A0 A1 | B0 B1 | ...
 [B]     [A]     [D]     [C]

This reordering can match a different texture format
without copying or reprocessing data!
```

## Detailed Explanation

### ASCII Diagram: 2-Bit Block Structure

```
32-bit Integer Breakdown (showing 8 bits for clarity):
=======================================================
Bit positions:  7  6  5  4  3  2  1  0
               ─────────────────────────
Original:       A₁ A₀│B₁ B₀│C₁ C₀│D₁ D₀
                 [A]   [B]   [C]   [D]
                  ↓     ↓     ↓     ↓
                  └──┐  └──┐  └──┐  └──┐
                     ↓     ↓     ↓     ↓
After swap:      B₁ B₀│A₁ A₀│D₁ D₀│C₁ C₀
                  [B]   [A]   [D]   [C]

Legend:
  [X] = 2-bit block (bits at positions 2i and 2i+1)
  Adjacent pairs swap: (A,B), (C,D), (E,F), ...
  Total swaps for 32-bit: 16 blocks → 8 swaps
```

### ASCII Diagram: Bit Masking Technique

```
Masking Strategy:
=================
To extract and swap 2-bit blocks, use two masks:

Mask 1 (0x33333333 in hex):
Binary: 00110011 00110011 00110011 00110011
        ││  ││   ││  ││   ││  ││   ││  ││
        └┴──┴┘   └┴──┴┘   └┴──┴┘   └┴──┴┘
        Selects positions: 0-1, 4-5, 8-9, ... (alternating pairs)

Mask 2 (0xCCCCCCCC in hex):
Binary: 11001100 11001100 11001100 11001100
        ││  ││   ││  ││   ││  ││   ││  ││
        └┴──┴┘   └┴──┴┘   └┴──┴┘   └┴──┴┘
        Selects positions: 2-3, 6-7, 10-11, ... (other alternating pairs)

Operation:
1. Extract blocks at positions (0-1, 4-5, ...): x & 0x33333333
2. Shift left by 2: (x & 0x33333333) << 2
3. Extract blocks at positions (2-3, 6-7, ...): x & 0xCCCCCCCC
4. Shift right by 2: (x & 0xCCCCCCCC) >> 2
5. Combine: ((x & 0x33333333) << 2) | ((x & 0xCCCCCCCC) >> 2)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** A single non-negative integer `x` (0 ≤ x ≤ 10⁹, treated as 32-bit unsigned)
- **Output:** The integer after swapping adjacent 2-bit blocks
- **Block Definition:** Bits at positions 2i and 2i+1 form block i (0-indexed from right)
- **Swap Operation:** Block i swaps with block i+1 for i = 0, 2, 4, ..., 30

Common interpretation mistake:

- ❌ **Wrong:** Swapping individual bits (bit 0 with bit 1, bit 2 with bit 3, etc.)
- ✅ **Correct:** Swapping 2-bit blocks as units (block [0-1] with block [2-3], block [4-5] with block [6-7], etc.)

### Understanding 2-Bit Blocks

```
Example: x = 6 (binary: 0110)
Blocks from right:
  Block 0: bits [1-0] = 10 (value 2)
  Block 1: bits [3-2] = 01 (value 1)

After swap:
  Block 0: bits [1-0] = 01 (value 1)  ← was block 1
  Block 1: bits [3-2] = 10 (value 2)  ← was block 0

Result: 1001 = 9
```

### Why Bit Manipulation is Fast

Checking each bit position individually would require multiple loops. The masking technique processes all 32 bits in constant time with just:

- 2 AND operations (masking)
- 2 shift operations
- 1 OR operation

Total: O(1) time, 5 basic operations regardless of input value!

## Naive Approach

### Intuition

The most straightforward approach is to extract each 2-bit block individually, collect them in swapped order, and reconstruct the number.

```
ASCII Diagram: Naive Block-by-Block Processing
===============================================
Input: x = 6 = 0110

Step 1: Extract all blocks
  Block 0 (bits 1-0): (x >> 0) & 3 = 0110 & 0011 = 10 (2)
  Block 1 (bits 3-2): (x >> 2) & 3 = 0001 & 0011 = 01 (1)

Step 2: Rebuild in swapped order
  result = 0
  result |= (block1 << 0) = 01 << 0 = 01
  result |= (block0 << 2) = 10 << 2 = 1000
  result = 1001 = 9

For 32-bit: repeat 16 times (once per block)
```

### Algorithm

1. Initialize `result = 0`
2. For `i` from 0 to 15 (16 blocks):
   - Extract block at position `2*(2i)`: `block_a = (x >> (4*i)) & 3`
   - Extract block at position `2*(2i+1)`: `block_b = (x >> (4*i + 2)) & 3`
   - Place `block_b` at position `4*i`: `result |= (block_b << (4*i))`
   - Place `block_a` at position `4*i + 2`: `result |= (block_a << (4*i + 2))`
3. Return `result`

### Time Complexity

- **O(1)** - Fixed number of iterations (16) regardless of input
- However, 16 iterations with multiple operations per iteration

### Space Complexity

- **O(1)** - Only storing result and loop variables

### Why This Works

Each 2-bit block is extracted, and we carefully place it in the swapped position. Since we process all blocks, the final result has all blocks swapped correctly.

### Limitations

- Multiple loop iterations (not truly constant time in practice)
- Many bit operations per iteration (extract, shift, OR)
- Not utilizing parallel bit manipulation
- Harder to optimize for compiler/CPU

## Optimal Approach

### Key Insight

Instead of processing blocks individually, we can swap ALL blocks simultaneously using bit masking! The key observation is that swapping can be decomposed into:

1. Move all "odd-positioned" blocks left by 2 bits
2. Move all "even-positioned" blocks right by 2 bits
3. Combine the results

This works because the masks ensure no overlap between the moved blocks.

### Algorithm

1. Create mask for odd blocks: `mask1 = 0x33333333` (binary: ...00110011)
2. Create mask for even blocks: `mask2 = 0xCCCCCCCC` (binary: ...11001100)
3. Extract and shift odd blocks: `part1 = (x & mask1) << 2`
4. Extract and shift even blocks: `part2 = (x & mask2) >> 2`
5. Combine: `result = part1 | part2`
6. Return `result`

### Time Complexity

- **O(1)** - Exactly 5 bitwise operations (2 AND, 2 shifts, 1 OR)
- True constant time, independent of input value

### Space Complexity

- **O(1)** - Only temporary variables for masks and parts

### Why This Is Optimal

**Theoretical Lower Bound:** We must read all 32 bits and write all 32 bits, giving Ω(1) for fixed-width integers. Our algorithm achieves O(1) with minimal operations.

**Proof of Correctness:**

- `mask1 = 0x33333333` selects bits at positions 0-1, 4-5, 8-9, ..., 28-29
- `mask2 = 0xCCCCCCCC` selects bits at positions 2-3, 6-7, 10-11, ..., 30-31
- `mask1` and `mask2` are complementary for these positions
- Shifting left by 2 moves blocks to where their swap partners were
- Shifting right by 2 moves blocks to where their swap partners were
- OR combines without collision since masks don't overlap after shifts

```
ASCII Diagram: Parallel Swapping
=================================
Original:     ...│B₃B₂│A₃A₂│B₁B₀│A₁A₀
                   [B'] [A'] [B ] [A ]

Mask1 & x:    ...│0 0 │A₃A₂│0 0 │A₁A₀  (select A blocks)
Shift << 2:   ...│A₃A₂│0 0 │A₁A₀│0 0   (move A right)

Mask2 & x:    ...│B₃B₂│0 0 │B₁B₀│0 0   (select B blocks)
Shift >> 2:   ...│0 0 │B₃B₂│0 0 │B₁B₀  (move B left)

OR result:    ...│A₃A₂│B₃B₂│A₁A₀│B₁B₀  (swapped!)
                   [A'] [B'] [A ] [B ]
```

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int swapAdjacent2BitBlocks(int x) {
        // Mask for bits at positions 0-1, 4-5, 8-9, ... (pattern: 00110011)
        int mask1 = 0x33333333;

        // Mask for bits at positions 2-3, 6-7, 10-11, ... (pattern: 11001100)
        int mask2 = 0xCCCCCCCC;

        // Extract blocks at odd positions and shift right (towards lower positions)
        int part1 = (x & mask1) << 2;

        // Extract blocks at even positions and shift left (towards higher positions)
        int part2 = (x & mask2) >>> 2; // Using >>> for unsigned right shift

        // Combine both parts
        return part1 | part2;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.swapAdjacent2BitBlocks(x);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def swap_adjacent_2bit_blocks(x: int) -> int:
    """
    Swap adjacent 2-bit blocks in a 32-bit integer.

    Time: O(1) - constant number of bitwise operations
    Space: O(1) - only using fixed variables
    """
    # Mask for bits at positions 0-1, 4-5, 8-9, ... (pattern: 00110011)
    mask1 = 0x33333333

    # Mask for bits at positions 2-3, 6-7, 10-11, ... (pattern: 11001100)
    mask2 = 0xCCCCCCCC

    # Extract blocks and swap
    part1 = (x & mask1) << 2
    part2 = (x & mask2) >> 2

    # Combine and ensure 32-bit result
    result = (part1 | part2) & 0xFFFFFFFF

    return result

def main():
    x = int(input().strip())
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
    int swapAdjacent2BitBlocks(int x) {
        // Mask for bits at positions 0-1, 4-5, 8-9, ... (pattern: 00110011)
        unsigned int mask1 = 0x33333333;

        // Mask for bits at positions 2-3, 6-7, 10-11, ... (pattern: 11001100)
        unsigned int mask2 = 0xCCCCCCCC;

        // Convert to unsigned for proper bit operations
        unsigned int ux = static_cast<unsigned int>(x);

        // Extract blocks and swap
        unsigned int part1 = (ux & mask1) << 2;
        unsigned int part2 = (ux & mask2) >> 2;

        // Combine both parts
        return static_cast<int>(part1 | part2);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x;
    cin >> x;

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
    // Mask for bits at positions 0-1, 4-5, 8-9, ... (pattern: 00110011)
    const mask1 = 0x33333333;

    // Mask for bits at positions 2-3, 6-7, 10-11, ... (pattern: 11001100)
    const mask2 = 0xcccccccc;

    // Extract blocks and swap
    const part1 = (x & mask1) << 2;
    const part2 = (x & mask2) >>> 2; // Unsigned right shift

    // Combine both parts (use >>> 0 to ensure 32-bit unsigned result)
    return (part1 | part2) >>> 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const x = parseInt(data[0]);

  const solution = new Solution();
  console.log(solution.swapAdjacent2BitBlocks(x));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample: **x = 6**

Binary representation: `00000000 00000000 00000000 00000110`

We maintain:

- **x** = input value (6)
- **mask1** = 0x33333333 (selects odd-positioned 2-bit blocks)
- **mask2** = 0xCCCCCCCC (selects even-positioned 2-bit blocks)

Initialize:

- x = 6 = `...00000110`
- mask1 = `...00110011`
- mask2 = `...11001100`

Now execute the algorithm:

|  Step |    Operation     | Binary Result | Decimal | Explanation                  |
| ----: | :--------------: | ------------: | ------- | ---------------------------- |
| Start |        x         |      00000110 | 6       | Input value                  |
|     1 |    x & mask1     |      00000010 | 2       | Extract bits [1-0]: 10       |
|     2 | (x & mask1) << 2 |      00001000 | 8       | Shift left by 2 positions    |
|     3 |    x & mask2     |      00000100 | 4       | Extract bits [3-2]: 01       |
|     4 | (x & mask2) >> 2 |      00000001 | 1       | Shift right by 2 positions   |
|     5 |  part1 \| part2  |      00001001 | 9       | Combine: 1000 \| 0001 = 1001 |

**Detailed breakdown:**

```
Original x = 6:
Bit positions:  7 6 5 4 3 2 1 0
Binary:         0 0 0 0 0 1 1 0
Blocks:             [0] [1] [2]
                     01  10

Step-by-step masking:
1. x & mask1 = 0110 & 0011 = 0010 (extracts block 0: 10)
2. Shift left by 2: 0010 << 2 = 1000 (moves to position of block 1)
3. x & mask2 = 0110 & 1100 = 0100 (extracts block 1: 01)
4. Shift right by 2: 0100 >> 2 = 0001 (moves to position of block 0)
5. OR: 1000 | 0001 = 1001 (combines both parts)

Result: 1001 (binary) = 9 (decimal)
```

**Observations:**

1. Block at positions [1-0] was `10` (value 2), moved to positions [3-2]
2. Block at positions [3-2] was `01` (value 1), moved to positions [1-0]
3. Blocks successfully swapped!
4. All other bits (positions 4-31) remain 0

Answer is **9**.

```
ASCII Visualization of Execution:
==================================
Original:  bits [3-2][1-0] = [01][10]

After mask1 & shift:
  Extract [10] → shift left → [10][ 0]

After mask2 & shift:
  Extract [01] → shift right → [ 0][01]

Combine:
  [10][00] OR [00][01] = [10][01]

Result: [10][01] = 1001 = 9 ✓
```

## ✅ Proof of Correctness

### Invariant

**Block Swap Property:** For any 2-bit block at position 2i (where i is even), it swaps with the block at position 2(i+1). Formally: `output[2i:2i+1] = input[2(i+1):2(i+1)+1]` and `output[2(i+1):2(i+1)+1] = input[2i:2i+1]`.

### Why the approach is correct

**Mathematical Foundation:**

**Lemma:** The masks 0x33333333 and 0xCCCCCCCC partition the 32 bits into two disjoint sets where each set contains alternating 2-bit blocks.

**Proof:**

1. mask1 = 0x33333333 = binary `...00110011` selects bits at positions where (position / 2) mod 2 = 0
2. mask2 = 0xCCCCCCCC = binary `...11001100` selects bits at positions where (position / 2) mod 2 = 1
3. These sets are disjoint: mask1 & mask2 = 0
4. These sets are complete: mask1 | mask2 = 0xFFFFFFFF (all bits)

**Theorem:** Shifting mask1-selected blocks left by 2 and mask2-selected blocks right by 2, then combining with OR, correctly swaps all adjacent 2-bit block pairs.

**Proof by Construction:**

- Let block A be at positions [2i, 2i+1] and block B at positions [2i+2, 2i+3] where i is even
- Block A is selected by mask1, shifted left by 2 → positions [2i+2, 2i+3] ✓
- Block B is selected by mask2, shifted right by 2 → positions [2i, 2i+1] ✓
- No collision: after shifts, mask1 blocks occupy former mask2 positions and vice versa
- OR combines without overlap since shifted blocks fill complementary positions

**Base Case:** For i=0, blocks at [0-1] and [2-3] swap correctly (verified in examples).

**Inductive Step:** If blocks at [2i, 2i+3] swap correctly, blocks at [2(i+2), 2(i+2)+3] also swap due to mask pattern repetition every 4 bits.

Therefore, the algorithm correctly swaps all 16 pairs of adjacent 2-bit blocks. ∎

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Swap Adjacent 4-Bit Blocks** - Modify to swap 4-bit blocks instead of 2-bit. (Hint: masks become 0x0F0F0F0F and 0xF0F0F0F0, shift by 4)
- **Extension 2: Reverse All Bits** - Reverse the entire bit sequence (bit 0 ↔ bit 31, bit 1 ↔ bit 30, etc.). (Hint: hierarchical swapping at multiple levels)
- **Extension 3: Swap by K Bits** - Generalize to swap adjacent k-bit blocks where k is a power of 2. (Pattern: generate masks and adjust shift amount)
- **Extension 4: SIMD Parallelization** - Process 4 integers simultaneously using SIMD instructions. (Relevant for texture processing)
- **Extension 5: In-Place Array Swap** - Apply this operation to millions of integers in an array with cache-efficient access. (Memory bandwidth optimization)

### C++ommon Mistakes to Avoid

1. **Using Signed Right Shift (>>)**

   - In Java/JavaScript, `>>` is arithmetic shift (sign-extends)
   - ❌ Wrong: `(x & mask2) >> 2` might introduce sign bits for negative numbers
   - ✅ Correct: Use `>>>` (unsigned right shift) in Java/JavaScript, or work with unsigned types

2. **Incorrect Mask Values**

   - ❌ Wrong: Using 0x55555555 (01010101 pattern) which selects individual bits, not 2-bit blocks
   - ✅ Correct: Use 0x33333333 (00110011 pattern) for alternating 2-bit blocks
   - Impact: Results in incorrect bit positions, completely wrong answer

3. **Forgetting to Combine Results**

   - After extracting and shifting both parts separately
   - ❌ Wrong: Returning only `part1` or only `part2`
   - ✅ Correct: `return part1 | part2` to combine both shifted parts

4. **Off-by-One in Shift Amount**

   - ❌ Wrong: Shifting by 1 instead of 2 (shifts individual bits, not 2-bit blocks)
   - ✅ Correct: Shift by exactly 2 to move 2-bit blocks to adjacent positions
   - Prevention: Remember blocks are 2 bits wide, so shift amount = block width

5. **Not Handling 32-Bit Boundary**
   - In languages like Python with arbitrary precision integers
   - ❌ Wrong: Not masking result with 0xFFFFFFFF, leading to extra high bits
   - ✅ Correct: `result & 0xFFFFFFFF` to ensure 32-bit result
   - Impact: Return value might exceed 32-bit range

## Related Concepts

- **Bit Masking** - Using AND operations to select specific bit patterns
- **Bit Shifting** - Moving bits left (<<) or right (>>) to new positions
- **Bit Interleaving** - Morton codes and Z-order curves for spatial indexing
- **Bit Permutations** - General bit rearrangement operations
- **SWAR (SIMD Within A Register)** - Processing multiple values in parallel within a single register
- **GPU Texture Swizzling** - Reordering color channels in graphics pipelines
- **Network Byte Order** - Converting between big-endian and little-endian representations
- **Hamming Distance** - Measuring bit differences after transformations
