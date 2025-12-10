# Simple Regex Matcher

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming, Recursion
**License:** Free to use for commercial purposes

## Problem Statement

Implement a simple regex matcher that supports two special characters: `.` (matches any single character) and `*` (matches zero or more of the preceding character). Given a string `text` and a pattern `pattern`, determine if the entire text matches the pattern.

Return `true` if text matches pattern, `false` otherwise.

## Constraints

- `1 <= text.length <= 20`
- `1 <= pattern.length <= 20`
- `text` contains only lowercase English letters
- `pattern` contains lowercase English letters, `.`, and `*`
- `*` always appears after a character (never at the start)

## Examples

### Example 1
```
Input: text = "aa", pattern = "a"
Output: false
Explanation: Pattern doesn't match the entire text.
```

### Example 2
```
Input: text = "aa", pattern = "a*"
Output: true
Explanation: '*' means zero or more 'a's, matching "aa".
```

### Example 3
```
Input: text = "ab", pattern = ".*"
Output: true
Explanation: ".*" matches any sequence.
```

### Example 4
```
Input: text = "mississippi", pattern = "mis*is*p*."
Output: false
Explanation: Pattern doesn't match the text.
```

### Example 5
```
Input: text = "aab", pattern = "c*a*b"
Output: true
Explanation: "c*" matches zero c's, "a*" matches "aa", "b" matches "b".
```

## Function Signature

### Python
```python
def is_match(text: str, pattern: str) -> bool:
    pass
```

### JavaScript
```javascript
function isMatch(text, pattern) {
    // Your code here
}
```

### Java
```java
public boolean isMatch(String text, String pattern) {
    // Your code here
}
```

## Hints

1. Use dynamic programming with 2D table dp[i][j]
2. dp[i][j] = does text[0:i] match pattern[0:j]?
3. Handle three cases: character match, dot match, star match
4. Star can match zero or more of preceding character
5. Time complexity: O(n * m), Space complexity: O(n * m)

## Tags
`string` `dynamic-programming` `recursion` `regex` `pattern-matching` `hard`
