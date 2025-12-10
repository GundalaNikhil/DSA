# Vintage Toy Collection Flip

**Difficulty:** Medium
**Topic:** Arrays, Dynamic Programming
**License:** Free to use for commercial purposes

## Problem Statement

A vintage toy collector monitors the price of a rare action figure over a series of days. To maintain their reputation as a hobbyist rather than a business, they are limited to at most **two** complete buy-sell cycles during this period. They must sell the figure before buying it again.

Given an array `prices` where `prices[i]` is the price on day `i`, find the maximum profit possible with at most two buy-sell transactions. You cannot engage in multiple transactions simultaneously (must sell before buying again).

## Constraints

- `1 <= prices.length <= 1000`
- `0 <= prices[i] <= 10000`

## Examples

### Example 1
```
Input: prices = [12, 18, 10, 15, 8, 20]
Output: 18
Explanation:
  Cycle 1: Buy at 12 (day 0), sell at 18 (day 1), profit = 6
  Cycle 2: Buy at 8 (day 4), sell at 20 (day 5), profit = 12
  Total profit = 18
```

### Example 2
```
Input: prices = [5, 10, 5, 10]
Output: 10
Explanation:
  Cycle 1: Buy at 5, sell at 10, profit = 5
  Cycle 2: Buy at 5, sell at 10, profit = 5
  Total profit = 10
```

### Example 3
```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Prices only decrease, no profitable flips possible.
```

### Example 4
```
Input: prices = [1, 5, 3, 8, 2]
Output: 9
Explanation:
  Cycle 1: Buy at 1, sell at 5, profit = 4
  Cycle 2: Buy at 3, sell at 8, profit = 5
  Total profit = 9
```

## Function Signature

### Python
```python
def max_profit_two_transactions(prices: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function maxProfitTwoTransactions(prices) {
    // Your code here
}
```

### Java
```java
public int maxProfitTwoTransactions(int[] prices) {
    // Your code here
}
```

## Hints

1. Think about dividing the array into two parts and finding the best transaction in each part
2. For each position, track: best profit from one transaction up to that point, and best profit from one transaction from that point onwards
3. The answer is the maximum sum of profits from both parts
4. Consider using dynamic programming with states for each transaction
5. Time complexity: O(n), Space complexity: O(n) or O(1) with optimization

## Tags
`array` `dynamic-programming` `optimization` `medium`
