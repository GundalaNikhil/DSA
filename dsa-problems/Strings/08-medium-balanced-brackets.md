# Balanced Bracket Validator

**Difficulty:** Medium
**Topic:** Strings, Stack
**License:** Free to use for commercial purposes

## Problem Statement

A code editor needs to validate bracket matching for syntax highlighting. Given a string `code` containing only bracket characters `()`, `{}`, `[]`, determine if all brackets are properly balanced and correctly nested.

Return `true` if brackets are valid, `false` otherwise.

## Constraints

- `1 <= code.length <= 10000`
- `code` contains only characters: `(`, `)`, `{`, `}`, `[`, `]`

## Examples

### Example 1
```
Input: code = "()"
Output: true
Explanation: Single pair of parentheses is balanced.
```

### Example 2
```
Input: code = "()[]{}"
Output: true
Explanation: All brackets are properly matched.
```

### Example 3
```
Input: code = "(]"
Output: false
Explanation: Mismatched bracket types.
```

### Example 4
```
Input: code = "([{}])"
Output: true
Explanation: Properly nested brackets.
```

### Example 5
```
Input: code = "((("
Output: false
Explanation: Unmatched opening brackets.
```

## Function Signature

### Python
```python
def is_valid_brackets(code: str) -> bool:
    pass
```

### JavaScript
```javascript
function isValidBrackets(code) {
    // Your code here
}
```

### Java
```java
public boolean isValidBrackets(String code) {
    // Your code here
}
```

## Hints

1. Use a stack to track opening brackets
2. Push opening brackets onto stack
3. For closing brackets, check if they match stack top
4. Stack should be empty at the end
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`string` `stack` `brackets` `validation` `medium`
