# Euler's Totient Function

**Difficulty:** Hard
**Topic:** Number Theory, Euler's Totient (Phi Function)
**License:** Free to use for commercial purposes

## Problem Statement

Calculate Euler's totient function φ(n) for a given positive integer `n`.

φ(n) counts the number of integers from 1 to n that are coprime with n (i.e., gcd(k, n) = 1 for 1 ≤ k ≤ n).

## Constraints

- `1 <= n <= 10000000` (10⁷)

## Examples

### Example 1
```
Input: n = 9
Output: 6
Explanation:
  Numbers from 1 to 9: 1, 2, 3, 4, 5, 6, 7, 8, 9
  Coprime with 9: 1, 2, 4, 5, 7, 8 (gcd = 1)
  Count = 6
```

### Example 2
```
Input: n = 10
Output: 4
Explanation:
  Numbers coprime with 10: 1, 3, 7, 9
  Count = 4
```

### Example 3
```
Input: n = 1
Output: 1
Explanation: φ(1) = 1 by definition.
```

### Example 4
```
Input: n = 12
Output: 4
Explanation:
  Numbers coprime with 12: 1, 5, 7, 11
  Count = 4
```

### Example 5
```
Input: n = 17
Output: 16
Explanation:
  17 is prime, so all numbers 1 to 16 are coprime with it.
  φ(prime) = prime - 1
```

## Function Signature

### Python
```python
def euler_totient(n: int) -> int:
    pass
```

### JavaScript
```javascript
function eulerTotient(n) {
    // Your code here
}
```

### Java
```java
public int eulerTotient(int n) {
    // Your code here
}
```

## Hints

1. **Naive approach**: Count numbers from 1 to n where gcd(k, n) = 1
   - Time: O(n × log n) - too slow for large n

2. **Formula approach**: If n = p1^k1 × p2^k2 × ... × pm^km (prime factorization)
   - φ(n) = n × (1 - 1/p1) × (1 - 1/p2) × ... × (1 - 1/pm)
   - Or: φ(n) = n × ∏(1 - 1/pi) for all prime factors pi

3. **Algorithm**:
   - Start with result = n
   - For each prime factor p of n:
     - result = result - result/p (or result = result × (p-1) / p)
   - Find prime factors by trial division up to √n

4. **Properties**:
   - φ(prime) = prime - 1
   - φ(prime^k) = prime^k - prime^(k-1)
   - φ(a × b) = φ(a) × φ(b) if gcd(a,b) = 1

5. Time complexity: O(√n)
6. Space complexity: O(1)

## Tags
`number-theory` `euler-totient` `phi-function` `prime-factors` `hard`
