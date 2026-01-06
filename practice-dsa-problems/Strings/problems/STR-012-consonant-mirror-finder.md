---
problem_id: STR_CONSONANT_MIRROR_FINDER__4872
display_id: NTB-STR-4872
slug: consonant-mirror-finder
title: "Consonant Mirror Finder"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - consonant-mirror-finder
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

# Consonant Mirror Finder

## Problem Statement

Given a lowercase string `s`, find the longest substring whose consonant-only projection is a palindrome. The consonant-only projection is formed by removing all vowels (`a, e, i, o, u`) and keeping the remaining characters in order.

If multiple substrings share the maximum length, choose the one with the smallest starting index.

## Input Format

- Single line: string `s`

## Output Format

- The chosen substring (possibly the entire string)

## Constraints

- `1 <= |s| <= 200000`
- `s` contains only lowercase English letters

## Clarifying Notes

- Vowels are ignored only for palindrome checking, but they still count toward the substring length.
- A substring with zero or one consonant is always valid.

## Example Input

```
raceacar
```

## Example Output

```
raceacar
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public String findLongestConsonantMirror(String s) {
        // Your code here
        return "";
    }
}
```

### Python

```python
class Solution:
    def findLongestConsonantMirror(self, s: str) -> str:
        # Your code here
        pass
```

### C++

```cpp
#include <string>

class Solution {
public:
    std::string findLongestConsonantMirror(std::string s) {
        // Your code here
        return "";
    }
};
```

### JavaScript

```javascript
class Solution {
  findLongestConsonantMirror(s) {
    // Your code here
    return "";
  }
}
```
