---
problem_id: STR_PATTERN_WITH_REVERSAL__6674
display_id: NTB-STR-6674
slug: pattern-with-reversal
title: "Pattern with Reversal"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - pattern-matching
  - pattern-with-reversal
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Pattern with Reversal

## Problem Statement

Given a text `T` and a pattern `P`, determine if there exists an index range in `T` that matches `P` after reversing at most one contiguous segment of `P`.

Formally, choose indices `l` and `r` with `1 <= l <= r <= |P|`, reverse `P[l..r]`, and check if the resulting string appears as a substring in `T`. You may also choose an empty reversal (no change).

Output `true` if such a match exists, otherwise `false`.

## Input Format

- First line: string `T`
- Second line: string `P`

## Output Format

- `true` or `false`

## Constraints

- `1 <= |T|, |P| <= 200000`
- Strings contain only lowercase English letters

## Clarifying Notes

- Reversal is applied to the pattern once at most.

## Example Input

```
abcdefghi
fed
```

## Example Output

```
true
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public boolean canMatchWithReversal(String t, String p) {
        // Your code here
        return false;
    }
}
```

### Python

```python
class Solution:
    def canMatchWithReversal(self, t: str, p: str) -> bool:
        # Your code here
        pass
```

### C++

```cpp
#include <string>

class Solution {
public:
    bool canMatchWithReversal(std::string t, std::string p) {
        // Your code here
        return false;
    }
};
```

### JavaScript

```javascript
class Solution {
  canMatchWithReversal(t, p) {
    // Your code here
    return false;
  }
}
```
