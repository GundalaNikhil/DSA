---
problem_id: REC_RECURSIVE_PRIORITY_INHERITANCE__6133
display_id: NTB-REC-6133
slug: recursive-priority-inheritance
title: "Recursive Priority Inheritance"
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
  - recursive-priority-inheritance
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Priority Inheritance

## Problem Statement

You are given a rooted tree. Each node has a value `v` and a local priority `p`. The effective priority of a node is the maximum of its local priority and the inherited priority from its parent.

Define `Eval(node, inherited)` as:

- `effective = max(inherited, p[node])`
- Return `v[node] * effective + sum(Eval(child, effective))`

Compute the value returned at the root with inherited priority `0`.

## Input Format

- First line: integer `n`
- Next `n` lines: `v p parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `-10^6 <= v <= 10^6`
- `0 <= p <= 10^6`

## Clarifying Notes

- Priority inheritance is purely along the parent chain.
- Use 64-bit integers for intermediate sums.

## Example Input

```
3
2 3 0
1 1 1
4 5 1
```

## Example Output

```
22
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long calculatePriorityInheritance(int n, long[][] nodes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def calculatePriorityInheritance(self, n: int, nodes: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    long long calculatePriorityInheritance(int n, vector<vector<long long>>& nodes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[][]} nodes
   * @returns {number}
   */
  calculatePriorityInheritance(n, nodes) {
    // Your code here
    return 0;
  }
}
```
