---
problem_id: REC_RECURSIVE_FREQUENCY_LIMITS__5814
display_id: NTB-REC-5814
slug: recursive-frequency-limits
title: "Recursive Frequency Limits"
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
  - recursive-frequency-limits
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Frequency Limits

## Problem Statement

You are given a rooted tree. Each node has a label `L`. A recursive traversal counts how many times each label is visited. If a label is visited more than `K` times, traversal stops at that node and its children are not visited.

Compute the total number of visited nodes.

## Input Format

- First line: integers `n` and `K`
- Next `n` lines: `label parent` (parent is 0 for root)

## Output Format

- Single integer: total number of visited nodes

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= 200000`
- `0 <= label <= 200000`

## Clarifying Notes

- Traversal is pre-order from the root.
- Once the label count exceeds `K`, that node is not counted and its subtree is skipped.

## Example Input

```
5 2
1 0
1 1
2 1
1 2
2 2
```

## Example Output

```
4
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public int countVisitedNodes(int n, int K, int[][] nodes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def countVisitedNodes(self, n: int, K: int, nodes: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int countVisitedNodes(int n, int K, vector<vector<int>>& nodes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} K
   * @param {number[][]} nodes
   * @returns {number}
   */
  countVisitedNodes(n, K, nodes) {
    // Your code here
    return 0;
  }
}
```
