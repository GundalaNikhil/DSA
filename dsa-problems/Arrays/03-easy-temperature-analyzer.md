# Temperature Range Finder

**Difficulty:** Easy
**Topic:** Arrays, Math
**License:** Free to use for commercial purposes

## Problem Statement

A weather station records hourly temperatures throughout the day. Given an array `temperatures` representing hourly readings in Celsius, find the temperature range (difference between maximum and minimum temperatures) for that day.

Return the temperature range as an integer.

## Constraints

- `1 <= temperatures.length <= 24`
- `-50 <= temperatures[i] <= 50`

## Examples

### Example 1
```
Input: temperatures = [18, 22, 25, 21, 19, 17]
Output: 8
Explanation: Maximum = 25, Minimum = 17, Range = 25 - 17 = 8
```

### Example 2
```
Input: temperatures = [5, 5, 5, 5]
Output: 0
Explanation: All temperatures are the same, so range is 0.
```

### Example 3
```
Input: temperatures = [-5, 0, 3, -2, 8, 12, 7]
Output: 17
Explanation: Maximum = 12, Minimum = -5, Range = 12 - (-5) = 17
```

## Function Signature

### Python
```python
def find_temperature_range(temperatures: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function findTemperatureRange(temperatures) {
    // Your code here
}
```

### Java
```java
public int findTemperatureRange(int[] temperatures) {
    // Your code here
}
```

## Hints

1. Find the maximum value in the array
2. Find the minimum value in the array
3. Subtract minimum from maximum
4. Be careful with negative numbers

## Tags
`array` `min-max` `math` `easy`
