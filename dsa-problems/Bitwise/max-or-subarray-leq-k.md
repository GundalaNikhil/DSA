---
unique_problem_id: bitwise_016
display_id: BITWISE-016
slug: max-or-subarray-leq-k
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - OR Operation
  - Sliding Window
  - Two Pointers
  - Bit Counting
---

# Max Bitwise OR Subarray <= K

## Problem Description

Find the maximum length of a contiguous subarray whose bitwise OR is less than or equal to `K`.

## Examples

- Example 1:
  - Input: `a = [1, 2, 4, 1]`, `K = 7`
  - Output: `4`
  - Explanation: OR of entire array = 1|2|4|1 = 7 ≤ 7. Length = 4.

- Example 2:
  - Input: `a = [1, 2, 8]`, `K = 3`
  - Output: `2`
  - Explanation: Subarrays: [1]=1≤3, [2]=2≤3, [8]=8>3, [1,2]=3≤3, [2,8]=10>3, [1,2,8]=11>3. Max length with OR≤3 is 2 ([1,2]).

- Example 3:
  - Input: `a = [15, 15, 15]`, `K = 10`
  - Output: `0`
  - Explanation: Every element is 15 > 10. No valid subarray exists.

## Constraints

- `1 <= n <= 200,000`
- `0 <= a[i], K <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int maxOrSubarrayLeqK(int[] a, int K) {
        // Implementation here
        return 0;
    }
}
```

### Python
```python
from typing import List

def max_or_subarray_leq_k(a: List[int], K: int) -> int:
    """
    Find maximum length subarray with OR <= K.
    
    Args:
        a: Input array
        K: Maximum allowed OR value
    
    Returns:
        Maximum length of valid subarray, or 0 if none exists
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maxOrSubarrayLeqK(const vector<int>& a, int K) {
        // Implementation here
        
    }
};
```

## Input Format

The input will be provided as:
- First line: Two integers `n` (array size) and `K` (max OR value)
- Second line: `n` space-separated integers representing the array

### Sample Input
```
4 7
1 2 4 1
```

## Hints

Use sliding window. Maintain count of each bit position in current window. OR exceeds K when any bit not in K is set; shrink window from left to remove that bit.

## Quiz

### Question 1
How does OR behave in a sliding window as we add elements?

A) OR can decrease  
B) OR can only increase or stay the same  
C) OR oscillates  
D) OR is unpredictable

**Correct Answer:** B

**Explanation:** OR only sets bits; adding an element can only add more 1 bits, never remove them.

### Question 2
Why do we need bit counting instead of just tracking the OR value?

A) To save memory  
B) To know when removing an element will change a bit in the OR  
C) To compute XOR  
D) Bit counting is not needed

**Correct Answer:** B

**Explanation:** When shrinking the window, we need to know if a bit can be cleared (count becomes 0). Just tracking OR doesn't tell us this.

### Question 3
What is the time complexity with bit counting approach?

A) O(n)  
B) O(n × 30)  
C) O(n²)  
D) O(n log n)

**Correct Answer:** B

**Explanation:** Each element is added/removed once, and each operation touches 30 bits. Total: O(30n) = O(n).

### Question 4
If K = 0, what is the maximum valid subarray length?

A) Always 0  
B) Count of 0s in the longest consecutive 0 sequence  
C) n (entire array)  
D) 1 if any 0 exists

**Correct Answer:** B

**Explanation:** OR ≤ 0 means OR must be exactly 0, which requires all elements in subarray to be 0. Find longest run of 0s.
