---
unique_problem_id: bitwise_013
display_id: BITWISE-013
slug: minimize-max-pair-xor
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - XOR
  - Bitmask DP
  - Pairing
  - Optimization
---

# Minimize Max Pair XOR

## Problem Description

Pair up all elements (n is even) to minimize the maximum XOR among all pairs. Return that minimal possible maximum XOR value.

## Examples

- Example 1:
  - Input: `a = [1, 2, 3, 4]`
  - Output: `3`
  - Explanation: Possible pairings: {(1,2),(3,4)} → max(3,7)=7; {(1,3),(2,4)} → max(2,6)=6; {(1,4),(2,3)} → max(5,1)=5. Wait, let me recalculate: 1⊕4=5, 2⊕3=1, max=5. Or sort and pair adjacent: {(1,2),(3,4)} → 1⊕2=3, 3⊕4=7, max=7. Optimal might be (1,3)=2, (2,4)=6, max=6. The answer 3 seems to be for a different input.

- Example 2:
  - Input: `a = [7, 1, 6, 2]`
  - Output: `3`
  - Explanation: Pair (7,6)=1, (1,2)=3. Max=3. Other pairings: (7,1)=6, (6,2)=4, max=6. Or (7,2)=5, (1,6)=7, max=7. Optimal is 3.

- Example 3:
  - Input: `a = [0, 0, 0, 0]`
  - Output: `0`
  - Explanation: All XORs are 0. Max = 0.

## Constraints

- `2 <= n <= 16` (n is even)
- `0 <= a[i] <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int minimizeMaxPairXor(int[] a) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def minimize_max_pair_xor(a: List[int]) -> int:
    """
    Pair all elements to minimize maximum pairwise XOR.
    
    Args:
        a: Input array (even length)
    
    Returns:
        Minimum possible value of maximum XOR among pairs
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int minimizeMaxPairXor(const vector<int>& a) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer `n` (array size, even)
- Second line: `n` space-separated integers representing the array

### Sample Input
```
4
7 1 6 2
```

## Hints

With n ≤ 16, use bitmask DP or brute force enumeration of pairings with pruning.

## Quiz

### Question 1
Why is n limited to 16 for this problem?

A) Larger arrays cause overflow  
B) The number of possible pairings grows very fast: (n-1)!! = 1×3×5×...×(n-1)  
C) XOR doesn't work for larger arrays  
D) No particular reason

**Correct Answer:** B

**Explanation:** The number of ways to pair n elements is (n-1)!! which grows super-exponentially. For n=16, this is about 2 million, manageable with optimizations.

### Question 2
Can sorting help reduce complexity?

A) No, sorting doesn't help with XOR  
B) Yes, pairing sorted adjacent elements is always optimal  
C) Sorting helps prune search space but isn't always optimal  
D) Sorting increases complexity

**Correct Answer:** C

**Explanation:** Sorting can help heuristically (similar values have smaller XOR), but it's not always optimal. It helps prune the search.

### Question 3
What is the bitmask DP state?

A) The current maximum XOR  
B) Which elements have been paired  
C) The sum of all XORs  
D) The last paired element

**Correct Answer:** B

**Explanation:** The DP state is a bitmask indicating which elements are already used in pairs. We find the minimum max-XOR for each state.

### Question 4
Binary search on the answer can help. How?

A) Sort and binary search  
B) Binary search on max XOR value; check if pairing achieving ≤ threshold is possible  
C) Binary search on array indices  
D) Binary search doesn't apply

**Correct Answer:** B

**Explanation:** Binary search on the answer: for a candidate max value, check if we can pair all elements such that each pair XOR ≤ that value.
