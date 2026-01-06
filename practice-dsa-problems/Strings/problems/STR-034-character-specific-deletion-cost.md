---
problem_id: STR_CHARACTER_SPECIFIC_DELETION_COST__8218
display_id: NTB-STR-8218
slug: character-specific-deletion-cost
title: "Character-Specific Deletion Cost"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - character-specific-deletion-cost
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

# Character-Specific Deletion Cost

## Problem Statement

Given two strings `A` and `B` and a deletion cost for each lowercase letter, you may delete characters from either string. Find the minimum total deletion cost needed to make the two strings equal.

## Input Format

- First line: string `A`
- Second line: string `B`
- Third line: 26 integers: deletion costs for `a` to `z`

## Output Format

- Single integer: minimum deletion cost

## Constraints

- `1 <= |A|, |B| <= 2000`
- `0 <= cost <= 10^9`
- Strings contain only lowercase English letters

## Clarifying Notes

- Only deletions are allowed.

## Example Input

```
sea
eat
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
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
    public long minDeletionCostToEqual(String a, String b, int[] weights) {
        // Your code here
        return 0;
    }
}
```

### Python

```python
from typing import List

class Solution:
    def minDeletionCostToEqual(self, a: str, b: str, weights: List[int]) -> int:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

class Solution {
public:
    long long minDeletionCostToEqual(std::string a, std::string b, std::vector<int>& weights) {
        // Your code here
        return 0;
    }
};
```

### JavaScript

```javascript
class Solution {
  minDeletionCostToEqual(a, b, weights) {
    // Your code here
    return 0;
  }
}
```
