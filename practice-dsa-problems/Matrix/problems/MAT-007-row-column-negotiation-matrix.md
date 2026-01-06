---
problem_id: MAT_ROW_COLUMN_NEGOTIATION_MATRIX__2559
display_id: NTB-MAT-2559
slug: row-column-negotiation-matrix
title: "Row-Column Negotiation Matrix"
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
  - row-column-negotiation-matrix
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Row-Column Negotiation Matrix

## Problem Statement

Each row proposes a value for all its cells. Each column has a minimum acceptable value and a cap. For each cell `(r, c)`:

- If `row_value < col_min`, the negotiation fails for that cell.
- Otherwise the final value is `min(row_value, col_cap)`.

Compute the final matrix and the number of failed cells.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: row proposals
- Next `m` lines: `col_min col_cap` for each column

## Output Format

- First line: integer `failures`
- Next `n` lines: `m` integers, using `-1` for failed cells

## Constraints

- `1 <= n, m <= 500`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- A cell fails only if `row_value < col_min`.
- A column cap can be less than the row value.

## Example Input

```
3 3
10 20 30
5 15
15 25
0 35
```

## Example Output

```
1
10 10 10
15 20 20
15 25 30
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class NegotiationResult {
        public int failures;
        public int[][] finalMatrix;
        public NegotiationResult(int failures, int[][] finalMatrix) {
            this.failures = failures;
            this.finalMatrix = finalMatrix;
        }
    }

    public NegotiationResult negotiateMatrix(int n, int m, int[] rowProposals, int[][] columnCriteria) {
        // Your code here
        return null;
    }
}
```

```python
class NegotiationResult:
    def __init__(self, failures: int, final_matrix: list[list[int]]):
        self.failures = failures
        self.final_matrix = final_matrix

class Solution:
    def negotiateMatrix(self, n: int, m: int, row_proposals: list[int], column_criteria: list[list[int]]) -> NegotiationResult:
        # Your code here
        return None
```

```cpp
#include <vector>

using namespace std;

struct NegotiationResult {
    int failures;
    vector<vector<int>> finalMatrix;
};

class Solution {
public:
    NegotiationResult negotiateMatrix(int n, int m, vector<int>& rowProposals, vector<pair<int, int>>& columnCriteria) {
        // Your code here
        return {};
    }
};
```

```javascript
class NegotiationResult {
  constructor(failures, finalMatrix) {
    this.failures = failures;
    this.finalMatrix = finalMatrix;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number[]} rowProposals
   * @param {number[][]} columnCriteria
   * @returns {NegotiationResult}
   */
  negotiateMatrix(n, m, rowProposals, columnCriteria) {
    // Your code here
    return null;
  }
}
```
