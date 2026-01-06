---
problem_id: MAT_ENERGY_GRID_RECHARGE_LINES__6236
display_id: NTB-MAT-6236
slug: energy-grid-recharge-lines
title: "Energy Grid with Recharge Lines"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - data-structures
  - energy-grid-recharge-lines
  - grids
  - matrix
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Energy Grid with Recharge Lines

## Problem Statement

You are given an `n x m` grid of base energy values, a recharge value for each row, and a drain value for each column. The net energy of cell `(r, c)` is:

```
net = base[r][c] + row_recharge[r] + col_drain[c]
```

A cell remains active if `net >= 0`.

Compute the number of active cells and output the active grid as `1` (active) or `0` (inactive).

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: row recharge values
- Third line: `m` integers: column drain values
- Next `n` lines: `m` integers (base energy grid)

## Output Format

- First line: integer `active_count`
- Next `n` lines: `m` integers (0 or 1)

## Constraints

- `1 <= n, m <= 2000` with `n * m <= 200000`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Column drain values can be negative (meaning extra recharge).

## Example Input

```
2 3
10 20
-5 -15 -25
0 0 0
0 0 0
```

## Example Output

```
4
1 1 0
1 1 0
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class EnergyResult {
        public int activeCount;
        public int[][] activeGrid;
        public EnergyResult(int activeCount, int[][] activeGrid) {
            this.activeCount = activeCount;
            this.activeGrid = activeGrid;
        }
    }

    public EnergyResult calculateActiveCells(int n, int m, int[] rowRecharge, int[] colDrain, int[][] baseEnergy) {
        // Your code here
        return null;
    }
}
```

```python
class EnergyResult:
    def __init__(self, active_count: int, active_grid: list[list[int]]):
        self.active_count = active_count
        self.active_grid = active_grid

class Solution:
    def calculateActiveCells(self, n: int, m: int, row_recharge: list[int], col_drain: list[int], base_energy: list[list[int]]) -> EnergyResult:
        # Your code here
        return None
```

```cpp
#include <vector>

using namespace std;

struct EnergyResult {
    int activeCount;
    vector<vector<int>> activeGrid;
};

class Solution {
public:
    EnergyResult calculateActiveCells(int n, int m, vector<int>& rowRecharge, vector<int>& colDrain, vector<vector<int>>& baseEnergy) {
        // Your code here
        return {};
    }
};
```

```javascript
class EnergyResult {
  constructor(activeCount, activeGrid) {
    this.activeCount = activeCount;
    this.activeGrid = activeGrid;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number[]} rowRecharge
   * @param {number[]} colDrain
   * @param {number[][]} baseEnergy
   * @returns {EnergyResult}
   */
  calculateActiveCells(n, m, rowRecharge, colDrain, baseEnergy) {
    // Your code here
    return null;
  }
}
```
