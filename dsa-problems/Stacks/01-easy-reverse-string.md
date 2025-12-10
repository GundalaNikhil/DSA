# Reverse String Using Stack

**Difficulty:** Easy
**Topic:** Stacks, String Manipulation
**License:** Free to use for commercial purposes

## Problem Statement

Given a string, reverse it using a stack data structure. Push all characters onto the stack, then pop them to get the reversed string.

Return the reversed string.

## Constraints

- `1 <= string.length <= 1000`
- String contains only English letters and spaces

## Examples

### Example 1
```
Input: s = "hello"
Output: "olleh"
Explanation: Push h,e,l,l,o then pop to get o,l,l,e,h
```

### Example 2
```
Input: s = "data structure"
Output: "erutcurts atad"
Explanation: Spaces are also reversed
```

### Example 3
```
Input: s = "a"
Output: "a"
Explanation: Single character unchanged
```

### Example 4
```
Input: s = "coding challenge"
Output: "egnellahc gnidoc"
```

## Function Signature

### Python
```python
def reverse_with_stack(s: str) -> str:
    pass
```

### JavaScript
```javascript
function reverseWithStack(s) {
    // Your code here
}
```

### Java
```java
public String reverseWithStack(String s) {
    // Your code here
}
```

## Hints

1. Create an empty stack
2. Push each character of string onto stack
3. Pop all characters and build result string
4. Stack follows LIFO (Last In First Out)
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `string` `reverse` `easy`
