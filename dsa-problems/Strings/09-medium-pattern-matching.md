# Pattern Matching Counter

**Difficulty:** Medium
**Topic:** Strings, Sliding Window
**License:** Free to use for commercial purposes

## Problem Statement

A DNA sequence analyzer needs to find specific patterns. Given a DNA string `sequence` containing only characters A, C, G, T, and a pattern string `pattern`, count how many times the pattern appears in the sequence (including overlapping occurrences).

Return the count of pattern occurrences.

## Constraints

- `1 <= sequence.length <= 100000`
- `1 <= pattern.length <= sequence.length`
- Both strings contain only uppercase letters A, C, G, T

## Examples

### Example 1
```
Input: sequence = "ACGTACGTACGT", pattern = "ACGT"
Output: 3
Explanation: Pattern appears at positions 0, 4, and 8.
```

### Example 2
```
Input: sequence = "AAAA", pattern = "AA"
Output: 3
Explanation: Overlapping matches at positions 0, 1, and 2.
```

### Example 3
```
Input: sequence = "ACGT", pattern = "XY"
Output: 0
Explanation: Pattern not found (though this violates constraints).
```

### Example 4
```
Input: sequence = "ATCGATCGATCG", pattern = "ATCG"
Output: 3
Explanation: Pattern appears at positions 0, 4, and 8.
```

## Function Signature

### Python
```python
def count_pattern_matches(sequence: str, pattern: str) -> int:
    pass
```

### JavaScript
```javascript
function countPatternMatches(sequence, pattern) {
    // Your code here
}
```

### Java
```java
public int countPatternMatches(String sequence, String pattern) {
    // Your code here
}
```

## Hints

1. Iterate through sequence with sliding window of pattern length
2. Compare each window with the pattern
3. Count matches including overlapping ones
4. Time complexity: O(n * m) naive approach, O(n) with KMP
5. Space complexity: O(1) for naive, O(m) for KMP

## Tags
`string` `pattern-matching` `sliding-window` `medium`
