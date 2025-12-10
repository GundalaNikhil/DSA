# Pizza Slice Calculator

**Difficulty:** Easy
**Topic:** Math, Percentages
**License:** Free to use for commercial purposes

## Problem Statement

A pizza restaurant cuts each pizza into `slicesPerPizza` equal slices. A customer orders `numberOfPizzas` pizzas but only wants to eat `desiredSlices` slices. Calculate what percentage of the total order they will consume.

Return the percentage rounded down to the nearest integer.

## Constraints

- `1 <= numberOfPizzas <= 100`
- `4 <= slicesPerPizza <= 16` (typical pizza slice counts)
- `1 <= desiredSlices <= numberOfPizzas × slicesPerPizza`

## Examples

### Example 1
```
Input: numberOfPizzas = 2, slicesPerPizza = 8, desiredSlices = 10
Output: 62
Explanation: Total slices = 2 × 8 = 16. Eating 10 out of 16 = (10/16) × 100 = 62.5%, rounded down to 62%.
```

### Example 2
```
Input: numberOfPizzas = 3, slicesPerPizza = 6, desiredSlices = 9
Output: 50
Explanation: Total slices = 3 × 6 = 18. Eating 9 out of 18 = (9/18) × 100 = 50%.
```

### Example 3
```
Input: numberOfPizzas = 1, slicesPerPizza = 8, desiredSlices = 8
Output: 100
Explanation: Eating all slices = 100%.
```

### Example 4
```
Input: numberOfPizzas = 5, slicesPerPizza = 12, desiredSlices = 20
Output: 33
Explanation: Total slices = 5 × 12 = 60. Eating 20 out of 60 = (20/60) × 100 = 33.333%, rounded down to 33%.
```

## Function Signature

### Python
```python
def calculate_pizza_percentage(numberOfPizzas: int, slicesPerPizza: int, desiredSlices: int) -> int:
    pass
```

### JavaScript
```javascript
function calculatePizzaPercentage(numberOfPizzas, slicesPerPizza, desiredSlices) {
    // Your code here
}
```

### Java
```java
public int calculatePizzaPercentage(int numberOfPizzas, int slicesPerPizza, int desiredSlices) {
    // Your code here
}
```

## Hints

1. Calculate total slices available
2. Calculate percentage: (desiredSlices / totalSlices) × 100
3. Use integer division or floor function to round down
4. Be careful with integer vs floating-point division
5. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `percentage` `division` `rounding` `easy`
