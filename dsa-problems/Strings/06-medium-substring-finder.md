# Unique Signal Frequency Band

**Difficulty:** Medium
**Topic:** Strings, Sliding Window
**License:** Free to use for commercial purposes

## Problem Statement

A radio receiver scans a frequency band represented by a string `signal`. To find the clearest transmission channel, it needs to identify the longest continuous segment of the signal where no frequency character repeats.

Return the length of this longest unique segment.

## Constraints

- `1 <= signal.length <= 5000`

## Examples

### Example 1
```
Input: signal = "bandwidth"
Output: 9
Explanation: "bandwidth" has all unique characters.
```

### Example 2
```
Input: signal = "communication"
Output: 6
Explanation: "unicat" is a valid unique substring.
```

### Example 3
```
Input: signal = "lossless"
Output: 3
Explanation: "los", "sle", "les". Max 3.
```

## Function Signature

### Python
```python
def find_clear_channel(signal: str) -> int:
    pass
```

### JavaScript
```javascript
function findClearChannel(signal) {
    // Your code here
}
```

### Java
```java
public int findClearChannel(String signal) {
    // Your code here
}
```

## Hints
1. Sliding window
2. Set for uniqueness

## Tags
`string` `sliding-window` `medium`
