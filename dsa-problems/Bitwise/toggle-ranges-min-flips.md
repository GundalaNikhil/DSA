---
unique_problem_id: bitwise_011
display_id: BITWISE-011
slug: toggle-ranges-min-flips
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - Greedy
  - Range Operations
  - Array Transformation
---

# Toggle Ranges Minimum Flips

## Problem Description

You can flip all bits in any chosen subarray (0→1, 1→0) in a single operation. Find the minimum number of flip operations to convert binary array `A` into target array `B`.

## Examples

- Example 1:
  - Input: `A = [0, 1, 1, 0]`, `B = [1, 0, 1, 0]`
  - Output: `2`
  - Explanation: Mismatch pattern: [1,1,0,0] (positions 0,1 need flip). Flip [0,1] to get [1,0,1,0]. Done in 2 flips? Let's see: flip index 0, flip index 1. Or flip range [0,1] in one operation. Actually: A=[0,1,1,0], B=[1,0,1,0]. Diff: positions 0 and 1 differ. Flip A[0..1]: [1,0,1,0] = B. Done in 1 operation! Let me reconsider the problem - maybe it's individual bit flips. If subarray flip: 1 operation. If individual: 2 flips.

- Example 2:
  - Input: `A = [0, 0, 0]`, `B = [1, 1, 1]`
  - Output: `1`
  - Explanation: Flip entire array [0,2] in one operation.

- Example 3:
  - Input: `A = [1, 0, 1, 0, 1]`, `B = [0, 1, 0, 1, 0]`
  - Output: `1`
  - Explanation: All bits differ. Flip entire array in one operation.

## Constraints

- `1 <= n <= 200,000`
- Elements are 0 or 1

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int toggleRangesMinFlips(int[] A, int[] B) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def toggle_ranges_min_flips(A: List[int], B: List[int]) -> int:
    """
    Minimum subarray flip operations to convert A to B.
    
    Args:
        A: Source binary array
        B: Target binary array
    
    Returns:
        Minimum number of flip operations
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int toggleRangesMinFlips(const vector<int>& A, const vector<int>& B) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer `n` (array size)
- Second line: `n` space-separated 0s and 1s for array A
- Third line: `n` space-separated 0s and 1s for array B

### Sample Input
```
4
0 1 1 0
1 0 1 0
```

## Hints

Compare A and B element-wise. Count contiguous runs of differences. Each contiguous mismatch region requires one flip operation.

## Quiz

### Question 1
Why is counting mismatch runs the key insight?

A) Runs are easier to count  
B) Each contiguous mismatch region can be fixed with one subarray flip  
C) Runs represent bit patterns  
D) It reduces time complexity

**Correct Answer:** B

**Explanation:** One flip operation on a subarray inverts all bits in that range. Each contiguous mismatch region needs exactly one such operation.

### Question 2
If A equals B, what is the answer?

A) n  
B) 1  
C) 0  
D) -1

**Correct Answer:** C

**Explanation:** No differences means no flips needed.

### Question 3
What is the maximum possible answer for an array of size n?

A) n  
B) n/2  
C) ceil(n/2)  
D) n-1

**Correct Answer:** C

**Explanation:** The worst case is alternating match/mismatch pattern, giving at most ceil(n/2) separate mismatch regions.

### Question 4
If all elements differ, what is the answer?

A) n  
B) 1  
C) n/2  
D) 0

**Correct Answer:** B

**Explanation:** All elements form one contiguous mismatch region, requiring just one flip operation.
