---
problem_id: REC_RECURSIVE_PATH_COMMITMENT__9550
display_id: NTB-REC-9550
slug: recursive-path-commitment
title: "Recursive Path Commitment"
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
  - recursive-path-commitment
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Path Commitment

## Problem Statement

You are given a rooted tree with node values. A committed recursion chooses exactly one child at each non-leaf node and continues recursively. Once a child is chosen, all siblings are ignored forever (no backtracking).

Find the maximum sum of values along a root-to-leaf path of **exact length** `L` (number of nodes). If no such path exists, output `-1`.

## Input Format

- First line: integers `n` and `L`
- Next `n` lines: `value parent` (parent is 0 for root)

## Output Format

- Single integer: maximum path sum of length `L`, or `-1`

## Constraints

- `1 <= n <= 200000`
- `1 <= L <= n`
- Values are 32-bit signed integers

## Clarifying Notes

- Path length counts nodes, not edges.

## Example Input

```
4 3
5 0
3 1
2 1
4 2
```

## Example Output

```
12
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long maxPathSumOfLengthL(int n, int L, long[][] nodes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def maxPathSumOfLengthL(self, n: int, L: int, nodes: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    long long maxPathSumOfLengthL(int n, int L, vector<vector<long long>>& nodes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} L
   * @param {number[][]} nodes
   * @returns {number}
   */
  maxPathSumOfLengthL(n, L, nodes) {
    // Your code here
    return 0;
  }
}
```
