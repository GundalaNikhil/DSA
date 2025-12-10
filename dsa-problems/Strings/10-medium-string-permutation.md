# Hidden Message in Noise

**Difficulty:** Medium
**Topic:** Strings, HashMap, Sliding Window
**License:** Free to use for commercial purposes

## Problem Statement

A spy is listening to a radio channel filled with static noise. They are looking for a hidden signal which is a scrambled version (permutation) of a known `key`.

Given the `noise` string and the `key`, determine if the key's permutation exists as a substring in the noise.

## Constraints

- `1 <= key.length <= noise.length <= 10000`

## Examples

### Example 1
```
Input: noise = "static_message_static", key = "sage"
Output: true
Explanation: "sage" is in "message".
```

### Example 2
```
Input: noise = "random_noise", key = "order"
Output: false
```

### Example 3
```
Input: noise = "abcde", key = "edcba"
Output: true
Explanation: "abcde" contains "edcba" reversed (which is a permutation).
```

## Function Signature

### Python
```python
def find_hidden_signal(noise: str, key: str) -> bool:
    pass
```

### JavaScript
```javascript
function findHiddenSignal(noise, key) {
    // Your code here
}
```

### Java
```java
public boolean findHiddenSignal(String noise, String key) {
    // Your code here
}
```

## Hints
1. Sliding window of key length
2. Frequency map comparison

## Tags
`string` `sliding-window` `medium`
