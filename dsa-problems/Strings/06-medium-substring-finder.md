# Unique Substring Finder

**Difficulty:** Medium
**Topic:** Strings, Sliding Window
**License:** Free to use for commercial purposes

## Problem Statement

A text editor needs to find the longest substring without repeating characters for auto-completion suggestions. Given a string `text`, find the length of the longest substring that contains all unique characters.

Return the length of the longest substring without repeating characters.

## Constraints

- `1 <= text.length <= 5000`
- `text` contains English letters, digits, spaces, and punctuation

## Examples

### Example 1
```
Input: text = "abcabcbb"
Output: 3
Explanation: The longest substring is "abc" with length 3.
```

### Example 2
```
Input: text = "bbbbb"
Output: 1
Explanation: The longest substring is "b" with length 1.
```

### Example 3
```
Input: text = "pwwkew"
Output: 3
Explanation: The longest substring is "wke" with length 3.
```

### Example 4
```
Input: text = "abcdef"
Output: 6
Explanation: The entire string has all unique characters.
```

## Function Signature

### Python
```python
def longest_unique_substring(text: str) -> int:
    pass
```

### JavaScript
```javascript
function longestUniqueSubstring(text) {
    // Your code here
}
```

### Java
```java
public int longestUniqueSubstring(String text) {
    // Your code here
}
```

## Hints

1. Use sliding window technique with two pointers
2. Use a hash set to track characters in current window
3. Expand window by moving right pointer, shrink when duplicate found
4. Time complexity: O(n), Space complexity: O(min(n, charset size))

## Tags
`string` `sliding-window` `hashset` `medium`
