# Derive Character Ordering

**Difficulty:** Hard
**Topic:** Graphs, Topological Sort, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

You are given a list of words sorted in a special alphabetical order. Derive the order of characters in this alphabet. Return the characters in their sorted order.

If multiple valid orders exist, return any. If the order is invalid or impossible to determine, return an empty string.

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- Words contain only lowercase letters
- Words are sorted according to the alien alphabet

## Examples

### Example 1
```
Input: words = ["baa", "abcd", "abca", "cab", "cad"]

Comparing adjacent words:
- "baa" vs "abcd": b comes before a
- "abcd" vs "abca": d comes before a (comparing 4th char)
- "abca" vs "cab": a comes before c
- "cab" vs "cad": b comes before d

Order: b → a → d, a → c, b → d
Topological sort: b, a, d, c OR b, a, c, d

Output: "badc" (or "bacd")
```

### Example 2
```
Input: words = ["z", "x"]

z comes before x

Output: "zx"
```

### Example 3
```
Input: words = ["abc", "ab"]

Invalid! "abc" cannot come before "ab" (prefix issue)

Output: ""
```

### Example 4
```
Input: words = ["xyz", "xya", "xba", "xbb", "yaa"]

Comparisons:
- xyz vs xya: z before a
- xya vs xba: y before b
- xba vs xbb: a before b
- xbb vs yaa: x before y

Order derivation: z→a, y→b, a→b, x→y
Possible: x, y, z, a, b or x, z, y, a, b

Output: "xyzab"
```

## Function Signature

### Python
```python
def alien_order(words: list[str]) -> str:
    pass
```

### JavaScript
```javascript
function alienOrder(words) {
    // Your code here
}
```

### Java
```java
public String alienOrder(String[] words) {
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
