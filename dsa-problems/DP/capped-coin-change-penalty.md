# Capped Coin Change With Penalty

## Problem Metadata
- **unique_problem_id**: `dp_002`
- **display_id**: `DP-002`
- **slug**: `capped-coin-change-penalty`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Coin Change", "Optimization"]`

## Problem Title
Capped Coin Change With Penalty

## Problem Description
You are given `k` coin denominations. Each denomination `d[i]` can be used at most `c[i]` times. Additionally, if you use more than `floor(c[i]/2)` coins of type `i`, you incur a penalty of `p[i]`.

Your goal is to make exactly the target amount using the minimum total of (number of coins used + total penalties incurred). If it's impossible to form the target, return -1.

## Examples

### Example 1
**Input:**
```
d = [1, 5]
c = [4, 2]
p = [2, 1]
target = 7
```

**Output:**
```
4
```

**Explanation:** Use 2 coins of denomination 5 and 2 coins of denomination 1: 5+5+1+1 = 12, wait that's wrong. Let me recalculate: 5+1+1 = 7 using 3 coins. But 5+5 = 10 (too much). Best is 1+1+5 = 7 using 3 coins, no penalty since we use 2 ones (≤ floor(4/2)=2) and 1 five (≤ floor(2/2)=1). Total = 3 coins + 0 penalty = 3. Actually, the example says 4... Let me reconsider.

Actually rereading: 5+5+1+1 would be 12, not 7. Let's use 5+1+1 = 7 with 3 coins. We use 2 ones (equals floor(4/2)=2, no penalty) and 1 five (≤ floor(2/2)=1, no penalty). Total cost = 3.

But the expected output is 4. Let me try another combination: Use 7 ones? That would be 7 coins, and using more than floor(4/2)=2 ones would incur penalty 2. So 7 coins + 2 penalty = 9. That's worse.

Let's go with 1×5 + 2×1 = 7, using 3 coins total with no penalties, so answer should be 3. I'll adjust the example.

**Corrected Output:**
```
3
```

**Explanation:** Use 1 coin of value 5 and 2 coins of value 1 to get 7. Total coins = 3. Since we use ≤ floor(4/2)=2 ones and ≤ floor(2/2)=1 fives, no penalties are incurred. Total cost = 3 + 0 = 3.

### Example 2
**Input:**
```
d = [2, 3]
c = [3, 2]
p = [1, 1]
target = 8
```

**Output:**
```
4
```

**Explanation:** Use 1 coin of value 3 and 2 coins of value 2 plus 1 more coin of value 3... wait, that doesn't work. Let me try: 2+2+2 = 6 (not 8), 3+3+2 = 8 (3 coins). We use 3 threes? No, c[1]=2 so max 2 threes. So 3+3+2 = 8 using 1 two and 2 threes. That's 3 coins. floor(3/2)=1 for twos, we use 1 (no penalty). floor(2/2)=1 for threes, we use 2 (penalty of 1). Total = 3 + 1 = 4.

## Constraints
- `1 <= k <= 50` (number of coin types)
- `1 <= target <= 5000`
- `1 <= d[i] <= target` (coin denominations)
- `1 <= c[i] <= 100` (max count for each coin)
- `0 <= p[i] <= 100` (penalty for each coin type)

## Function Signatures

### Java
```java
class Solution {
    public int minCoinsWithPenalty(int[] d, int[] c, int[] p, int target) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def minCoinsWithPenalty(self, d: List[int], c: List[int], p: List[int], target: int) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int minCoinsWithPenalty(vector<int>& d, vector<int>& c, vector<int>& p, int target) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Two space-separated integers: k (number of coin types), target
Line 2: k space-separated integers representing denominations d[]
Line 3: k space-separated integers representing max counts c[]
Line 4: k space-separated integers representing penalties p[]
```

### Sample Input
```
2 8
2 3
3 2
1 1
```

## Hints
- Use 2D DP tracking (amount, coin usage state)
- For each coin type, track how many times it's been used
- Calculate penalties dynamically based on usage counts
- Consider state as (amount formed, coins used, penalties incurred)
- Optimize by only tracking necessary states

## Related Topics Quiz

### Question 1
What makes this problem different from standard coin change?
- A) Multiple denominations
- B) Caps on coin usage and penalties
- C) Finding minimum coins
- D) Exact target required

**Answer:** B) Caps on coin usage and penalties - Standard coin change has unlimited coins and no penalties.

### Question 2
What is the time complexity of the DP solution?
- A) O(k * target)
- B) O(k * target * max(c[i]))
- C) O(target^2)
- D) O(k^2 * target)

**Answer:** B) O(k * target * max(c[i])) - We need to track amount, coin type, and usage count.

### Question 3
When should we incur a penalty for coin type i?
- A) When we use any coins of that type
- B) When we use more than c[i] coins
- C) When we use more than floor(c[i]/2) coins
- D) When we use exactly c[i] coins

**Answer:** C) When we use more than floor(c[i]/2) coins - The penalty threshold is more than half the cap.

### Question 4
What should we return if the target cannot be formed?
- A) 0
- B) -1
- C) Integer.MAX_VALUE
- D) The closest achievable value

**Answer:** B) -1 - This indicates impossibility as per the problem statement.
