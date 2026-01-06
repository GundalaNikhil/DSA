---
problem_id: REC_RECURSIVE_UNDO_FORBIDDEN__3415
display_id: NTB-REC-3415
slug: recursive-undo-forbidden
title: "Recursive Undo-Forbidden System"
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
  - recursive-undo-forbidden
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Undo-Forbidden System

## Problem Statement

You are given a rooted tree where each node has a boolean flag `ok`. A recursive procedure must choose one child to continue at each non-leaf node. If the chosen child eventually fails, you cannot backtrack to siblings.

A node succeeds if all nodes on the chosen root-to-leaf path have `ok = 1`.

Determine if the root succeeds when always choosing the **leftmost** child first.

## Input Format

- First line: integer `n`
- Next `n` lines: `ok parent` (parent is 0 for root)

## Output Format

- `YES` if the root succeeds, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `ok` is 0 or 1

## Clarifying Notes

- Children are ordered by node id.
- No backtracking is allowed once a child is chosen.

## Example Input

```
3
1 0
0 1
1 1
```

## Example Output

```
NO
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String doesRootSucceed(int n, int[][] nodes) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def doesRootSucceed(self, n: int, nodes: list[list[int]]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string doesRootSucceed(int n, vector<vector<int>>& nodes) {
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
   * @returns {string}
   */
  doesRootSucceed(n, nodes) {
    // Your code here
    return "";
  }
}
```
