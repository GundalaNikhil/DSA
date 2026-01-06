---
problem_id: REC_RECURSIVE_WATERFALL_CONSTRAINTS__3539
display_id: NTB-REC-3539
slug: recursive-waterfall-constraints
title: "Recursive Waterfall Constraints"
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
  - recursive-waterfall-constraints
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Waterfall Constraints

## Problem Statement

You are given a rooted tree. Each node has a value `v` and a constraint interval `[lo, hi]` relative to its parent.

- The root has an absolute allowed interval `[L0, R0]`.
- A non-root node `u` is valid if `v[u]` lies within `[v[parent] + lo[u], v[parent] + hi[u]]`.

Determine whether all nodes in the tree are valid.

## Input Format

- First line: integers `n`, `L0`, `R0`
- Next `n` lines: `v lo hi parent` (parent is 0 for root)

## Output Format

- `YES` if all nodes are valid, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= v, L0, R0, lo, hi <= 10^9`

## Clarifying Notes

- For the root, only `[L0, R0]` is used; its `lo` and `hi` are ignored.
- Constraints cascade downwards from parent values, not from global bounds.

## Example Input

```
3 0 10
5 0 0 0
6 -1 2 1
2 -5 0 1
```

## Example Output

```
YES
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String validateWaterfall(int n, long L0, long R0, long[][] nodes) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def validateWaterfall(self, n: int, L0: int, R0: int, nodes: list[list[int]]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string validateWaterfall(int n, long long L0, long long R0, vector<vector<long long>>& nodes) {
        // Your code here
        return "";
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} L0
   * @param {number} R0
   * @param {number[][]} nodes
   * @returns {string}
   */
  validateWaterfall(n, L0, R0, nodes) {
    // Your code here
    return "";
  }
}
```
