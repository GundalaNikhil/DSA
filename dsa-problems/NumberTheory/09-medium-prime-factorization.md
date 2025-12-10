# Chemical Compound Decomposition

**Difficulty:** Medium
**Topic:** Number Theory, Prime Factors
**License:** Free to use for commercial purposes

## Problem Statement

A chemist analyzes a compound with molecular weight `n`. The weight is composed of fundamental atomic weights (prime factors). Decompose `n` into its prime factors.

Return a sorted list of prime factors.

## Constraints

- `2 <= n <= 10^6`

## Examples

### Example 1
```
Input: n = 28
Output: [2, 2, 7]
Explanation: 2 * 2 * 7 = 28.
```

### Example 2
```
Input: n = 13
Output: [13]
```

### Example 3
```
Input: n = 45
Output: [3, 3, 5]
Explanation: 9 * 5 = 45 -> 3 * 3 * 5.
```

## Function Signature

### Python
```python
def decompose_compound(n: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function decomposeCompound(n) {
    // Your code here
}
```

### Java
```java
public List<Integer> decomposeCompound(int n) {
    // Your code here
}
```

## Hints
1. Trial division up to sqrt(n)
2. Divide n by factor as long as divisible

## Tags
`number-theory` `prime-factors` `medium`
