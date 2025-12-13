# Problem 10: Early Discount With Stay Window (ARR-010)

**Topic Tags**: `Array`, `Sliding Window`, `Stock Trading`, `Optimization`  
**Difficulty**: Medium  
**Problem ID**: ARRAY-010

---

## Problem Summary

Find maximum profit buying and selling stock with a mandatory hold window [dMin, dMax] and a price ceiling C.

## Real-World Scenario

Imagine you're trading stocks with a special promotion: you must hold any stock for at least `dMin` days and at most `dMax` days. Additionally, there's a price ceiling `C` - even if the stock price exceeds `C`, you can only sell at price `C` (think of it as a capped profit scheme). What's the maximum profit you can make?

---

## Detailed Explanation

### Why is this challenging?

1. **Constraint Window**: You can't sell immediately; you must wait at least `dMin` days
2. **Maximum Hold**: You can't hold forever; you must sell by `dMax` days
3. **Price Ceiling**: Prices above `C` are capped at `C`
4. **Optimization**: Need to find the best buy-sell pair within these constraints

### Key Concepts

- **Buy Day**: Any day you purchase the stock
- **Sell Window**: Days `[buy + dMin, buy + dMax]` are valid sell days
- **Effective Price**: `min(actualPrice, C)` - prices are capped
- **Profit**: `effectiveSellPrice - buyPrice`

---

## Approach 1: Naive Solution

### Idea

Try every possible buy day, then check all valid sell days within the window, computing profit for each combination.

### Why is this inefficient?

```
For each buy day (n days):
    For each valid sell day in window (up to dMax - dMin days):
        Compute profit
```

If window size is large (dMax - dMin), we're doing redundant work!

### Complexity Analysis

**Time Complexity**: O(n × window_size)

- **Why?** For each of n possible buy days, we scan through the valid sell window
- **Detailed breakdown**: If window is W days, we do n × W operations
- **Worst case**: If window = n, this becomes O(n²)

**Space Complexity**: O(1)

- Only tracking maximum profit and current calculations

---

## Approach 2: Optimal Solution ⭐

### Key Insight

For each buy day, we don't need to check every sell day individually - we just need the **maximum price** in the sell window! This can be found in a single pass through the window.

### Algorithm

1. For each potential buy day `i`:
   - Calculate valid sell range: `[i + dMin, min(i + dMax, n-1)]`
   - Find **maximum price** in this range
   - Apply ceiling: `effectiveSellPrice = min(maxPrice, C)`
   - Calculate profit: `effectiveSellPrice - prices[i]`
   - Track global maximum profit
2. Return maximum profit (guaranteed ≥ 0 since we can choose not to trade)

### Optimization Notes

- We scan each window once to find maximum
- For overlapping windows, we could use a sliding window max technique (deque)
- Current implementation is simple and efficient for moderate window sizes

### Complexity Analysis

**Time Complexity**: O(n × window_size)

- **Why?** For each buy position, we scan the sell window once
- **Practical Performance**: Much faster than naive because we only compute max once per window
- **Can be optimized to O(n)** using sliding window maximum with deque

**Space Complexity**: O(1)

- Only using variables for tracking max profit and current window max

---

## Visual Representation

### Example: `prices = [3, 1, 4, 1, 5, 9, 2]`, `dMin = 2`, `dMax = 4`, `C = 6`

```
Day:        0  1  2  3  4  5  6
Price:      3  1  4  1  5  9  2
Ceiling:    C = 6

Buy Day 0 (price=3):
  Valid sell days: [0+2, 0+4] = [2, 4]
  Prices in window: [4, 1, 5]
  Max price: 5
  Effective price: min(5, 6) = 5
  Profit: 5 - 3 = 2 ✓

Buy Day 1 (price=1):
  Valid sell days: [1+2, 1+4] = [3, 5]
  Prices in window: [1, 5, 9]
  Max price: 9
  Effective price: min(9, 6) = 6 (capped!)
  Profit: 6 - 1 = 5 ✓✓ (best!)

Buy Day 2 (price=4):
  Valid sell days: [2+2, 2+4] = [4, 6]
  Prices in window: [5, 9, 2]
  Max price: 9
  Effective price: min(9, 6) = 6
  Profit: 6 - 4 = 2 ✓

Buy Day 3 (price=1):
  Valid sell days: [3+2, 3+4] = [5, 7]
  But day 7 doesn't exist, so [5, 6]
  Prices in window: [9, 2]
  Max price: 9
  Effective price: min(9, 6) = 6
  Profit: 6 - 1 = 5 ✓✓ (tied for best!)

Maximum Profit: 5
```

