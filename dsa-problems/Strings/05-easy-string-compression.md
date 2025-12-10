# Satellite Data Packet Compression

**Difficulty:** Easy
**Topic:** Strings, Counting
**License:** Free to use for commercial purposes

## Problem Statement

A satellite transmits data as a stream of characters. To save bandwidth, consecutive repeating characters are compressed (e.g., "xx" -> "x2"). If the compressed version is not shorter, send the original.

## Constraints

- `1 <= stream.length <= 1000`

## Examples

### Example 1
```
Input: stream = "xxxyyyyyz"
Output: "x3y5z1"
```

### Example 2
```
Input: stream = "signal"
Output: "signal"
Explanation: "s1i1g1n1a1l1" is longer.
```

### Example 3
```
Input: stream = "aabbcc"
Output: "a2b2c2"
```

## Function Signature

### Python
```python
def compress_stream(stream: str) -> str:
    pass
```

### JavaScript
```javascript
function compressStream(stream) {
    // Your code here
}
```

### Java
```java
public String compressStream(String stream) {
    // Your code here
}
```

## Hints
1. Count consecutive chars

## Tags
`string` `compression` `easy`
