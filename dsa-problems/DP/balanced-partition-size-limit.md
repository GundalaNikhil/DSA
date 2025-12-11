# Balanced Partition With Size Limit

## Problem Metadata
- **unique_problem_id**: `dp_012`
- **display_id**: `DP-012`
- **slug**: `balanced-partition-size-limit`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Partition", "Optimization", "Subset"]`

## Problem Title
Balanced Partition With Size Limit

## Problem Description
Given an array of integers `a` and a maximum allowed sum difference `D`, partition the array into two non-empty groups such that:

1. The absolute difference between the two groups' sums is at most `D`
2. The size of the larger group is minimized

Return the minimum possible size of the larger group. If no valid partition exists, return -1.

## Examples

### Example 1
**Input:**
```
a = [3, 1, 4, 2]
D = 1
```

**Output:**
```
2
```

**Explanation:**
- Total sum = 10
- Group 1: {3, 2} = 5, Group 2: {1, 4} = 5
- Difference: |5 - 5| = 0 ≤ 1 ✓
- Sizes: 2 and 2, larger group size = 2

### Example 2
**Input:**
```
a = [1, 2, 3, 4, 5, 6]
D = 2
```

**Output:**
```
3
```

**Explanation:**
- Total sum = 21
- Group 1: {6, 5} = 11, Group 2: {1, 2, 3, 4} = 10
- Difference: |11 - 10| = 1 ≤ 2 ✓
- Sizes: 2 and 4, larger group size = 4... but output is 3?

Let me try different partition:
- Group 1: {1, 6, 4} = 11, Group 2: {2, 3, 5} = 10
- Difference: |11 - 10| = 1 ≤ 2 ✓
- Sizes: 3 and 3, larger group size = 3 ✓

### Example 3
**Input:**
```
a = [10, 20]
D = 5
```

**Output:**
```
-1
```

**Explanation:**
- Group 1: {10}, Group 2: {20} → difference = 10 > 5 ✗
- Group 1: {20}, Group 2: {10} → difference = 10 > 5 ✗
- No valid partition exists

## Constraints
- `1 <= n <= 50`
- `1 <= D <= 5000`
- `-500 <= a[i] <= 500`
- Both groups must be non-empty

## Function Signatures

### Java
```java
class Solution {
    public int minLargerGroupSize(int[] a, int D) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def minLargerGroupSize(self, a: List[int], D: int) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int minLargerGroupSize(vector<int>& a, int D) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Two space-separated integers: n (array length), D (max difference)
Line 2: n space-separated integers representing array elements
```

### Sample Input
```
4 1
3 1 4 2
```

## Hints
- Use DP to track all possible (sum_difference, group1_size) states
- State: dp[diff][size] = true if we can achieve sum difference `diff` with group1 having `size` elements
- For each element, decide which group it joins
- Sum difference can range from -total_sum to +total_sum, use offset for indexing
- After DP, find minimum max(size, n - size) where |diff| ≤ D
- Alternatively, use dp[i][sum][count] tracking first i elements, sum of group1, and count in group1

## Related Topics Quiz

### Question 1
What is the time complexity of the DP solution?
- A) O(n × sum × n)
- B) O(n²)
- C) O(n × D)
- D) O(2^n)

**Answer:** A) O(n × sum × n) - We track position, possible sums, and group sizes.

### Question 2
Why might this problem return -1?
- A) Array is empty
- B) No partition satisfies the sum difference constraint
- C) Array has negative numbers
- D) D is too large

**Answer:** B) No partition satisfies the sum difference constraint - If elements are too unbalanced.

### Question 3
Can both groups be the same size?
- A) No, one must be larger
- B) Yes, when n is even
- C) Only if n is odd
- D) Never allowed

**Answer:** B) Yes, when n is even - If n is even, we can have equal group sizes.

### Question 4
What happens if we partition into groups of size 1 and n-1?
- A) Always valid
- B) Valid only if sum difference ≤ D
- C) Never optimal
- D) Creates an error

**Answer:** B) Valid only if sum difference ≤ D - Must still satisfy the difference constraint.

### Question 5
How do we handle negative numbers in the array?
- A) Take absolute value
- B) Ignore them
- C) Include them normally in DP
- D) Not allowed

**Answer:** C) Include them normally in DP - The DP handles negative values through sum differences.
