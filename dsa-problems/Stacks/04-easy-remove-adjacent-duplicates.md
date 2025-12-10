# Chemical Reaction Reducer

**Difficulty:** Easy
**Topic:** Stacks, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

In a chemical simulation, certain adjacent elements react and disappear. Specifically, if two identical elements (represented by characters) are adjacent, they react and vanish. This process continues until no more adjacent identical elements exist.

Given a string `compound` representing the sequence of elements, return the final stable compound after all reactions.

## Constraints

- `1 <= compound.length <= 5000`
- `compound` contains only lowercase English letters

## Examples

### Example 1
```
Input: compound = "abbaca"
Output: "ca"
Explanation:
- "bb" react and vanish → "aaca"
- "aa" react and vanish → "ca"
```

### Example 2
```
Input: compound = "azxxzy"
Output: "ay"
Explanation:
- "xx" react → "azzy"
- "zz" react → "ay"
```

### Example 3
```
Input: compound = "aabbccdd"
Output: ""
Explanation: All elements react in pairs and vanish.
```

### Example 4
```
Input: compound = "abcdefg"
Output: "abcdefg"
Explanation: No adjacent identical elements to react.
```

## Function Signature

### Python
```python
def reduce_compound(compound: str) -> str:
    pass
```

### JavaScript
```javascript
function reduceCompound(compound) {
    // Your code here
}
```

### Java
```java
public String reduceCompound(String compound) {
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
