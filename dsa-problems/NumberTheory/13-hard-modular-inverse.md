# Decryption Key Recovery

**Difficulty:** Hard
**Topic:** Number Theory, Modular Inverse
**License:** Free to use for commercial purposes

## Problem Statement

To decrypt a message, you need to find a private key `d` such that `(e * d) % phi == 1`.
Given `e` (public exponent) and `phi` (totient), find the modular multiplicative inverse `d`.

If no inverse exists, return -1.

## Constraints

- `1 <= e < phi <= 10^9`

## Examples

### Example 1
```
Input: e = 3, phi = 11
Output: 4
Explanation: (3 * 4) % 11 = 12 % 11 = 1.
```

### Example 2
```
Input: e = 10, phi = 17
Output: 12
Explanation: (10 * 12) % 17 = 120 % 17 = 1.
```

### Example 3
```
Input: e = 4, phi = 6
Output: -1
Explanation: gcd(4, 6) = 2 != 1. No inverse.
```

## Function Signature

### Python
```python
def recover_key(e: int, phi: int) -> int:
    pass
```

### JavaScript
```javascript
function recoverKey(e, phi) {
    // Your code here
}
```

### Java
```java
public int recoverKey(int e, int phi) {
    // Your code here
}
```

## Hints
1. Extended Euclidean Algorithm
2. ax + by = gcd(a, b)

## Tags
`number-theory` `modular-inverse` `hard`
