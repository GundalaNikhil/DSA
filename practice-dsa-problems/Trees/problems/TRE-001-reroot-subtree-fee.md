---
problem_id: TRE_REROOT_SUBTREE_FEE__1675
display_id: NTB-TRE-1675
slug: reroot-subtree-fee
title: "Subtree Size Queries Under Changing Root"
difficulty: Medium
difficulty_score: 50
topics:
  - Trees
tags:
  - algorithms
  - binary-trees
  - coding-interviews
  - data-structures
  - reroot-subtree-fee
  - technical-interview-prep
  - traversal
  - trees
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Subtree Size Queries Under Changing Root

## Problem Statement

You are given a tree with `n` nodes. You process `q` queries. Each query provides a root `r` and a node `x`.

For that query, treat the tree as rooted at `r`. Let `subtree_r(x)` be the number of nodes in the subtree of `x` under root `r` (including `x`).

Additionally, changing the root between consecutive queries costs `C` (the first query sets the initial root with no fee).

For each query, output: `subtree_r(x) + (root_changed ? C : 0)`

## Input Format

- First line: `n`, `q`, `C`
- Next `n-1` lines: `u v`
- Next `q` lines: `r x`

## Output Format

- For each query, a single integer on its own line.

## Constraints

- `2 <= n <= 2*10^5`
- `1 <= q <= 2*10^5`
- `0 <= C <= 10^9`

## Clarifying Notes

- Root-change fee applies when `r != previous_root`.
- Subtree is defined by parent-child direction induced by the chosen root.

## Example Input

```
5 3 10
1 2
2 3
3 4
4 5
1 3
1 2
3 2
```

## Example Output

```
3
4
12
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<Long> solveSubtreeSizeQueries(int n, int q, int c, int[][] edges, int[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

### Python

```python
from typing import List

class Solution:
    def solveSubtreeSizeQueries(self, n: int, q: int, c: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Your code here
        pass
```

### C++

```cpp
#include <vector>

class Solution {
public:
    std::vector<long long> solveSubtreeSizeQueries(int n, int q, int c, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  solveSubtreeSizeQueries(n, q, c, edges, queries) {
    // Your code here
    return [];
  }
}
```
