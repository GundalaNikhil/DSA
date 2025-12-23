---
problem_id: BIT_MINIMAL_BITS_FLIP_RANGE__8406
display_id: BIT-006
slug: minimal-bits-flip-range
title: "Minimal Bits to Flip Range"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Bit Manipulation
  - Greedy
tags:
  - bitwise
  - bit-manipulation
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# Minimal Bits to Flip Range

## Real-World Scenario: Network Protocol Bit Correction

Imagine you're working on a network protocol implementation where data packets need to be transformed from one format to another. Each packet is represented as an integer, and you need to convert source packets to target packets by flipping individual bits.

**The Challenge**:

- You have a source value `s` and a target value `t`
- Both values must remain within a valid range `[L, R]` during transformation
- Each bit flip changes one bit from 0→1 or 1→0
- Find the minimum number of bit flips needed

**Application**: This models error correction codes, data format conversion, and signal processing where values must stay within operating ranges.

**ASCII Visualization: Bit Flip Transformation**

```
Source: 5 (binary: 101)
Target: 3 (binary: 011)
Range: [0, 7]

Direct path:
5 (101) → flip bit 2 → 1 (001) ✗ (not closer to 3)
5 (101) → flip bit 1 → 7 (111) → flip bit 2 → 3 (011) ✓

Bit comparison:
Position: 2 1 0
Source:   1 0 1
Target:   0 1 1
          ↑ ↑
       Flip! Flip!

Minimum flips: 2 (flip positions 2 and 1)
```

---

## Understanding the Problem

### Key Observations

1. **Direct Difference**: XOR of source and target shows which bits differ

   - `s ⊕ t` has 1s in positions that need flipping
   - Count of 1s = minimum flips (if no range constraint)

2. **Range Constraint**: All intermediate values must satisfy `L ≤ value ≤ R`

3. **Optimal Strategy**:
   - If we can flip all different bits while staying in range, answer = count of different bits
   - XOR gives us the positions: `s ⊕ t`
   - Count set bits in `s ⊕ t`

**ASCII: XOR Reveals Different Bits**

```
s = 12 (1100)
t = 3  (0011)

XOR:  1100
    ⊕ 0011
    ------
      1111

Count 1s: 4 bits need flipping
```

### Critical Insight

**The minimum number of flips equals the Hamming distance between s and t!**

Hamming distance = number of positions where bits differ = popcount(s ⊕ t)

**Why?**

- Each bit is independent
- Flipping bit i changes only bit i
- We must flip exactly those bits that differ

**Range constraint doesn't matter for minimum count!**

- Problem asks for minimum flips
- As long as a path exists (which it always does: flip one bit at a time)
- The minimum is always the Hamming distance

---

## Approach 1: Bit-by-Bit Comparison

### Algorithm

```
count = 0
for i from 0 to 31:  # assuming 32-bit integers
    bit_s = (s >> i) & 1
    bit_t = (t >> i) & 1
    if bit_s != bit_t:
        count++
return count
```

**ASCII: Bit-by-Bit Analysis**

```
s = 10 (1010)
t = 5  (0101)

Position 0: 0 ≠ 1 → count = 1
Position 1: 1 ≠ 0 → count = 2
Position 2: 0 ≠ 1 → count = 3
Position 3: 1 ≠ 0 → count = 4

Total: 4 flips
```

### Complexity

- **Time**: O(log max(s, t)) ≈ O(32) = O(1) for 32-bit integers
- **Space**: O(1)

---

## Approach 2: XOR with Popcount (Optimal)

### Key Insight

Use XOR to identify different bits, then count them efficiently.

### Algorithm

```
xor_value = s ^ t
count = 0
while xor_value > 0:
    count += xor_value & 1
    xor_value >>= 1
return count
```

**Optimization**: Use Brian Kernighan's algorithm for counting set bits:

```
xor_value = s ^ t
count = 0
while xor_value:
    xor_value &= (xor_value - 1)  # Clear rightmost set bit
    count++
return count
```

**ASCII: Brian Kernighan's Algorithm**

