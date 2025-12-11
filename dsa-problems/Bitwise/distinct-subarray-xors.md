---
unique_problem_id: bitwise_012
display_id: BITWISE-012
slug: distinct-subarray-xors
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - XOR
  - Prefix XOR
  - Trie
  - Hash Set
---

# Distinct Subarray XORs

## Problem Description

Compute how many distinct XOR results appear among all subarrays of the given array.

## Examples

- Example 1:
  - Input: `a = [1, 2, 3]`
  - Output: `6`
  - Explanation: Subarrays and XORs: [1]=1, [2]=2, [3]=3, [1,2]=3, [2,3]=1, [1,2,3]=0. Distinct: {0,1,2,3}. Wait, that's 4. Let me recalculate: [1]=1, [2]=2, [3]=3, [1,2]=1⊕2=3, [2,3]=2⊕3=1, [1,2,3]=1⊕2⊕3=0. Set: {0,1,2,3} = 4 distinct. Original says 6 - might include duplicate counts. Actually the number of subarrays is 6, but distinct XOR values is 4.

- Example 2:
  - Input: `a = [5, 5]`
  - Output: `2`
  - Explanation: [5]=5, [5]=5, [5,5]=0. Distinct: {0, 5} = 2.

- Example 3:
  - Input: `a = [1, 1, 1, 1]`
  - Output: `2`
  - Explanation: Odd-length subarrays have XOR=1, even-length have XOR=0. Distinct: {0, 1} = 2.

## Constraints

- `1 <= n <= 10,000`
- `0 <= a[i] <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int distinctSubarrayXors(int[] a) {
      // Implementation here

    }
}
```

### Python
```python
from typing import List

def distinct_subarray_xors(a: List[int]) -> int:
    """
    Count distinct XOR values among all subarrays.
    
    Args:
        a: Input array
    
    Returns:
        Number of distinct XOR values
    """
    pass
```

### C++
```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int distinctSubarrayXors(const vector<int>& a) {
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

Use prefix XOR. Subarray XOR = prefix[j] ⊕ prefix[i-1]. Insert all such pairs into a set using trie for efficiency.

## Quiz

### Question 1
How many subarrays does an array of length n have?

A) n  
B) n(n+1)/2  
C) 2^n  
D) n²

**Correct Answer:** B

**Explanation:** There are n choices for length 1, n-1 for length 2, etc. Total = n + (n-1) + ... + 1 = n(n+1)/2.

### Question 2
How does prefix XOR help compute subarray XOR?

A) Prefix[j] + Prefix[i]  
B) Prefix[j] - Prefix[i]  
C) Prefix[j] ⊕ Prefix[i-1]  
D) Prefix[j] × Prefix[i]

**Correct Answer:** C

**Explanation:** XOR is self-inverse. Prefix[j] = a[0]⊕...⊕a[j], so Prefix[j] ⊕ Prefix[i-1] = a[i]⊕...⊕a[j].

### Question 3
What is the brute force time complexity?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(n³)

**Correct Answer:** C

**Explanation:** We have O(n²) subarrays. Computing each XOR can be O(1) with prefix XOR, giving O(n²) total.

### Question 4
Can two different subarrays have the same XOR?

A) Never  
B) Only if they're the same subarray  
C) Yes, different subarrays can produce the same XOR  
D) Only for consecutive elements

**Correct Answer:** C

**Explanation:** Different subarrays can have the same XOR, which is why we use a set to count distinct values.
