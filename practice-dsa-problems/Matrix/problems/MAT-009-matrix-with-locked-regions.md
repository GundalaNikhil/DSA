---
problem_id: MAT_MATRIX_WITH_LOCKED_REGIONS__1116
display_id: NTB-MAT-1116
slug: matrix-with-locked-regions
title: "Matrix with Locked Regions"
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
  - matrix-with-locked-regions
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix with Locked Regions

## Problem Statement

You are given a matrix and a list of locked rectangles. An update adds a value `delta` to every cell in a rectangle, but locked cells are never modified.

For each update, report how many locked cells were skipped. After all updates, output the final matrix.

## Input Format

- First line: integers `n`, `m`, `L`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `L` lines: `r1 c1 r2 c2` (1-based locked rectangles, inclusive)
- Next `q` lines: `r1 c1 r2 c2 delta` (updates)

## Output Format

- For each update: one line with the number of locked cells skipped
- After all updates: `n` lines with `m` integers (final matrix)

## Constraints

- `1 <= n, m <= 200`
- `0 <= L, q <= 200000`
- `-10^9 <= values, delta <= 10^9`

## Clarifying Notes

- Locked rectangles may overlap; any cell covered by at least one lock is immutable.

## Example Input

```
2 2 1 1
1 2
3 4
1 1 1 1
1 1 2 2 5
```

## Example Output

```
1
1 7
8 9
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class UpdateResult {
        public List<Integer> skippedCells;
        public long[][] finalMatrix;
        public UpdateResult(List<Integer> skippedCells, long[][] finalMatrix) {
            this.skippedCells = skippedCells;
            this.finalMatrix = finalMatrix;
        }
    }

    public UpdateResult processUpdates(int n, int m, int L, int q, int[][] initialMatrix, int[][] locks, int[][] updates) {
        // Your code here
        return null;
    }
}
```

```python
class UpdateResult:
    def __init__(self, skipped_cells: list[int], final_matrix: list[list[int]]):
        self.skipped_cells = skipped_cells
        self.final_matrix = final_matrix

class Solution:
    def processUpdates(self, n: int, m: int, L: int, q: int, initial_matrix: list[list[int]], locks: list[list[int]], updates: list[list[int]]) -> UpdateResult:
        # Your code here
        return None
```

```cpp
#include <vector>

using namespace std;

struct UpdateResult {
    vector<int> skippedCells;
    vector<vector<long long>> finalMatrix;
};

class Solution {
public:
    UpdateResult processUpdates(int n, int m, int L, int q, vector<vector<int>>& initialMatrix, vector<vector<int>>& locks, vector<vector<long long>>& updates) {
        // Your code here
        return {};
    }
};
```

```javascript
class UpdateResult {
  constructor(skippedCells, finalMatrix) {
    this.skippedCells = skippedCells;
    this.finalMatrix = finalMatrix;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} L
   * @param {number} q
   * @param {number[][]} initialMatrix
   * @param {number[][]} locks
   * @param {number[][]} updates
   * @returns {UpdateResult}
   */
  processUpdates(n, m, L, q, initialMatrix, locks, updates) {
    // Your code here
    return null;
  }
}
```
