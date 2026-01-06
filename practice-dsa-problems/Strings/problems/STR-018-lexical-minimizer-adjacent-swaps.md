---
problem_id: STR_LEXICAL_MINIMIZER_ADJACENT_SWAPS__1606
display_id: NTB-STR-1606
slug: lexical-minimizer-adjacent-swaps
title: "Lexical Minimizer with Swaps"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - lexical-minimizer-adjacent-swaps
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Lexical Minimizer with Swaps

## Problem Statement

Given a string `s` and an integer `K`, you may perform at most `K` adjacent swaps. Return the lexicographically smallest string that can be obtained.

## Input Format

- First line: string `s`
- Second line: integer `K`

## Output Format

- The lexicographically smallest achievable string

## Constraints

- `1 <= |s| <= 200000`
- `0 <= K <= 10^12`
- `s` contains only lowercase English letters

## Clarifying Notes

- Adjacent swaps are swaps of positions `i` and `i+1`.

## Example Input

```
dcba
2
```

## Example Output

```
bdca
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public String getLexicallySmallest(String s, long k) {
        // Your code here
        return "";
    }
}
```

### Python

```python
class Solution:
    def getLexicallySmallest(self, s: str, k: int) -> str:
        # Your code here
        pass
```

### C++

```cpp
#include <string>

class Solution {
public:
    std::string getLexicallySmallest(std::string s, long long k) {
        // Your code here
        return "";
    }
};
```

### JavaScript

```javascript
class Solution {
  getLexicallySmallest(s, k) {
    // Your code here
    return "";
  }
}
```
