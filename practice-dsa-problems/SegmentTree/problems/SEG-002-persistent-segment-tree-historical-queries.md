---
problem_id: SEG_PERSISTENT_SEGMENT_TREE_HISTORICAL_QUERIES__8670
display_id: NTB-SEG-8670
slug: persistent-segment-tree-historical-queries
title: "Persistent Segment Tree for Historical Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Segment Tree
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - persistent-segment-tree-historical-queries
  - range-queries
  - segmenttree
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Persistent Segment Tree for Historical Queries

## Problem Statement

You are given an initial array `a1..an`. Each update creates a **new version** of the array by modifying a single index. Queries can be performed on any version.

- Version `0` is the initial array.
- Each update creates the next version ID in order: `1, 2, 3, ...`.

Support two operations:

- `U v idx val`: create a new version based on version `v` where `a[idx]` becomes `val`.
- `Q v l r`: return the sum of `a[l..r]` in version `v`.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: operations `U` or `Q` as defined above

## Output Format

- For each `Q` operation, output the range sum on its own line

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, val <= 10^9`
- `1 <= idx <= n`
- `1 <= l <= r <= n`

## Clarifying Notes

- Updates do not modify earlier versions.
- Version IDs are 0-based, and update operations always create the next version ID.
- The intended data structure is a persistent segment tree with `O(log n)` per operation.

## Example Input

```
5 5
1 2 3 4 5
Q 0 1 3
U 0 3 10
Q 1 2 4
U 1 5 -2
Q 2 4 5
```

## Example Output

```
6
16
2
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<Long> solvePersistentQueries(int n, int q, int[] a, List<Query> queries) {
        // Your code here
        return new ArrayList<>();
    }

    public static class Query {
        char type;
        int v, idx, val, l, r;

        public Query(char type, int v, int idx, int val) {
            this.type = type;
            this.v = v;
            this.idx = idx;
            this.val = val;
        }

        public Query(char type, int v, int l, int r) {
            this.type = type;
            this.v = v;
            this.l = l;
            this.r = r;
        }
    }
}
```

### Python

```python
from typing import List, Union

class Query:
    def __init__(self, type: str, v: int, arg1: int, arg2: int):
        self.type = type
        self.v = v
        if type == 'U':
            self.idx = arg1
            self.val = arg2
        else:
            self.l = arg1
            self.r = arg2

class Solution:
    def solvePersistentQueries(self, n: int, q: int, a: List[int], queries: List[Query]) -> List[int]:
        # Your code here
        pass
```

### C++

```cpp
#include <vector>

struct Query {
    char type;
    int v, idx, val, l, r;
};

class Solution {
public:
    std::vector<long long> solvePersistentQueries(int n, int q, std::vector<int>& a, std::vector<Query>& queries) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  solvePersistentQueries(n, q, a, queries) {
    // Your code here
    return [];
  }
}
```
