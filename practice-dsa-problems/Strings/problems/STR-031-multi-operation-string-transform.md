---
problem_id: STR_MULTI_OPERATION_STRING_TRANSFORM__8837
display_id: NTB-STR-8837
slug: multi-operation-string-transform
title: "Multi-Operation String Transform"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - multi-operation-string-transform
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Multi-Operation String Transform

## Problem Statement

Given strings `A` and `B`, transform `A` into `B` with minimum cost. Allowed operations:

- `SWAP`: swap two adjacent characters in the current string (cost `cs`).
- `REPLACE`: replace one character with another (cost `cr`).
- `INSERT`: insert one character (cost `ci`).
- `DELETE`: delete one character (cost `cd`).

Find the minimum total cost.

## Input Format

- First line: string `A`
- Second line: string `B`
- Third line: integers `cs cr ci cd`

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= |A|, |B| <= 2000`
- `0 <= cs, cr, ci, cd <= 10^9`
- Strings contain only lowercase English letters

## Clarifying Notes

- All operations can be applied any number of times.

## Example Input

```
horse
ros
1 2 1 1
```

## Example Output

```
3
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public long minCostTransform(String a, String b, int cs, int cr, int ci, int cd) {
        // Your code here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def minCostTransform(self, a: str, b: str, cs: int, cr: int, ci: int, cd: int) -> int:
        # Your code here
        pass
```

### C++

```cpp
#include <string>

class Solution {
public:
    long long minCostTransform(std::string a, std::string b, int cs, int cr, int ci, int cd) {
        // Your code here
        return 0;
    }
};
```

### JavaScript

```javascript
class Solution {
  minCostTransform(a, b, cs, cr, ci, cd) {
    // Your code here
    return 0;
  }
}
```
