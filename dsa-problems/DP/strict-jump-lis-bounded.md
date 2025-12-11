# Strict Jump LIS With Max Gap

## Problem Metadata
- **unique_problem_id**: `dp_006`
- **display_id**: `DP-006`
- **slug**: `strict-jump-lis-bounded`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Segment Tree", "Longest Increasing Subsequence", "Binary Indexed Tree"]`

## Problem Title
Strict Jump LIS With Max Gap

## Problem Description
Given an array `a` of integers and two integers `d` and `g` (where d ≤ g), find the longest subsequence where each next element is at least `d` larger and at most `g` larger than the previous element.

Formally, find the longest subsequence a[i₁], a[i₂], ..., a[iₖ] where:
- i₁ < i₂ < ... < iₖ (indices are strictly increasing)
- For all consecutive pairs: d ≤ a[iⱼ₊₁] - a[iⱼ] ≤ g

Return the length of the longest such subsequence.

## Examples

### Example 1
**Input:**
```
a = [1, 3, 4, 9, 10]
d = 2
g = 6
```

**Output:**
```
3
```

**Explanation:**
- Subsequence [1, 3, 9]: differences are 2 and 6 (both in range [2, 6]) ✓
- Subsequence [1, 4, 9]: differences are 3 and 5 (both in range [2, 6]) ✓
- Subsequence [1, 3, 4]: differences are 2 and 1 (1 < d) ✗

The longest valid subsequence has length 3.

### Example 2
**Input:**
```
a = [5, 10, 15, 20, 25]
d = 5
g = 5
```

**Output:**
```
5
```

**Explanation:** The entire array forms a valid subsequence since each difference is exactly 5.

### Example 3
**Input:**
```
a = [1, 2, 3, 4, 5]
d = 10
g = 20
```

**Output:**
```
1
```

**Explanation:** No two elements have a difference ≥ 10, so each element forms its own subsequence of length 1.

## Constraints
- `1 <= n <= 10^5`
- `-10^9 <= a[i] <= 10^9`
- `0 <= d <= g <= 10^9`

## Function Signatures

### Java
```java
class Solution {
    public int longestStrictJumpSubsequence(int[] a, int d, int g) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def longestStrictJumpSubsequence(self, a: List[int], d: int, g: int) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int longestStrictJumpSubsequence(vector<int>& a, int d, int g) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Three space-separated integers: n (array length), d (minimum gap), g (maximum gap)
Line 2: n space-separated integers representing the array elements
```

### Sample Input
```
5 2 6
1 3 4 9 10
```

## Hints
- This is a variant of Longest Increasing Subsequence (LIS) with constraints
- Use coordinate compression if values have large range
- Segment Tree or Fenwick Tree (BIT) can efficiently query range maximum
- For each element a[i], query the maximum length from range [a[i]-g, a[i]-d]
- Update the segment tree at position a[i] with the new length
- Time complexity: O(n log n) with segment tree and coordinate compression

## Related Topics Quiz

### Question 1
Why is a segment tree useful for this problem?
- A) To sort the array efficiently
- B) To query maximum DP value in a range [a[i]-g, a[i]-d]
- C) To find the minimum element
- D) To count elements

**Answer:** B) To query maximum DP value in a range [a[i]-g, a[i]-d] - We need efficient range maximum queries.

### Question 2
What is coordinate compression used for?
- A) To reduce memory usage when value range is large
- B) To sort the array
- C) To find duplicates
- D) To compress the output

**Answer:** A) To reduce memory usage when value range is large - Maps values to a smaller range [0, n-1].

### Question 3
What is the time complexity with segment tree and coordinate compression?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(n² log n)

**Answer:** B) O(n log n) - Sorting for compression is O(n log n), and each update/query is O(log n).

### Question 4
If d = 0 and g = infinity, what problem does this reduce to?
- A) Longest Decreasing Subsequence
- B) Standard Longest Increasing Subsequence
- C) Longest Common Subsequence
- D) Maximum Subarray Sum

**Answer:** B) Standard Longest Increasing Subsequence - No gap constraints, just strictly increasing.

### Question 5
What should dp[i] represent in this problem?
- A) The length of longest subsequence ending at index i
- B) The length of longest subsequence starting at index i
- C) The maximum value in the subsequence
- D) The sum of elements in the subsequence

**Answer:** A) The length of longest subsequence ending at index i - Classic DP state for subsequence problems.
