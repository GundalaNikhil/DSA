# Ancient Rune Sequence

**Difficulty:** Hard
**Topic:** Graphs, Topological Sort, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

Archaeologists have discovered a list of words written in an unknown ancient script. The words are known to be sorted lexicographically according to the script's own alphabet order.

Your task is to deduce the order of the characters (runes) in this ancient alphabet.

Return a string of the unique characters in the correct order. If multiple valid orders exist, return any. If the given list implies a contradiction (impossible order), return an empty string.

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- Words contain only lowercase English letters (representing runes)

## Examples

### Example 1
```
Input: words = ["k", "ka", "kb", "m", "ma"]

Analysis:
- "k" vs "ka": prefix, valid.
- "ka" vs "kb": 'a' comes before 'b'.
- "kb" vs "m": 'k' comes before 'm'.
- "m" vs "ma": prefix, valid.

Order: k -> m, a -> b.
Combined: k, m, a, b (or a, b, k, m - they are independent chains?)
Wait, 'k' is before 'm'. 'a' is before 'b'.
Is there a relation between k/m and a/b? No.
So "kamb" is valid. "akbm" is valid.

Output: "kamb"
```

### Example 2
```
Input: words = ["z", "x", "z"]
Output: ""
Explanation: z < x and x < z implies cycle. Impossible.
```

### Example 3
```
Input: words = ["apple", "app"]
Output: ""
Explanation: "apple" comes before "app" in input, but "app" is a prefix of "apple", so "app" should be first. Contradiction.
```

## Function Signature

### Python
```python
def rune_order(words: list[str]) -> str:
    pass
```

### JavaScript
```javascript
function runeOrder(words) {
    // Your code here
}
```

### Java
```java
public String runeOrder(String[] words) {
    // Your code here
}
```

## Hints

1. Compare adjacent words to find character precedence
2. Build a directed graph: edge from char1 to char2 means char1 < char2
3. Use topological sort to get the order
4. Detect invalid cases: prefix problem, cycles in graph
5. Not all characters may have ordering constraints

## Tags
`graph` `topological-sort` `string` `ordering` `hard`
