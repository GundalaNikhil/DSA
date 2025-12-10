# Word Reverser

**Difficulty:** Easy
**Topic:** Strings, Manipulation
**License:** Free to use for commercial purposes

## Problem Statement

A messaging app wants to add a fun feature that reverses the order of words in a message while keeping each word's spelling intact. Given a string `message` containing words separated by spaces, reverse the order of the words.

Return the string with words in reversed order, maintaining single spaces between words.

## Constraints

- `1 <= message.length <= 1000`
- `message` contains only English letters and spaces
- Words are separated by single spaces
- No leading or trailing spaces
- At least one word is present

## Examples

### Example 1
```
Input: message = "hello world"
Output: "world hello"
Explanation: The order of words is reversed.
```

### Example 2
```
Input: message = "coding is fun"
Output: "fun is coding"
Explanation: Three words reversed: coding → fun, is → is, fun → coding
```

### Example 3
```
Input: message = "apple"
Output: "apple"
Explanation: Single word remains unchanged.
```

### Example 4
```
Input: message = "one two three four"
Output: "four three two one"
Explanation: Four words completely reversed.
```

## Function Signature

### Python
```python
def reverse_words(message: str) -> str:
    pass
```

### JavaScript
```javascript
function reverseWords(message) {
    // Your code here
}
```

### Java
```java
public String reverseWords(String message) {
    // Your code here
}
```

## Hints

1. Split the string into words
2. Reverse the array of words
3. Join them back with spaces
4. Time complexity: O(n), Space complexity: O(n)

## Tags
`string` `array` `reverse` `easy`
