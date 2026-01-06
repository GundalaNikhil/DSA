---
problem_id: STR_BINARY_SUBSTRING_XOR__6488
display_id: NTB-STR-6488
slug: binary-substring-xor
title: "Binary Substring XOR"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - binary-substring-xor
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

# Binary Substring XOR

## Problem Statement

Given a binary string `s` and `q` queries, each query specifies a range `[l, r]` (1-based). For each query, consider **all** substrings fully contained in `s[l..r]`. Interpret each substring as a binary number with the leftmost bit as the most significant bit. Output the bitwise XOR of all these substring values.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: integers `l r`

## Output Format

- For each query, output the XOR value on its own line

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- `1 <= l <= r <= |s|`
- `r - l + 1 <= 30`
- `s` contains only `0` and `1`

## Clarifying Notes

- All substring values fit within 32-bit signed integers due to the length limit.

## Example Input

```
1011
1
2 4
```

## Example Output

```
6
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<Integer> solveBinaryXorQueries(String s, int q, int[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

### Python

```python
from typing import List

class Solution:
    def solveBinaryXorQueries(self, s: str, q: int, queries: List[List[int]]) -> List[int]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> solveBinaryXorQueries(std::string s, int q, std::vector<std::pair<int, int>>& queries) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  solveBinaryXorQueries(s, q, queries) {
    // Your code here
    return [];
  }
}
```
