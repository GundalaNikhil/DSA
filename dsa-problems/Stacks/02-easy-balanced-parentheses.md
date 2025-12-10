# Check Balanced Parentheses

**Difficulty:** Easy
**Topic:** Stacks, String Validation
**License:** Free to use for commercial purposes

## Problem Statement

Given a string containing only parentheses characters '(', ')', '{', '}', '[' and ']', check if they are balanced.

Balanced means: every opening bracket has a matching closing bracket in correct order.

Return `true` if balanced, `false` otherwise.

## Constraints

- `0 <= string.length <= 5000`
- String contains only bracket characters

## Examples

### Example 1
```
Input: s = "()[]{}"
Output: true
Explanation: All brackets properly closed
```

### Example 2
```
Input: s = "([{}])"
Output: true
Explanation: Nested brackets properly matched
```

### Example 3
```
Input: s = "([)]"
Output: false
Explanation: Brackets interleaved incorrectly
```

### Example 4
```
Input: s = "((("
Output: false
Explanation: Opening brackets never closed
```

## Function Signature

### Python
```python
def is_balanced(s: str) -> bool:
    pass
```

### JavaScript
```javascript
function isBalanced(s) {
    // Your code here
}
```

### Java
```java
public boolean isBalanced(String s) {
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
