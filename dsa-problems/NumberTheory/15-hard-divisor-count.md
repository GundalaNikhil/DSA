# Divisor Count Calculator

**Difficulty:** Hard
**Topic:** Number Theory, Divisors, Prime Factorization
**License:** Free to use for commercial purposes

## Problem Statement

Given a positive integer `n`, calculate the total number of divisors (factors) of `n`.

For example, divisors of 12 are: 1, 2, 3, 4, 6, 12 → count = 6

## Constraints

- `1 <= n <= 1000000000` (10⁹)

## Examples

### Example 1
```
Input: n = 12
Output: 6
Explanation: Divisors of 12: {1, 2, 3, 4, 6, 12} → 6 divisors
```

### Example 2
```
Input: n = 1
Output: 1
Explanation: Only divisor of 1 is 1 itself.
```

### Example 3
```
Input: n = 7
Output: 2
Explanation: 7 is prime, divisors: {1, 7} → 2 divisors
```

### Example 4
```
Input: n = 100
Output: 9
Explanation: Divisors of 100: {1, 2, 4, 5, 10, 20, 25, 50, 100} → 9 divisors
```

### Example 5
```
Input: n = 36
Output: 9
Explanation:
  36 = 2² × 3²
  Divisors: {1, 2, 3, 4, 6, 9, 12, 18, 36} → 9 divisors
```

### Example 6
```
Input: n = 1000000
Output: 49
Explanation:
  1000000 = 2⁶ × 5⁶
  Number of divisors = (6+1) × (6+1) = 49
```

## Function Signature

### Python
```python
def count_divisors(n: int) -> int:
    pass
```

### JavaScript
```javascript
function countDivisors(n) {
    // Your code here
}
```

### Java
```java
public int countDivisors(int n) {
    // Your code here
}
```

## Hints

1. **Naive approach**: Check all numbers from 1 to n
   - Time: O(n) - too slow for large n

2. **Optimized approach**: Check only up to √n
   - For each divisor d where d ≤ √n:
     - If n % d == 0:
       - Count d as a divisor
       - If d ≠ n/d, also count n/d
   - Time: O(√n)

3. **Most efficient approach**: Use prime factorization
   - If n = p1^k1 × p2^k2 × ... × pm^km
   - Number of divisors = (k1 + 1) × (k2 + 1) × ... × (km + 1)
   - Example: 12 = 2² × 3¹ → divisors = (2+1) × (1+1) = 6

4. **Algorithm**:
   - Find prime factorization
   - For each prime factor with exponent k, multiply result by (k+1)

5. Time complexity: O(√n) for factorization
6. Space complexity: O(1)

## Tags
`number-theory` `divisors` `prime-factorization` `multiplicative-function` `hard`
