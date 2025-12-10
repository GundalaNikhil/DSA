# Inventory Item Categorization

**Difficulty:** Medium
**Topic:** Strings, HashMap, Sorting
**License:** Free to use for commercial purposes

## Problem Statement

A warehouse robot scans labels on misplaced items. Some labels are scrambled versions of the correct product names. The robot needs to group these items together based on their character composition (anagrams).

Given a list of `labels`, group the anagrams together.

## Constraints

- `1 <= labels.length <= 1000`

## Examples

### Example 1
```
Input: labels = ["parts", "traps", "strap", "wolf", "flow"]
Output: 2
Explanation:
Group 1: ["parts", "traps", "strap"]
Group 2: ["wolf", "flow"]
```

### Example 2
```
Input: labels = ["gear", "rage"]
Output: 1
```

### Example 3
```
Input: labels = ["bolt", "nut", "screw"]
Output: 3
```

## Function Signature

### Python
```python
def group_items(labels: list[str]) -> int:
    pass
```

### JavaScript
```javascript
function groupItems(labels) {
    // Your code here
}
```

### Java
```java
public int groupItems(String[] labels) {
    // Your code here
}
```

## Hints
1. Sort string as key
2. Map to list of strings

## Tags
`string` `anagram` `medium`
