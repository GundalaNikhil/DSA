# Recursive Pattern Expansion

**Difficulty:** Medium
**Topic:** Stacks, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

A compression algorithm represents patterns in a string using a specific format: `k{pattern}`, where `pattern` is repeated `k` times. The `pattern` itself can contain other nested compressed patterns.

Given an encoded string, expand it to its full form.

Format: `k{substring}` means repeat `substring` `k` times. `k` is always a positive integer.

## Constraints

- `1 <= string.length <= 500`
- String contains only uppercase English letters, digits, and curly braces `{}`
- Input format is always valid

## Examples

### Example 1
```
Input: s = "3{A}2{BC}"
Output: "AAABCBC"
Explanation: "A" repeated 3 times + "BC" repeated 2 times.
```

### Example 2
```
Input: s = "2{A3{B}}"
Output: "ABBBABBB"
Explanation: Inner "3{B}" becomes "BBB". Outer "2{ABBB}" becomes "ABBBABBB".
```

### Example 3
```
Input: s = "10{Z}"
Output: "ZZZZZZZZZZ"
Explanation: "Z" repeated 10 times.
```

### Example 4
```
Input: s = "2{XY}3{Z}W"
Output: "XYXYZZZW"
```

## Function Signature

### Python
```python
def expand_pattern(s: str) -> str:
    pass
```

### JavaScript
```javascript
function expandPattern(s) {
    // Your code here
}
```

### Java
```java
public String expandPattern(String s) {
    // Your code here
}
```

## Hints

1. Use two stacks: one for repetition counts, one for partial strings
2. When you see '{', push current count and string to stacks
3. When you see '}', pop and repeat the string
4. Build number character by character (may be multi-digit)
5. Time complexity: O(output length), Space complexity: O(depth of nesting)

## Tags
`stack` `string` `encoding` `recursion` `medium`
