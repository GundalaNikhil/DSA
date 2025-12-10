# Simple String Compression

**Difficulty:** Easy
**Topic:** Strings, Counting
**License:** Free to use for commercial purposes

## Problem Statement

A file compression tool needs a simple compression algorithm. Given a string `text` with consecutive repeating characters, compress it by replacing sequences of the same character with the character followed by the count. If a character appears only once, just keep the character.

Return the compressed string. Only apply compression if it makes the string shorter.

## Constraints

- `1 <= text.length <= 1000`
- `text` contains only lowercase English letters

## Examples

### Example 1
```
Input: text = "aaabbc"
Output: "a3b2c"
Explanation: 'a' appears 3 times, 'b' appears 2 times, 'c' appears 1 time.
```

### Example 2
```
Input: text = "abc"
Output: "abc"
Explanation: No consecutive repeating characters, compression would make it longer.
```

### Example 3
```
Input: text = "aaaaaa"
Output: "a6"
Explanation: 'a' appears 6 times consecutively.
```

### Example 4
```
Input: text = "aabbaabb"
Output: "a2b2a2b2"
Explanation: Multiple groups of repeating characters.
```

## Function Signature

### Python
```python
def compress_string(text: str) -> str:
    pass
```

### JavaScript
```javascript
function compressString(text) {
    // Your code here
}
```

### Java
```java
public String compressString(String text) {
    // Your code here
}
```

## Hints

1. Iterate through string and count consecutive characters
2. Build compressed string as you go
3. Compare lengths and return shorter version
4. Time complexity: O(n), Space complexity: O(n)

## Tags
`string` `counting` `compression` `easy`
