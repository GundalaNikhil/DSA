# Prime Factorization

**Difficulty:** Medium
**Topic:** Number Theory, Prime Factors
**License:** Free to use for commercial purposes

## Problem Statement

Find the prime factorization of a positive integer `n`. Return a list of prime factors in ascending order, including duplicates.

For example:
- 12 = 2 × 2 × 3 → [2, 2, 3]
- 15 = 3 × 5 → [3, 5]
- 7 = 7 → [7] (already prime)

## Constraints

- `2 <= n <= 1000000` (10⁶)

## Examples

### Example 1
```
Input: n = 12
Output: [2, 2, 3]
Explanation: 12 = 2² × 3
```

### Example 2
```
Input: n = 30
Output: [2, 3, 5]
Explanation: 30 = 2 × 3 × 5
```

### Example 3
```
Input: n = 17
Output: [17]
Explanation: 17 is prime.
```

### Example 4
```
Input: n = 100
Output: [2, 2, 5, 5]
Explanation: 100 = 2² × 5²
```

### Example 5
```
Input: n = 2
Output: [2]
Explanation: Smallest prime number.
```

### Example 6
```
Input: n = 999999
Output: [3, 3, 3, 7, 11, 13, 37]
Explanation: 999999 = 3³ × 7 × 11 × 13 × 37
```

## Function Signature

### Python
```python
def prime_factorize(n: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function primeFactorize(n) {
    // Your code here
}
```

### Java
```java
public List<Integer> primeFactorize(int n) {
    // Your code here
}
```

## Hints

1. **Algorithm**:
   - Start with divisor d = 2
   - While d ≤ √n:
     - If n is divisible by d, add d to result and divide n by d
     - If not divisible, move to next potential divisor
   - If n > 1 after loop, n itself is a prime factor

2. **Optimization**:
   - After checking 2, only check odd numbers
   - No need to check if d is prime - composite divisors are eliminated by smaller primes

3. **Example trace** for n = 12:
   - d=2: 12 % 2 = 0 → factors=[2], n=6
   - d=2: 6 % 2 = 0 → factors=[2,2], n=3
   - d=2: 3 % 2 ≠ 0
   - d=3: 3 % 3 = 0 → factors=[2,2,3], n=1
   - Done

4. Time complexity: O(√n)
5. Space complexity: O(log n) for storing factors

## Tags
`number-theory` `prime-factorization` `factors` `division` `medium`
