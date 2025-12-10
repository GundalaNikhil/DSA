# Remove Adjacent Duplicates

**Difficulty:** Easy
**Topic:** Stacks, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

Given a string, repeatedly remove adjacent duplicate characters until no more duplicates exist.

For example, "aabbcc" becomes "" (aa removed, bb removed, cc removed). "abccba" becomes "" (cc removed first, then bb, then aa).

Return the final string after all removals.

## Constraints

- `1 <= string.length <= 5000`
- String contains only lowercase English letters

## Examples

### Example 1
```
Input: s = "abbaca"
Output: "ca"
Explanation:
- Remove "bb" → "aaca"
- Remove "aa" → "ca"
```

### Example 2
```
Input: s = "azxxzy"
Output: "ay"
Explanation:
- Remove "xx" → "azzy"
- Remove "zz" → "ay"
```

### Example 3
```
Input: s = "aabbccdd"
Output: ""
Explanation: All characters removed in pairs
```

### Example 4
```
Input: s = "abcdefg"
Output: "abcdefg"
Explanation: No adjacent duplicates to remove
```

## Function Signature

### Python
```python
def remove_duplicates(s: str) -> str:
    pass
```

### JavaScript
```javascript
function removeDuplicates(s) {
    // Your code here
}
```

### Java
```java
public String removeDuplicates(String s) {
    // Your code here
}
```

## Hints

1. Use stack to track characters
2. For each character, check if it equals top of stack
3. If yes, pop from stack (remove pair)
4. If no, push to stack
5. Final stack contents form the result
6. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `string` `duplicates` `easy`
