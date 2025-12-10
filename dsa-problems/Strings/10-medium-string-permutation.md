# String Permutation Detector

**Difficulty:** Medium
**Topic:** Strings, HashMap, Sliding Window
**License:** Free to use for commercial purposes

## Problem Statement

A security system checks if a password permutation exists within a log entry. Given two strings `text` and `pattern`, determine if any permutation of `pattern` exists as a substring in `text`.

Return `true` if any permutation of pattern exists in text, `false` otherwise.

## Constraints

- `1 <= pattern.length <= text.length <= 10000`
- Both strings contain only lowercase English letters

## Examples

### Example 1
```
Input: text = "eidbaooo", pattern = "ab"
Output: true
Explanation: "ba" (permutation of "ab") exists at position 4-5.
```

### Example 2
```
Input: text = "eidboaoo", pattern = "ab"
Output: false
Explanation: No permutation of "ab" exists in text.
```

### Example 3
```
Input: text = "hello", pattern = "ell"
Output: true
Explanation: "ell" itself exists (identity permutation).
```

### Example 4
```
Input: text = "programming", pattern = "gram"
Output: true
Explanation: "gram" exists in "programming".
```

## Function Signature

### Python
```python
def has_permutation_substring(text: str, pattern: str) -> bool:
    pass
```

### JavaScript
```javascript
function hasPermutationSubstring(text, pattern) {
    // Your code here
}
```

### Java
```java
public boolean hasPermutationSubstring(String text, String pattern) {
    // Your code here
}
```

## Hints

1. Use sliding window of size pattern.length
2. Compare character frequencies using hash maps
3. Slide window one character at a time
4. Can optimize by tracking changes incrementally
5. Time complexity: O(n), Space complexity: O(1) - max 26 letters

## Tags
`string` `hashmap` `sliding-window` `permutation` `medium`
