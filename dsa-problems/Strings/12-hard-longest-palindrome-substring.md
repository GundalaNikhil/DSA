# Symmetric Core Extraction

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming
**License:** Free to use for commercial purposes

## Problem Statement

A mining drill extracts a cylindrical core. Geologists are interested in the longest section of the core that has a symmetric composition (reads the same forwards and backwards).

Given a string `core_sample`, find the longest palindromic substring.

## Constraints

- `1 <= core_sample.length <= 1000`

## Examples

### Example 1
```
Input: core_sample = "layer1_level_layer1"
Output: "layer1_level_layer1"
```

### Example 2
```
Input: core_sample = "abxyzyxdef"
Output: "xyzyx"
```

### Example 3
```
Input: core_sample = "abcd"
Output: "a"
```

## Function Signature

### Python
```python
def extract_symmetric_core(core_sample: str) -> str:
    pass
```

### JavaScript
```javascript
function extractSymmetricCore(coreSample) {
    // Your code here
}
```

### Java
```java
public String extractSymmetricCore(String coreSample) {
    // Your code here
}
```

## Hints
1. Expand around center

## Tags
`string` `palindrome` `hard`
