# Modular Exponentiation

**Difficulty:** Medium
**Topic:** Number Theory, Modular Arithmetic, Fast Exponentiation
**License:** Free to use for commercial purposes

## Problem Statement

Calculate (base^exponent) % modulo efficiently. The result can be very large, so return it modulo `modulo`.

Given three integers `base`, `exponent`, and `modulo`, compute:
result = (base ^ exponent) mod modulo

## Constraints

- `1 <= base <= 10^9`
- `0 <= exponent <= 10^9`
- `1 <= modulo <= 10^9`

## Examples

### Example 1
```
Input: base = 2, exponent = 10, modulo = 1000
Output: 24
Explanation: 2^10 = 1024, 1024 % 1000 = 24
```

### Example 2
```
Input: base = 5, exponent = 3, modulo = 13
Output: 8
Explanation: 5^3 = 125, 125 % 13 = 8
```

### Example 3
```
Input: base = 7, exponent = 0, modulo = 100
Output: 1
Explanation: Any number^0 = 1, 1 % 100 = 1
```

### Example 4
```
Input: base = 3, exponent = 5, modulo = 7
Output: 5
Explanation: 3^5 = 243, 243 % 7 = 5
```

### Example 5
```
Input: base = 2, exponent = 1000000000, modulo = 1000000007
Output: 140625001
Explanation: Calculate 2^(10^9) mod (10^9+7) efficiently.
```

## Function Signature

### Python
```python
def modular_exponentiation(base: int, exponent: int, modulo: int) -> int:
    pass
```

### JavaScript
```javascript
function modularExponentiation(base, exponent, modulo) {
    // Your code here
}
```

### Java
```java
public int modularExponentiation(int base, int exponent, int modulo) {
    // Your code here
}
```

## Hints

1. **Naive approach**: Compute base^exponent then mod
   - Fails for large exponent (number too large, timeout)

2. **Binary Exponentiation (Fast Power)**:
   - Use property: (a × b) mod m = ((a mod m) × (b mod m)) mod m
   - If exponent is even: base^exp = (base^(exp/2))²
   - If exponent is odd: base^exp = base × base^(exp-1)

3. **Algorithm**:
   ```
   result = 1
   base = base % modulo
   while exponent > 0:
       if exponent is odd:
           result = (result × base) % modulo
       exponent = exponent // 2
       base = (base × base) % modulo
   return result
   ```

4. Time complexity: O(log exponent)
5. Space complexity: O(1) for iterative, O(log exponent) for recursive

## Tags
`number-theory` `modular-arithmetic` `exponentiation` `binary-exponentiation` `medium`
