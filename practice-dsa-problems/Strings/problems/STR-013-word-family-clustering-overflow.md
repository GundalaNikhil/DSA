---
problem_id: STR_WORD_FAMILY_CLUSTERING_OVERFLOW__8241
display_id: NTB-STR-8241
slug: word-family-clustering-overflow
title: "Word Family Clustering with Overflow"
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
  - word-family-clustering-overflow
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Word Family Clustering with Overflow

## Problem Statement

You are given `n` words. Words belong to the same family if they are anagrams (same multiset of characters). For each family, keep words in their original input order and split them into groups of size `K`. If a family has leftover words fewer than `K`, concatenate those leftovers (in order) into a single word to form the final group.

Output all groups in the order of the families' first appearance in the input.

## Input Format

- First line: integers `n` and `K`
- Next `n` lines: one word per line

## Output Format

- First line: integer `g`, number of groups
- Next `g` lines: one group per line with its words separated by spaces

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- Total length of all words <= 200000
- Words contain only lowercase English letters

## Clarifying Notes

- The leftover concatenation is done without separators.
- Groups within a family are output in input order.

## Example Input

```
6 2
eat
tea
tan
ate
nat
bat
```

## Example Output

```
4
eat tea
ate
tan nat
bat
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<String> clusterWordFamilies(int n, int k, String[] words) {
        // Your code here
        return new ArrayList<>();
    }
}
```

### Python

```python
from typing import List

class Solution:
    def clusterWordFamilies(self, n: int, k: int, words: List[str]) -> List[str]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> clusterWordFamilies(int n, int k, std::vector<std::string>& words) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  clusterWordFamilies(n, k, words) {
    // Your code here
    return [];
  }
}
```
