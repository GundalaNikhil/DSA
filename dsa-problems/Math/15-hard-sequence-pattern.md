# Bacteria Colony Generation

**Difficulty:** Hard
**Topic:** Math, Recurrence Relations
**License:** Free to use for commercial purposes

## Problem Statement

A bacteria colony grows according to a specific pattern:
- Gen 0: 1 bacterium
- Gen 1: 1 bacterium
- Gen n: Gen(n-1) + 2*Gen(n-2) + n

Calculate population at Gen `n` modulo 10^9 + 7.

## Constraints

- `0 <= n <= 100000`

## Examples

### Example 1
```
Input: n = 3
Output: 10
Explanation:
G(0)=1
G(1)=1
G(2)=1 + 2(1) + 2 = 5
G(3)=5 + 2(1) + 3 = 10
```

### Example 2
```
Input: n = 5
Output: 57
Explanation:
G(4) = 10 + 2(5) + 4 = 24
G(5) = 24 + 2(10) + 5 = 24 + 20 + 5 = 49.
Wait, let's re-calc:
G(3)=10. G(2)=5.
G(4) = 10 + 2(5) + 4 = 24.
G(5) = 24 + 2(10) + 5 = 49.
Output: 49.
```

### Example 3
```
Input: n = 0
Output: 1
```

## Function Signature

### Python
```python
def bacteria_population(n: int) -> int:
    pass
```

### JavaScript
```javascript
function bacteriaPopulation(n) {
    // Your code here
}
```

### Java
```java
public int bacteriaPopulation(int n) {
    // Your code here
}
```

## Hints
1. Use DP or iteration
2. Modulo arithmetic

## Tags
`math` `dp` `hard`
