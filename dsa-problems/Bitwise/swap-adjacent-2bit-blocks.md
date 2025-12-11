---
unique_problem_id: bitwise_015
display_id: BITWISE-015
slug: swap-adjacent-2bit-blocks
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Bitwise
  - Problem Solving
---

# Swap Adjacent 2-Bit Blocks

## Problem Description

Treat the 32-bit representation of `x` as 2-bit blocks: swap each pair of adjacent blocks (bits 0-1 with 2-3, 4-5 with 6-7, etc.). Return the resulting integer.

## Examples

- Input: `x=13 (0000...1101b)` (bits: 01 11 -> swapped to 11 01 = 13? use clearer)
  - Input: `x=6 (0110b)` -> blocks `01|10` -> swap -> `10|01` = 9

## Constraints

`0 <= x <= 10^9`, assume unsigned 32-bit operations.

## Function Signatures

### Java
```java
public class Solution {
    public int[] swapAdjacent2bitBlocks(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def swapAdjacent2bitBlocks(arr: List[int]) -> List[int]:
    """
    Solve the problem.

    Args:
        arr: Input array

    Returns:
        Result array
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<int> swapAdjacent2bitBlocks(vector<int>& arr) {
        // Implementation here
        return {};
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer n (size of array)
- Second line: n space-separated integers representing the array

### Sample Input
```
5
1 2 3 4 5
```

## Hints

No hints available.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Swap Adjacent 2-Bit Blocks'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Bitwise
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Bitwise techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
