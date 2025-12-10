# Signal Processing Filter

**Difficulty:** Hard
**Topic:** Math, Polynomials, Horner's Method
**License:** Free to use for commercial purposes

## Problem Statement

A digital filter's response is modeled by a polynomial where `coeffs` are the filter taps. Calculate the output response for a given input signal value `x`.

Polynomial: `coeffs[0]*x^n + ... + coeffs[n]`

## Constraints

- `1 <= len(coeffs) <= 1000`

## Examples

### Example 1
```
Input: coeffs = [1, 2, 1], x = 3
Output: 16.0
Explanation: x^2 + 2x + 1 at x=3 -> 9 + 6 + 1 = 16.
```

### Example 2
```
Input: coeffs = [5], x = 100
Output: 5.0
```

### Example 3
```
Input: coeffs = [2, 0, 0], x = 4
Output: 32.0
Explanation: 2*x^2 -> 2*16 = 32.
```

## Function Signature

### Python
```python
def filter_response(coeffs: list[int], x: int) -> float:
    pass
```

### JavaScript
```javascript
function filterResponse(coeffs, x) {
    // Your code here
}
```

### Java
```java
public double filterResponse(int[] coeffs, int x) {
    // Your code here
}
```

## Hints
1. Use Horner's method for efficiency

## Tags
`math` `polynomials` `hard`
