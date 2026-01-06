---
problem_id: REC_RECURSIVE_TYPE_CHECKER__7512
display_id: NTB-REC-7512
slug: recursive-type-checker
title: "Recursive Type Checker"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-type-checker
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Type Checker

## Problem Statement

You are given an expression tree with the following node types:

- `INT x`: integer literal
- `BOOL x`: boolean literal (`0` or `1`)
- `ADD a b`: integer addition
- `AND a b`: boolean and
- `EQ a b`: equality (both operands must have the same type)

Each node refers to its child indices. Determine the type of the root expression (`INT` or `BOOL`). If the expression is not well-typed, output `TYPE_ERROR`.

## Input Format

- First line: integer `n`
- Next `n` lines: a node description
  - Literals: `INT x` or `BOOL x`
  - Operators: `ADD a b`, `AND a b`, `EQ a b`

## Output Format

- `INT`, `BOOL`, or `TYPE_ERROR`

## Constraints

- `1 <= n <= 200000`
- Node indices are 1-based

## Clarifying Notes

- `ADD` requires both operands to be `INT`.
- `AND` requires both operands to be `BOOL`.
- `EQ` is valid only if both operands have the same type.

## Example Input

```
3
INT 5
INT 7
EQ 1 2
```

## Example Output

```
BOOL
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String checkType(int n, List<String[]> nodeDescriptions) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def checkType(self, n: int, node_descriptions: list[list[str]]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string checkType(int n, vector<vector<string>>& nodeDescriptions) {
        // Your code here
        return "";
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {string[][]} nodeDescriptions
   * @returns {string}
   */
  checkType(n, nodeDescriptions) {
    // Your code here
    return "";
  }
}
```
