# Auditorium Max Sum With Gap Three

## Problem Metadata
- **unique_problem_id**: `dp_007`
- **display_id**: `DP-007`
- **slug**: `auditorium-max-sum-gap-three`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Array", "Greedy"]`

## Problem Title
Auditorium Max Sum With Gap Three

## Problem Description
Given an array of integers representing values, select elements to maximize the sum such that any two chosen indices differ by at least 3. In other words, you must skip at least 2 elements between any two selected elements.

Return the maximum sum achievable.

## Examples

### Example 1
**Input:**
```
arr = [4, 1, 2, 9, 3]
```

**Output:**
```
13
```

**Explanation:**
- Select elements at indices 0 and 3: arr[0] + arr[3] = 4 + 9 = 13
- Cannot select index 4 because 4 - 3 = 1 < 3
- This is the maximum possible sum.

### Example 2
**Input:**
```
arr = [5, 1, 3, 2, 10, 7, 4, 8]
```

**Output:**
```
27
```

**Explanation:**
- Select indices 0, 3, 6: arr[0] + arr[3] + arr[6] = 5 + 2 + 4 = 11 (not optimal)
- Select indices 0, 4, 7: arr[0] + arr[4] + arr[7] = 5 + 10 + 8 = 23 (not optimal)
- Select indices 1, 4, 7: arr[1] + arr[4] + arr[7] = 1 + 10 + 8 = 19 (not optimal)
- Select indices 4, 7: arr[4] + arr[7] = 10 + 8 = 18 (not optimal)
- Best: indices 0, 3, 7: 5 + 2 + 8 = 15 or 0, 4, 7: 5 + 10 + 8 = 23... let me recalculate

Actually the optimal might be different. Let me try:
- Indices 2, 5: arr[2] + arr[5] = 3 + 7 = 10
- Indices 4, 7: arr[4] + arr[7] = 10 + 8 = 18
- Indices 0, 4, 7: 5 + 10 + 8 = 23 (gap of 4 between 0 and 4, gap of 3 between 4 and 7) ✓
- Wait, can we add more? Indices 0, 3, 7: 5 + 2 + 8 = 15 (nope, worse)

Let me try: 1, 4, 7: 1 + 10 + 8 = 19, or 2, 5: 3 + 7 = 10

Hmm, 23 seems good. But output says 27. Let me try 0, 4, 7: gap is 4 and 3, both ≥ 3. Sum = 5 + 10 + 8 = 23.
What about 1, 4, 7: 1 + 10 + 8 = 19? Or 2, 5: 3 + 7 = 10.

I'll adjust the example to match the sum.

**Corrected Output:**
```
23
```

**Explanation:** Select indices 0, 4, 7: arr[0] + arr[4] + arr[7] = 5 + 10 + 8 = 23.

### Example 3
**Input:**
```
arr = [10]
```

**Output:**
```
10
```

**Explanation:** Only one element, select it.

## Constraints
- `1 <= n <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

## Function Signatures

### Java
```java
class Solution {
    public long maxSumWithGapThree(int[] arr) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def maxSumWithGapThree(self, arr: List[int]) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    long long maxSumWithGapThree(vector<int>& arr) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Integer n (array length)
Line 2: n space-separated integers representing the array elements
```

### Sample Input
```
5
4 1 2 9 3
```

## Hints
- Use dynamic programming with state dp[i] = maximum sum achievable considering elements up to index i
- Recurrence: dp[i] = max(dp[i-1], dp[i-3] + arr[i])
  - Either skip current element (take dp[i-1])
  - Or take current element (must skip from i-3 or earlier)
- Handle base cases carefully for i < 3
- Time complexity: O(n), Space complexity: O(n) or O(1) with optimization

## Related Topics Quiz

### Question 1
What is the recurrence relation for this problem?
- A) dp[i] = max(dp[i-1], dp[i-2] + arr[i])
- B) dp[i] = max(dp[i-1], dp[i-3] + arr[i])
- C) dp[i] = dp[i-1] + dp[i-3]
- D) dp[i] = max(dp[i-2], dp[i-3]) + arr[i]

**Answer:** B) dp[i] = max(dp[i-1], dp[i-3] + arr[i]) - We either skip current or take it with best from 3 positions back.

### Question 2
How is this problem similar to "House Robber"?
- A) Both involve selecting non-adjacent elements
- B) Both maximize sum with gap constraints
- C) Both use dynamic programming
- D) All of the above

**Answer:** D) All of the above - This is a variant with a larger gap requirement.

### Question 3
What is the minimum gap required between selected elements?
- A) 1
- B) 2
- C) 3
- D) 4

**Answer:** C) 3 - Indices must differ by at least 3.

### Question 4
Can we optimize space complexity to O(1)?
- A) No, we need O(n) space
- B) Yes, we only need to track last 3 DP values
- C) Yes, but only if we sort the array first
- D) Only for positive numbers

**Answer:** B) Yes, we only need to track last 3 DP values - We only reference dp[i-1], dp[i-2], and dp[i-3].

### Question 5
If all elements are negative, what should we return?
- A) 0
- B) The least negative element
- C) -1
- D) The sum of all elements

**Answer:** B) The least negative element - We must select at least one element; choose the maximum (least negative).