### Visual Flow Diagram

```
Timeline View:

Day 0 1 2 3 4 5 6
    ├─┼─┼─┼─┼─┼─┤
    3 1 4 1 5 9 2

Buy at day 1 (price=1):
    ↓
    Wait dMin=2 days
    ↓
    Can sell days 3,4,5
    └→ Day 3: price=1, profit=0
    └→ Day 4: price=5, profit=4
    └→ Day 5: price=9→6 (capped), profit=5 ← BEST!
```

---

## Test Case Walkthrough

### Input: `prices = [5, 2, 7, 3, 6, 1, 4]`, `dMin = 1`, `dMax = 3`, `C = 10`

```
Step-by-step Analysis:

Buy Day 0 (price=5):
  Sell window: [1, 3] → prices [2, 7, 3]
  Max in window: 7
  Effective: min(7, 10) = 7
  Profit: 7 - 5 = 2

Buy Day 1 (price=2):
  Sell window: [2, 4] → prices [7, 3, 6]
  Max in window: 7
  Effective: min(7, 10) = 7
  Profit: 7 - 2 = 5 ← Current best

Buy Day 2 (price=7):
  Sell window: [3, 5] → prices [3, 6, 1]
  Max in window: 6
  Effective: min(6, 10) = 6
  Profit: 6 - 7 = -1 (negative, skip)

Buy Day 3 (price=3):
  Sell window: [4, 6] → prices [6, 1, 4]
  Max in window: 6
  Effective: min(6, 10) = 6
  Profit: 6 - 3 = 3

Buy Day 4 (price=6):
  Sell window: [5, 7] → but only day 5,6 exist → [1, 4]
  Max in window: 4
  Effective: min(4, 10) = 4
  Profit: 4 - 6 = -2 (negative)

Buy Day 5 (price=1):
  Sell window: [6, 8] → only day 6 exists → [4]
  Max in window: 4
  Effective: min(4, 10) = 4
  Profit: 4 - 1 = 3

Buy Day 6 (price=4):
  Sell window: [7, 9] → no days exist
  Can't sell, skip

Maximum Profit: 5 (buy day 1, sell day 2)
```

---

## Common Mistakes & Pitfalls

### 1. Forgetting the Price Ceiling ⚠️

- ❌ Using raw price when it exceeds `C`
- ✅ Always apply: `effectivePrice = min(price, C)`
- Example: Price is 100, C is 50 → can only sell at 50

### 2. Window Boundary Errors ⚠️

- ❌ Selling before `dMin` days have passed
- ❌ Selling after `dMax` days
- ✅ Valid range: `[buy + dMin, min(buy + dMax, n-1)]`

### 3. Off-by-One in Window Calculation ⚠️

- ❌ Using `buy + dMax + 1` as end
- ✅ Remember: if buy at day 0, dMax=3, can sell on days 3 (inclusive)

### 4. Not Handling Insufficient Days ⚠️

- ❌ Assuming there are always enough future days
- ✅ Check: if `buy + dMin >= n`, can't sell from this buy

### 5. Returning Negative Profit ⚠️

- ❌ Returning best profit even if negative
- ✅ Return `max(0, bestProfit)` - we can choose not to trade!

### 6. Integer Overflow with Large Prices ⚠️

- ❌ Using `int` when prices can be large
- ✅ Use `long` if needed, though typically int suffices for stock prices

---

## Implementations

### Java

```java
class Solution {
    public int maxProfit(int[] prices, int dMin, int dMax, int C) {
        int n = prices.length;
        int maxProfit = 0;

        for (int buy = 0; buy < n; buy++) {
            int sellStart = buy + dMin;
            int sellEnd = Math.min(buy + dMax, n - 1);

            // Check if we have enough days to sell
            if (sellStart >= n) break;

            // Find maximum price in the sell window
            int maxSellPrice = 0;
            for (int sell = sellStart; sell <= sellEnd; sell++) {
                maxSellPrice = Math.max(maxSellPrice, prices[sell]);
            }

            // Apply price ceiling
            int actualSellPrice = Math.min(maxSellPrice, C);

            // Calculate profit
            int profit = actualSellPrice - prices[buy];
            maxProfit = Math.max(maxProfit, profit);
        }

        return maxProfit;
    }
}
```

