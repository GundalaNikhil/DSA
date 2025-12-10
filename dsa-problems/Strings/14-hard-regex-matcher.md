# Flexible Command Parser

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming, Recursion
**License:** Free to use for commercial purposes

## Problem Statement

A CLI tool supports flexible command matching using wildcards.
- `.` matches any single char.
- `*` matches zero or more of the preceding char.

Given `command` and `pattern`, check if they match.

## Constraints

- `1 <= command.length <= 20`

## Examples

### Example 1
```
Input: command = "run_fast", pattern = "run.*"
Output: true
```

### Example 2
```
Input: command = "init", pattern = "in*t"
Output: true
Explanation: 'n*' matches 'ni'. Wait. 'n*' matches zero or more 'n'.
Input: command = "int", pattern = "in*t" -> true (n* matches n).
Input: command = "it", pattern = "in*t" -> true (n* matches empty).
Input: command = "innnt", pattern = "in*t" -> true.
```

### Example 3
```
Input: command = "start", pattern = "stop"
Output: false
```

## Function Signature

### Python
```python
def is_match(command: str, pattern: str) -> bool:
    pass
```

### JavaScript
```javascript
function isMatch(command, pattern) {
    // Your code here
}
```

### Java
```java
public boolean isMatch(String command, String pattern) {
    // Your code here
}
```

## Hints
1. DP table

## Tags
`string` `regex` `hard`
