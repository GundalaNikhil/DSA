---
problem_id: MAT_MATRIX_HEAT_LEAKAGE__3460
display_id: NTB-MAT-3460
slug: matrix-heat-leakage
title: "Matrix Heat Leakage"
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
  - matrix-heat-leakage
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Heat Leakage

## Problem Statement

You are given a heat matrix `A` of size `n x m`. At each step, every cell leaks a fixed percentage `P` of its current heat to its 4-directional neighbors. The leakage rule is:

- `leak_total = floor(A[r][c] * P / 100)`
- Each neighbor receives `floor(leak_total / deg)` where `deg` is the number of in-bounds neighbors
- Any remainder stays in the cell

All updates occur simultaneously. After `T` steps, output the final matrix and the total remaining heat.

## Input Format

- First line: integers `n`, `m`, `T`, `P`
- Next `n` lines: `m` integers (initial heat)

## Output Format

- First line: integer `total` (sum of all cells after `T` steps)
- Next `n` lines: `m` integers (final heat matrix)

## Constraints

- `1 <= n, m <= 100`
- `0 <= T <= 1000`
- `0 <= P <= 100`
- `0 <= A[r][c] <= 10^9`

## Clarifying Notes

- Heat values are integers at all times.
- If `deg = 0` (only possible for `n = m = 1`), no leakage occurs.

## Example Input

```
2 2 1 50
4 0
0 0
```

## Example Output

```
4
2 1
1 0
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class HeatResult {
        public long totalHeat;
        public int[][] finalMatrix;
        public HeatResult(long totalHeat, int[][] finalMatrix) {
            this.totalHeat = totalHeat;
            this.finalMatrix = finalMatrix;
        }
    }

    public HeatResult simulateHeatLeakage(int n, int m, int T, int P, int[][] initialHeat) {
        // Your code here
        return null;
    }
}
```

```python
class HeatResult:
    def __init__(self, total_heat: int, final_matrix: list[list[int]]):
        self.total_heat = total_heat
        self.final_matrix = final_matrix

class Solution:
    def simulateHeatLeakage(self, n: int, m: int, T: int, P: int, initial_heat: list[list[int]]) -> HeatResult:
        # Your code here
        return None
```

```cpp
#include <vector>

using namespace std;

struct HeatResult {
    long long totalHeat;
    vector<vector<int>> finalMatrix;
};

class Solution {
public:
    HeatResult simulateHeatLeakage(int n, int m, int T, int P, vector<vector<int>>& initialHeat) {
        // Your code here
        return {};
    }
};
```

```javascript
class HeatResult {
  constructor(totalHeat, finalMatrix) {
    this.totalHeat = totalHeat;
    this.finalMatrix = finalMatrix;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} T
   * @param {number} P
   * @param {number[][]} initialHeat
   * @returns {HeatResult}
   */
  simulateHeatLeakage(n, m, T, P, initialHeat) {
    // Your code here
    return null;
  }
}
```
