# Crypto Trading Opportunity

**Difficulty:** Medium
**Topic:** Arrays, Dynamic Programming
**License:** Free to use for commercial purposes

## Problem Statement

A cryptocurrency trader has access to historical hourly prices of a coin for one day. The trader can make at most TWO transactions (buy once and sell once per transaction, and must complete the first transaction before starting the second).

Given an array `prices` where `prices[i]` is the price at hour `i`, find the maximum profit possible with at most two buy-sell transactions. You cannot engage in multiple transactions simultaneously (must sell before buying again).

## Constraints

- `1 <= prices.length <= 1000`
- `0 <= prices[i] <= 10000`

## Examples

### Example 1
```
Input: prices = [12, 18, 10, 15, 8, 20]
Output: 18
Explanation:
  Transaction 1: Buy at price 12 (hour 0), sell at price 18 (hour 1), profit = 6
  Transaction 2: Buy at price 8 (hour 4), sell at price 20 (hour 5), profit = 12
  Total profit = 18
```

### Example 2
```
Input: prices = [5, 10, 5, 10]
Output: 10
Explanation:
  Transaction 1: Buy at 5, sell at 10, profit = 5
  Transaction 2: Buy at 5, sell at 10, profit = 5
  Total profit = 10
```

### Example 3
```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Prices only decrease, no profitable transactions possible.
```

### Example 4
```
Input: prices = [1, 5, 3, 8, 2]
Output: 9
Explanation:
  Transaction 1: Buy at 1, sell at 5, profit = 4
  Transaction 2: Buy at 3, sell at 8, profit = 5
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
`array` `dynamic-programming` `stock-trading` `medium`
