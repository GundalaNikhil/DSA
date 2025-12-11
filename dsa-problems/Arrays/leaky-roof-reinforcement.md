---
unique_problem_id: arrays_011
display_id: ARRAYS-011
slug: leaky-roof-reinforcement
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Dynamic Programming
  - Greedy
---

# Leaky Roof Reinforcement

## Problem Description

Given roof heights, you can add planks on top of any positions (increase height) so that water will not spill off either end when raining (heights become non-decreasing from left to peak and non-increasing to right). Find the minimum total plank height to add to achieve a single-peak non-leaking profile; peak can be any index.

## Examples

### Example 1
- Input: `[4, 1, 3, 1, 5]`
- Output: `7`
- Explanation: Choose peak at index 4 (value 5). Make heights non-decreasing to the left: [4, 4, 4, 4, 5]. Changes needed: +3 at index 1, +1 at index 2, +3 at index 3. Total = 7.

### Example 2
- Input: `[1, 2, 3, 2, 1]`
- Output: `0`
- Explanation: Already forms a valid peak at index 2. Heights are non-decreasing [1,2,3] then non-increasing [3,2,1]. No planks needed.

### Example 3
- Input: `[5, 5, 5, 5]`
- Output: `0`
- Explanation: All heights are equal, forming a flat peak. Already valid, no planks needed.

### Example 4
- Input: `[1, 5, 2, 4, 3]`
- Output: `5`
- Explanation: If peak at index 1 (value 5): left side needs [1→5] = +4 at index 0. Right side needs [2→5, 4→5, 3→5] or descending pattern. For descending after peak: keep 2, make 4→2 (-2 not allowed, must add). Better: peak at index 3, calculate costs.

## Constraints

- `1 <= n <= 2 * 10^5` (array length)
- `0 <= height[i] <= 10^9` (roof heights)
- Can only add planks (increase heights), not remove
- Must form a bitonic sequence (non-decreasing then non-increasing)
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] leakyRoofReinforcement(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def leakyRoofReinforcement(arr: List[int]) -> List[int]:
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
    vector<int> leakyRoofReinforcement(vector<int>& arr) {
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

Precompute non-decreasing prefix maxima and suffix maxima; for each peak, cost = sum(maxLeft[i],maxRight[i]) - current heights; take minimum.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Leaky Roof Reinforcement'?**

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

A) Arrays
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Arrays techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
