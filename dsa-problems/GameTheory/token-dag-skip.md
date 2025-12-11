---
unique_problem_id: gametheory_011
display_id: GAMETHEORY-011
slug: token-dag-skip
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Problem Solving
---

# Token on DAG with Skip Move

## Problem Description

DAG game; from a node, a move can go along an outgoing edge or skip over one node (two edges) if path exists. Compute winning nodes.

## Examples

- Input: 0->1->2
  - Output: node0 winning, node1 winning, node2 losing

## Constraints

n<=2e5, m<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] tokenDagSkip(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def tokenDagSkip(arr: List[int]) -> List[int]:
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
    vector<int> tokenDagSkip(vector<int>& arr) {
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

Topo order; consider both lengths 1 and 2 transitions.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Token on DAG with Skip Move'?**

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
