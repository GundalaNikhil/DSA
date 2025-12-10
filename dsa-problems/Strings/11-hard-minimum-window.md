# Minimum Window Substring

**Difficulty:** Hard
**Topic:** Strings, Sliding Window, HashMap
**License:** Free to use for commercial purposes

## Problem Statement

A search engine needs to find the smallest snippet containing all query terms. Given a string `document` and a string `query`, find the minimum length substring in `document` that contains all characters from `query` (including duplicates). If no such substring exists, return an empty string.

Return the minimum window substring or "" if none exists.

## Constraints

- `1 <= document.length <= 100000`
- `1 <= query.length <= document.length`
- Both strings contain English letters, digits, and spaces

## Examples

### Example 1
```
Input: document = "ADOBECODEBANC", query = "ABC"
Output: "BANC"
Explanation: "BANC" is the shortest substring containing A, B, and C.
```

### Example 2
```
Input: document = "a", query = "a"
Output: "a"
Explanation: The entire string is the minimum window.
```

### Example 3
```
Input: document = "a", query = "aa"
Output: ""
Explanation: Document doesn't contain two 'a's.
```

### Example 4
```
Input: document = "abc", query = "cba"
Output: "abc"
Explanation: The entire string is needed.
```

## Function Signature

### Python
```python
def min_window_substring(document: str, query: str) -> str:
    pass
```

### JavaScript
```javascript
function minWindowSubstring(document, query) {
    // Your code here
}
```

### Java
```java
public String minWindowSubstring(String document, String query) {
    // Your code here
}
```

## Hints

1. Use two hash maps: one for query frequencies, one for window
2. Use two pointers for sliding window
3. Expand right until all characters are found
4. Contract left while maintaining all characters
5. Track minimum window found
6. Time complexity: O(n + m), Space complexity: O(m)

## Tags
`string` `sliding-window` `hashmap` `two-pointers` `hard`
