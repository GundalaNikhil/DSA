---
problem_id: MAT_MATRIX_RANK_DRIFT__6461
display_id: NTB-MAT-6461
slug: matrix-rank-drift
title: "Matrix Rank Drift"
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
  - matrix-rank-drift
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Rank Drift

## Problem Statement

You are given an `n x m` integer matrix. Process `q` operations and report the matrix rank after each operation. Rank is defined over the real numbers.

Operations:

- `SWAP r1 r2`: swap two rows
- `SET r v1 v2 ... vm`: replace row `r` with given values
- `ADD r1 r2`: set row `r1 = row r1 + row r2`

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `q` lines: one operation per line

## Output Format

- After each operation, output the current rank on its own line

## Constraints

- `1 <= n, m <= 50`
- `1 <= q <= 500`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Row indices are 1-based.
- Row swaps do not change rank, but other operations can.

## Example Input

```
2 2 2
1 2
2 4
ADD 1 2
SET 2 0 1
```

## Example Output

```
1
2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processRankOperations(int n, int m, int q, double[][] initialMatrix, List<String> operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processRankOperations(self, n: int, m: int, q: int, initial_matrix: list[list[float]], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processRankOperations(int n, int m, int q, vector<vector<double>>& initialMatrix, vector<string>& operations) {
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
   * @param {number} q
   * @param {number[][]} initialMatrix
   * @param {string[]} operations
   * @returns {number[]}
   */
  processRankOperations(n, m, q, initialMatrix, operations) {
    // Your code here
    return [];
  }
}
```
