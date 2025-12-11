# Required Weight Knapsack

## Problem Metadata
- **unique_problem_id**: `dp_003`
- **display_id**: `DP-003`
- **slug**: `required-weight-knapsack`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Knapsack", "Optimization"]`

## Problem Title
Required Weight Knapsack

## Problem Description
You are given `n` items, each with a weight `weight[i]` and value `value[i]`. You have a knapsack with capacity `W`, and there's a required minimum total weight `R` (where R ≤ W).

You must select items such that:
1. The total weight is at least `R` (minimum requirement)
2. The total weight is at most `W` (capacity constraint)
3. The total value is maximized

Return the maximum value achievable under these constraints, or -1 if it's impossible to satisfy both weight constraints.

## Examples

### Example 1
**Input:**
```
weight = [2, 3, 4]
value = [4, 5, 6]
W = 6
R = 5
```

**Output:**
```
10
```

**Explanation:** Select items with weights 2 and 3 (total weight = 5, total value = 4 + 5 = 9). Wait, that's 9, not 10. Let me recalculate. Items with weights 3 and 4 would exceed W=6 (total 7). So we can pick items 0 and 1 (weights 2,3 → total 5, values 4,5 → total 9) or just item 2 (weight 4, value 6). Since we need weight ≥ 5, option 1 gives value 9, option 2 gives value 6. So maximum is 9.

Let me check the original: it says output is 10, items 1 and 2. Items 1 and 2 have weights 3 and 4 (total 7 > W=6). That's invalid!

Let me reinterpret: 0-indexed, items 1 and 2 would be the second and third items. That's weights 3+4=7 which exceeds capacity. There must be an error. Let me assume they mean items at indices 0 and 1 which gives us weights 2+3=5 and values 4+5=9.

I'll correct this to 9.

**Corrected Output:**
```
9
```

**Explanation:** Select items at indices 0 and 1 with weights 2 and 3 (total weight = 5, total value = 4 + 5 = 9). This satisfies R ≤ 5 ≤ W.

### Example 2
**Input:**
```
weight = [1, 2, 3]
value = [10, 15, 40]
W = 6
R = 4
```

**Output:**
```
55
```

**Explanation:** Select items with weights 1, 2, and 3 (total weight = 6, total value = 10 + 15 + 40 = 65). Wait that's 65, not 55. Let me check: 10+15+40 = 65. I'll use 65.

**Corrected Output:**
```
65
```

## Constraints
- `1 <= n <= 200`
- `1 <= W <= 5000`
- `1 <= R <= W`
- `1 <= weight[i] <= W`
- `1 <= value[i] <= 10^4`

## Function Signatures

### Java
```java
class Solution {
    public int maxValueKnapsack(int[] weight, int[] value, int W, int R) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def maxValueKnapsack(self, weight: List[int], value: List[int], W: int, R: int) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int maxValueKnapsack(vector<int>& weight, vector<int>& value, int W, int R) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Three space-separated integers: n (number of items), W (capacity), R (required minimum weight)
Line 2: n space-separated integers representing weights
Line 3: n space-separated integers representing values
```

### Sample Input
```
3 6 4
1 2 3
10 15 40
```

## Hints
- Start with standard 0/1 knapsack DP
- Track dp[i][w] = maximum value using first i items with total weight w
- After filling the DP table, only consider states where w >= R and w <= W
- Alternative: use dp[i][w] where w represents weights from R to W
- Return maximum value among all valid weight states

## Related Topics Quiz

### Question 1
How is this problem different from classic 0/1 knapsack?
- A) It allows fractional items
- B) It requires a minimum weight constraint
- C) It has unlimited items
- D) It minimizes weight instead of maximizing value

**Answer:** B) It requires a minimum weight constraint - We must ensure total weight ≥ R.

### Question 2
What is the space complexity if we use 1D DP optimization?
- A) O(1)
- B) O(n)
- C) O(W)
- D) O(W - R)

**Answer:** C) O(W) - We need to track all possible weights up to capacity W.

### Question 3
If no valid solution exists (cannot reach minimum weight R), what should we return?
- A) 0
- B) -1
- C) Maximum value ignoring R
- D) Throw an exception

**Answer:** B) -1 - This indicates impossibility as specified in the problem.

### Question 4
What is the recurrence relation for this problem?
- A) dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
- B) dp[i][w] = dp[i-1][w] + dp[i-1][w-weight[i]]
- C) dp[i][w] = min(dp[i-1][w], dp[i][w-1])
- D) dp[i][w] = dp[i-1][w] * value[i]

**Answer:** A) dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i]) - Standard 0/1 knapsack recurrence; we just filter results by R constraint at the end.
