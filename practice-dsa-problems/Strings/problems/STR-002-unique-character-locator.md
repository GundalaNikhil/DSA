---
problem_id: STR_UNIQUE_CHARACTER_LOCATOR__7709
display_id: NTB-STR-7709
slug: unique-character-locator
title: "Unique Character Locator"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
  - unique-character-locator
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Unique Character Locator

## Problem Statement

Given a string `s`, find the first character that appears exactly once in `s`. The order is the original left-to-right order. If no such character exists, output `-1`.

## Input Format

- Single line: string `s`

## Output Format

- Single character (the first unique), or `-1`

## Constraints

- `1 <= |s| <= 200000`
- `s` contains printable ASCII characters

## Clarifying Notes

- Character matching is case-sensitive.
- If multiple unique characters exist, return the one with smallest index.

## Example Input

```
message
```

## Example Output

```
m
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public String findFirstUnique(String s) {
        // Your code here
        return "-1";
    }
}
```

### Python

```python
class Solution:
    def findFirstUnique(self, s: str) -> str:
        # Your code here
        pass
```

### C++

```cpp
#include <string>

class Solution {
public:
    std::string findFirstUnique(std::string s) {
        // Your code here
        return "-1";
    }
};
```

### JavaScript

```javascript
class Solution {
  findFirstUnique(s) {
    // Your code here
    return "-1";
  }
}
```
