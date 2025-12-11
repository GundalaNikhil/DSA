---
unique_problem_id: bitwise_015
display_id: BITWISE-015
slug: swap-adjacent-2bit-blocks
version: 1.0.0
difficulty: Easy
topic_tags:
  - Bitwise
  - Bit Manipulation
  - Masking
  - Shift Operations
---

# Swap Adjacent 2-Bit Blocks

## Problem Description

Treat the 32-bit representation of `x` as sixteen 2-bit blocks. Swap each pair of adjacent 2-bit blocks: bits [0-1] swap with [2-3], bits [4-5] swap with [6-7], etc. Return the resulting integer.

## Examples

- Example 1:
  - Input: `x = 6` (binary: `0110`)
  - Output: `9` (binary: `1001`)
  - Explanation: 2-bit blocks: `01|10`. Swap adjacent pairs: `10|01` = 1001 = 9.

- Example 2:
  - Input: `x = 13` (binary: `1101`)
  - Output: `14` (binary: `1110`)
  - Explanation: Blocks: `11|01`. Swap: `01|11` = 0111 = 7. Wait, let me reconsider: 13 = 00001101. Groups of 2: ...00|00|11|01. Swap adjacent pairs: ...00|00|01|11 = 0111 = 7. Actually, we swap (00,00), (11,01) → (00,00), (01,11). Result: 00000111 = 7.

- Example 3:
  - Input: `x = 0`
  - Output: `0`
  - Explanation: All zeros remain zeros after any swap.

## Constraints

- `0 <= x <= 10^9`
- Assume unsigned 32-bit operations

## Function Signatures

### Java
```java
class Solution {
    public int swapAdjacent2BitBlocks(int x) {
        // Implementation here
    }
}
```

### Python
```python
def swap_adjacent_2bit_blocks(x: int) -> int:
    """
    Solve the problem.

    Args:
        x: Input integer (32-bit unsigned)
    
    Returns:
        Result after swapping adjacent 2-bit blocks
    """
    pass
```

### C++
```cpp
class Solution {
public:
    unsigned int swapAdjacent2BitBlocks(unsigned int x) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single line: Integer `x`

### Sample Input
```
6
```

## Hints

Create masks for 2-bit blocks at even positions (0,4,8...) and odd positions (2,6,10...). Use `0x33333333` and `0xCCCCCCCC` patterns, shift appropriately.

## Quiz

### Question 1
What mask extracts bits at positions 0-1, 4-5, 8-9, etc.?

A) 0x55555555  
B) 0x33333333  
C) 0x0F0F0F0F  
D) 0xAAAAAAAA

**Correct Answer:** B

**Explanation:** 0x33333333 = 0011 0011 0011... in binary, which masks 2-bit blocks at positions (0-1), (4-5), (8-9), etc.

### Question 2
What mask extracts bits at positions 2-3, 6-7, 10-11, etc.?

A) 0x55555555  
B) 0x33333333  
C) 0xCCCCCCCC  
D) 0xF0F0F0F0

**Correct Answer:** C

**Explanation:** 0xCCCCCCCC = 1100 1100 1100... in binary, which masks 2-bit blocks at positions (2-3), (6-7), etc.

### Question 3
To swap adjacent 2-bit blocks, what shifts are needed?

A) Shift one group left by 2, other right by 2  
B) Shift one group left by 1, other right by 1  
C) Shift both left  
D) No shifting needed

**Correct Answer:** A

**Explanation:** We shift the lower 2-bit blocks (from positions 0-1,4-5,...) left by 2, and upper blocks (2-3,6-7,...) right by 2, then OR.

### Question 4
Is this operation its own inverse?

A) Yes, applying it twice returns the original  
B) No, it's not reversible  
C) Only for even numbers  
D) Only for powers of 2

**Correct Answer:** A

**Explanation:** Swapping adjacent blocks twice returns to original: (A,B) → (B,A) → (A,B).
