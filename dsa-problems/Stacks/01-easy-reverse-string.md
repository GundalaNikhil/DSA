# Undo Text Editor

**Difficulty:** Easy
**Topic:** Stacks, String Manipulation
**License:** Free to use for commercial purposes

## Problem Statement

A text editor needs to implement an "undo" feature that reverses the sequence of typed characters. Given a string `typed_text`, simulate the reversal process using a stack to show the text in reverse order.

Return the reversed string.

## Constraints

- `1 <= typed_text.length <= 1000`
- `typed_text` contains only English letters and spaces

## Examples

### Example 1
```
Input: typed_text = "hello"
Output: "olleh"
Explanation: Pushing h,e,l,l,o to stack and popping gives o,l,l,e,h.
```

### Example 2
```
Input: typed_text = "data structure"
Output: "erutcurts atad"
Explanation: Spaces are treated as characters and reversed too.
```

### Example 3
```
Input: typed_text = "a"
Output: "a"
Explanation: Single character remains the same.
```

### Example 4
```
Input: typed_text = "coding challenge"
Output: "egnellahc gnidoc"
```

## Function Signature

### Python
```python
def reverse_editor_text(typed_text: str) -> str:
    pass
```

### JavaScript
```javascript
function reverseEditorText(typedText) {
    // Your code here
}
```

### Java
```java
public String reverseEditorText(String typedText) {
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
