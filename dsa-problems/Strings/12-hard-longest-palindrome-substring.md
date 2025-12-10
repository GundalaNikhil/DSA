# Longest Palindromic Substring

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming
**License:** Free to use for commercial purposes

## Problem Statement

A text analysis tool needs to find the longest palindromic substring for literary analysis. Given a string `text`, find the longest substring that is a palindrome. If multiple palindromes have the same maximum length, return the first one found.

Return the longest palindromic substring.

## Constraints

- `1 <= text.length <= 1000`
- `text` contains only lowercase English letters

## Examples

### Example 1
```
Input: text = "babad"
Output: "bab"
Explanation: "bab" is a palindrome. "aba" is also valid but "bab" appears first.
```

### Example 2
```
Input: text = "cbbd"
Output: "bb"
Explanation: "bb" is the longest palindrome.
```

### Example 3
```
Input: text = "a"
Output: "a"
Explanation: Single character is always a palindrome.
```

### Example 4
```
Input: text = "racecar"
Output: "racecar"
Explanation: The entire string is a palindrome.
```

## Function Signature

### Python
```python
def longest_palindrome(text: str) -> str:
    pass
```

### JavaScript
```javascript
function longestPalindrome(text) {
    // Your code here
}
```

### Java
```java
public String longestPalindrome(String text) {
    // Your code here
}
```

## Hints

1. Expand around center approach: try each position as potential center
2. Handle both odd-length (single center) and even-length (two centers) palindromes
3. Alternative: dynamic programming with 2D table
4. Alternative: Manacher's algorithm for O(n) time
5. Expand around center: Time O(n²), Space O(1)

## Tags
`string` `palindrome` `dynamic-programming` `expand-center` `hard`
