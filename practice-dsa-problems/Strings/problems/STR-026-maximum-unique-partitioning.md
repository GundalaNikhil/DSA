---
problem_id: STR_MAXIMUM_UNIQUE_PARTITIONING__4090
display_id: NTB-STR-4090
slug: maximum-unique-partitioning
title: "Maximum Unique Partitioning"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - maximum-unique-partitioning
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Maximum Unique Partitioning

## Problem Statement

Given a string `s`, split it into the maximum number of contiguous substrings such that all substrings are distinct. You must output one optimal partition.

## Input Format

- Single line: string `s`

## Output Format

- First line: integer `k`, the maximum number of substrings
- Second line: the `k` substrings separated by spaces

## Constraints

- `1 <= |s| <= 30`
- `s` contains only lowercase English letters

## Clarifying Notes

- If multiple optimal partitions exist, output any one.

## Example Input

```
ababccc
```

## Example Output

```
5
a b ab c cc
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<String> findMaxUniquePartition(String s) {
        // Your code here
        return new ArrayList<>();
    }
}
```

### Python

```python
from typing import List

class Solution:
    def findMaxUniquePartition(self, s: str) -> List[str]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> findMaxUniquePartition(std::string s) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  findMaxUniquePartition(s) {
    // Your code here
    return [];
  }
}
```
