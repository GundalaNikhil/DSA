---
problem_id: REC_RECURSIVE_PARTIAL_ORDERING__1339
display_id: NTB-REC-1339
slug: recursive-partial-ordering
title: "Recursive Partial Ordering"
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
  - recursive-partial-ordering
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Partial Ordering

## Problem Statement

You are given a rooted tree. Each node has children with a partial order constraint: some child must be evaluated before another child. When a node evaluates its children, it chooses any order that respects all constraints.

The node's value is:

`v[node] + sum(orderIndex(child) * childValue)`

where `orderIndex(child)` is the 1-based position of that child in the chosen evaluation order, and `childValue` is the value returned by that child.

Compute the maximum possible value for the root, or report `IMPOSSIBLE` if any node's child constraints contain a cycle.

## Input Format

- First line: integer `n`
- Next `n` lines: `v parent` (parent is 0 for root)
- Next line: integer `c` (number of ordering constraints)
- Next `c` lines: `parent u v` meaning for `parent`, child `u` must be evaluated before child `v`

## Output Format

- Single integer: maximum root value, or `IMPOSSIBLE`

## Constraints

- `1 <= n <= 200000`
- Each node has at most `8` children
- `0 <= c <= 200000`
- `-10^9 <= v <= 10^9`

## Clarifying Notes

- Constraints are local to each parent; cycles at any parent make the result impossible.
- Child values are computed independently before ordering decisions at the parent.

## Example Input

```
5
1 0
2 1
3 1
4 1
5 1
2
1 2 3
1 3 4
```

## Example Output

```
29
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String maxRootValueWithOrdering(int n, long[][] nodes, int c, int[][] constraints) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def maxRootValueWithOrdering(self, n: int, nodes: list[list[int]], c: int, constraints: list[list[int]]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string maxRootValueWithOrdering(int n, vector<vector<long long>>& nodes, int c, vector<vector<int>>& constraints) {
        // Your code here
        return "";
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[][]} nodes
   * @param {number} c
   * @param {number[][]} constraints
   * @returns {string}
   */
  maxRootValueWithOrdering(n, nodes, c, constraints) {
    // Your code here
    return "";
  }
}
```
