# Bakery Inventory Counter

**Difficulty:** Easy
**Topic:** Arrays, Counting
**License:** Free to use for commercial purposes

## Problem Statement

A bakery tracks daily pastry sales in an array where each number represents the quantity of a specific pastry type sold. The owner wants to know how many pastry types sold more than a target quantity on a given day.

Given an array `sales` and an integer `target`, return the count of pastry types that sold more than the `target` quantity.

## Constraints

- `1 <= sales.length <= 500`
- `0 <= sales[i] <= 1000`
- `0 <= target <= 1000`

## Examples

### Example 1
```
Input: sales = [45, 23, 67, 12, 89, 34], target = 30
Output: 3
Explanation: Three pastry types (45, 67, 89) sold more than 30 units.
```

### Example 2
```
Input: sales = [15, 8, 22, 9], target = 20
Output: 1
Explanation: Only one pastry type (22) sold more than 20 units.
```

### Example 3
```
Input: sales = [100, 200, 150], target = 99
Output: 3
Explanation: All three pastry types exceeded the target of 99 units.
```

## Function Signature

### Python
```python
def count_high_sellers(sales: list[int], target: int) -> int:
    pass
```

### JavaScript
```javascript
function countHighSellers(sales, target) {
    // Your code here
}
```

### Java
```java
public int countHighSellers(int[] sales, int target) {
    // Your code here
}
```

## Hints

1. You need to iterate through the array once
2. Keep a counter for elements greater than target
3. Time complexity should be O(n)

## Tags
`array` `iteration` `counting` `easy`
