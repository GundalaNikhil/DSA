# Paint Coverage Calculator

**Difficulty:** Easy
**Topic:** Math, Division, Ceiling
**License:** Free to use for commercial purposes

## Problem Statement

A painter needs to paint rectangular walls. Each paint can covers `coveragePerCan` square meters. Given the dimensions of a wall (length and width in meters), calculate the minimum number of paint cans needed to completely cover the wall.

Note: Partial cans cannot be purchased - you must buy whole cans.

## Constraints

- `1 <= length <= 1000`
- `1 <= width <= 1000`
- `1 <= coveragePerCan <= 500`
- All measurements are in meters

## Examples

### Example 1
```
Input: length = 10, width = 8, coveragePerCan = 25
Output: 4
Explanation: Wall area = 10 × 8 = 80 m². Each can covers 25 m².
Need 80 ÷ 25 = 3.2 cans, must buy 4 cans.
```

### Example 2
```
Input: length = 15, width = 12, coveragePerCan = 30
Output: 6
Explanation: Wall area = 15 × 12 = 180 m². Each can covers 30 m².
Need 180 ÷ 30 = 6 cans exactly.
```

### Example 3
```
Input: length = 7, width = 5, coveragePerCan = 10
Output: 4
Explanation: Wall area = 7 × 5 = 35 m². Each can covers 10 m².
Need 35 ÷ 10 = 3.5 cans, must buy 4 cans.
```

### Example 4
```
Input: length = 3, width = 2, coveragePerCan = 100
Output: 1
Explanation: Wall area = 3 × 2 = 6 m². One can is more than enough.
```

## Function Signature

### Python
```python
def calculate_paint_cans(length: int, width: int, coveragePerCan: int) -> int:
    pass
```

### JavaScript
```javascript
function calculatePaintCans(length, width, coveragePerCan) {
    // Your code here
}
```

### Java
```java
public int calculatePaintCans(int length, int width, int coveragePerCan) {
    // Your code here
}
```

## Hints

1. Calculate the total wall area
2. Divide area by coverage per can
3. Use ceiling function to round up to nearest whole number
4. In Python: `math.ceil()`, JavaScript: `Math.ceil()`, Java: `Math.ceil()`
5. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `division` `ceiling` `area-calculation` `easy`
