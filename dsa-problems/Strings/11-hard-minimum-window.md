# Rare Element Collection

**Difficulty:** Hard
**Topic:** Strings, Sliding Window, HashMap
**License:** Free to use for commercial purposes

## Problem Statement

A geologist is analyzing a core sample represented by a string `sample`. They want to find the smallest section of the core that contains all the rare elements specified in `elements`.

Given `sample` and `elements`, find the minimum length substring in `sample` that contains all characters from `elements` (including duplicates).

## Constraints

- `1 <= sample.length <= 100000`

## Examples

### Example 1
```
Input: sample = "iron_copper_zinc_iron_gold", elements = "iron_gold"
Output: "iron_gold"
Explanation: "iron_gold" contains both.
Wait, "iron_gold" is 9 chars. "zinc_iron_gold" is 14.
Let's use single chars for simplicity in examples but story implies elements.
Input: sample = "geo_layer_x_y_z_layer", elements = "xyz"
Output: "x_y_z"
```

### Example 2
```
Input: sample = "aaabbbccc", elements = "abc"
Output: "ab"
Explanation: Wait, "ab" doesn't have c.
Input: sample = "aaabbbccc", elements = "abc"
Output: "abbbc" (length 5) or "c" (no).
Let's use standard chars.
Input: sample = "xyyzyx", elements = "xyz"
Output: "zyx"
```

### Example 3
```
Input: sample = "a", elements = "aa"
Output: ""
```

## Function Signature

### Python
```python
def find_collection_window(sample: str, elements: str) -> str:
    pass
```

### JavaScript
```javascript
function findCollectionWindow(sample, elements) {
    // Your code here
}
```

### Java
```java
public String findCollectionWindow(String sample, String elements) {
    // Your code here
}
```

## Hints
1. Sliding window
2. Count required vs current

## Tags
`string` `sliding-window` `hard`
