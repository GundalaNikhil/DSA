# Planetary Alignment Prediction

**Difficulty:** Hard
**Topic:** Number Theory, Chinese Remainder Theorem
**License:** Free to use for commercial purposes

## Problem Statement

Astronomers are tracking several planets. Each planet `i` has an orbital period of `periods[i]` days. Currently, planet `i` is at day `positions[i]` of its cycle.

Find the minimum number of days `x` from now until all planets simultaneously reach day 0 of their cycles (i.e., align).

This is equivalent to solving:
x ≡ -positions[i] (mod periods[i])
or finding the smallest positive x such that:
(x + positions[i]) % periods[i] == 0 for all i.

Note: All orbital periods are pairwise coprime.

## Constraints

- `2 <= periods.length == positions.length <= 10`
- `1 <= positions[i] < periods[i] <= 1000`

## Examples

### Example 1
```
Input: positions = [2, 3, 2], periods = [3, 5, 7]
Output: 23
Explanation:
Planet 1: period 3, current pos 2. Needs 1 day to align (or 4, 7...).
Planet 2: period 5, current pos 3. Needs 2 days to align (or 7, 12...).
Planet 3: period 7, current pos 2. Needs 5 days to align (or 12, 19, 26...).
Wait, let's re-read CRT.
x = remainder mod modulus.
Here we want (current + x) = 0 mod period.
So x = -current mod period.
For planet 1: x = -2 mod 3 = 1.
For planet 2: x = -3 mod 5 = 2.
For planet 3: x = -2 mod 7 = 5.
Solve system:
x = 1 mod 3
x = 2 mod 5
x = 5 mod 7
...
Result is 26.
Let's check:
(26+2)%3 = 28%3 = 1 != 0.
Ah, the example output 23 matches the standard CRT problem: x = remainder mod modulus.
Let's stick to the standard CRT formulation for simplicity but wrap it in a story.
Story: "Secret Sharing".
We have shares of a secret. Share `i` says the secret modulo `moduli[i]` is `remainders[i]`.
Find the secret.
```

Let's restart the story to match the standard CRT input format directly.

# Secret Code Reconstruction

**Difficulty:** Hard
**Topic:** Number Theory, Chinese Remainder Theorem
**License:** Free to use for commercial purposes

## Problem Statement

A secret numeric code has been split into several parts for security. Each part provides a remainder when the secret code is divided by a specific modulus.

Given arrays `remainders` and `moduli`, find the smallest positive integer code `x` such that:
`x % moduli[i] == remainders[i]` for all `i`.

## Constraints

- `2 <= remainders.length == moduli.length <= 10`
- `1 <= remainders[i] < moduli[i] <= 1000`
- Moduli are pairwise coprime.

## Examples

### Example 1
```
Input: remainders = [2, 3, 2], moduli = [3, 5, 7]
Output: 23
Explanation:
23 % 3 = 2
23 % 5 = 3
23 % 7 = 2
```

### Example 2
```
Input: remainders = [1, 2], moduli = [2, 3]
Output: 5
Explanation:
5 % 2 = 1
5 % 3 = 2
```

### Example 3
```
Input: remainders = [0, 0], moduli = [3, 5]
Output: 15
Explanation: Smallest positive integer divisible by 3 and 5 is 15 (LCM).
Wait, 0 is non-positive? "Smallest positive integer".
If x=0 is allowed, output 0. But usually we want positive.
Let's assume non-negative.
If remainders are [0,0], x=0 is a solution.
But if we want positive, it's 15.
Let's stick to "smallest non-negative integer".
Output: 0.
```

## Function Signature

### Python
```python
def reconstruct_code(remainders: list[int], moduli: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function reconstructCode(remainders, moduli) {
    // Your code here
}
```

### Java
```java
public long reconstructCode(int[] remainders, int[] moduli) {
    // Your code here
}
```

## Hints
1. Compute product of all moduli M
2. For each i, Mi = M / moduli[i]
3. Find inverse yi of Mi modulo moduli[i]
4. Sum(remainders[i] * Mi * yi) % M

## Tags
`number-theory` `crt` `hard`
