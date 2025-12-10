# Projectile Trajectory Impact

**Difficulty:** Hard
**Topic:** Math, Algebra, Quadratic Equations
**License:** Free to use for commercial purposes

## Problem Statement

The height of a projectile is modeled by `h(t) = at^2 + bt + c`. Find the time points `t` when the projectile hits the ground (`h(t) = 0`).

Return sorted list of real roots rounded to 2 decimals.

## Constraints

- `a != 0`

## Examples

### Example 1
```
Input: a = -4.9, b = 19.6, c = 0
Output: [0.00, 4.00]
Explanation: -4.9t^2 + 19.6t = 0 -> t(-4.9t + 19.6) = 0. t=0 or t=4.
```

### Example 2
```
Input: a = 1, b = 0, c = -4
Output: [-2.00, 2.00]
Explanation: t^2 - 4 = 0 -> t = +/- 2.
```

### Example 3
```
Input: a = 1, b = 0, c = 1
Output: []
Explanation: t^2 + 1 = 0. No real solution.
```

## Function Signature

### Python
```python
def find_impact_times(a: float, b: float, c: float) -> list[float]:
    pass
```

### JavaScript
```javascript
function findImpactTimes(a, b, c) {
    // Your code here
}
```

### Java
```java
public double[] findImpactTimes(double a, double b, double c) {
    // Your code here
}
```

## Hints
1. Quadratic formula
2. Check discriminant

## Tags
`math` `algebra` `hard`
