---
problem_id: STR_OVERLAP_GRAPH_ASSEMBLY__6006
display_id: NTB-STR-6006
slug: overlap-graph-assembly
title: "Overlap Graph Assembly"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - overlap-graph-assembly
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Overlap Graph Assembly

## Problem Statement

You are given `n` strings (`n <= 15`). Build the shortest superstring that contains every given string as a substring. If multiple shortest superstrings exist, output the lexicographically smallest one.

## Input Format

- First line: integer `n`
- Next `n` lines: one string per line

## Output Format

- Single line: the shortest superstring

## Constraints

- `1 <= n <= 15`
- `1 <= |s_i| <= 200`
- Total length of all strings <= 2000
- Strings contain only lowercase English letters

## Clarifying Notes

- If a string is a substring of another, it still must be considered present but does not need extra length.

## Example Input

```
5
catg
ctaagt
gcta
ttca
atgcatc
```

## Example Output

```
ctaagttcatgcatc
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public String findShortestSuperstring(int n, String[] strings) {
        // Your code here
        return "";
    }
}
```

### Python

```python
from typing import List

class Solution:
    def findShortestSuperstring(self, n: int, strings: List[str]) -> str:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::string findShortestSuperstring(int n, std::vector<std::string>& strings) {
        // Your code here
        return "";
    }
};
```

### JavaScript

```javascript
class Solution {
  findShortestSuperstring(n, strings) {
    // Your code here
    return "";
  }
}
```
