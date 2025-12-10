# Character Frequency Finder

**Difficulty:** Easy
**Topic:** Strings, HashMap
**License:** Free to use for commercial purposes

## Problem Statement

A password strength analyzer needs to find the most frequently occurring character in a password. Given a string `password`, find the character that appears most frequently. If there are multiple characters with the same highest frequency, return the one that appears first in the string.

Return the most frequent character.

## Constraints

- `1 <= password.length <= 1000`
- `password` contains only lowercase English letters

## Examples

### Example 1
```
Input: password = "hello"
Output: "l"
Explanation: 'l' appears 2 times, all others appear once.
```

### Example 2
```
Input: password = "programming"
Output: "g"
Explanation: 'g', 'r', 'a', 'm' each appear twice, but 'g' appears first in string.
```

### Example 3
```
Input: password = "aabbcc"
Output: "a"
Explanation: All characters appear twice, 'a' comes first.
```

### Example 4
```
Input: password = "z"
Output: "z"
Explanation: Single character.
```

## Function Signature

### Python
```python
def find_most_frequent(password: str) -> str:
    pass
```

### JavaScript
```javascript
function findMostFrequent(password) {
    // Your code here
}
```

### Java
```java
public char findMostFrequent(String password) {
    // Your code here
}
```

## Hints

1. Use a hash map to count character frequencies
2. Track the maximum frequency and corresponding character
3. In case of tie, keep the first occurrence
4. Time complexity: O(n), Space complexity: O(1) - at most 26 letters

## Tags
`string` `hashmap` `counting` `easy`
