# Palindrome Checker

**Difficulty:** Easy
**Topic:** Strings, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A word game app needs to identify palindrome words. A palindrome is a word that reads the same forward and backward. Given a string `word` containing only lowercase letters, determine if it is a palindrome.

Return `true` if the word is a palindrome, `false` otherwise.

## Constraints

- `1 <= word.length <= 1000`
- `word` contains only lowercase English letters

## Examples

### Example 1
```
Input: word = "racecar"
Output: true
Explanation: "racecar" reads the same forward and backward.
```

### Example 2
```
Input: word = "hello"
Output: false
Explanation: "hello" backward is "olleh", which is different.
```

### Example 3
```
Input: word = "a"
Output: true
Explanation: Single character is always a palindrome.
```

### Example 4
```
Input: word = "noon"
Output: true
Explanation: "noon" is a palindrome.
```

## Function Signature

### Python
```python
def is_palindrome(word: str) -> bool:
    pass
```

### JavaScript
```javascript
function isPalindrome(word) {
    // Your code here
}
```

### Java
```java
public boolean isPalindrome(String word) {
    // Your code here
}
```

## Hints

1. Use two pointers approach - one from start, one from end
2. Compare characters moving towards center
3. Can also reverse and compare with original
4. Time complexity: O(n), Space complexity: O(1)

## Tags
`string` `two-pointers` `palindrome` `easy`
