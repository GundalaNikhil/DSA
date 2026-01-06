---
problem_id: MAT_ROW_AUTHORITY_MATRIX__8808
display_id: NTB-MAT-8808
slug: row-authority-matrix
title: "Row Authority Matrix"
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
  - row-authority-matrix
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Row Authority Matrix

## Problem Statement

You manage an access-control matrix with `n` rows and `m` columns. Each row has a base authority value. Each column applies one of three dominance rules to every cell in that column:

- Type `0`: no override (cell keeps the row authority value).
- Type `1`: cap with value `c` (cell becomes `min(row_value, c)`).
- Type `2`: force with value `f` (cell becomes exactly `f`).

Compute the final matrix after all rules are applied.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: row authorities
- Next `m` lines: `type value` for each column (value is ignored when type = 0)

## Output Format

- `n` lines, each with `m` integers: the final matrix

## Constraints

- `1 <= n, m <= 500`
- `-10^9 <= row_value, value <= 10^9`

## Clarifying Notes

- Column rules apply to all rows independently.
- Type 2 (force) overrides any row value.

## Example Input

```
3 3
10 20 30
0 0
1 15
0 0
```

## Example Output

```
10 10 10
20 15 20
30 15 30
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public int[][] computeAuthorityMatrix(int n, int m, int[] rowAuthorities, int[][] columnRules) {
        // Your code here
        return new int[n][m];
    }
}
```

```python
class Solution:
    def computeAuthorityMatrix(self, n: int, m: int, row_authorities: list[int], column_rules: list[list[int]]) -> list[list[int]]:
        # Your code here
        return [[]]
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> computeAuthorityMatrix(int n, int m, vector<int>& rowAuthorities, vector<vector<int>>& columnRules) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number[]} rowAuthorities
   * @param {number[][]} columnRules
   * @returns {number[][]}
   */
  computeAuthorityMatrix(n, m, rowAuthorities, columnRules) {
    // Your code here
    return [[]];
  }
}
```
