---
problem_id: MAT_MATRIX_FLOW_CONSERVATION__5034
display_id: NTB-MAT-5034
slug: matrix-flow-conservation
title: "Matrix with Flow Conservation"
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
  - matrix-flow-conservation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix with Flow Conservation

## Problem Statement

You are given an `n x m` matrix of non-negative values. Each operation moves an amount between adjacent cells.

Operation format:

```
MOVE r1 c1 r2 c2 x
```

The move is valid only if `(r1, c1)` and `(r2, c2)` are 4-directional neighbors and `A[r1][c1] >= x`.

Find the first invalid operation. If all operations are valid, output `0` and the final matrix.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `q` lines: operations

## Output Format

- If an operation is invalid: output its 1-based index
- Otherwise: output `0` and the final matrix

## Constraints

- `1 <= n, m <= 200`
- `0 <= A[r][c] <= 10^9`
- `1 <= q <= 200000`
- `0 <= x <= 10^9`

## Clarifying Notes

- Total sum must remain constant if all operations are valid.

## Example Input

```
2 2 2
5 0
0 0
MOVE 1 1 1 2 3
MOVE 1 1 2 1 3
```

## Example Output

```
2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class FlowResult {
        public int firstInvalid; // 0 if all valid
        public long[][] finalMatrix; // only if all valid
        public FlowResult(int firstInvalid, long[][] finalMatrix) {
            this.firstInvalid = firstInvalid;
            this.finalMatrix = finalMatrix;
        }
    }

    public FlowResult processMoves(int n, int m, int q, long[][] initialMatrix, List<String> operations) {
        // Your code here
        return null;
    }
}
```

```python
class FlowResult:
    def __init__(self, first_invalid: int, final_matrix: list[list[int]] = None):
        self.first_invalid = first_invalid
        self.final_matrix = final_matrix

class Solution:
    def processMoves(self, n: int, m: int, q: int, initial_matrix: list[list[int]], operations: list[str]) -> FlowResult:
        # Your code here
        return None
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct FlowResult {
    int firstInvalid;
    vector<vector<long long>> finalMatrix;
};

class Solution {
public:
    FlowResult processMoves(int n, int m, int q, vector<vector<long long>>& initialMatrix, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class FlowResult {
  constructor(firstInvalid, finalMatrix) {
    this.firstInvalid = firstInvalid;
    this.finalMatrix = finalMatrix;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} q
   * @param {number[][]} initialMatrix
   * @param {string[]} operations
   * @returns {FlowResult}
   */
  processMoves(n, m, q, initialMatrix, operations) {
    // Your code here
    return null;
  }
}
```
