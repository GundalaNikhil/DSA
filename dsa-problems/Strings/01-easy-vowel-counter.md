# Ancient Rune Power Level

**Difficulty:** Easy
**Topic:** Strings, Counting
**License:** Free to use for commercial purposes

## Problem Statement

In a fantasy game, a spell's power is determined by the number of "magic vowels" (a, e, i, o, u) in its incantation. Given a spell string `incantation`, calculate its power level.

Return the total count of vowels (both uppercase and lowercase).

## Constraints

- `1 <= incantation.length <= 1000`
- Contains English letters and spaces.

## Examples

### Example 1
```
Input: incantation = "Abracadabra"
Output: 5
Explanation: A, a, a, a, a. Total 5.
```

### Example 2
```
Input: incantation = "Cryptic Hymn"
Output: 0
Explanation: No vowels.
```

### Example 3
```
Input: incantation = "Expelliarmus"
Output: 5
Explanation: E, e, i, a, u.
```

## Function Signature

### Python
```python
def calculate_power(incantation: str) -> int:
    pass
```

### JavaScript
```javascript
function calculatePower(incantation) {
    // Your code here
}
```

### Java
```java
public int calculatePower(String incantation) {
    // Your code here
}
```

## Hints
1. Check against set of vowels

## Tags
`string` `counting` `easy`
