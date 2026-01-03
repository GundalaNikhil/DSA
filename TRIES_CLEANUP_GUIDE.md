# Tries Templates - Cleanup Guide: Remove Unused Helper Methods

**Issue Identified**: 14 out of 16 Tries problems have private helper methods that are **NEVER called from main()**, making them unnecessary scaffolding.

**Standard HackerRank/LeetCode Pattern**:
- `main()` should call only the public interface methods
- Helper methods should NOT be pre-defined if they're not called from main
- Students should implement all necessary helpers themselves

---

## Detailed Cleanup Instructions

### ✅ KEEP AS-IS (2 problems)

#### TRI-006: Lexicographic k-th String Not Present
**Status**: KEEP - Helper `generateCombinations()` is actually called from main
```java
// CORRECT - Called from main:
for (int length = 2; length <= L; length++) {
    generateCombinations(String.valueOf(c), length - 1, inserted, allStrings);
}
```

#### TRI-012: Prefix-Free Check After Inserts
**Status**: KEEP - Only defines `insert()` which is the public interface
```java
// CORRECT - Only one method, it IS the interface:
public boolean insert(String number) {
    //Implement here
    return false;
}
```

---

### 🗑️ REMOVE HELPER METHODS (14 problems)

#### TRI-001: Autocomplete Top-K with Freshness Decay

**Current Template Problem**:
```java
public List<String> autocomplete(...) { ... }
private void collectWords(...) { ... }  // ❌ NEVER CALLED
```

**Main only calls**: `insertWord()`, `autocomplete()`

**Action**: REMOVE `collectWords()` / `_collect_words()` from all 4 languages
- Students will implement this themselves if needed

**Corrected Java**:
```java
class Solution {
    private TrieNode root = new TrieNode();
    private Map<String, WordMetadata> metadata = new HashMap<>();

    public Solution() {
        this.root = new TrieNode();
    }

    public void insertWord(String word, int frequency, int timestamp) {
        //Implement here
    }

    public List<String> autocomplete(String prefix, int currentTime, int D, int k) {
        //Implement here
        return new ArrayList<>();
    }
}
```

---

#### TRI-002: Longest Common Prefix After One Deletion

**Current**: Has `insertWord()` and `dfs()` helpers never called

**Main only calls**: `longestCommonPrefixAfterOneDeletion(words)`

**Action**: REMOVE `_insertWord()`, `_dfs()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root = new TrieNode();
    private String longestPrefix = "";

    public Solution() {
        this.root = new TrieNode();
    }

    public String longestCommonPrefixAfterOneDeletion(String[] words) {
        //Implement here
        return "";
    }
}
```

---

#### TRI-003: Distinct Substrings Count via Trie

**Current**: Has `insertSuffix()` helper

**Main only calls**: `countDistinctSubstrings(s)`

**Action**: REMOVE `_insertSuffix()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root = new TrieNode();

    public Solution() {
        this.root = new TrieNode();
    }

    public int countDistinctSubstrings(String s) {
        //Implement here
        return 0;
    }
}
```

---

#### TRI-004: Replace Words with Shortest Rare Prefix

**Current**: Has `insert()` and `findReplacement()` helpers

**Main only calls**: `replaceWords(dictionary, sentence)`

**Action**: REMOVE `_insert()`, `_findReplacement()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root = new TrieNode();

    public Solution() {
        this.root = new TrieNode();
    }

    public String replaceWords(Map<String, Integer> dictionary, String sentence) {
        //Implement here
        return "";
    }
}
```

---

#### TRI-005: Binary Trie Min XOR Pair Under Limit

**Current**: Has `insert()` and `query()` helpers

**Main only calls**: `minXORPairUnderLimit(arr, L)`

**Additional Issue**: JavaScript has BUG on line ~263
```javascript
// WRONG:
minXORPairUnderLimit(arr, L);  // ❌ Missing solution. prefix

// CORRECT:
solution.minXORPairUnderLimit(arr, L);
```

**Action**:
1. REMOVE `_insert()`, `_query()` from all 4 languages
2. FIX JavaScript bug

