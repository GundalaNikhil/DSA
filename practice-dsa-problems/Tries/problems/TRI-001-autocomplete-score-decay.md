---
problem_id: TRI_AUTOCOMPLETE_SCORE_DECAY__4055
display_id: NTB-TRI-4055
slug: autocomplete-score-decay
title: "Autocomplete System with Score Decay"
difficulty: Medium
difficulty_score: 50
topics:
  - Tries
tags:
  - algorithms
  - autocomplete-score-decay
  - coding-interviews
  - data-structures
  - efficient-search
  - prefix-trees
  - technical-interview-prep
  - tries
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Autocomplete System with Score Decay

## Problem Statement

Build an autocomplete system that supports insertions and prefix queries. Each word has an integer score that changes over time.

You are given a decay percentage `D` (0 to 100). After every query, any word that is **not** returned as a suggestion has its score decayed as:

```
score = floor(score * (100 - D) / 100)
```

A query returns up to 5 suggestions that start with the given prefix, ordered by:

1. Higher current score
2. Lexicographically smaller word

Words returned in the suggestion list do not decay for that query. Words not returned (including words that do not match the prefix) do decay.

## Input Format

- First line: integers `n` and `D`
- Next `n` lines: `word score`
- Next line: integer `q`
- Next `q` lines: one of the following
  - `I word score` (insert or overwrite the score for `word`)
  - `Q prefix` (query)

## Output Format

- For each `Q` operation, output a line with up to 5 words separated by spaces
- If there are no matching words, output an empty line

## Constraints

- `1 <= n, q <= 200000`
- `1 <= word length <= 50`
- Words contain only lowercase English letters
- `0 <= D <= 100`
- `0 <= score <= 10^9`

## Clarifying Notes

- An insert with an existing word overwrites its current score.
- Decay is applied **after** producing the suggestions for a query.
- The trie must support prefix search; the decay mechanism is deterministic and global.

## Example Input

```
3 10
car 100
cat 80
dog 90
3
Q ca
Q d
Q ca
```

## Example Output

```
car cat
dog
car cat
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<List<String>> solveAutocompleteWithDecay(int n, int d, WordScore[] initialWords, int q, Op[] ops) {
        // Your code here
        return new ArrayList<>();
    }

    public static class WordScore {
        String word;
        int score;
        public WordScore(String word, int score) { this.word = word; this.score = score; }
    }

    public static class Op {
        char type;
        String word;
        int score;
        public Op(char type, String word) { this.type = type; this.word = word; }
        public Op(char type, String word, int score) { this.type = type; this.word = word; this.score = score; }
    }
}
```

### Python

```python
from typing import List

class WordScore:
    def __init__(self, word: str, score: int):
        self.word = word
        self.score = score

class Op:
    def __init__(self, type: str, word: str, score: int = 0):
        self.type = type
        self.word = word
        self.score = score

class Solution:
    def solveAutocompleteWithDecay(self, n: int, d: int, initialWords: List[WordScore], q: int, ops: List[Op]) -> List[List[str]]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

struct WordScore {
    std::string word;
    int score;
};

struct Op {
    char type;
    std::string word;
    int score;
};

class Solution {
public:
    std::vector<std::vector<std::string>> solveAutocompleteWithDecay(int n, int d, std::vector<WordScore>& initialWords, int q, std::vector<Op>& ops) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  solveAutocompleteWithDecay(n, d, initialWords, q, ops) {
    // Your code here
    return [];
  }
}
```
