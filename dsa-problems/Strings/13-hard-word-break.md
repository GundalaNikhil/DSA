# Word Break Validator

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming, Trie
**License:** Free to use for commercial purposes

## Problem Statement

An auto-complete system needs to validate if a string can be segmented into dictionary words. Given a string `text` and a list of strings `dictionary`, determine if `text` can be segmented into one or more dictionary words. Dictionary words can be reused multiple times.

Return `true` if text can be segmented, `false` otherwise.

## Constraints

- `1 <= text.length <= 300`
- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 20`
- All strings contain only lowercase English letters
- All dictionary words are unique

## Examples

### Example 1
```
Input: text = "leetcode", dictionary = ["leet", "code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code".
```

### Example 2
```
Input: text = "applepenapple", dictionary = ["apple", "pen"]
Output: true
Explanation: "applepenapple" can be segmented as "apple pen apple".
```

### Example 3
```
Input: text = "catsandog", dictionary = ["cats", "dog", "sand", "and", "cat"]
Output: false
Explanation: Cannot segment into dictionary words.
```

### Example 4
```
Input: text = "cars", dictionary = ["car", "ca", "rs"]
Output: true
Explanation: "cars" can be segmented as "car s" or "ca rs".
```

## Function Signature

### Python
```python
def can_segment_string(text: str, dictionary: list[str]) -> bool:
    pass
```

### JavaScript
```javascript
function canSegmentString(text, dictionary) {
    // Your code here
}
```

### Java
```java
public boolean canSegmentString(String text, List<String> dictionary) {
    // Your code here
}
```

## Hints

1. Use dynamic programming: dp[i] = can we segment text[0:i]?
2. For each position i, check all possible words ending at i
3. dp[i] = true if dp[j] = true and text[j:i] is in dictionary
4. Convert dictionary to set for O(1) lookup
5. Time complexity: O(n² * m) where m is avg word length
6. Space complexity: O(n)

## Tags
`string` `dynamic-programming` `hash-set` `segmentation` `hard`
