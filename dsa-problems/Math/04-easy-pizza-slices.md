# Pie Share Calculation

**Difficulty:** Easy
**Topic:** Math, Percentages
**License:** Free to use for commercial purposes

## Problem Statement

A bakery sells pies cut into `slicesPerPie`. A customer buys `numberOfPies` but plans to serve only `slicesNeeded`. Calculate what percentage of the total purchased pies will be served.

Return the percentage rounded down to the nearest integer.

## Constraints

- `1 <= numberOfPies <= 50`
- `4 <= slicesPerPie <= 12`
- `1 <= slicesNeeded <= numberOfPies * slicesPerPie`

## Examples

### Example 1
```
Input: numberOfPies = 3, slicesPerPie = 8, slicesNeeded = 12
Output: 50
Explanation: Total slices = 24. Needed 12. 12/24 = 50%.
```

### Example 2
```
Input: numberOfPies = 2, slicesPerPie = 6, slicesNeeded = 4
Output: 33
Explanation: Total 12. Needed 4. 4/12 = 33.33% -> 33%.
```

### Example 3
```
Input: numberOfPies = 1, slicesPerPie = 10, slicesNeeded = 10
Output: 100
```

## Function Signature

### Python
```python
def calculate_pie_percentage(numberOfPies: int, slicesPerPie: int, slicesNeeded: int) -> int:
    pass
```

### JavaScript
```javascript
function calculatePiePercentage(numberOfPies, slicesPerPie, slicesNeeded) {
    // Your code here
}
```

### Java
```java
public int calculatePiePercentage(int numberOfPies, int slicesPerPie, int slicesNeeded) {
    // Your code here
}
```

## Hints
1. Calculate total slices
2. (needed / total) * 100
3. Floor the result

## Tags
`math` `percentage` `easy`
