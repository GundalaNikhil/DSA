# Exact Count Subset Sum

## Problem Metadata
- **unique_problem_id**: `dp_004`
- **display_id**: `DP-004`
- **slug**: `exact-count-subset-sum`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Subset Sum", "Combinatorics"]`

## Problem Title
Exact Count Subset Sum

## Problem Description
Given an array of positive integers `arr` and two integers `target` and `k`, determine if there exists a subset of exactly `k` elements from the array that sums to `target`.

Return `true` if such a subset exists, otherwise return `false`.

## Examples

### Example 1
**Input:**
```
arr = [3, 1, 9, 7]
target = 10
k = 2
```

**Output:**
```
true
```

**Explanation:** The subset {3, 7} has exactly 2 elements and sums to 10.

### Example 2
**Input:**
```
arr = [2, 4, 6, 8]
target = 15
k = 3
```

**Output:**
```
false
```

**Explanation:** No combination of exactly 3 elements sums to 15. Closest would be {2,4,8}=14 or {2,6,8}=16.

### Example 3
**Input:**
```
arr = [1, 2, 3, 4, 5]
target = 9
k = 3
```

**Output:**
```
true
```

**Explanation:** The subset {1, 3, 5} has exactly 3 elements and sums to 9. Another valid subset is {2, 3, 4}.

## Constraints
- `1 <= n <= 200` (length of array)
- `1 <= target <= 5000`
- `1 <= k <= n`
- `1 <= arr[i] <= 1000`

## Function Signatures

### Java
```java
class Solution {
    public boolean canPartitionKSubset(int[] arr, int target, int k) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def canPartitionKSubset(self, arr: List[int], target: int, k: int) -> bool:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    bool canPartitionKSubset(vector<int>& arr, int target, int k) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Three space-separated integers: n (array length), target, k (required count)
Line 2: n space-separated integers representing the array elements
```

### Sample Input
```
4 10 2
3 1 9 7
```

## Hints
- Use 2D DP: dp[count][sum] represents if we can achieve sum using exactly count elements
- State: dp[i][j] = true if we can select exactly i elements with sum j
- Base case: dp[0][0] = true (0 elements, 0 sum)
- Transition: For each element, decide to include it or not
- Iterate through items in outer loop, then iterate count and sum in reverse order
- Space optimization: Use 2D array of size (k+1) × (target+1)

## Related Topics Quiz

### Question 1
What is the time complexity of the DP solution?
- A) O(n * target)
- B) O(n * k * target)
- C) O(n^2 * k)
- D) O(k * target)

**Answer:** B) O(n * k * target) - We iterate through n items, and for each we update k × target states.

### Question 2
Why do we need to iterate count and sum in reverse order when using space optimization?
- A) To avoid using the same element multiple times
- B) For better cache performance
- C) To maintain sorted order
- D) It's not necessary

**Answer:** A) To avoid using the same element multiple times - This ensures we use the previous iteration's values.

### Question 3
What is the space complexity with optimization?
- A) O(n * k * target)
- B) O(k * target)
- C) O(target)
- D) O(n)

**Answer:** B) O(k * target) - We only need to track states for all combinations of count (0 to k) and sum (0 to target).

### Question 4
What should be the base case for this DP problem?
- A) dp[0][0] = true
- B) dp[k][target] = true
- C) dp[1][arr[0]] = true
- D) All dp[i][0] = true

**Answer:** A) dp[0][0] = true - Selecting 0 elements to get sum 0 is always possible (empty subset).

### Question 5
How does this differ from regular subset sum?
- A) It requires negative numbers
- B) It requires exactly k elements in the subset
- C) It allows duplicates
- D) It finds the minimum sum

**Answer:** B) It requires exactly k elements in the subset - Regular subset sum doesn't care about the count.
