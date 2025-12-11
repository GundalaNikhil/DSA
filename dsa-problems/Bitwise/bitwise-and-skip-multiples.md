---
unique_problem_id: bitwise_003
display_id: BITWISE-003
slug: bitwise-and-skip-multiples
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - AND Operation
  - Range Queries
  - Number Theory
  - Bit Manipulation
---

# Bitwise AND Skipping Multiples

## Problem Description

Given integers `L`, `R`, and `m`, compute the bitwise AND of all numbers in the range `[L, R]` that are NOT divisible by `m`. If no such numbers exist, return `-1`.

## Examples

- Example 1:
  - Input: `L = 10`, `R = 15`, `m = 3`
  - Output: `8`
  - Explanation: Numbers in [10,15]: 10,11,12,13,14,15. Exclude multiples of 3: 12,15. Remaining: 10,11,13,14. AND: `10 & 11 & 13 & 14 = 1010 & 1011 & 1101 & 1110 = 1000 = 8`.

- Example 2:
  - Input: `L = 6`, `R = 6`, `m = 2`
  - Output: `-1`
  - Explanation: Only number is 6, which is divisible by 2. No valid numbers remain.

- Example 3:
  - Input: `L = 1`, `R = 7`, `m = 10`
  - Output: `0`
  - Explanation: No multiples of 10 in range. AND all: `1 & 2 & 3 & 4 & 5 & 6 & 7 = 0` (different bit patterns cancel out).

## Constraints

- `0 <= L <= R <= 10^12`
- `1 <= m <= 10^6`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public long bitwiseAndSkipMultiples(long L, long R, int m) {

        // Implementation here
        return 0;
    }
}
```

### Python
```python
def bitwise_and_skip_multiples(L: int, R: int, m: int) -> int:
    """
    Compute AND of numbers in [L,R] not divisible by m.
    
    Args:
        L: Left bound of range (inclusive)
        R: Right bound of range (inclusive)
        m: Divisor to exclude multiples of
    
    Returns:
        Bitwise AND of valid numbers, or -1 if none exist
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    long long bitwiseAndSkipMultiples(long long L, long long R, int m) {
        // Implementation here
        return 0;
    }
};
```

## Input Format

The input will be provided as:
- Single line: Three integers `L`, `R`, and `m`

### Sample Input
```
10 15 3
```

## Hints

If a contiguous span of allowed numbers crosses a power-of-2 boundary, AND becomes 0. Identify and check these spans carefully.

## Quiz

### Question 1
What happens when we AND two consecutive integers like n and n+1?

A) Result is always n  
B) Result is always n+1  
C) Result loses the lowest differing bit and below  
D) Result is always 0

**Correct Answer:** C

**Explanation:** Consecutive numbers differ in their lowest bit(s). ANDing them clears all bits from the lowest differing position downward.

### Question 2
When does the AND of a range [a, b] equal 0?

A) When b - a >= 2  
B) When the range crosses a power of 2 boundary  
C) When a is odd  
D) When b is even

**Correct Answer:** B

**Explanation:** If the range includes numbers like 2^k - 1 and 2^k, their AND is 0 (highest bit differs), making the total AND 0.

### Question 3
Why do we need to handle the m=1 case specially?

A) Division by 1 is undefined  
B) All numbers are multiples of 1, so result is always -1  
C) m=1 causes overflow  
D) m=1 makes the problem trivial

**Correct Answer:** B

**Explanation:** Every integer is divisible by 1, so excluding multiples of 1 leaves no valid numbers, returning -1.

### Question 4
What is the time complexity concern for large ranges?

A) Memory overflow  
B) Iterating through all numbers is O(R-L) which can be 10^12  
C) Recursion depth  
D) There is no concern

**Correct Answer:** B

**Explanation:** Naively iterating is infeasible. We must use properties of AND (result stabilizes quickly) or identify contiguous valid spans.
