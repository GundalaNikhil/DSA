# Synchronized Signal LCM

**Difficulty:** Medium
**Topic:** Number Theory, LCM, GCD
**License:** Free to use for commercial purposes

## Problem Statement

Two signal beacons flash at different intervals: one every `a` seconds and another every `b` seconds. If they flash together at time 0, determine the next time (in seconds) they will flash simultaneously (Least Common Multiple).

## Constraints

- `1 <= a, b <= 100000`

## Examples

### Example 1
```
Input: a = 4, b = 6
Output: 12
Explanation:
4: 4, 8, 12, 16...
6: 6, 12, 18...
Match at 12.
```

### Example 2
```
Input: a = 7, b = 5
Output: 35
```

### Example 3
```
Input: a = 15, b = 25
Output: 75
Explanation:
15: 15, 30, 45, 60, 75
25: 25, 50, 75
```

## Function Signature

### Python
```python
def next_sync_time(a: int, b: int) -> int:
    pass
```

### JavaScript
```javascript
function nextSyncTime(a, b) {
    // Your code here
}
```

### Java
```java
public long nextSyncTime(int a, int b) {
    // Your code here
}
```

## Hints
1. LCM(a, b) = (a * b) / GCD(a, b)

## Tags
`number-theory` `lcm` `medium`
