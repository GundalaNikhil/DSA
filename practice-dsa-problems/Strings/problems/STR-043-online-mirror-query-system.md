---
problem_id: STR_ONLINE_MIRROR_QUERY_SYSTEM__5996
display_id: NTB-STR-5996
slug: online-mirror-query-system
title: "Online Mirror Query System"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - online-mirror-query-system
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Online Mirror Query System

## Problem Statement

You start with an empty string and process `q` operations:

- `ADD c`: append character `c` to the end of the current string.
- `ASK l r`: determine whether the substring from index `l` to `r` (1-based) is a palindrome.

Output `true` or `false` for each `ASK` operation.

## Input Format

- First line: integer `q`
- Next `q` lines: one operation per line

## Output Format

- For each `ASK`, output `true` or `false` on its own line

## Constraints

- `1 <= q <= 200000`
- All characters are lowercase English letters
- `1 <= l <= r <= current_length` at the time of query

## Clarifying Notes

- The string grows only by appends; no deletions.
- The intended solution uses rolling hashes or palindromic tree with dynamic updates.

## Example Input

```
5
ADD a
ADD b
ASK 1 2
ADD a
ASK 1 3
```

## Example Output

```
false
true
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<Boolean> solveOnlineMirrorQueries(int q, List<MirrorOp> ops) {
        // Your code here
        return new ArrayList<>();
    }

    public static class MirrorOp {
        String type;
        char c;
        int l, r;
    }
}
```

### Python

```python
from typing import List

class MirrorOp:
    def __init__(self, type: str, arg1: str, arg2: int = 0):
        self.type = type
        if type == 'ADD':
            self.c = arg1
        else:
            self.l = int(arg1)
            self.r = arg2

class Solution:
    def solveOnlineMirrorQueries(self, q: int, ops: List[MirrorOp]) -> List[bool]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

struct MirrorOp {
    std::string type;
    char c;
    int l, r;
};

class Solution {
public:
    std::vector<bool> solveOnlineMirrorQueries(int q, std::vector<MirrorOp>& ops) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  solveOnlineMirrorQueries(q, ops) {
    // Your code here
    return [];
  }
}
```
