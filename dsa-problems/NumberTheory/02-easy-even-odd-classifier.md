# Traffic Light Cycle Counter

**Difficulty:** Easy
**Topic:** Number Theory, Parity
**License:** Free to use for commercial purposes

## Problem Statement

A traffic monitoring system records the duration (in seconds) of green lights at various intersections. The system categorizes durations into "standard" (even seconds) and "extended" (odd seconds).

Given an array of `durations`, count how many are standard (even) and how many are extended (odd).

Return `[standardCount, extendedCount]`.

## Constraints

- `1 <= durations.length <= 10000`
- `1 <= durations[i] <= 1000`

## Examples

### Example 1
```
Input: durations = [30, 45, 60, 90, 15]
Output: [3, 2]
Explanation:
Even (Standard): 30, 60, 90 (3 counts)
Odd (Extended): 45, 15 (2 counts)
```

### Example 2
```
Input: durations = [12, 14, 16]
Output: [3, 0]
```

### Example 3
```
Input: durations = [11, 13, 17]
Output: [0, 3]
```

## Function Signature

### Python
```python
def count_light_cycles(durations: list[int]) -> list[int]:
    pass
```

### JavaScript
```javascript
function countLightCycles(durations) {
    // Your code here
}
```

### Java
```java
public int[] countLightCycles(int[] durations) {
    // Your code here
}
```

## Hints
1. Check n % 2 == 0

## Tags
`number-theory` `parity` `easy`
