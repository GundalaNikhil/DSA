---
problem_id: MAT_MATRIX_PARTIAL_ORDER_CONSTRAINTS__1846
display_id: NTB-MAT-1846
slug: matrix-partial-order-constraints
title: "Matrix with Partial Order Constraints"
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
  - matrix-partial-order-constraints
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix with Partial Order Constraints

## Problem Statement

You are given an `n x m` matrix of integer ranges. For each cell `(r, c)`, you know a lower bound `L` and upper bound `U` (inclusive). You are also given `k` constraints of the form:

```
cell A <= cell B
```

Your task is to determine whether a valid assignment exists. If it does, output any assignment that satisfies all bounds and constraints.

## Input Format

- First line: integers `n`, `m`, `k`
- Next `n * m` lines: `L U` for each cell in row-major order
- Next `k` lines: `r1 c1 r2 c2` meaning `M[r1][c1] <= M[r2][c2]`

## Output Format

- If impossible: `IMPOSSIBLE`
- Otherwise:
  - `POSSIBLE`
  - `n` lines with `m` integers forming a valid matrix

## Constraints

- `1 <= n, m <= 200`
- `0 <= k <= 200000`
- `-10^9 <= L <= U <= 10^9`

## Clarifying Notes

- Indices are 1-based.
- Constraints may form cycles; cycles imply equality across the cycle.

## Example Input

```
1 2 1
0 5
0 5
1 1 1 2
```

## Example Output

```
POSSIBLE
0 0
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class Constraint {
        public int r1, c1, r2, c2;
        public Constraint(int r1, int c1, int r2, int c2) {
            this.r1 = r1;
            this.c1 = c1;
            this.r2 = r2;
            this.c2 = c2;
        }
    }

    public static class Range {
        public long L, U;
        public Range(long L, long U) {
            this.L = L;
            this.U = U;
        }
    }

    public static class AssignmentResult {
        public boolean possible;
        public long[][] matrix;
        public AssignmentResult(boolean possible, long[][] matrix) {
            this.possible = possible;
            this.matrix = matrix;
        }
    }

    public AssignmentResult findAssignment(int n, int m, int k, Range[][] ranges, List<Constraint> constraints) {
        // Your code here
        return null;
    }
}
```

```python
class Constraint:
    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2

class Range:
    def __init__(self, L, U):
        self.L = L
        self.U = U

class AssignmentResult:
    def __init__(self, possible, matrix):
        self.possible = possible
        self.matrix = matrix

class Solution:
    def findAssignment(self, n: int, m: int, k: int, ranges: list[list[Range]], constraints: list[Constraint]) -> AssignmentResult:
        # Your code here
        return None
```

```cpp
#include <vector>

using namespace std;

struct Constraint {
    int r1, c1, r2, c2;
};

struct Range {
    long long L, U;
};

struct AssignmentResult {
    bool possible;
    vector<vector<long long>> matrix;
};

class Solution {
public:
    AssignmentResult findAssignment(int n, int m, int k, vector<vector<Range>>& ranges, vector<Constraint>& constraints) {
        // Your code here
        return {};
    }
};
```

```javascript
class Constraint {
  constructor(r1, c1, r2, c2) {
    this.r1 = r1;
    this.c1 = c1;
    this.r2 = r2;
    this.c2 = c2;
  }
}

class Range {
  constructor(L, U) {
    this.L = L;
    this.U = U;
  }
}

class AssignmentResult {
  constructor(possible, matrix) {
    this.possible = possible;
    this.matrix = matrix;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} k
   * @param {Range[][]} ranges
   * @param {Constraint[]} constraints
   * @returns {AssignmentResult}
   */
  findAssignment(n, m, k, ranges, constraints) {
    // Your code here
    return null;
  }
}
```
