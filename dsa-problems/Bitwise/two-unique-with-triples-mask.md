---
unique_problem_id: bitwise_002
display_id: BITWISE-002
slug: two-unique-with-triples-mask
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - XOR
  - Bit Counting
  - Modular Arithmetic
  - Array Processing
---

# Two Unique With Triple Others Under Mask

## Problem Description

Every number in the array appears exactly three times except two distinct numbers that appear once each. Additionally, a mask `M` is given; the two unique numbers are guaranteed to differ in at least one bit that is set in `M`. Find the two unique numbers.

## Examples

- Example 1:
  - Input: `arr = [5, 5, 5, 9, 9, 9, 3, 6]`, `M = 2`
  - Output: `[3, 6]`
  - Explanation: 5 and 9 appear 3 times each (cancel out mod 3). 3 (`011`) and 6 (`110`) appear once each. They differ in bit 2 (value 2), which is set in M. Count each bit mod 3 to get XOR of uniques, then split using a differing bit from M.

- Example 2:
  - Input: `arr = [1, 1, 1, 2, 2, 2, 4, 8]`, `M = 12`
  - Output: `[4, 8]`
  - Explanation: 4 (`0100`) and 8 (`1000`) are unique. They differ in bits 2 and 3, both set in M=12 (`1100`).

- Example 3:
  - Input: `arr = [7, 7, 7, 3, 3, 3, 1, 2]`, `M = 3`
  - Output: `[1, 2]`
  - Explanation: 1 (`01`) and 2 (`10`) differ in both bits 0 and 1, both set in M=3 (`11`).

## Constraints

- `2 <= n <= 200,000` (array size, where all but 2 elements appear exactly 3 times)
- `0 <= arr[i] <= 10^9`
- `0 <= M <= 10^9`
- The two uniques differ in at least one bit set in M

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int[] twoUniqueWithTriplesMask(int[] arr, int M) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def two_unique_with_triples_mask(arr: List[int], M: int) -> List[int]:
    """
    Find two numbers appearing once when all others appear thrice.
    
    Args:
        arr: Input array where all but 2 elements appear exactly 3 times
        M: Mask guaranteeing the two uniques differ in at least one bit set in M
    
    Returns:
        List of the two unique numbers
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoUniqueWithTriplesMask(const vector<int>& arr, int M) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Two integers `n` (array size) and `M` (mask)
- Second line: `n` space-separated integers representing the array

### Sample Input
```
8 2
5 5 5 9 9 9 3 6
```

## Hints

Count bits mod 3 to cancel out triples. Use the mask M to identify a differing bit between the two uniques, then partition and solve separately.

## Quiz

### Question 1
Why do we count bits modulo 3 instead of using XOR directly?

A) XOR doesn't work with negative numbers  
B) Elements appear 3 times, not 2 times, so XOR won't cancel them  
C) Counting is faster than XOR  
D) XOR only works with powers of 2

**Correct Answer:** B

**Explanation:** XOR cancels pairs (a⊕a=0), but with triples (a⊕a⊕a=a), it doesn't cancel. Counting each bit mod 3 effectively filters out numbers appearing 3 times.

### Question 2
What is the purpose of the mask M in this problem?

A) To encrypt the output  
B) To guarantee a differing bit exists for splitting the two uniques  
C) To reduce the search space  
D) To validate the input

**Correct Answer:** B

**Explanation:** The mask M guarantees that the two unique numbers differ in at least one bit that is set in M, allowing us to split them into separate groups.

### Question 3
What is the time complexity of the optimal solution?

A) O(n)  
B) O(n log n)  
C) O(n × 32) which is O(n)  
D) O(n²)

**Correct Answer:** C

**Explanation:** We iterate through the array counting each of 32 bits mod 3, giving O(32n) = O(n).

### Question 4
After counting bits mod 3, what do we obtain?

A) The sum of the two unique numbers  
B) The XOR of the two unique numbers  
C) The AND of the two unique numbers  
D) The product of the two unique numbers

**Correct Answer:** B

**Explanation:** Each bit position with count mod 3 = 1 means that bit is set in exactly one of the two uniques, giving us their XOR.
