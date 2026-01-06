---
problem_id: STR_FIXED_LENGTH_FREQUENCY_RANKING__2012
display_id: NTB-STR-2012
slug: fixed-length-frequency-ranking
title: "Fixed-Length Frequency Ranking"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - fixed-length-frequency-ranking
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Fixed-Length Frequency Ranking

## Problem Statement

Given a string `s`, an integer `L`, and an integer `K`, count the frequency of every substring of length `L`. Output the top `K` substrings by frequency (descending). Break ties by lexicographically smaller substring.

## Input Format

- First line: string `s`
- Second line: integers `L` and `K`

## Output Format

- One line per reported substring: `<substring> <count>`
- If there are fewer than `K` distinct substrings of length `L`, output all of them

## Constraints

- `1 <= |s| <= 200000`
- `1 <= L <= |s|`
- `1 <= K <= 200000`
- `s` contains only lowercase English letters

## Clarifying Notes

- Output order must follow the ranking rules.

## Example Input

```
ababcabc
2 2
```

## Example Output

```
ab 2
bc 2
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<String> findTopKSubstrings(String s, int l, int k) {
        // Your code here
        return new ArrayList<>();
    }
}
```

### Python

```python
from typing import List

class Solution:
    def findTopKSubstrings(self, s: str, l: int, k: int) -> List[str]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> findTopKSubstrings(std::string s, int l, int k) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  findTopKSubstrings(s, l, k) {
    // Your code here
    return [];
  }
}
```
