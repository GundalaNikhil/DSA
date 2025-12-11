---
unique_problem_id: linkedlist_002
display_id: LINKEDLIST-002
slug: campus-badge-search
version: 1.0.0
difficulty: Easy
topic_tags:
  - Linked Lists
  - Linear Search
  - List Traversal
---

# Campus Badge Search

## Problem Description

Given the head of a singly linked list and a target value, return the 0-based index of its first occurrence, or -1 if absent.

## Examples

### Example 1
- Input: `list = 5 -> 1 -> 5 -> 9`, `target = 9`
- Output: `3`
- Explanation: Target 9 is found at index 3 (0-indexed). Indices: 5(0), 1(1), 5(2), 9(3).

### Example 2
- Input: `list = 2 -> 4 -> 6 -> 8`, `target = 4`
- Output: `1`
- Explanation: Target 4 is at index 1.

### Example 3
- Input: `list = 1 -> 2 -> 3`, `target = 5`
- Output: `-1`
- Explanation: Target 5 not found in list. Return -1.

### Example 4
- Input: `list = 7`, `target = 7`
- Output: `0`
- Explanation: Single node list. Target found at index 0.

### Example 5
- Input: `list = 3 -> 3 -> 3 -> 5`, `target = 3`
- Output: `0`
- Explanation: Multiple occurrences of 3. Return first occurrence at index 0.

## Constraints

- `1 <= n <= 10^5` (number of nodes)
- `-10^9 <= node.val <= 10^9` (node values)
- `-10^9 <= target <= 10^9`
- Return 0-based index of first occurrence
- Return -1 if target not found
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] campusBadgeSearch(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def campusBadgeSearch(arr: List[int]) -> List[int]:
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
    vector<int> campusBadgeSearch(vector<int>& arr) {
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

Linear scan with a position counter.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Campus Badge Search'?**

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

A) Linked Lists
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Linked Lists techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
