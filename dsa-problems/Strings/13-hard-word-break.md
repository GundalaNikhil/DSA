# Ancient Script Deciphering

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming, Trie
**License:** Free to use for commercial purposes

## Problem Statement

Archaeologists have discovered a long string of symbols `inscription` from an ancient civilization. They also have a `lexicon` of known valid runes. They need to determine if the entire inscription can be deciphered by segmenting it into a sequence of valid runes from the lexicon.

Given the string `inscription` and a list of strings `lexicon`, determine if `inscription` can be fully segmented into one or more lexicon runes. Runes from the lexicon can be reused multiple times.

## Constraints

- `1 <= inscription.length <= 300`
- `1 <= lexicon.length <= 1000`
- `1 <= lexicon[i].length <= 20`
- All strings contain only lowercase English letters (representing symbols)
- All lexicon runes are unique

## Examples

### Example 1
```
Input: inscription = "zenithpeakzenith", lexicon = ["zenith", "peak"]
Output: true
Explanation: "zenithpeakzenith" can be deciphered as "zenith peak zenith".
```

### Example 2
```
Input: inscription = "galaxyquest", lexicon = ["gal", "axy", "quest", "galaxy"]
Output: true
Explanation: "galaxyquest" can be deciphered as "galaxy quest".
```

### Example 3
```
Input: inscription = "forestrun", lexicon = ["forest", "rest", "run"]
Output: true
Explanation: "forestrun" can be deciphered as "forest run".
```

### Example 4
```
Input: inscription = "thunderstorm", lexicon = ["thunder", "storm", "thun", "der"]
Output: true
Explanation: "thunderstorm" can be deciphered as "thunder storm".
```

### Example 5
```
Input: inscription = "blueocean", lexicon = ["blue", "bean"]
Output: false
Explanation: "ocean" cannot be formed from the lexicon.
```

## Function Signature

### Python
```python
def can_decipher_script(inscription: str, lexicon: list[str]) -> bool:
    pass
```

### JavaScript
```javascript
function canDecipherScript(inscription, lexicon) {
    // Your code here
}
```

### Java
```java
public boolean canDecipherScript(String inscription, List<String> lexicon) {
    // Your code here
}
```

## Hints
1. Use dynamic programming: dp[i] = can we decipher inscription[0:i]?
2. For each position i, check all possible runes ending at i
3. dp[i] = true if dp[j] = true and inscription[j:i] is in lexicon
4. Convert lexicon to set for O(1) lookup
5. Time complexity: O(n² * m) where m is avg rune length
6. Space complexity: O(n)

## Tags
`string` `dynamic-programming` `hash-set` `segmentation` `hard`
