# Staircase With Cracked Steps and Max Jump

## Problem Metadata
- **unique_problem_id**: `dp_001`
- **display_id**: `DP-001`
- **slug**: `staircase-cracked-steps-maxjump`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Sliding Window", "Array"]`

## Problem Title
Staircase With Cracked Steps and Max Jump

## Problem Description
A staircase has `n` steps numbered from 0 to n. You start at step 0 and want to reach step `n`. You can climb anywhere from 1 to J steps at a time (where J is given). However, some steps are cracked and cannot be landed on (though you may jump over them).

Count the number of distinct ways to reach step `n` from step 0.

## Examples

### Example 1
**Input:**
```
n = 4
J = 3
cracked = [2]
```

**Output:**
```
3
```

**Explanation:** The valid paths are:
- 0 → 1 → 3 → 4 (skip cracked step 2)
- 0 → 1 → 4 (jump directly over 2 and 3)
- 0 → 3 → 4 (jump over 1 and 2)

### Example 2
**Input:**
```
n = 5
J = 2
cracked = [1, 3]
```

**Output:**
```
2
```

**Explanation:** The valid paths are:
- 0 → 2 → 4 → 5
- 0 → 2 → 5

## Constraints
- `1 <= n <= 10^5`
- `1 <= J <= 50`
- `0 <= cracked.length <= 10^5`
- All cracked steps are unique and within range [1, n-1]

## Function Signatures

### Java
```java
class Solution {
    public int countWaysToClimb(int n, int J, int[] cracked) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def countWaysToClimb(self, n: int, J: int, cracked: List[int]) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int countWaysToClimb(int n, int J, vector<int>& cracked) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Three space-separated integers: n, J, and crackedCount (number of cracked steps)
Line 2: crackedCount space-separated integers representing the cracked step indices
```

### Sample Input
```
4 3 1
2
```

## Hints
- Use dynamic programming with sliding-window sum technique
- Maintain dp array where dp[i] represents number of ways to reach step i
- For each step, sum the ways from the last J non-cracked positions
- Mark cracked steps with dp[i] = 0
- Use a set or boolean array for O(1) cracked step lookup

## Related Topics Quiz

### Question 1
What is the time complexity of the sliding window approach for this problem?
- A) O(n)
- B) O(n * J)
- C) O(n log n)
- D) O(n^2)

**Answer:** A) O(n) - With proper sliding window technique, we can achieve linear time.

### Question 2
If we didn't have cracked steps, what would be the recurrence relation?
- A) dp[i] = dp[i-1] + dp[i-2]
- B) dp[i] = sum(dp[i-j] for j in 1..J)
- C) dp[i] = max(dp[i-1], dp[i-J])
- D) dp[i] = dp[i-1] * J

**Answer:** B) dp[i] = sum(dp[i-j] for j in 1..J) - We sum all reachable previous positions.

### Question 3
Why is a sliding window approach better than recalculating the sum each time?
- A) It uses less memory
- B) It reduces time complexity from O(n*J) to O(n)
- C) It handles cracked steps better
- D) It prevents integer overflow

**Answer:** B) It reduces time complexity from O(n*J) to O(n) - By maintaining a running sum, we avoid redundant calculations.

### Question 4
What should be the base case for this problem?
- A) dp[0] = 0
- B) dp[0] = 1, dp[1] = 1
- C) dp[0] = 1
- D) dp[n] = 1

**Answer:** C) dp[0] = 1 - There is exactly one way to be at the starting position (doing nothing).
