# Pyramid Block Construction

**Difficulty:** Easy
**Topic:** Math, Arithmetic Sequence
**License:** Free to use for commercial purposes

## Problem Statement

Builders are constructing a pyramid. The top level (level 1) has 1 block. Level 2 has 2 blocks. Level 3 has 3 blocks, and so on.

Calculate the total number of blocks required to build a pyramid with `levels` height.

## Constraints

- `1 <= levels <= 10000`

## Examples

### Example 1
```
Input: levels = 4
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
```

### Example 2
```
Input: levels = 6
Output: 21
Explanation: Sum of 1 to 6 is 21.
```

### Example 3
```
Input: levels = 1
Output: 1
```

## Function Signature

### Python
```python
def count_pyramid_blocks(levels: int) -> int:
    pass
```

### JavaScript
```javascript
function countPyramidBlocks(levels) {
    // Your code here
}
```

### Java
```java
public int countPyramidBlocks(int levels) {
    // Your code here
}
```

## Hints
1. Sum of first n integers formula: n*(n+1)/2

## Tags
`math` `arithmetic-sequence` `easy`
