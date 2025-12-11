---
unique_problem_id: bitwise_008
display_id: BITWISE-008
slug: maximize-or-k-picks
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - OR Operation
  - Greedy
  - Bit Manipulation
---

# Maximize OR With K Picks

## Problem Description

Choose exactly `k` elements from the array to maximize the bitwise OR of the chosen set.

## Examples

- Example 1:
  - Input: `a = [1, 2, 4]`, `k = 2`
  - Output: `6`
  - Explanation: Choose 2 and 4. OR = 2 | 4 = 6. Other options: {1,2}=3, {1,4}=5, {2,4}=6.

- Example 2:
  - Input: `a = [7, 3, 1, 2]`, `k = 1`
  - Output: `7`
  - Explanation: Choose 7. Single element, OR = 7.

- Example 3:
  - Input: `a = [5, 5, 5]`, `k = 3`
  - Output: `5`
  - Explanation: All elements are 5. OR of any combination is 5.

## Constraints

- `1 <= n <= 200,000`
- `1 <= k <= n`
- `0 <= a[i] <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int maximizeOrKPicks(int[] a, int k) {
        // Implementation here
        return 0;
    }
}
```

### Python
```python
from typing import List

def maximize_or_k_picks(a: List[int], k: int) -> int:
    """
    Choose k elements to maximize their bitwise OR.
    
    Args:
        a: Input array
        k: Number of elements to choose
    
    Returns:
        Maximum possible OR value
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maximizeOrKPicks(const vector<int>& a, int k) {
        // Implementation here
        
    }
};
```

## Input Format

The input will be provided as:
- First line: Two integers `n` (array size) and `k` (number of picks)
- Second line: `n` space-separated integers representing the array

### Sample Input
```
3 2
1 2 4
```

## Hints

Greedy by bits from high to low. Always include elements that contribute the highest remaining bits not yet set in the current OR.

## Quiz

### Question 1
Why does a greedy approach work for maximizing OR?

A) OR is commutative  
B) Once a bit is set in OR, it stays set regardless of additional elements  
C) OR distributes over addition  
D) Greedy doesn't actually work

**Correct Answer:** B

**Explanation:** Adding more elements can only add more 1 bits to OR, never remove them. So we greedily pick elements with highest bits.

### Question 2
If k equals n, what is the answer?

A) 0  
B) OR of all elements  
C) AND of all elements  
D) XOR of all elements

**Correct Answer:** B

**Explanation:** We must pick all elements, so the answer is simply the OR of the entire array.

### Question 3
What is a simple upper bound for the maximum OR?

A) Sum of all elements  
B) OR of all elements  
C) Maximum element  
D) n × max_element

**Correct Answer:** B

**Explanation:** The maximum possible OR is achieved when we can pick elements that together cover all bits in the full array OR. So OR of all is the upper bound.

### Question 4
If all elements are the same value v, what is the answer for any k >= 1?

A) 0  
B) v  
C) k × v  
D) v ^ k

**Correct Answer:** B

**Explanation:** OR of same values is that value: v | v | ... | v = v.
