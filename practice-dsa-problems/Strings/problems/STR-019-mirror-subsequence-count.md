---
problem_id: STR_MIRROR_SUBSEQUENCE_COUNT__5368
display_id: NTB-STR-5368
slug: mirror-subsequence-count
title: "Mirror Subsequence Count"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - mirror-subsequence-count
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Mirror Subsequence Count

## Problem Statement

Given a string `s` and a modulus `M`, count the number of palindromic subsequences in `s`. Subsequence counting is based on index choices, so identical strings from different index sets are counted separately.

Output the count modulo `M`.

## Input Format

- First line: string `s`
- Second line: integer `M`

## Output Format

- Single integer: count modulo `M`

## Constraints

- `1 <= |s| <= 2000`
- `1 <= M <= 10^9 + 7`
- `s` contains only lowercase English letters

## Clarifying Notes

- The empty subsequence is not counted.
- A single character is a palindrome.

## Example Input

```
aba
1000000007
```

## Example Output

```
5
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public int countPalindromicSubsequences(String s, int m) {
        // Your code here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def countPalindromicSubsequences(self, s: str, m: int) -> int:
        # Your code here
        pass
```

### C++

```cpp
#include <string>

class Solution {
public:
    int countPalindromicSubsequences(std::string s, int m) {
        // Your code here
        return 0;
    }
};
```

### JavaScript

```javascript
class Solution {
  countPalindromicSubsequences(s, m) {
    // Your code here
    return 0;
  }
}
```
