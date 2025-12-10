# Scientific Notation Precision

**Difficulty:** Easy
**Topic:** Number Theory, Factorials
**License:** Free to use for commercial purposes

## Problem Statement

In a scientific simulation, large numbers are generated using factorials (n!). We need to determine the magnitude of the number by counting how many trailing zeros it has.

Given `n`, calculate the number of trailing zeros in `n!`.

## Constraints

- `0 <= n <= 10000`

## Examples

### Example 1
```
Input: n = 6
Output: 1
Explanation: 6! = 720. One zero.
```

### Example 2
```
Input: n = 12
Output: 2
Explanation: 12! = 479001600. Two zeros.
```

### Example 3
```
Input: n = 30
Output: 7
Explanation: 30/5 = 6. 30/25 = 1. Total 7.
```

## Function Signature

### Python
```python
def count_precision_zeros(n: int) -> int:
    pass
```

### JavaScript
```javascript
function countPrecisionZeros(n) {
    // Your code here
}
```

### Java
```java
public int countPrecisionZeros(int n) {
    // Your code here
}
```

## Hints
1. Count factors of 5 in n!
2. n/5 + n/25 + n/125 ...

## Tags
`number-theory` `factorial` `easy`
