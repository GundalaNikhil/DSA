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
---

# Bitwise AND Skipping Multiples - Editorial

![Problem Header](../images/BIT-003/header.png)

## Problem Summary

Compute bitwise AND of all numbers in range [L, R] that are NOT divisible by m. Return -1 if no valid numbers exist.

## Real-World Scenario

**Network Packet Filtering System**

A network router needs to apply a bitmask filter to valid packet IDs in a range, excluding maintenance channels (multiples of m). The AND operation identifies common bits across all valid packets for routing optimization.

## Approach

### Key Insights

1. **AND Property**: Bitwise AND is monotonically decreasing - adding more numbers never increases the result
2. **Power-of-2 Boundary**: If the range crosses a bit boundary, that bit becomes 0 in the result
3. **Contiguous Spans**: Identify contiguous blocks of non-multiples for efficient computation

### Algorithm

**Step 1**: Filter valid numbers (not divisible by m)
**Step 2**: Compute bitwise AND of all valid numbers
**Step 3**: Return -1 if no valid numbers exist

### Optimization

For large ranges (R - L > 10⁶), use bit-level analysis:

- Find the highest bit where L and R differ
- All lower bits will be 0 in the final AND result
- Early termination when result reaches 0

## Implementation

### Python

```python
def bitwise_and_skip_multiples(L: int, R: int, m: int) -> int:
    result = None

    for num in range(L, R + 1):
        if num % m != 0:
            if result is None:
                result = num
            else:
                result &= num
            # Early termination if result becomes 0
            if result == 0:
                return 0

    return -1 if result is None else result
```

### Java

```java
class Solution {
    public long bitwiseAndSkipMultiples(long L, long R, int m) {
        Long result = null;

        for (long num = L; num <= R; num++) {
            if (num % m != 0) {
                if (result == null) {
                    result = num;
                } else {
                    result &= num;
                }
                // Early termination
                if (result == 0) {
                    return 0;
                }
            }
        }

        return result == null ? -1 : result;
    }
}
```

### C++

```cpp
class Solution {
public:
    long long bitwiseAndSkipMultiples(long long L, long long R, int m) {
        long long result = -1;
        bool found = false;

        for (long long num = L; num <= R; num++) {
            if (num % m != 0) {
                if (!found) {
                    result = num;
                    found = true;
                } else {
                    result &= num;
                }
                // Early termination
                if (result == 0) {
                    return 0;
                }
            }
        }

        return found ? result : -1;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number} L
 * @param {number} R
 * @param {number} m
 * @return {number}
 */
var bitwiseAndSkipMultiples = function(L, R, m) {
    let result = -1;
    let found = false;

    for (let num = L; num <= R; num++) {
        if (num % m !== 0) {
            if (!found) {
                result = num;
                found = true;
            } else {
                result &= num;
            }
            // Early termination
            if (result === 0) {
                return 0;
            }
        }
    }

    return found ? result : -1;
};
```

### C++omplexity Analysis

**Time Complexity**: O(R - L)

- Iterate through range once
- Modulo operation is O(1)
- AND operation is O(1)

**Space Complexity**: O(1)

- Only storing result variable

## Edge Cases

1. **All multiples**: L=6, R=12, m=3 → All divisible → Return -1
2. **Single number**: L=R=5, m=3 → Return 5
3. **Large range**: Use optimization to avoid timeout
4. **m=1**: All numbers divisible → Return -1
5. **L=0**: Handle zero correctly (0 is divisible by any m)

### C++ommon Mistakes

1. **Not handling empty result**: Forget to return -1 when no valid numbers
2. **Integer overflow**: Use long/long long for large ranges
3. **Inefficient iteration**: Not using early termination when result becomes 0
4. **Incorrect modulo**: Forgetting that 0 % m = 0

## Related Problems

- Range Bitwise AND
- Count Multiples in Range
- Bitwise OR of Subarray
