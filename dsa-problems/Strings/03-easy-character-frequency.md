# DNA Mutation Hotspot

**Difficulty:** Easy
**Topic:** Strings, HashMap
**License:** Free to use for commercial purposes

## Problem Statement

A geneticist is analyzing DNA sequences to find mutation hotspots. Given a DNA string `sequence`, identify the nucleotide (character) that appears most frequently. If there's a tie, return the one that appears first in the sequence.

## Constraints

- `1 <= sequence.length <= 1000`
- Contains only letters.

## Examples

### Example 1
```
Input: sequence = "gattaca"
Output: "a"
Explanation: 'a' appears 3 times. 't' appears 2 times.
```

### Example 2
```
Input: sequence = "cytosine"
Output: "c"
Explanation: 'c' appears 1 time, but is first. Wait, 'c' appears 1 time? No, 'c', 'y', 't', 'o', 's', 'i', 'n', 'e'. All 1. 'c' is first.
```

### Example 3
```
Input: sequence = "helix"
Output: "h"
```

## Function Signature

### Python
```python
def find_hotspot(sequence: str) -> str:
    pass
```

### JavaScript
```javascript
function findHotspot(sequence) {
    // Your code here
}
```

### Java
```java
public char findHotspot(String sequence) {
    // Your code here
}
```

## Hints
1. Hash map for frequency

## Tags
`string` `hashmap` `easy`
