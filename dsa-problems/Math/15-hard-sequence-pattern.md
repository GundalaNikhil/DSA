# Recurrence Sequence Calculator

**Difficulty:** Hard
**Topic:** Math, Recurrence Relations, Dynamic Programming
**License:** Free to use for commercial purposes

## Problem Statement

A special sequence is defined by the following recurrence relation:
- F(0) = 1
- F(1) = 1
- F(n) = F(n-1) + 2 × F(n-2) + n

Given an integer `n`, calculate F(n). Since the result can be very large, return the result modulo 10⁹ + 7.

## Constraints

- `0 <= n <= 100000`
- Return result modulo 10⁹ + 7

## Examples

### Example 1
```
Input: n = 0
Output: 1
Explanation: Base case F(0) = 1
```

### Example 2
```
Input: n = 1
Output: 1
Explanation: Base case F(1) = 1
```

### Example 3
```
Input: n = 2
Output: 5
Explanation:
  F(2) = F(1) + 2×F(0) + 2
  = 1 + 2×1 + 2
  = 5
```

### Example 4
```
Input: n = 3
Output: 10
Explanation:
  F(3) = F(2) + 2×F(1) + 3
  = 5 + 2×1 + 3
  = 10
```

### Example 5
```
Input: n = 4
Output: 24
Explanation:
  F(4) = F(3) + 2×F(2) + 4
  = 10 + 10 + 4
  = 24
```

### Example 6
```
Input: n = 10
Output: 1701
Explanation: Computing iteratively through the recurrence relation yields 1701.
```

## Function Signature

### Python
```python
def calculate_sequence(n: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateSequence(n) {
    // Your code here
}
```

### Java
```java
public int calculateSequence(int n) {
    // Your code here
}
```

## Hints

1. **Naive recursive approach**: Will cause stack overflow for large n (exponential time)

2. **Dynamic Programming approach**:
   - Use iteration with two variables to track F(n-1) and F(n-2)
   - Or use an array dp[n+1] to store all values
   - Time: O(n), Space: O(1) or O(n)

3. Apply modulo at each step to prevent integer overflow:
   - result = (result + value) % (10^9 + 7)

4. Base cases: handle n=0 and n=1 separately

5. For n >= 2, iterate and compute using the recurrence relation

## Tags
`math` `recurrence-relations` `dynamic-programming` `modular-arithmetic` `hard`