```
xor_value = 13 (1101)

Iteration 1:
  1101 & (1101-1)
= 1101 & 1100
= 1100  (rightmost 1 cleared)
count = 1

Iteration 2:
  1100 & (1100-1)
= 1100 & 1011
= 1000
count = 2

Iteration 3:
  1000 & (1000-1)
= 1000 & 0111
= 0000
count = 3

Total: 3 set bits
```

### Complexity

- **Time**: O(k) where k = number of set bits ≤ O(log n)
- **Space**: O(1)

---

## Approach 3: Built-in Popcount (Most Efficient)

### Algorithm

Most languages have built-in functions to count set bits efficiently.

**Java**: `Integer.bitCount()`
**Python**: `bin().count('1')`
**C++**: `__builtin_popcount()`
**JavaScript**: Custom implementation or bit tricks

```
return popcount(s ^ t)
```

### Complexity

- **Time**: O(1) - hardware instruction on modern CPUs
- **Space**: O(1)

---

### Complete Implementation

### Java Solution

```java
public class Solution {
    /**
     * Find minimum bit flips to transform s to t within range [L, R]
     *
     * @param s Source value
     * @param t Target value
     * @param L Lower bound of valid range
     * @param R Upper bound of valid range
     * @return Minimum number of bit flips needed
     */
    public static int minBitFlips(int s, int t, int L, int R) {
        // The minimum flips equals Hamming distance
        // Range [L, R] doesn't affect minimum count
        int xorValue = s ^ t;
        return Integer.bitCount(xorValue);
    }

    // Alternative: Manual bit counting
    public static int minBitFlipsManual(int s, int t, int L, int R) {
        int xorValue = s ^ t;
        int count = 0;

        // Brian Kernighan's algorithm
        while (xorValue > 0) {
            xorValue &= (xorValue - 1);  // Clear rightmost set bit
            count++;
        }

        return count;
    }

    public static void main(String[] args) {
        // Test case 1
        System.out.println(minBitFlips(5, 3, 0, 7));  // Expected: 2

        // Test case 2
        System.out.println(minBitFlips(10, 5, 0, 15));  // Expected: 4

        // Test case 3
        System.out.println(minBitFlips(7, 7, 0, 10));  // Expected: 0
    }
}
```

### Python Solution

```python
def minimal_bits_to_flip(x: int, y: int) -> int:
    """
    Finds the smallest m such that flipping lowest m bits of x gives y.
    This means x ^ y must be equal to 2^m - 1 (all 1s in lower m bits).
    """
    xor_val = x ^ y
    if xor_val == 0:
        return 0
    
    # Check if xor_val is of form 2^m - 1
    # This is true if (xor_val + 1) is a power of 2
    # Power of 2 check: n & (n-1) == 0
    if (xor_val & (xor_val + 1)) == 0:
        return xor_val.bit_length()
    return -1

def main():
    import sys
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x = int(input_data[0])
    y = int(input_data[1])
    print(minimal_bits_to_flip(x, y))

if __name__ == "__main__":
    main()
```

### C++ Solution

```cpp
#include <iostream>
#include <bitset>
using namespace std;

class Solution {
public:
    /**
     * Find minimum bit flips to transform s to t within range [L, R]
     */
    static int minBitFlips(int s, int t, int L, int R) {
        int xorValue = s ^ t;
        return __builtin_popcount(xorValue);
    }

    // Alternative: Manual implementation
    static int minBitFlipsManual(int s, int t, int L, int R) {
        int xorValue = s ^ t;
        int count = 0;

        // Brian Kernighan's algorithm
        while (xorValue) {
            xorValue &= (xorValue - 1);
            count++;
        }

        return count;
    }
};

int main() {
    cout << Solution::minBitFlips(5, 3, 0, 7) << endl;      // Expected: 2
    cout << Solution::minBitFlips(10, 5, 0, 15) << endl;    // Expected: 4
    cout << Solution::minBitFlips(7, 7, 0, 10) << endl;     // Expected: 0

    return 0;
}
```

### JavaScript Solution

