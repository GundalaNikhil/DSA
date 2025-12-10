# Modular Multiplicative Inverse

**Difficulty:** Hard
**Topic:** Number Theory, Modular Inverse, Extended Euclidean Algorithm
**License:** Free to use for commercial purposes

## Problem Statement

Find the modular multiplicative inverse of `a` modulo `m`. The modular inverse of `a` modulo `m` is an integer `x` such that:
(a × x) ≡ 1 (mod m)

The inverse exists if and only if `a` and `m` are coprime (gcd(a, m) = 1).

If the inverse exists, return it. Otherwise, return -1.

## Constraints

- `1 <= a < m <= 1000000000` (10⁹)
- `2 <= m <= 1000000000`

## Examples

### Example 1
```
Input: a = 3, m = 11
Output: 4
Explanation:
  (3 × 4) mod 11 = 12 mod 11 = 1 ✓
  So 4 is the modular inverse of 3 modulo 11.
```

### Example 2
```
Input: a = 10, m = 17
Output: 12
Explanation:
  (10 × 12) mod 17 = 120 mod 17 = 1 ✓
```

### Example 3
```
Input: a = 4, m = 6
Output: -1
Explanation:
  gcd(4, 6) = 2 ≠ 1
  No modular inverse exists.
```

### Example 4
```
Input: a = 5, m = 13
Output: 8
Explanation:
  (5 × 8) mod 13 = 40 mod 13 = 1 ✓
```

### Example 5
```
Input: a = 1, m = 100
Output: 1
Explanation:
  (1 × 1) mod 100 = 1 ✓
  1 is always its own inverse.
```

## Function Signature

### Python
```python
def modular_inverse(a: int, m: int) -> int:
    pass
```

### JavaScript
```javascript
function modularInverse(a, m) {
    // Your code here
}
```

### Java
```java
public int modularInverse(int a, int m) {
    // Your code here
}
```

## Hints

1. **Extended Euclidean Algorithm**:
   - Find integers x and y such that: a×x + m×y = gcd(a, m)
   - If gcd(a, m) = 1, then a×x ≡ 1 (mod m)
   - So x is the modular inverse

2. **Algorithm** (Extended Euclidean):
   ```
   function extgcd(a, b):
       if b == 0:
           return (a, 1, 0)  # gcd, x, y
       gcd, x1, y1 = extgcd(b, a % b)
       x = y1
       y = x1 - (a // b) × y1
       return (gcd, x, y)

   gcd, x, y = extgcd(a, m)
   if gcd != 1:
       return -1
   return (x % m + m) % m  # Ensure positive result
   ```

3. **Alternative** (if m is prime):
   - Use Fermat's Little Theorem: a^(m-1) ≡ 1 (mod m)
   - So a^(m-2) is the inverse of a modulo m
   - Use modular exponentiation

4. Time complexity: O(log min(a, m))
5. Space complexity: O(log min(a, m)) for recursion

## Tags
`number-theory` `modular-inverse` `extended-euclidean` `gcd` `hard`
