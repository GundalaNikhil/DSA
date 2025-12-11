---
unique_problem_id: bitwise_009
display_id: BITWISE-009
slug: smallest-absent-xor
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - XOR
  - Linear Basis
  - MEX (Minimum Excludant)
---

# Smallest Absent XOR

## Problem Description

Given an array `a`, find the smallest non-negative integer `x` such that no pair `(i, j)` with `i <= j` has `a[i] XOR a[j] == x`.

## Examples

- Example 1:
  - Input: `a = [1, 2, 3]`
  - Output: `4`
  - Explanation: Possible XORs: 1⊕1=0, 1⊕2=3, 1⊕3=2, 2⊕2=0, 2⊕3=1, 3⊕3=0. Set: {0,1,2,3}. Smallest missing = 4.

- Example 2:
  - Input: `a = [0]`
  - Output: `1`
  - Explanation: Only XOR is 0⊕0=0. Missing integers: 1,2,3,... Smallest = 1.

- Example 3:
  - Input: `a = [5, 7]`
  - Output: `1`
  - Explanation: XORs: 5⊕5=0, 5⊕7=2, 7⊕7=0. Set: {0, 2}. Smallest missing = 1.

## Constraints

- `1 <= n <= 200,000`
- `0 <= a[i] <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int smallestAbsentXor(int[] a) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def smallest_absent_xor(a: List[int]) -> int:
    """
    Find smallest integer not expressible as XOR of any pair.
    
    Args:
        a: Input array
    
    Returns:
        Smallest non-negative integer not achievable as a[i] XOR a[j]
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int smallestAbsentXor(const vector<int>& a) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer `n` (array size)
- Second line: `n` space-separated integers representing the array

### Sample Input
```
3
1 2 3
```

## Hints

Build XOR linear basis. The set of reachable XORs forms a vector space of size up to 2^(basis_size). Find the MEX of this space.

## Quiz

### Question 1
What is a XOR linear basis?

A) A sorting algorithm  
B) A set of vectors such that any reachable XOR can be expressed as XOR of subset  
C) The largest XOR value  
D) The average XOR value

**Correct Answer:** B

**Explanation:** A linear basis for XOR is a minimal set of values that can generate all possible XOR combinations through subset XOR.

### Question 2
If the basis has k independent vectors, how many distinct XOR values are reachable?

A) k  
B) 2k  
C) 2^k  
D) k!

**Correct Answer:** C

**Explanation:** Each subset of k basis vectors produces a unique XOR, giving 2^k total reachable values.

### Question 3
Why is 0 always reachable?

A) 0 is in every array  
B) We can XOR any element with itself: a[i] ⊕ a[i] = 0  
C) 0 is the identity  
D) The empty XOR is 0

**Correct Answer:** B

**Explanation:** Any element XORed with itself gives 0, so 0 is always in the reachable set.

### Question 4
For array [1], what is the smallest absent XOR?

A) 0  
B) 1  
C) 2  
D) -1

**Correct Answer:** C

**Explanation:** Pairs: (0,0) gives 1⊕1=0. Only XORs are {0}. But wait, also 1 is reachable? No, we need pairs. Only one element, so only 1⊕1=0. Reachable: {0}. Smallest absent: 1.
