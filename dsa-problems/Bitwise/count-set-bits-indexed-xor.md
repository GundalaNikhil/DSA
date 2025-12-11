---
unique_problem_id: bitwise_007
display_id: BITWISE-007
slug: count-set-bits-indexed-xor
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - XOR
  - Bit Counting
  - Popcount
---

# Count Set Bits Of Indexed XOR

## Problem Description

Compute the total number of set bits (1s) in the sequence `b[i] = i XOR a[i]` for `i` from `0` to `n-1`.

## Examples

- Example 1:
  - Input: `a = [0, 2]`
  - Output: `2`
  - Explanation: `b[0] = 0 ⊕ 0 = 0` (0 bits), `b[1] = 1 ⊕ 2 = 3` (2 bits). Total = 0 + 2 = 2.

- Example 2:
  - Input: `a = [1, 1, 1, 1]`
  - Output: `4`
  - Explanation: `b = [0⊕1, 1⊕1, 2⊕1, 3⊕1] = [1, 0, 3, 2]`. Popcounts: 1 + 0 + 2 + 1 = 4.

- Example 3:
  - Input: `a = [7, 7, 7]`
  - Output: `6`
  - Explanation: `b = [0⊕7, 1⊕7, 2⊕7] = [7, 6, 5] = [111, 110, 101]`. Popcounts: 3 + 2 + 1 = 6.

## Constraints

- `1 <= n <= 200,000`
- `0 <= a[i] <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public long countSetBitsIndexedXor(int[] a) {
        // Implementation here
        return 0;
    }
}
```

### Python
```python
from typing import List

def count_set_bits_indexed_xor(a: List[int]) -> int:
    """
    Count total set bits in i XOR a[i] for all i.
    
    Args:
        a: Input array
    
    Returns:
        Total count of set bits across all b[i] = i XOR a[i]
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    long long countSetBitsIndexedXor(const vector<int>& a) {
        // Implementation here
        return 0;
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer `n` (array size)
- Second line: `n` space-separated integers representing the array

### Sample Input
```
2
0 2
```

## Hints

Process bits independently. For bit k, count how many indices have bit k set and how many array values have bit k set. XOR produces 1 when they differ.

## Quiz

### Question 1
For a specific bit position k, when does (i XOR a[i]) have bit k set?

A) When both i and a[i] have bit k set  
B) When neither i nor a[i] has bit k set  
C) When exactly one of i or a[i] has bit k set  
D) Always

**Correct Answer:** C

**Explanation:** XOR produces 1 when inputs differ. So bit k is set when i's bit k ≠ a[i]'s bit k.

### Question 2
How do we count set bits in indices 0 to n-1 at bit position k?

A) n / 2^k  
B) Count directly using formula for arithmetic sequences of bits  
C) Always n/2  
D) Cannot be computed without iteration

**Correct Answer:** B

**Explanation:** For bit k in range [0, n-1], the pattern repeats every 2^(k+1). We can compute the count using: full_cycles × 2^k + remainder.

### Question 3
What is the time complexity of the optimal solution?

A) O(n)  
B) O(n log n)  
C) O(n × 30) which is O(n)  
D) O(n²)

**Correct Answer:** C

**Explanation:** We process 30 bits, and for each count how many 1s are in array at that bit position O(n), giving O(30n).

### Question 4
If all a[i] = 0, what is the answer?

A) 0  
B) Sum of popcount(i) for i from 0 to n-1  
C) n  
D) n × 30

**Correct Answer:** B

**Explanation:** b[i] = i ⊕ 0 = i. So we sum popcount of all indices.
