# Symmetric Drone Flight Path

**Difficulty:** Easy
**Topic:** Strings, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A drone's flight path is encoded as a string of directional codes. A "stable" path is one that is symmetric (reads the same forwards and backwards). Given a `flight_path` string, determine if it is stable.

## Constraints

- `1 <= flight_path.length <= 1000`

## Examples

### Example 1
```
Input: flight_path = "rotator"
Output: true
```

### Example 2
```
Input: flight_path = "xyzyx"
Output: true
```

### Example 3
```
Input: flight_path = "alpha"
Output: false
```

## Function Signature

### Python
```python
def is_stable_path(flight_path: str) -> bool:
    pass
```

### JavaScript
```javascript
function isStablePath(flightPath) {
    // Your code here
}
```

### Java
```java
public boolean isStablePath(String flightPath) {
    // Your code here
}
```

## Hints
1. Two pointers

## Tags
`string` `palindrome` `easy`
