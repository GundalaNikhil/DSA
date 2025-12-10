# Vowel Counter

**Difficulty:** Easy
**Topic:** Strings, Counting
**License:** Free to use for commercial purposes

## Problem Statement

A text analysis tool needs to count vowels in user reviews. Given a string `text`, count how many vowels (a, e, i, o, u) it contains. Both uppercase and lowercase vowels should be counted.

Return the total count of vowels in the string.

## Constraints

- `1 <= text.length <= 1000`
- `text` contains only English letters, spaces, and punctuation marks

## Examples

### Example 1
```
Input: text = "Hello World"
Output: 3
Explanation: Vowels are 'e', 'o', 'o' = 3 vowels
```

### Example 2
```
Input: text = "Programming"
Output: 3
Explanation: Vowels are 'o', 'a', 'i' = 3 vowels
```

### Example 3
```
Input: text = "AEIOU"
Output: 5
Explanation: All characters are uppercase vowels
```

### Example 4
```
Input: text = "xyz"
Output: 0
Explanation: No vowels in the string
```

## Function Signature

### Python
```python
def count_vowels(text: str) -> int:
    pass
```

### JavaScript
```javascript
function countVowels(text) {
    // Your code here
}
```

### Java
```java
public int countVowels(String text) {
    // Your code here
}
```

## Hints

1. Create a set of vowels for easy checking
2. Iterate through each character
3. Handle both uppercase and lowercase
4. Time complexity: O(n), Space complexity: O(1)

## Tags
`string` `counting` `iteration` `easy`