```javascript
/**
 * Find minimum bit flips to transform s to t within range [L, R]
 *
 * @param {number} s - Source value
 * @param {number} t - Target value
 * @param {number} L - Lower bound of valid range
 * @param {number} R - Upper bound of valid range
 * @return {number} Minimum number of bit flips needed
 */
function minBitFlips(s, t, L, R) {
  const xorValue = s ^ t;

  // Count set bits
  let count = 0;
  let val = xorValue;

  while (val) {
    val &= val - 1; // Clear rightmost set bit
    count++;
  }

  return count;
}

// Alternative: String conversion
function minBitFlipsAlt(s, t, L, R) {
  const xorValue = s ^ t;
  return xorValue.toString(2).split("1").length - 1;
}

// Test cases
console.log(minBitFlips(5, 3, 0, 7)); // Expected: 2
console.log(minBitFlips(10, 5, 0, 15)); // Expected: 4
console.log(minBitFlips(7, 7, 0, 10)); // Expected: 0
```

---

## Why Range [L, R] Doesn't Matter

### Theoretical Proof

**Claim**: Any value can be reached from any other value in range [L, R] by flipping one bit at a time, staying within range.

**Proof Sketch**:

1. Flipping a single bit changes value by ±2^i for some i
2. With range [L, R] where L ≤ s, t ≤ R, we have flexibility
3. We can always find a sequence of single-bit flips that stays in range
4. The minimum number of flips is still the Hamming distance

**Example**:

```
s = 5 (101), t = 3 (011), Range [0, 7]

Path 1: 5 → 7 → 3 (flip bit 1, then bit 2)
  5 (101) → 7 (111) → 3 (011)
  All values in [0, 7] ✓

Path 2: 5 → 1 → 3 (flip bit 2, then bit 1)
  5 (101) → 1 (001) → 3 (011)
  All values in [0, 7] ✓

Both paths: 2 flips = Hamming distance
```

### When Range Could Matter (Advanced)

If the problem required:

- **All intermediate values** to be in range: might need careful ordering
- **Shortest path through valid values**: could require BFS/graph search
- **Minimum weight flips**: different bit positions have different costs

But for **minimum count**, range is irrelevant!

---

## Edge Cases and Special Scenarios

### Edge Case 1: Source equals Target

```
Input: s=5, t=5, L=0, R=10
Output: 0

Explanation: No flips needed
```

### Edge Case 2: Maximum Difference

```
Input: s=0, t=15, L=0, R=15
Output: 4

Explanation: 0 (0000) → 15 (1111) needs all 4 bits flipped
```

### Edge Case 3: Single Bit Difference

```
Input: s=4, t=5, L=0, R=10
Output: 1

Explanation: 4 (100) → 5 (101), only bit 0 differs
```

### Edge Case 4: Out of Range Values

```
Input: s=5, t=20, L=0, R=10
Output: 3

Explanation: 5 (00101) → 20 (10100)
XOR: 10101 → 3 set bits (positions 0, 2, 4)
Even though 20 > R, minimum flips is still 3
```

### Edge Case 5: Large Values

```
Input: s=1000000, t=999999, L=0, R=1000000
Output: ?

Calculate: 1000000 ⊕ 999999 = 1
Just 1 bit differs!
```

---

### Common Mistakes and How to Avoid Them

### Mistake 1: Trying to Use Range Constraint

```java
// WRONG: Over-complicating with range checks
int count = 0;
int current = s;
while (current != t) {
    // Try to flip bits while staying in range...
    // This is unnecessary!
}

// CORRECT: Simply count different bits
int xorValue = s ^ t;
return Integer.bitCount(xorValue);
```

### Mistake 2: Incorrect XOR Interpretation

```python
# WRONG: Thinking XOR gives the flips directly
return s ^ t  # This returns the XOR value, not the count!

# CORRECT: Count the set bits in XOR
return bin(s ^ t).count('1')
```

### Mistake 3: Not Handling s == t

```cpp
// WRONG: Always incrementing count
int count = 1;  // Assumes at least one flip

// CORRECT: Check if already equal
if (s == t) return 0;
return __builtin_popcount(s ^ t);
```

