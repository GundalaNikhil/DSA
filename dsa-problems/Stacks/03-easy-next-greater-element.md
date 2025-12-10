# Temperature Trend Analysis

**Difficulty:** Easy
**Topic:** Stacks, Array
**License:** Free to use for commercial purposes

## Problem Statement

A weather station records daily temperatures. For each day's temperature, meteorologists want to know the next higher temperature that occurred in the subsequent days. If no higher temperature was recorded in the future days, use -1.

Given an array `temperatures`, return an array where each position contains the next higher temperature.

## Constraints

- `1 <= temperatures.length <= 3000`
- `-100 <= temperatures[i] <= 100`

## Examples

### Example 1
```
Input: temperatures = [40, 70, 30, 90, 20]
Output: [70, 90, 90, -1, -1]
Explanation:
- 40: next higher is 70
- 70: next higher is 90
- 30: next higher is 90
- 90: no higher temperature later
- 20: no higher temperature later
```

### Example 2
```
Input: temperatures = [13, 8, 11, 6, 15]
Output: [15, 11, 15, 15, -1]
Explanation:
- 13: next higher is 15
- 8: next higher is 11
- 11: next higher is 15
- 6: next higher is 15
- 15: no higher temperature later
```

### Example 3
```
Input: temperatures = [5, 4, 3, 2, 1]
Output: [-1, -1, -1, -1, -1]
Explanation: Temperatures are strictly decreasing.
```

### Example 4
```
Input: temperatures = [10, 20, 30, 40, 50]
Output: [20, 30, 40, 50, -1]
Explanation: Each day is warmer than the previous.
```

## Function Signature

### Python
```python
from typing import List

def next_warmer_temperatures(temperatures: List[int]) -> List[int]:
    pass
```

### JavaScript
```javascript
function nextWarmerTemperatures(temperatures) {
    // Your code here
}
```

### Java
```java
public int[] nextWarmerTemperatures(int[] temperatures) {
    // Your code here
}
```

## Hints

1. Use stack to keep track of elements waiting for their next greater
2. Traverse array from right to left
3. For each element, pop from stack while top is smaller
4. Top of stack is the next greater element
5. Push current element to stack
6. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `array` `monotonic-stack` `easy`
