# Code Syntax Validator

**Difficulty:** Easy
**Topic:** Stacks, String Validation
**License:** Free to use for commercial purposes

## Problem Statement

A compiler needs to check if the brackets in a code snippet are correctly balanced. The code snippet contains only the characters '(', ')', '{', '}', '[' and ']'.

A snippet is considered valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Return `true` if the snippet is valid, `false` otherwise.

## Constraints

- `0 <= snippet.length <= 5000`
- `snippet` contains only bracket characters

## Examples

### Example 1
```
Input: snippet = "()[]{}"
Output: true
Explanation: All bracket pairs are correctly closed.
```

### Example 2
```
Input: snippet = "([{}])"
Output: true
Explanation: Nested brackets are properly matched.
```

### Example 3
```
Input: snippet = "([)]"
Output: false
Explanation: Brackets are interleaved incorrectly.
```

### Example 4
```
Input: snippet = "((("
Output: false
Explanation: Opening brackets are never closed.
```

## Function Signature

### Python
```python
def is_valid_syntax(snippet: str) -> bool:
    pass
```

### JavaScript
```javascript
function isValidSyntax(snippet) {
    // Your code here
}
```

### Java
```java
public boolean isValidSyntax(String snippet) {
    // Your code here
}
```

## Hints

1. Use stack to track opening brackets
2. When you see opening bracket, push to stack
3. When you see closing bracket, check if it matches top of stack
4. If stack is empty at end, brackets are balanced
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `string` `parentheses` `validation` `easy`
