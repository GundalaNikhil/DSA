# Chinese Remainder Theorem Solver

**Difficulty:** Hard
**Topic:** Number Theory, Chinese Remainder Theorem
**License:** Free to use for commercial purposes

## Problem Statement

Solve a system of congruences using the Chinese Remainder Theorem. Given arrays `remainders` and `moduli` where:
- x ≡ remainders[0] (mod moduli[0])
- x ≡ remainders[1] (mod moduli[1])
- ...
- x ≡ remainders[n-1] (mod moduli[n-1])

Find the smallest non-negative integer `x` that satisfies all congruences.

**Note**: All moduli are pairwise coprime (gcd of any two moduli is 1).

## Constraints

- `2 <= remainders.length == moduli.length <= 10`
- `1 <= remainders[i] < moduli[i] <= 1000`
- All moduli are pairwise coprime
- Solution exists and fits in 64-bit integer

## Examples

### Example 1
```
Input: remainders = [2, 3, 2], moduli = [3, 5, 7]
Output: 23
Explanation:
  x ≡ 2 (mod 3) → x could be 2, 5, 8, 11, 14, 17, 20, 23, 26...
  x ≡ 3 (mod 5) → x could be 3, 8, 13, 18, 23, 28...
  x ≡ 2 (mod 7) → x could be 2, 9, 16, 23, 30...
  Smallest common: x = 23
```

### Example 2
```
Input: remainders = [1, 2], moduli = [2, 3]
Output: 5
Explanation:
  x ≡ 1 (mod 2) → x is odd: 1, 3, 5, 7, 9...
  x ≡ 2 (mod 3) → x could be 2, 5, 8, 11...
  Smallest common: x = 5
```

### Example 3
```
Input: remainders = [0, 3, 4], moduli = [5, 7, 11]
Output: 235
Explanation:
  x ≡ 0 (mod 5)
  x ≡ 3 (mod 7)
  x ≡ 4 (mod 11)
  Smallest x = 235
```

### Example 4
```
Input: remainders = [1, 1, 1], moduli = [2, 3, 5]
Output: 1
Explanation: x = 1 satisfies all congruences.
```

## Function Signature

### Python
```python
def solve_crt(remainders: list[int], moduli: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function solveCrt(remainders, moduli) {
    // Your code here
}
```

### Java
```java
public long solveCrt(int[] remainders, int[] moduli) {
    // Your code here
}
```

## Hints

1. **Chinese Remainder Theorem Algorithm**:
   - Calculate M = product of all moduli
   - For each i: Mi = M / moduli[i]
   - Find yi such that (Mi × yi) ≡ 1 (mod moduli[i]) using Extended Euclidean Algorithm
   - Solution: x = Σ(remainders[i] × Mi × yi) mod M

2. **Extended Euclidean Algorithm** to find modular inverse:
   - Find y such that (a × y) ≡ 1 (mod m)

3. **Example trace** for remainders=[2,3,2], moduli=[3,5,7]:
   - M = 3 × 5 × 7 = 105
   - M0=35, M1=21, M2=15
   - Find y0: 35×y0 ≡ 1 (mod 3) → y0=2
   - Find y1: 21×y1 ≡ 1 (mod 5) → y1=1
   - Find y2: 15×y2 ≡ 1 (mod 7) → y2=1
   - x = (2×35×2 + 3×21×1 + 2×15×1) mod 105
   - x = (140 + 63 + 30) mod 105 = 233 mod 105 = 23

4. Time complexity: O(n × log(max(moduli)))
5. Space complexity: O(1)

## Tags
`number-theory` `chinese-remainder-theorem` `modular-arithmetic` `extended-euclidean` `hard`
