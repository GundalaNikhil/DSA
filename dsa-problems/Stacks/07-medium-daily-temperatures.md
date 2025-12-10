# Next Higher Revenue Day

**Difficulty:** Medium
**Topic:** Stacks, Array
**License:** Free to use for commercial purposes

## Problem Statement

A business analyst wants to analyze daily revenue data. For each day, they want to know how many days they had to wait until a day with strictly higher revenue occurred. If no such future day exists, record 0.

Given an array `revenues`, return an array where each position shows the number of days to wait for a higher revenue.

## Constraints

- `1 <= revenues.length <= 10000`
- `0 <= revenues[i] <= 10000`

## Examples

### Example 1
```
Input: revenues = [100, 120, 110, 130, 100]
Output: [1, 2, 1, 0, 0]
Explanation:
- Day 0 (100): higher on Day 1 (120) -> wait 1 day
- Day 1 (120): higher on Day 3 (130) -> wait 2 days
- Day 2 (110): higher on Day 3 (130) -> wait 1 day
- Day 3 (130): no higher revenue later -> 0
- Day 4 (100): no higher revenue later -> 0
```

### Example 2
```
Input: revenues = [50, 60, 70, 80]
Output: [1, 1, 1, 0]
Explanation: Revenue strictly increases each day.
```

### Example 3
```
Input: revenues = [90, 80, 70]
Output: [0, 0, 0]
Explanation: Revenue strictly decreases, never rebounds.
```

### Example 4
```
Input: revenues = [50, 50, 50]
Output: [0, 0, 0]
Explanation: Revenue stays same, never strictly higher.
```

## Function Signature

### Python
```python
from typing import List

def days_until_higher_revenue(revenues: List[int]) -> List[int]:
    pass
```

### JavaScript
```javascript
function daysUntilHigherRevenue(revenues) {
    // Your code here
}
```

### Java
```java
public int[] daysUntilHigherRevenue(int[] revenues) {
    // Your code here
}
```

## Hints

1. Use stack to store indices of days waiting for higher revenue
2. Iterate through revenues
3. While current revenue is higher than revenue at stack top index, pop and calculate difference
4. Push current index to stack
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `array` `monotonic-stack` `medium`
