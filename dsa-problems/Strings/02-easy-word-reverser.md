# Mirror Dimension Message

**Difficulty:** Easy
**Topic:** Strings, Manipulation
**License:** Free to use for commercial purposes

## Problem Statement

A scientist communicating with a mirror dimension realizes that while individual words are correct, their order is reversed. To understand the message, you must reverse the order of words in the string `transmission`.

Return the corrected message.

## Constraints

- `1 <= transmission.length <= 1000`

## Examples

### Example 1
```
Input: transmission = "critical failure system"
Output: "system failure critical"
```

### Example 2
```
Input: transmission = "start sequence launch"
Output: "launch sequence start"
```

### Example 3
```
Input: transmission = "alpha"
Output: "alpha"
```

## Function Signature

### Python
```python
def decode_message(transmission: str) -> str:
    pass
```

### JavaScript
```javascript
function decodeMessage(transmission) {
    // Your code here
}
```

### Java
```java
public String decodeMessage(String transmission) {
    // Your code here
}
```

## Hints
1. Split by space
2. Reverse list
3. Join

## Tags
`string` `reverse` `easy`
