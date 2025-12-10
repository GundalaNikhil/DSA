# Days Until Warmer Temperature

**Difficulty:** Medium
**Topic:** Stacks, Array
**License:** Free to use for commercial purposes

## Problem Statement

Given an array of daily temperatures, for each day calculate how many days you have to wait until a warmer temperature. If no warmer day exists, use 0.

Return an array where each position shows days to wait.

## Constraints

- `1 <= temperatures.length <= 10000`
- `30 <= temperatures[i] <= 100`

## Examples

### Example 1
```
Input: temps = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation:
- Day 0 (73): warmer on day 1 (74), wait 1 day
- Day 1 (74): warmer on day 2 (75), wait 1 day
- Day 2 (75): warmer on day 6 (76), wait 4 days
- Day 3 (71): warmer on day 5 (72), wait 2 days
- Day 4 (69): warmer on day 5 (72), wait 1 day
- Day 5 (72): warmer on day 6 (76), wait 1 day
- Day 6 (76): no warmer day, 0
- Day 7 (73): no warmer day, 0
```

### Example 2
```
Input: temps = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
Explanation: Each day is warmer than previous, except last
```

### Example 3
```
Input: temps = [90, 80, 70, 60]
Output: [0, 0, 0, 0]
Explanation: No warmer days ahead for any
```

### Example 4
```
Input: temps = [55, 60, 55, 65]
Output: [1, 2, 1, 0]
Explanation:
- Day 0: warmer at day 1
- Day 1: warmer at day 3 (skip day 2 which is cooler)
- Day 2: warmer at day 3
- Day 3: no warmer
```

## Function Signature

### Python
```python
from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    pass
```

### JavaScript
```javascript
function dailyTemperatures(temperatures) {
    // Your code here
}
```

### Java
```java
public int[] dailyTemperatures(int[] temperatures) {
    // Your code here
}
```

## Hints

1. Use stack to store indices of days waiting for warmer temperature
2. Iterate through temperatures
3. While current temp is warmer than temp at stack top index, pop and calculate difference
4. Push current index to stack
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `array` `monotonic-stack` `medium`
