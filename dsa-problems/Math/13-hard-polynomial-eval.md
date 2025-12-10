# Polynomial Evaluator

**Difficulty:** Hard
**Topic:** Math, Polynomials, Horner's Method
**License:** Free to use for commercial purposes

## Problem Statement

Given a polynomial represented as an array of coefficients and a value `x`, evaluate the polynomial at `x`.

The polynomial is represented as: `coefficients[0] × x^n + coefficients[1] × x^(n-1) + ... + coefficients[n]`

Where `n` is the degree of the polynomial (length of array - 1).

For example, `[2, -3, 0, 5]` represents: `2x³ - 3x² + 0x + 5`

Return the result of evaluating the polynomial at the given `x` value.

## Constraints

- `1 <= coefficients.length <= 1000`
- `-1000 <= coefficients[i] <= 1000`
- `-100 <= x <= 100`
- Return result as floating-point (may be very large)

## Examples

### Example 1
```
Input: coefficients = [2, -3, 5], x = 2
Output: 7.0
Explanation:
  2x² - 3x + 5 at x=2
  = 2(4) - 3(2) + 5
  = 8 - 6 + 5
  = 7
```

### Example 2
```
Input: coefficients = [1, 0, 0, 0], x = 5
Output: 125.0
Explanation:
  x³ at x=5
  = 5³ = 125
```

### Example 3
```
Input: coefficients = [1, -1], x = 10
Output: 9.0
Explanation:
  x - 1 at x=10
  = 10 - 1
  = 9
```

### Example 4
```
Input: coefficients = [3], x = 7
Output: 3.0
Explanation:
  Constant polynomial = 3
  Result is always 3 regardless of x
```

### Example 5
```
Input: coefficients = [1, 2, 3, 4, 5], x = 2
Output: 57.0
Explanation:
  x⁴ + 2x³ + 3x² + 4x + 5 at x=2
  = 16 + 16 + 12 + 8 + 5
  = 57
```

## Function Signature

### Python
```python
def evaluate_polynomial(coefficients: list[int], x: int) -> float:
    pass
```

### JavaScript
```javascript
function evaluatePolynomial(coefficients, x) {
    // Your code here
}
```

### Java
```java
public double evaluatePolynomial(int[] coefficients, int x) {
    // Your code here
}
```

## Hints

1. **Naive approach**: Calculate each term separately and sum them
   - result = sum(coef[i] × x^(n-i) for i in range(n+1))
   - Time complexity: O(n²) due to repeated exponentiation

2. **Optimal approach - Horner's Method**:
   - Rewrite: ax² + bx + c as ((a × x) + b) × x + c
   - Start from the first coefficient and work forward
   - result = coef[0]; for each next coef: result = result × x + coef
   - Time complexity: O(n), Space complexity: O(1)

3. Horner's method avoids repeated exponentiation
4. Handles large polynomials efficiently

## Tags
`math` `polynomials` `horners-method` `evaluation` `hard`
