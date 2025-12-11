---
unique_problem_id: greedy_004
display_id: GREEDY-004
slug: library-power-backup
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Library Power Backup

## Problem Description

Backup batteries have capacities `c[i]`. You must power a server for `T` hours; each hour you may draw from one battery until empty. Choose batteries and ordering to minimize the number of battery swaps (times you change to a new battery). Return swaps or -1 if not enough total capacity.

## Examples

- Input: `c=[3,5,2], T=7`
  - Output: `1`

## Constraints

`1 <= n <= 10^5`, `1 <= c[i] <= 10^9`, `1 <= T <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] libraryPowerBackup(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def libraryPowerBackup(arr: List[int]) -> List[int]:
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
    vector<int> libraryPowerBackup(vector<int>& arr) {
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

Greedy pick largest capacities first; swaps = chosen batteries - 1.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Library Power Backup'?**

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

A) Greedy
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Greedy techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
