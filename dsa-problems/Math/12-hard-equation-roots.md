# Quadratic Equation Solver

**Difficulty:** Hard
**Topic:** Math, Algebra, Quadratic Equations
**License:** Free to use for commercial purposes

## Problem Statement

Solve a quadratic equation of the form: ax² + bx + c = 0

Given coefficients `a`, `b`, and `c`, find the roots of the equation. Return the roots in ascending order. If there are:
- Two distinct real roots: return `[root1, root2]` where root1 < root2
- One repeated real root: return `[root, root]`
- No real roots (complex roots): return an empty array `[]`

Use the quadratic formula:
x = (-b ± √(b² - 4ac)) / (2a)

## Constraints

- `-1000 <= a, b, c <= 1000`
- `a ≠ 0` (guaranteed to be a quadratic equation)
- Round roots to 2 decimal places

## Examples

### Example 1
```
Input: a = 1, b = -5, c = 6
Output: [2.00, 3.00]
Explanation:
  x² - 5x + 6 = 0
  Discriminant = 25 - 24 = 1
  x = (5 ± 1) / 2 = {3, 2}
  Sorted: [2.00, 3.00]
```

### Example 2
```
Input: a = 1, b = -4, c = 4
Output: [2.00, 2.00]
Explanation:
  x² - 4x + 4 = 0
  (x - 2)² = 0
  Discriminant = 16 - 16 = 0
  One repeated root: x = 2
```

### Example 3
```
Input: a = 1, b = 0, c = 4
Output: []
Explanation:
  x² + 4 = 0
  Discriminant = 0 - 16 = -16 < 0
  No real roots (complex roots: ±2i)
```

### Example 4
```
Input: a = 2, b = -8, c = 6
Output: [1.00, 3.00]
Explanation:
  2x² - 8x + 6 = 0
  x² - 4x + 3 = 0
  Discriminant = 16 - 12 = 4
  x = (4 ± 2) / 2 = {3, 1}
  Sorted: [1.00, 3.00]
```

### Example 5
```
Input: a = 1, b = 2, c = 1
Output: [-1.00, -1.00]
Explanation:
  x² + 2x + 1 = 0
  (x + 1)² = 0
  One repeated root: x = -1
```

## Function Signature

### Python
```python
def solve_quadratic(a: float, b: float, c: float) -> list[float]:
    pass
```

### JavaScript
```javascript
function solveQuadratic(a, b, c) {
    // Your code here
}
```

### Java
```java
public double[] solveQuadratic(double a, double b, double c) {
    // Your code here
}
```

## Hints

1. Calculate discriminant: D = b² - 4ac
2. If D < 0: no real roots, return empty array
3. If D = 0: one repeated root = -b / (2a)
4. If D > 0: two roots using ± in the formula
5. Use square root function for √D
6. Remember to round to 2 decimal places
7. Sort roots in ascending order
8. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `algebra` `quadratic-equations` `discriminant` `hard`
