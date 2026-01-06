---
problem_id: MAT_MATRIX_CONFLICT_RESOLUTION__9566
display_id: NTB-MAT-9566
slug: matrix-conflict-resolution
title: "Matrix Conflict Resolution"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - data-structures
  - grids
  - matrix
  - matrix-conflict-resolution
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Conflict Resolution

## Problem Statement

Multiple sources propose values for cells in a matrix. A global strategy determines how to resolve conflicts for each cell.

Strategies:

- `1` (priority): highest priority wins; tie by earliest timestamp; then smaller source id
- `2` (timestamp): earliest timestamp wins; tie by highest priority; then smaller source id
- `3` (majority): most frequent value wins; tie by highest priority, then earliest timestamp, then smaller source id

Compute the final matrix after resolving all proposals.

## Input Format

- First line: integers `n`, `m`, `p`, `S`
- Next `p` lines: `r c value priority time source_id`

## Output Format

- `n` lines with `m` integers: the resolved matrix (cells with no proposals are 0)

## Constraints

- `1 <= n, m <= 500`
- `0 <= p <= 200000`
- `1 <= S <= 3`
- `-10^9 <= value <= 10^9`
- `0 <= priority, time, source_id <= 10^9`

## Clarifying Notes

- All indices are 1-based.
- Proposals for different cells are independent.

## Example Input

```
2 2 3 1
1 1 5 2 10 7
1 1 8 1 5 3
2 2 4 9 1 2
```

## Example Output

```
5 0
0 4
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class Proposal {
        public int r, c, value, priority, time, source_id;
        public Proposal(int r, int c, int value, int priority, int time, int source_id) {
            this.r = r;
            this.c = c;
            this.value = value;
            this.priority = priority;
            this.time = time;
            this.source_id = source_id;
        }
    }

    public int[][] resolveConflicts(int n, int m, int p, int S, List<Proposal> proposals) {
        // Your code here
        return new int[n][m];
    }
}
```

```python
class Proposal:
    def __init__(self, r: int, c: int, value: int, priority: int, time: int, source_id: int):
        self.r = r
        self.c = c
        self.value = value
        self.priority = priority
        self.time = time
        self.source_id = source_id

class Solution:
    def resolveConflicts(self, n: int, m: int, p: int, S: int, proposals: list[Proposal]) -> list[list[int]]:
        # Your code here
        return [[]]
```

```cpp
#include <vector>

using namespace std;

struct Proposal {
    int r, c, value, priority, time, source_id;
};

class Solution {
public:
    vector<vector<int>> resolveConflicts(int n, int m, int p, int S, vector<Proposal>& proposals) {
        // Your code here
        return {};
    }
};
```

```javascript
class Proposal {
  constructor(r, c, value, priority, time, source_id) {
    this.r = r;
    this.c = c;
    this.value = value;
    this.priority = priority;
    this.time = time;
    this.source_id = source_id;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} p
   * @param {number} S
   * @param {Proposal[]} proposals
   * @returns {number[][]}
   */
  resolveConflicts(n, m, p, S, proposals) {
    // Your code here
    return [[]];
  }
}
```
