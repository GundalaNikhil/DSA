# Log File Error Detection

**Difficulty:** Medium
**Topic:** Strings, Sliding Window
**License:** Free to use for commercial purposes

## Problem Statement

A system administrator is scanning a large log file for a specific error code pattern. Given the `log_content` and the `error_code`, count how many times the error code appears.

## Constraints

- `1 <= log_content.length <= 100000`

## Examples

### Example 1
```
Input: log_content = "error_critical_error_warning", error_code = "error"
Output: 2
```

### Example 2
```
Input: log_content = "failfailfail", error_code = "fail"
Output: 3
```

### Example 3
```
Input: log_content = "success", error_code = "fail"
Output: 0
```

## Function Signature

### Python
```python
def count_errors(log_content: str, error_code: str) -> int:
    pass
```

### JavaScript
```javascript
function countErrors(logContent, errorCode) {
    // Your code here
}
```

### Java
```java
public int countErrors(String logContent, String errorCode) {
    // Your code here
}
```

## Hints
1. String search or sliding window

## Tags
`string` `search` `medium`
