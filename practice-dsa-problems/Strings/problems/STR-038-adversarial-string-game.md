---
problem_id: STR_ADVERSARIAL_STRING_GAME__2054
display_id: NTB-STR-2054
slug: adversarial-string-game
title: "Adversarial String Game"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - adversarial-string-game
  - algorithms
  - coding-interviews
  - data-structures
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Adversarial String Game

## Problem Statement

Two players play a game on a string `s`. On each turn, a player chooses a contiguous substring of identical characters with length between `L` and `R` (inclusive) and removes it. The remaining parts concatenate to form the new string. The player who cannot move loses.

Determine the winner assuming optimal play. Output `FIRST` if the first player wins, otherwise output `SECOND`.

## Input Format

- First line: string `s`
- Second line: integers `L` and `R`

## Output Format

- `FIRST` or `SECOND`

## Constraints

- `1 <= |s| <= 200000`
- `1 <= L <= R <= |s|`
- `s` contains only lowercase English letters

## Clarifying Notes

- Only substrings of identical characters are legal moves.

## Example Input

```
aaaab
2 3
```

## Example Output

```
FIRST
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public String getGameWinner(String s, int l, int r) {
        // Your code here
        return "SECOND";
    }
}
```

### Python

```python
class Solution:
    def getGameWinner(self, s: str, l: int, r: int) -> str:
        # Your code here
        pass
```

### C++

```cpp
#include <string>

class Solution {
public:
    std::string getGameWinner(std::string s, int l, int r) {
        // Your code here
        return "SECOND";
    }
};
```

### JavaScript

```javascript
class Solution {
  getGameWinner(s, l, r) {
    // Your code here
    return "SECOND";
  }
}
```
