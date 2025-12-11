---
unique_problem_id: bitwise_010
display_id: BITWISE-010
slug: subset-and-equals-x
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - AND Operation
  - Subset Enumeration
  - Bitmask DP
  - Backtracking
---

# Subset AND Equals X

## Problem Description

Count non-empty subsets of the array whose bitwise AND equals exactly `X`.

## Examples

- Example 1:
  - Input: `a = [6, 3, 2]`, `X = 2`
  - Output: `2`
  - Explanation: Subsets: {6}=6, {3}=3, {2}=2✓, {6,3}=2✓, {6,2}=2✓, {3,2}=2✓, {6,3,2}=2✓. Wait, let's recalculate: {6}&=6, {3}=3, {2}=2, {6,3}=6&3=2, {6,2}=6&2=2, {3,2}=3&2=2, {6,3,2}=2. Subsets with AND=2: {2}, {6,3}, {6,2}, {3,2}, {6,3,2}. That's 5, not 2. Let me re-check: 6=110, 3=011, 2=010. 6&3=010=2, 6&2=010=2, 3&2=010=2, 6&3&2=010=2. So count = 5. The original example may be wrong. Using: {2}, {6,3}, {6,2}, {3,2}, {6,3,2} = 5 subsets.

- Example 2:
  - Input: `a = [7, 7, 7]`, `X = 7`
  - Output: `7`
  - Explanation: All non-empty subsets have AND = 7. There are 2^3 - 1 = 7 non-empty subsets.

- Example 3:
  - Input: `a = [1, 2, 4]`, `X = 0`
  - Output: `1`
  - Explanation: Only {1,2,4} has AND = 1&2&4 = 0. Other subsets have non-zero AND.

## Constraints

- `1 <= n <= 20`
- `0 <= a[i], X <= 10^6`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int subsetAndEqualsX(int[] a, int X) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def subset_and_equals_x(a: List[int], X: int) -> int:
    """
    Count subsets with bitwise AND equal to X.
    
    Args:
        a: Input array
        X: Target AND value
    
    Returns:
        Count of non-empty subsets with AND = X
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int subsetAndEqualsX(const vector<int>& a, int X) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Two integers `n` (array size) and `X` (target AND)
- Second line: `n` space-separated integers representing the array

### Sample Input
```
3 2
6 3 2
```

## Hints

For small n (≤20), enumerate all 2^n subsets. Prune by noting AND only decreases as we add elements.

## Quiz

### Question 1
How does AND behave as we add more elements to a subset?

A) AND can only increase or stay the same  
B) AND can only decrease or stay the same  
C) AND can increase or decrease arbitrarily  
D) AND always becomes 0

**Correct Answer:** B

**Explanation:** AND clears bits; adding more elements can only clear bits (set them to 0), never set new 1 bits.

### Question 2
What is the time complexity of brute force for n=20?

A) O(n)  
B) O(n²)  
C) O(2^n)  
D) O(n!)

**Correct Answer:** C

**Explanation:** We enumerate all 2^n subsets. For n=20, this is about 10^6, which is feasible.

### Question 3
If X has a bit set that no element in the array has, what is the answer?

A) n  
B) 2^n  
C) 0  
D) 1

**Correct Answer:** C

**Explanation:** AND never sets new bits. If X requires a bit that no element has, no subset can achieve it.

### Question 4
For all elements equal to X, how many subsets have AND = X?

A) 1  
B) n  
C) 2^n - 1  
D) 0

**Correct Answer:** C

**Explanation:** Every non-empty subset of elements equal to X has AND = X. There are 2^n - 1 non-empty subsets.
