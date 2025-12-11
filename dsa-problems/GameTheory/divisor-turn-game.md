---
unique_problem_id: gametheory_006
display_id: GAMETHEORY-006
slug: divisor-turn-game
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Problem Solving
---

# Divisor Turn Game

## Problem Description

Start with integer `n`. A move: replace n with any proper divisor (greater than 1). Player who cannot move loses. Determine winner.

## Examples

- Input: n=2
  - Output: `Second`

## Constraints

`2 <= n <= 10^6`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] divisorTurnGame(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def divisorTurnGame(arr: List[int]) -> List[int]:
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
    vector<int> divisorTurnGame(vector<int>& arr) {
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

Precompute win/lose; n is losing if all divisors lead to winning positions.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Divisor Turn Game'?**

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
