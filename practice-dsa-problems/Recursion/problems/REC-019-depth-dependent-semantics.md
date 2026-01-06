---
problem_id: REC_DEPTH_DEPENDENT_SEMANTICS__7310
display_id: NTB-REC-7310
slug: depth-dependent-semantics
title: "Recursion with Depth-Dependent Semantics"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - depth-dependent-semantics
  - recursion
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursion with Depth-Dependent Semantics

## Problem Statement

You are given an expression tree with operators `+` and `*` and integer leaves. The meaning of operators depends on depth:

- At even depth, `+` means max, `*` means min.
- At odd depth, `+` means min, `*` means max.

Compute the value of the expression.

## Input Format

- First line: integer `n`
- Next `n` lines: `type value left right`

`type` is `0` for leaf (value is used) and `1` for operator (value is `+` or `*`). Children are 0 for null.

Root is node `1`.

## Output Format

- Single integer: expression value

## Constraints

- `1 <= n <= 200000`
- Leaf values are 32-bit signed integers

## Clarifying Notes

- Depth of root is 0.

## Example Input

```
3
1 + 2 3
0 5 0 0
0 2 0 0
```

## Example Output

```
5
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long evaluateExpressionTree(int n, List<String> nodes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def evaluateExpressionTree(self, n: int, nodes: list[str]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    long long evaluateExpressionTree(int n, vector<string>& nodes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {string[]} nodes
   * @returns {number}
   */
  evaluateExpressionTree(n, nodes) {
    // Your code here
    return 0;
  }
}
```
