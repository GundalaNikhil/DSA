---
problem_id: MAT_MATRIX_STABILIZATION__8520
display_id: NTB-MAT-8520
slug: matrix-stabilization
title: "Matrix Stabilization"
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
  - matrix-stabilization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Stabilization

## Problem Statement

You are given a binary matrix (values 0 or 1). At each step, all cells update simultaneously using this rule:

- Let `d` be the number of 4-directional neighbors (up, down, left, right) whose value differs from the cell.
- If `d >= 2`, the cell changes to the **majority value among its neighbors**.
- If there is a tie among neighbor values, the cell becomes `0`.
- If `d < 2`, the cell remains unchanged.

Repeat until a previous state reappears. If the process reaches a fixed point, report it as stable. Otherwise, report the cycle length and the first state in the cycle.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: `m` characters each (`0` or `1`)

## Output Format

- If stable: output `STABLE t` where `t` is the number of steps taken, then the matrix
- If cyclic: output `CYCLE p` where `p` is the cycle length, then the first matrix in the cycle

## Constraints

- `1 <= n, m <= 15`

## Clarifying Notes

- Step count `t` is 0 if the initial matrix is already stable.
- Neighbor counts use only in-bounds cells.

## Example Input

```
3 3
101
010
101
```

## Example Output

```
STABLE 2
000
000
000
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class StabilizationResult {
        public String type; // "STABLE" or "CYCLE"
        public int value; // t or p
        public int[][] matrix;
        public StabilizationResult(String type, int value, int[][] matrix) {
            this.type = type;
            this.value = value;
            this.matrix = matrix;
        }
    }

    public StabilizationResult stabilizeMatrix(int n, int m, int[][] initialMatrix) {
        // Your code here
        return null;
    }
}
```

```python
class StabilizationResult:
    def __init__(self, type_str: str, value: int, matrix: list[list[int]]):
        self.type = type_str
        self.value = value
        self.matrix = matrix

class Solution:
    def stabilizeMatrix(self, n: int, m: int, initial_matrix: list[list[int]]) -> StabilizationResult:
        # Your code here
        return None
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct StabilizationResult {
    string type;
    int value;
    vector<vector<int>> matrix;
};

class Solution {
public:
    StabilizationResult stabilizeMatrix(int n, int m, vector<vector<int>>& initialMatrix) {
        // Your code here
        return {};
    }
};
```

```javascript
class StabilizationResult {
  constructor(type, value, matrix) {
    this.type = type;
    this.value = value;
    this.matrix = matrix;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number[][]} initialMatrix
   * @returns {StabilizationResult}
   */
  stabilizeMatrix(n, m, initialMatrix) {
    // Your code here
    return null;
  }
}
```
