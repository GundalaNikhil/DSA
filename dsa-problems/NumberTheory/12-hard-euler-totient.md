# Cryptographic Key Strength

**Difficulty:** Hard
**Topic:** Number Theory, Euler's Totient
**License:** Free to use for commercial purposes

## Problem Statement

In RSA encryption, the strength of a key depends on the properties of a large integer `n`. Specifically, we need to calculate the count of positive integers less than `n` that are relatively prime to `n`.

Calculate Euler's Totient function φ(n).

## Constraints

- `1 <= n <= 10^7`

## Examples

### Example 1
```
Input: n = 9
Output: 6
Explanation: 1, 2, 4, 5, 7, 8 are coprime to 9.
```

### Example 2
```
Input: n = 10
Output: 4
Explanation: 1, 3, 7, 9.
```

### Example 3
```
Input: n = 13
Output: 12
Explanation: 13 is prime. All 1..12 are coprime.
```

## Function Signature

### Python
```python
def calculate_key_strength(n: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateKeyStrength(n) {
    // Your code here
}
```

### Java
```java
public int calculateKeyStrength(int n) {
    // Your code here
}
```

## Hints
1. Formula: n * product(1 - 1/p) for each prime factor p
2. Use trial division to find prime factors

## Tags
`number-theory` `euler-phi` `hard`
