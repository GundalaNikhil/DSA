# Wallpaper Roll Estimator

**Difficulty:** Easy
**Topic:** Math, Division, Ceiling
**License:** Free to use for commercial purposes

## Problem Statement

A decorator needs to cover a rectangular wall with wallpaper. Each roll of wallpaper covers `coveragePerRoll` square meters. Given the `height` and `width` of the wall in meters, calculate the minimum number of rolls required.

Note: You can only buy whole rolls.

## Constraints

- `1 <= height, width <= 1000`
- `1 <= coveragePerRoll <= 500`

## Examples

### Example 1
```
Input: height = 3, width = 5, coveragePerRoll = 5
Output: 3
Explanation: Area = 15 sq meters. Each roll covers 5. 15/5 = 3 rolls.
```

### Example 2
```
Input: height = 4, width = 6, coveragePerRoll = 10
Output: 3
Explanation: Area = 24. 24/10 = 2.4. Must buy 3 rolls.
```

### Example 3
```
Input: height = 10, width = 10, coveragePerRoll = 100
Output: 1
Explanation: Exact coverage.
```

## Function Signature

### Python
```python
def calculate_wallpaper_rolls(height: int, width: int, coveragePerRoll: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateWallpaperRolls(height, width, coveragePerRoll) {
    // Your code here
}
```

### Java
```java
public int calculateWallpaperRolls(int height, int width, int coveragePerRoll) {
    // Your code here
}
```

## Hints
1. Calculate area = height * width
2. Divide area by coverage
3. Use ceiling function to round up

## Tags
`math` `division` `ceiling` `easy`
