# Perfect Square Validator

**Difficulty:** Easy
**Topic:** Number Theory, Perfect Squares
**License:** Free to use for commercial purposes

## Problem Statement

Determine if a given positive integer `n` is a perfect square. A perfect square is a number that can be expressed as the product of an integer with itself.

For example: 1 (1×1), 4 (2×2), 9 (3×3), 16 (4×4), 25 (5×5) are perfect squares.

Return `true` if `n` is a perfect square, `false` otherwise.

## Constraints

- `1 <= n <= 1000000`

## Examples

### Example 1
```
Input: n = 16
Output: true
Explanation: 16 = 4 × 4
```

### Example 2
```
Input: n = 14
Output: false
Explanation: No integer squared equals 14.
```

### Example 3
```
Input: n = 1
Output: true
Explanation: 1 = 1 × 1
```

### Example 4
```
Input: n = 100
Output: true
Explanation: 100 = 10 × 10
```

### Example 5
```
Input: n = 99
Output: false
Explanation: √99 ≈ 9.95, not a perfect square.
```

## Function Signature

### Python
```python
def is_perfect_square(n: int) -> bool:
    pass
```

### JavaScript
```javascript
function isPerfectSquare(n) {
    // Your code here
}
```

### Java
```java
public boolean isPerfectSquare(int n) {
    // Your code here
}
```

## Hints

1. **Method 1**: Calculate square root and check if it's an integer
   - sqrt_n = √n
   - Check if sqrt_n × sqrt_n == n
   - Or check if sqrt_n is a whole number

2. **Method 2**: Binary search for the square root
   - Search for an integer i where i² = n
   - Range: 1 to n

3. **Method 3**: Iterate from 1 upward
   - Check if i² == n for increasing i
   - Stop when i² > n

4. Be careful with floating-point precision when using square root
5. Time complexity: O(1) for sqrt method, O(log n) for binary search, O(√n) for iteration

## Tags
`number-theory` `perfect-square` `square-root` `easy`
