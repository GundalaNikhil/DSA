---
problem_id: STR_SUFFIX_AUTOMATON_FREQUENCY__3193
display_id: NTB-STR-3193
slug: suffix-automaton-frequency
title: "Suffix Automaton with Frequency"
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
  - suffix-automaton-frequency
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Suffix Automaton with Frequency

## Problem Statement

You are given a string `s` and must answer `q` queries about its substrings:

- `EXISTS p`: output `true` if `p` is a substring of `s`, otherwise `false`.
- `COUNT p`: output the number of occurrences of `p` in `s`.
- `KTH p k`: output the starting index (1-based) of the `k`-th occurrence of `p` in `s`, ordered by starting index. If `p` occurs fewer than `k` times, output `-1`.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: one query as described

## Output Format

- For each query, output the required answer on its own line

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- `1 <= |p| <= 200000`
- Total length of all patterns <= 200000
- `s` and `p` contain only lowercase English letters

## Clarifying Notes

- Occurrences can overlap.
- The intended solution uses a suffix automaton augmented with occurrence counts and position tracking.

## Example Input

```
abracadabra
3
EXISTS abra
COUNT abra
KTH abra 2
```

## Example Output

```
true
2
8
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<Object> solveSuffixAutomatonQueries(String s, int q, List<Query> queries) {
        // Your code here
        return new ArrayList<>();
    }

    public static class Query {
        String type;
        String p;
        int k;
    }
}
```

### Python

```python
from typing import List, Union

class Query:
    def __init__(self, type: str, p: str, k: int = 0):
        self.type = type
        self.p = p
        self.k = k

class Solution:
    def solveSuffixAutomatonQueries(self, s: str, q: int, queries: List[Query]) -> List[Union[bool, int]]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>
#include <variant>

struct Query {
    std::string type;
    std::string p;
    int k;
};

class Solution {
public:
    std::vector<std::variant<bool, int>> solveSuffixAutomatonQueries(std::string s, int q, std::vector<Query>& queries) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  solveSuffixAutomatonQueries(s, q, queries) {
    // Your code here
    return [];
  }
}
```
