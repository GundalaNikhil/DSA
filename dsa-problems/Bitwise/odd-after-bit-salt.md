---
unique_problem_id: bitwise_001
display_id: BITWISE-001
slug: odd-after-bit-salt
version: 1.0.0
difficulty: Easy
topic_tags:
  - Bitwise
  - XOR
  - Bit Manipulation
  - Array Processing
---

# Odd After Bit Salt

## Problem Description

Each array element `x` is first transformed to `x' = x XOR salt`, where `salt` is a given constant applied to all elements. In the transformed multiset, exactly one value appears an odd number of times, while others appear an even number of times. Find that odd-occurring transformed value without explicitly building the transformed array.

## Examples

- Example 1:
  - Input: `arr = [4, 1, 2, 1, 2, 4, 7]`, `salt = 3`
  - Output: `4`
  - Explanation: Transform each element: `[4^3, 1^3, 2^3, 1^3, 2^3, 4^3, 7^3] = [7, 2, 1, 2, 1, 7, 4]`. XOR all transformed values: `7^2^1^2^1^7^4 = 4`. Since XOR cancels pairs, only the odd-occurring value (4) remains.

- Example 2:
  - Input: `arr = [5, 5, 5]`, `salt = 0`
  - Output: `5`
  - Explanation: No transformation (salt=0). 5 appears 3 times (odd). XOR: `5^5^5 = 5`.

- Example 3:
  - Input: `arr = [10, 20, 10]`, `salt = 15`
  - Output: `27`
  - Explanation: Transformed: `[10^15, 20^15, 10^15] = [5, 27, 5]`. XOR: `5^27^5 = 27`.

## Constraints

- `1 <= n <= 200,000` (array size)
- `-10^9 <= arr[i] <= 10^9`
- `-10^9 <= salt <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int oddAfterBitSalt(int[] arr, int salt) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def odd_after_bit_salt(arr: List[int], salt: int) -> int:
    """
    Find the element that appears odd number of times after XOR with salt.
    
    Args:
        arr: Input array of integers
        salt: XOR salt value to apply to each element
    
    Returns:
        The transformed value appearing an odd number of times
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int oddAfterBitSalt(const vector<int>& arr, int salt) {
      //Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Two integers `n` (array size) and `salt`
- Second line: `n` space-separated integers representing the array

### Sample Input
```
7 3
4 1 2 1 2 4 7
```

## Hints

XOR is associative and self-inverse. XOR of all transformed elements directly gives the odd-occurring value without building the array.

## Quiz

### Question 1
What property of XOR makes this problem efficiently solvable?

A) XOR is commutative only  
B) XOR of a number with itself is 0 (self-inverse)  
C) XOR always increases the value  
D) XOR distributes over addition

**Correct Answer:** B

**Explanation:** `a XOR a = 0` means paired elements cancel out, leaving only the odd-occurring element.

### Question 2
What is the time complexity of the optimal solution?

A) O(1)  
B) O(n)  
C) O(n log n)  
D) O(n²)

**Correct Answer:** B

**Explanation:** We traverse the array once, XORing each element with salt and accumulating the result.

### Question 3
Can we solve this without knowing the salt value?

A) Yes, always  
B) No, salt is essential for the transformation  
C) Only if salt is 0  
D) Only if all elements are positive

**Correct Answer:** B

**Explanation:** The salt transforms each value before counting occurrences, so we must know it to compute the transformed odd-occurring value.

### Question 4
If the array has multiple elements appearing an odd number of times, what happens?

A) The algorithm returns their sum  
B) The algorithm returns their XOR  
C) The algorithm fails  
D) The algorithm returns the smallest

**Correct Answer:** B

**Explanation:** XOR of all elements returns the XOR of all odd-occurring elements, not just one. The problem guarantees exactly one such element.
