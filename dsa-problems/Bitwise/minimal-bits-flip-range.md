---
unique_problem_id: bitwise_006
display_id: BITWISE-006
slug: minimal-bits-flip-range
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - XOR
  - Bit Manipulation
  - Math
---

# Minimal Bits to Flip Range

## Problem Description

Find the smallest `m` such that flipping the lowest `m` bits of `x` transforms it into `y`. In other words, `x XOR y` should have all 1s only in the lower `m` bit positions. If impossible, return -1.

## Examples

- Example 1:
  - Input: `x = 10` (binary: `1010`), `y = 5` (binary: `0101`)
  - Output: `4`
  - Explanation: `x ⊕ y = 10 ⊕ 5 = 15 = 1111`. All 1s are contiguous from bit 0. Flipping lowest 4 bits of 10 gives 5.

- Example 2:
  - Input: `x = 12` (binary: `1100`), `y = 8` (binary: `1000`)
  - Output: `-1`
  - Explanation: `x ⊕ y = 12 ⊕ 8 = 4 = 0100`. Bit 2 is set but bits 0,1 are not. Not a contiguous range from bit 0.

- Example 3:
  - Input: `x = 7` (binary: `111`), `y = 0` (binary: `000`)
  - Output: `3`
  - Explanation: `x ⊕ y = 7 = 111`. Flip lowest 3 bits of 7 to get 0.

## Constraints

- `0 <= x, y <= 10^12`

## Function Signatures

### Java
```java
class Solution {
    public int minimalBitsFlipRange(long x, long y) {
        // Implementation here
    }
}
```

### Python
```python
def minimal_bits_flip_range(x: int, y: int) -> int:
    """
    Find minimum m such that flipping lowest m bits of x gives y.
    
    Args:
        x: Source number
        y: Target number
    
    Returns:
        Minimum m, or -1 if impossible
    """
    pass
```

### C++
```cpp
class Solution {
public:
    int minimalBitsFlipRange(long long x, long long y) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single line: Two integers `x` and `y`

### Sample Input
```
10 5
```

## Hints

Compute `diff = x XOR y`. Check if `diff` equals `2^m - 1` for some m (i.e., all 1s in lower m bits, no 1s above). Use `diff & (diff + 1) == 0`.

## Quiz

### Question 1
How do we check if a number has all 1s in its lowest m bits and 0s elsewhere?

A) n & (n + 1) == 0  
B) n & (n - 1) == 0  
C) n | (n + 1) == 0  
D) n ^ (n + 1) == 0

**Correct Answer:** A

**Explanation:** If n = 2^m - 1 (all 1s in lowest m bits), then n + 1 = 2^m (single 1 at position m). Their AND is 0.

### Question 2
What is the result when x equals y?

A) -1  
B) 0  
C) 1  
D) Undefined

**Correct Answer:** B

**Explanation:** x ⊕ y = 0, which equals 2^0 - 1 = 0. So m = 0 (flip zero bits).

### Question 3
Why can't diff = 4 (binary 100) be achieved by flipping lowest m bits?

A) 4 is too small  
B) 4 is not a power of 2  
C) Flipping lowest m bits gives 2^m - 1, not a single 1 bit  
D) The XOR is wrong

**Correct Answer:** C

**Explanation:** Flipping m bits converts to a pattern like 111...1 (2^m - 1), not 100. So diff = 4 is impossible.

### Question 4
For x = 0, y = 7, what is m?

A) 0  
B) 3  
C) 7  
D) -1

**Correct Answer:** B

**Explanation:** diff = 0 ⊕ 7 = 7 = 111 (binary) = 2^3 - 1. So m = 3.
