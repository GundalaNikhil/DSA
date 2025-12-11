---
unique_problem_id: gametheory_001
display_id: GAMETHEORY-001
slug: pile-split-choice
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Game Theory
  - Problem Solving
---

# Pile Split Choice

## Problem Description

A pile of `n` stones; on each turn a player may split one pile into two non-empty piles of different sizes. Player who cannot move loses. Determine the winner with optimal play for given `n`.

## Examples

- Input: `n=3`
  - Output: `First`

## Constraints

`1 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] pileSplitChoice(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def pileSplitChoice(arr: List[int]) -> List[int]:
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
    vector<int> pileSplitChoice(vector<int>& arr) {
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

Compute Grundy for n using mex of splits; note pattern for small n.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Pile Split Choice'?**

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

A) Game Theory
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Game Theory techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
