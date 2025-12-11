# Paint Fence With Switch Cost

## Problem Metadata
- **unique_problem_id**: `dp_013`
- **display_id**: `DP-013`
- **slug**: `paint-fence-switch-cost`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Optimization", "State Machine"]`

## Problem Title
Paint Fence With Switch Cost

## Problem Description
You need to paint `n` fence posts using `k` different colors. There are the following rules:

1. No more than two adjacent posts can have the same color
2. Each post costs 1 to paint (regardless of color)
3. Switching colors from post `i-1` to post `i` incurs an additional cost of `s[i]`

Given an array `s` where `s[i]` is the switch cost at position `i`, find the minimum total cost to paint all posts.

## Examples

### Example 1
**Input:**
```
n = 3
k = 2
s = [0, 2, 1]
```

**Output:**
```
4
```

**Explanation:**
- Option 1: Colors A, A, B
  - Post 0: cost 1 (no switch cost)
  - Post 1: cost 1 (same color, no switch)
  - Post 2: cost 1 + 1 = 2 (switch from A to B)
  - Total: 1 + 1 + 2 = 4 ✓

- Option 2: Colors A, B, A
  - Post 0: cost 1
  - Post 1: cost 1 + 2 = 3 (switch)
  - Post 2: cost 1 + 1 = 2 (switch)
  - Total: 1 + 3 + 2 = 6

- Minimum: 4

### Example 2
**Input:**
```
n = 4
k = 3
s = [0, 1, 1, 1]
```

**Output:**
```
6
```

**Explanation:**
- Colors: A, A, B, B
  - Costs: 1 + 1 + (1+1) + 1 = 5
- Wait, that's 5, not 6. Let me recalculate:
  - Post 0: 1 (base)
  - Post 1: 1 (same color A)
  - Post 2: 1 + 1 = 2 (switch to B)
  - Post 3: 1 (same color B)
  - Total: 1 + 1 + 2 + 1 = 5

Let me try: A, A, A... wait, can't have 3 adjacent same colors.
Try: A, A, B, C
- Costs: 1 + 1 + 2 + 2 = 6 ✓

## Constraints
- `1 <= n <= 10^5`
- `1 <= k <= 50`
- `0 <= s[i] <= 10^4`
- `s[0]` is typically 0 (no switch cost for first post)

## Function Signatures

### Java
```java
class Solution {
    public int minPaintCost(int n, int k, int[] s) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def minPaintCost(self, n: int, k: int, s: List[int]) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int minPaintCost(int n, int k, vector<int>& s) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Two space-separated integers: n (number of posts), k (number of colors)
Line 2: n space-separated integers representing switch costs s[]
```

### Sample Input
```
3 2
0 2 1
```

## Hints
- Use DP tracking the state of last two posts
- States: dp[i][same] = cost to paint first i posts where last two have same color
- States: dp[i][diff] = cost to paint first i posts where last two have different colors
- Transitions:
  - Same color: Can only come from diff state (to avoid 3 consecutive)
  - Different color: Can come from both same and diff states, add switch cost
- Base case: First post costs 1, second post can be same (cost 1) or different (cost 1 + s[1])
- Time complexity: O(n)

## Related Topics Quiz

### Question 1
Why can't we have three consecutive posts with the same color?
- A) It's aesthetically unpleasing
- B) It's a constraint of the problem
- C) It causes overflow
- D) We don't have enough colors

**Answer:** B) It's a constraint of the problem - The problem explicitly states this rule.

### Question 2
What is the time complexity of the DP solution?
- A) O(n × k)
- B) O(n)
- C) O(n²)
- D) O(k²)

**Answer:** B) O(n) - We process each post once with constant-time transitions.

### Question 3
What does dp[i][same] represent?
- A) All posts have the same color
- B) Post i and i-1 have the same color
- C) Cost to paint i posts with all same color
- D) Number of same colors used

**Answer:** B) Post i and i-1 have the same color - Tracks the state of consecutive colors.

### Question 4
When do we add the switch cost s[i]?
- A) Always
- B) Only when changing colors
- C) Only for the first post
- D) Never

**Answer:** B) Only when changing colors - Switch cost applies when colors differ.

### Question 5
Can we optimize space complexity?
- A) No, we need O(n) space
- B) Yes, to O(1) by keeping only last two states
- C) Yes, to O(k)
- D) Only if k = 2

**Answer:** B) Yes, to O(1) by keeping only last two states - We only need current and previous states.
