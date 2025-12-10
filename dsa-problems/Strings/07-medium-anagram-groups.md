# Anagram Group Counter

**Difficulty:** Medium
**Topic:** Strings, HashMap, Sorting
**License:** Free to use for commercial purposes

## Problem Statement

A word puzzle game needs to group anagrams together. Given an array of strings `words`, group anagrams and return the count of distinct anagram groups. Two words are anagrams if they contain the same characters in different orders.

Return the number of anagram groups.

## Constraints

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 100`
- `words[i]` contains only lowercase English letters

## Examples

### Example 1
```
Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: 3
Explanation: Groups are ["eat","tea","ate"], ["tan","nat"], ["bat"]
```

### Example 2
```
Input: words = ["abc", "bca", "cab", "xyz"]
Output: 2
Explanation: Groups are ["abc","bca","cab"], ["xyz"]
```

### Example 3
```
Input: words = ["a", "b", "c"]
Output: 3
Explanation: Each word is its own group.
```

### Example 4
```
Input: words = ["listen", "silent", "enlist"]
Output: 1
Explanation: All are anagrams of each other.
```

## Function Signature

### Python
```python
def count_anagram_groups(words: list[str]) -> int:
    pass
```

### JavaScript
```javascript
function countAnagramGroups(words) {
    // Your code here
}
```

### Java
```java
public int countAnagramGroups(String[] words) {
    // Your code here
}
```

## Hints

1. Sort characters in each word to create a signature
2. Use a hash map with sorted word as key
3. Count unique keys in the map
4. Time complexity: O(n * k log k) where k is avg word length
5. Space complexity: O(n)

## Tags
`string` `hashmap` `sorting` `anagram` `medium`