**Corrected Java**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public int minXORPairUnderLimit(int[] arr, int L) {
        //Implement here
        return -1;
    }
}
```

---

#### TRI-007: Minimum Unique Prefix Lengths

**Current**: Has `insert()` and `findMinLength()` helpers

**Main only calls**: `findMinimumPrefixLengths(words)`

**Action**: REMOVE `_insert()`, `_find_min_length()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public int[] findMinimumPrefixLengths(String[] words) {
        //Implement here
        return new int[0];
    }
}
```

---

#### TRI-008: Dictionary Compression Size

**Current**: Has `insert()` helper

**Main only calls**: `countTrieNodes(words)`

**Action**: REMOVE `_insert()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public int countTrieNodes(String[] words) {
        //Implement here
        return 0;
    }
}
```

---

#### TRI-009: Wildcard Search

**Current**: Has `dfs()` helper

**Main only calls**: `insertWord()` and `search(pattern)`

**Action**: REMOVE `_dfs()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public void insertWord(String word) {
        //Implement here
    }

    public boolean search(String pattern) {
        //Implement here
        return false;
    }
}
```

---

#### TRI-010: Trie-Based Spell Checker

**Current**: Has `dfs()` helper

**Main only calls**: `insertWord()` and `hasEditDistance1(query)`

**Action**: REMOVE `_dfs()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public void insertWord(String word) {
        //Implement here
    }

    public boolean hasEditDistance1(String query) {
        //Implement here
        return false;
    }
}
```

---

#### TRI-011: Suffix Trie Longest Repeat

**Current**: Has `insertSuffix()` and `dfs()` helpers

**Main only calls**: `longestRepeatedSubstring(s)`

**Action**: REMOVE `_insertSuffix()`, `_dfs()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;
    private int maxLength;

    public Solution() {
        this.root = new TrieNode();
        this.maxLength = 0;
    }

    public int longestRepeatedSubstring(String s) {
        //Implement here
        return 0;
    }
}
```

---

#### TRI-013: Shortest Absent Binary String of Length L

**Current**: Has `insert()` and `dfs()` helpers

**Main only calls**: `findShortestAbsent(binaryStrings, L)`

**Action**: REMOVE `_insert()`, `_dfs()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public String findShortestAbsent(String[] binaryStrings, int L) {
        //Implement here
        return "";
    }
}
```

---

#### TRI-014: Longest Word Buildable by At Least K Prefixes

**Current**: Has `insert()` and `countPrefixes()` helpers

**Main only calls**: `longestWordWithKPrefixes(words, k)`

**Action**: REMOVE `_insert()`, `_count_prefixes()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public String longestWordWithKPrefixes(String[] words, int k) {
        //Implement here
        return "";
    }
}
```

---

#### TRI-015: XOR Minimization With Trie

**Current**: Has `insert()` and `query()` helpers

**Main only calls**: `minimizeXOR(a, X)`

**Action**: REMOVE `_insert()`, `_query()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public int minimizeXOR(int[] a, int X) {
        //Implement here
        return 0;
    }
}
```

---

#### TRI-016: Trie-Based Kth Smallest String

**Current**: Has `insert()` and `dfs()` helpers

**Main only calls**: `kthSmallest(words, k)`

**Action**: REMOVE `_insert()`, `_dfs()` from all 4 languages

**Corrected**:
```java
class Solution {
    private TrieNode root;
    private String result;
    private int remaining;

    public Solution() {
        this.root = new TrieNode();
        this.result = "";
        this.remaining = 0;
    }

    public String kthSmallest(String[] words, int k) {
        //Implement here
        return "";
    }
}
```

---

## Summary

### Files to Update

| Problem | Remove Methods | Fix Issues |
|---------|----------------|-----------|
| TRI-001 | collectWords() | None |
| TRI-002 | insertWord(), dfs() | None |
| TRI-003 | insertSuffix() | None |
| TRI-004 | insert(), findReplacement() | None |
| TRI-005 | insert(), query() | JS bug: missing `solution.` prefix |
| TRI-006 | NONE | KEEP AS-IS |
| TRI-007 | insert(), findMinLength() | None |
| TRI-008 | insert() | None |
| TRI-009 | dfs() | None |
| TRI-010 | dfs() | None |
| TRI-011 | insertSuffix(), dfs() | None |
| TRI-012 | NONE | KEEP AS-IS |
| TRI-013 | insert(), dfs() | None |
| TRI-014 | insert(), countPrefixes() | None |
| TRI-015 | insert(), query() | None |
| TRI-016 | insert(), dfs() | None |

---

## Implementation Pattern

### Before (with unused helpers):
```java
class Solution {
    private TrieNode root;

    public ReturnType mainMethod(...) { ... }

    private void unusedHelper1(...) { ... }  // ❌ REMOVE
    private void unusedHelper2(...) { ... }  // ❌ REMOVE
}
```

### After (clean, only public interface):
```java
class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode();
    }

    public ReturnType mainMethod(...) {
        //Implement here
        return default;
    }
}
```

---

## Why This Matters

1. **HackerRank/LeetCode Standard**: These platforms don't define helper methods in stubs
2. **Student Learning**: Students should implement their own helper methods
3. **Code Clarity**: Unused scaffolding confuses students about what they need to implement
4. **Maintenance**: Less code to maintain and test

---

**Next Steps**: Apply these cleanup changes to all 14 identified problems across all 4 languages.

