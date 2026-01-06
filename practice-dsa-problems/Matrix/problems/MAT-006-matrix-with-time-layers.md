---
problem_id: MAT_MATRIX_WITH_TIME_LAYERS__4094
display_id: NTB-MAT-4094
slug: matrix-with-time-layers
title: "Matrix with Time Layers"
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
  - matrix-with-time-layers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix with Time Layers

## Problem Statement

You manage a persistent matrix over discrete time. Each update applies to all future time layers, while past layers remain unchanged.

Operations:

- `SET t r c v`: for all time `T >= t`, the value at `(r, c)` becomes `v` unless overwritten by a later `SET` with time `t' <= T`.
- `GET t r c`: report the value at `(r, c)` at time `t`.

Given a sequence of operations, output the results of all `GET` queries.

## Input Format

- First line: integers `n`, `m`, `q`
- Second line: `n * m` integers, row-major initial matrix
- Next `q` lines: operations `SET` or `GET`

## Output Format

- For each `GET`, output the value on its own line

## Constraints

- `1 <= n, m <= 400`
- `1 <= q <= 200000`
- `0 <= t <= 10^9`
- `-10^9 <= v <= 10^9`

## Clarifying Notes

- If no `SET` has been applied to `(r, c)` at or before time `t`, use the initial value.
- Time does not need to be in order.

## Example Input

```
2 2 4
1 2 3 4
SET 0 1 1 5
SET 3 1 1 10
GET 2 1 1
GET 4 1 1
```

## Example Output

```
5
10
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processMatrixOperations(int n, int m, int q, int[] initialMatrix, List<String> operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processMatrixOperations(self, n: int, m: int, q: int, initial_matrix: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processMatrixOperations(int n, int m, int q, vector<int>& initialMatrix, vector<string>& operations) {
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
   * @param {number[]} initialMatrix
   * @param {string[]} operations
   * @returns {number[]}
   */
  processMatrixOperations(n, m, q, initialMatrix, operations) {
    // Your code here
    return [];
  }
}
```
