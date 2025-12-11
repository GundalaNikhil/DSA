---
unique_problem_id: gametheory_003
display_id: GAMETHEORY-003
slug: subtract-square-ban-list
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Problem Solving
---

# Subtract-a-Square with Ban List

## Problem Description

Starting with `n`, players subtract a perfect square s.t. the square is not in a banned set `B`. Player who reaches exactly 0 wins. Determine winner.

## Examples

- Input: n=7, B={1}
  - Output: `Second`

## Constraints

`1 <= n <= 10^5`, `|B| <= 100`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] subtractSquareBanList(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def subtractSquareBanList(arr: List[int]) -> List[int]:
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
    vector<int> subtractSquareBanList(vector<int>& arr) {
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

DP/Grundy up to n; moves exclude banned squares.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Subtract-a-Square with Ban List'?**

A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

**Correct Answer:** B

**Explanation:** The solution requires additional space proportional to the input size for preprocessing or storage.

### Question 2
**What technique is most applicable to solve this problem efficiently?**

A) Two pointers
B) Divide and conquer
C) Dynamic programming
D) Greedy approach

**Correct Answer:** A

**Explanation:** The problem can be efficiently solved using the two-pointer technique.

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