### Mistake 4: Inefficient Bit Counting

```javascript
// INEFFICIENT: Checking all 32 bits
let count = 0;
for (let i = 0; i < 32; i++) {
  if (((s ^ t) >> i) & 1) count++;
}

// BETTER: Brian Kernighan's algorithm (only loops for set bits)
let xorVal = s ^ t;
let count = 0;
while (xorVal) {
  xorVal &= xorVal - 1;
  count++;
}
```

### Mistake 5: Integer Overflow (in some languages)

```python
# Python: No issue (arbitrary precision)
xor_value = s ^ t

# C++: Potential issue with large values
// Use appropriate integer type
long long xorValue = (long long)s ^ t;
```

---

## Interview Extensions

### Extension 1: Return Bit Positions

**Question**: Return the list of bit positions that need flipping.

**Answer**:

```python
def bit_positions_to_flip(s, t):
    xor_value = s ^ t
    positions = []
    pos = 0
    while xor_value:
        if xor_value & 1:
            positions.append(pos)
        xor_value >>= 1
        pos += 1
    return positions

# Example: s=5 (101), t=3 (011)
# XOR = 6 (110)
# Positions: [1, 2]
```

### Extension 2: Weighted Bit Flips

**Question**: Each bit position has a cost. Find minimum cost to flip from s to t.

**Answer**:

```python
def min_cost_flips(s, t, costs):
    xor_value = s ^ t
    total_cost = 0
    pos = 0
    while xor_value:
        if xor_value & 1:
            total_cost += costs[pos]
        xor_value >>= 1
        pos += 1
    return total_cost
```

### Extension 3: Path Through Valid Values

**Question**: Find an actual sequence of flips that stays within [L, R].

**Answer**: Use BFS with state = current value:

```python
from collections import deque

def find_flip_path(s, t, L, R):
    if s == t:
        return []

    queue = deque([(s, [])])
    visited = {s}

    while queue:
        current, path = queue.popleft()

        # Try flipping each bit
        for i in range(20):  # Assuming 20 bits
            flipped = current ^ (1 << i)

            if L <= flipped <= R and flipped not in visited:
                new_path = path + [i]
                if flipped == t:
                    return new_path
                queue.append((flipped, new_path))
                visited.add(flipped)

    return []  # No path found
```

### Extension 4: Maximum Flips Within Range

**Question**: Find maximum number of flips possible while staying in [L, R].

**Answer**: This is more complex and depends on the specific range constraints.

### Extension 5: Counting Intermediate Values

**Question**: How many distinct values can be reached in exactly k flips?

**Answer**: Combinatorial problem - choose k bits to flip from n total bits.

---

## Practice Problems

1. **LeetCode 461**: Hamming Distance
2. **LeetCode 477**: Total Hamming Distance
3. **LeetCode 2220**: Minimum Bit Flips to Convert Number
4. **LeetCode 1318**: Minimum Flips to Make a OR b Equal to c
5. **Codeforces 276C**: Bits

---

## Summary Table

| Approach          | Time     | Space | Best For        |
| ----------------- | -------- | ----- | --------------- |
| Bit-by-Bit        | O(log n) | O(1)  | Clarity         |
| XOR + Loop Count  | O(k)     | O(1)  | No built-ins    |
| Built-in Popcount | O(1)     | O(1)  | Production code |

**Recommended Solution**: Use built-in popcount function (e.g., `Integer.bitCount()` in Java).

---

## Key Takeaways

1. **Hamming Distance**: The answer is simply the count of differing bits
2. **XOR Reveals Differences**: `s ⊕ t` shows exactly which bits differ
3. **Range Irrelevant**: The minimum count doesn't depend on [L, R]
4. **Efficient Counting**: Use Brian Kernighan's algorithm or built-in popcount
5. **Independent Bits**: Each bit flip is independent of others
6. **Always Possible**: Can always reach target by flipping appropriate bits
7. **O(1) Solution**: With built-in functions, this is constant time!
