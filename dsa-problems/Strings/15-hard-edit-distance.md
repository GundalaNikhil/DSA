# Edit Distance Calculator

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming
**License:** Free to use for commercial purposes

## Problem Statement

A spell-checker needs to calculate the minimum edit distance between two words. Given two strings `word1` and `word2`, find the minimum number of operations required to convert `word1` to `word2`. You can perform three operations: insert a character, delete a character, or replace a character.

Return the minimum number of edit operations needed.

## Constraints

- `0 <= word1.length, word2.length <= 500`
- Both strings contain only lowercase English letters

## Examples

### Example 1
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
  horse -> rorse (replace 'h' with 'r')
  rorse -> rose (remove 'r')
  rose -> ros (remove 'e')
```

### Example 2
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
  intention -> inention (remove 't')
  inention -> enention (replace 'i' with 'e')
  enention -> exention (replace 'n' with 'x')
  exention -> exection (replace 'n' with 'c')
  exection -> execution (insert 'u')
```

### Example 3
```
Input: word1 = "abc", word2 = "abc"
Output: 0
Explanation: Words are identical, no operations needed.
```

### Example 4
```
Input: word1 = "", word2 = "abc"
Output: 3
Explanation: Insert all three characters.
```

## Function Signature

### Python
```python
def min_edit_distance(word1: str, word2: str) -> int:
    pass
```

### JavaScript
```javascript
function minEditDistance(word1, word2) {
    // Your code here
}
```

### Java
```java
public int minEditDistance(String word1, String word2) {
    // Your code here
}
```

## Hints

1. Use 2D dynamic programming table dp[i][j]
2. dp[i][j] = min edit distance between word1[0:i] and word2[0:j]
3. If characters match: dp[i][j] = dp[i-1][j-1]
4. If not: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
5. Initialize first row and column for base cases
6. Time complexity: O(n * m), Space complexity: O(n * m)

## Tags
`string` `dynamic-programming` `edit-distance` `levenshtein` `hard`
