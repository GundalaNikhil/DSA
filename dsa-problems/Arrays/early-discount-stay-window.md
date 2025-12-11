---
unique_problem_id: arrays_010
display_id: ARRAYS-010
slug: early-discount-stay-window
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Sliding Window
  - Dynamic Programming
---

# Early Discount With Stay Window and Ceiling

## Problem Description

You may buy once and sell once. You must hold the item for at least `dMin` days and at most `dMax` days, and the sell price must not exceed a ceiling `C` (if price > C, you are forced to sell at C). Return maximum achievable profit (or 0 if not profitable).

## Examples

### Example 1
- Input: prices = `[7, 2, 5, 1, 9]`, `dMin = 1`, `dMax = 3`, `C = 6`
- Output: `5`
- Explanation: Buy at price 1 on day 3, sell on day 4 at min(9, 6) = 6. Profit = 6 - 1 = 5. The holding period is 1 day, which satisfies dMin ≤ 1 ≤ dMax.

### Example 2
- Input: prices = `[10, 8, 6, 4, 2]`, `dMin = 1`, `dMax = 2`, `C = 100`
- Output: `0`
- Explanation: Prices are strictly decreasing. No profitable transaction possible, return 0.

### Example 3
- Input: prices = `[3, 5, 2, 8, 1, 10]`, `dMin = 2`, `dMax = 4`, `C = 7`
- Output: `5`
- Explanation: Buy at 2 (day 2), must hold for at least 2 days. Can sell on day 4 or 5. At day 5 (price 10, capped at 7), profit = 7 - 2 = 5. At day 4 (price 8, capped at 7), profit = 7 - 2 = 5. Maximum profit is 5.

## Constraints

- `1 <= n <= 2 * 10^5` (number of days)
- `0 <= price[i] <= 10^9` (price on day i)
- `1 <= dMin <= dMax <= n` (holding period constraints)
- `0 <= C <= 10^9` (price ceiling)
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] earlyDiscountStayWindow(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def earlyDiscountStayWindow(arr: List[int]) -> List[int]:
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
    vector<int> earlyDiscountStayWindow(vector<int>& arr) {
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

Track best effective buy value up to day i-dMin; when selling on day i, profit = min(price[i], C) - best buy in window [i-dMax, i-dMin].

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Early Discount With Stay Window and Ceiling'?**

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
