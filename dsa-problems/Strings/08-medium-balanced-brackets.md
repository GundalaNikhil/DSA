# Code Block Validator

**Difficulty:** Medium
**Topic:** Strings, Stack
**License:** Free to use for commercial purposes

## Problem Statement

A syntax highlighter needs to verify that code blocks are properly closed. The code contains three types of grouping symbols: `()`, `[]`, `{}`.

Given a string `code_snippet` containing only these characters, determine if the nesting is valid.

## Constraints

- `1 <= code_snippet.length <= 10000`

## Examples

### Example 1
```
Input: code_snippet = "{[]}"
Output: true
```

### Example 2
```
Input: code_snippet = "([)]"
Output: false
Explanation: Mismatched nesting order.
```

### Example 3
```
Input: code_snippet = "((()))"
Output: true
```

## Function Signature

### Python
```python
def is_valid_syntax(code_snippet: str) -> bool:
    pass
```

### JavaScript
```javascript
function isValidSyntax(codeSnippet) {
    // Your code here
}
```

### Java
```java
public boolean isValidSyntax(String codeSnippet) {
    // Your code here
}
```

## Hints
1. Stack for opening brackets
2. Pop and match for closing

## Tags
`string` `stack` `medium`
