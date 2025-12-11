---
unique_problem_id: greedy_007
display_id: GREEDY-007
slug: campus-wifi-expansion
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Campus Wi-Fi Expansion

## Problem Description

You must connect `n` buildings. Some cables already exist; laying a new cable between buildings `i` and `j` costs `|h[i]-h[j]|` where `h` is building height. Find the min total cost to connect all buildings.

## Examples

- Input: `h = [5, 1, 9]`
  - Output: `8`

## Constraints

`1 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] campusWifiExpansion(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def campusWifiExpansion(arr: List[int]) -> List[int]:
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
    vector<int> campusWifiExpansion(vector<int>& arr) {
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

Build candidate edges only between adjacent buildings when sorted by height; then run Kruskal.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Campus Wi-Fi Expansion'?**

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