### Python

```python
def max_profit(prices, dMin, dMax, C):
    n = len(prices)
    max_profit = 0

    for buy in range(n):
        sell_start = buy + dMin
        sell_end = min(buy + dMax, n - 1)

        # Check if we have enough days to sell
        if sell_start >= n:
            break

        # Find maximum price in the sell window
        max_sell_price = max(prices[sell_start:sell_end + 1])

        # Apply price ceiling
        actual_sell_price = min(max_sell_price, C)

        # Calculate profit
        profit = actual_sell_price - prices[buy]
        max_profit = max(max_profit, profit)

    return max_profit
```

### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int dMin, int dMax, int C) {
        int n = prices.size();
        int maxProfit = 0;

        for (int buy = 0; buy < n; buy++) {
            int sellStart = buy + dMin;
            int sellEnd = min(buy + dMax, n - 1);

            // Check if we have enough days to sell
            if (sellStart >= n) break;

            // Find maximum price in the sell window
            int maxSellPrice = 0;
            for (int sell = sellStart; sell <= sellEnd; sell++) {
                maxSellPrice = max(maxSellPrice, prices[sell]);
            }

            // Apply price ceiling
            int actualSellPrice = min(maxSellPrice, C);

            // Calculate profit
            int profit = actualSellPrice - prices[buy];
            maxProfit = max(maxProfit, profit);
        }

        return maxProfit;
    }
};
```

---

## Quick Comparison Table

| Aspect             | Naive O(n²)           | Optimal O(n×W)           |
| ------------------ | --------------------- | ------------------------ |
| For n=1000, W=10   | ~500,000 ops          | ~10,000 ops              |
| For n=1000, W=100  | ~500,000 ops          | ~100,000 ops             |
| Space              | O(1)                  | O(1)                     |
| Further Optimized? | No                    | Yes (sliding window max) |
| Window Max Finding | Repeated for each buy | Computed once per window |

**Note**: W = window size = dMax - dMin + 1

---

## Quiz Questions

### Q1: If you buy at price 10, the maximum price in the sell window is 20, and C=15, what's the profit?

- A) 10
- B) 5
- C) 15
- D) 20

<details>
<summary>Answer</summary>

**B) 5**

Explanation: Effective sell price = min(20, 15) = 15 (capped by C). Profit = 15 - 10 = 5.

</details>

### Q2: With dMin=2, if you buy on day 0, what's the earliest day you can sell?

- A) Day 0
- B) Day 1
- C) Day 2
- D) Day 3

<details>
<summary>Answer</summary>

**C) Day 2**

Explanation: You must hold for at least dMin=2 days. Buy day 0, can sell starting day 0+2=2.

</details>

### Q3: What's the time complexity of the current optimal solution?

- A) O(n)
- B) O(n log n)
- C) O(n × window_size)
- D) O(n²)

<details>
<summary>Answer</summary>

**C) O(n × window_size)**

Explanation: For each of n buy days, we scan the window to find max price. Window size = dMax - dMin + 1.

</details>

### Q4: If prices = [5, 3, 8], dMin=1, dMax=2, C=100, what's max profit?

- A) 3
- B) 5
- C) 8
- D) 95

<details>
<summary>Answer</summary>

**B) 5**

Explanation:

- Buy day 0 (price=5): sell window [1,2] → max(3,8)=8 → profit=8-5=3
- Buy day 1 (price=3): sell window [2,2] → 8 → profit=8-3=5 ← best
- Buy day 2: no valid sell days
</details>

### Q5: Why do we return max(0, bestProfit) instead of just bestProfit?

- A) To handle negative prices
- B) Because we can choose not to trade
- C) To prevent overflow
- D) It's a coding convention

<details>
<summary>Answer</summary>

**B) Because we can choose not to trade**

Explanation: If all possible trades result in losses, we simply don't trade and profit = 0, not negative.

</details>

---


## Tags

`#arrays` `#sliding-window` `#stock-trading` `#optimization` `#medium`
