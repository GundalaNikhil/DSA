# Decode Encoded String

**Difficulty:** Medium
**Topic:** Stacks, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

Given an encoded string where numbers indicate repetition count and brackets group the content to repeat, decode it.

Format: `number[string]` means repeat the string number times. Can be nested.

For example: "3[a]" becomes "aaa", "2[b3[c]]" becomes "bcccbccc"

Return the decoded string.

## Constraints

- `1 <= string.length <= 500`
- String contains only lowercase letters, digits, and brackets
- All numbers are positive integers
- Input is always valid

## Examples

### Example 1
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Explanation: "a" repeated 3 times + "bc" repeated 2 times
```

### Example 2
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Explanation: "abc"×2 + "cd"×3 + "ef"
```

### Example 3
```
Input: s = "2[a2[b]]"
Output: "abbabb"
Explanation: Inner "b"×2 = "bb", then "abb"×2 = "abbabb"
```

### Example 4
```
Input: s = "10[x]"
Output: "xxxxxxxxxx"
Explanation: "x" repeated 10 times
```

## Function Signature

### Python
```python
def decode_string(s: str) -> str:
    pass
```

### JavaScript
```javascript
function decodeString(s) {
    // Your code here
}
```

### Java
```java
public String decodeString(String s) {
    // Your code here
}
```

## Hints

1. Use two stacks: one for numbers, one for strings
2. When you see '[', push current number and string to stacks
3. When you see ']', pop and repeat the string
4. Build number character by character (may be multi-digit)
5. Time complexity: O(n × k) where k is max repetition, Space complexity: O(n)

## Tags
`stack` `string` `encoding` `recursion` `medium`
