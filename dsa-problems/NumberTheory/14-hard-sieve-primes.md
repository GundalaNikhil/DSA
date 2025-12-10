# Prime Number Generator (Sieve of Eratosthenes)

**Difficulty:** Hard
**Topic:** Number Theory, Sieve of Eratosthenes, Prime Generation
**License:** Free to use for commercial purposes

## Problem Statement

Generate all prime numbers less than or equal to a given number `n` using the Sieve of Eratosthenes algorithm.

Return the primes in ascending order.

## Constraints

- `2 <= n <= 10000000` (10⁷)

## Examples

### Example 1
```
Input: n = 10
Output: [2, 3, 5, 7]
Explanation: All primes ≤ 10 are 2, 3, 5, 7.
```

### Example 2
```
Input: n = 20
Output: [2, 3, 5, 7, 11, 13, 17, 19]
Explanation: All primes ≤ 20.
```

### Example 3
```
Input: n = 2
Output: [2]
Explanation: 2 is the smallest prime.
```

### Example 4
```
Input: n = 30
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Explanation: All primes ≤ 30.
```

### Example 5
```
Input: n = 100
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Explanation: There are 25 primes ≤ 100.
```

## Function Signature

### Python
```python
def sieve_of_eratosthenes(n: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function sieveOfEratosthenes(n) {
    // Your code here
}
```

### Java
```java
public List<Integer> sieveOfEratosthenes(int n) {
    // Your code here
}
```

## Hints

1. **Sieve of Eratosthenes Algorithm**:
   - Create a boolean array `is_prime` of size n+1, initialize all to true
   - Set is_prime[0] = is_prime[1] = false
   - For each number p from 2 to √n:
     - If is_prime[p] is true:
       - Mark all multiples of p (p², p²+p, p²+2p, ...) as false
   - Collect all numbers where is_prime[i] = true

2. **Optimization**:
   - Start marking multiples from p² (not 2p)
   - Only iterate p up to √n
   - All composite numbers have a prime factor ≤ √n

3. **Example trace** for n=10:
   - Initial: [F, F, T, T, T, T, T, T, T, T, T]
   - p=2: Mark 4, 6, 8, 10
   - p=3: Mark 6, 9 (6 already marked)
   - p>√10, done
   - Primes: [2, 3, 5, 7]

4. Time complexity: O(n log log n)
5. Space complexity: O(n)

## Tags
`number-theory` `sieve-of-eratosthenes` `prime-generation` `array` `hard`
