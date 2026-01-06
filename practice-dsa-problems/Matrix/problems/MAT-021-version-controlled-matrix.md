---
problem_id: MAT_VERSION_CONTROLLED_MATRIX__7399
display_id: NTB-MAT-7399
slug: version-controlled-matrix
title: "Version-Controlled Matrix"
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
  - technical-interview-prep
  - version-controlled-matrix
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Version-Controlled Matrix

## Problem Statement

You maintain multiple versions of a matrix. Version `0` is the initial matrix. New versions are created by update or merge operations.

Operations:

- `SET v r c x`: create a new version based on version `v` with `M[r][c] = x`.
- `MERGE v1 v2 base`: create a new version using three-way merge of versions `v1` and `v2` with explicit base version `base`.
- `GET v r c`: report the value at `(r, c)` in version `v`.

Three-way merge rules for each cell:

1. If both `v1` and `v2` equal `base`, keep `base`.
2. If exactly one differs from `base`, take the differing value.
3. If both differ and are equal to each other, take that value.
4. Otherwise it is a conflict. Count it, and choose the smaller of the two values.

For each `MERGE`, output the conflict count.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `q` lines: operations

## Output Format

- For each `GET`, output the value
- For each `MERGE`, output the conflict count

## Constraints

- `1 <= n, m <= 50`
- `1 <= q <= 200000`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Version ids are assigned incrementally as new versions are created by `SET` or `MERGE`.
- The `base` version in `MERGE` is explicitly given and may be any existing version.

## Example Input

```
2 2 4
1 2
3 4
SET 0 1 1 5
SET 0 1 1 7
MERGE 1 2 0
GET 3 1 1
```

## Example Output

```
1
5
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class VersionResult {
        public List<Integer> mergeConflicts;
        public List<Integer> getResults;
        public VersionResult(List<Integer> mergeConflicts, List<Integer> getResults) {
            this.mergeConflicts = mergeConflicts;
            this.getResults = getResults;
        }
    }

    public VersionResult processVersionOperations(int n, int m, int q, int[][] initialMatrix, List<String> operations) {
        // Your code here
        return null;
    }
}
```

```python
class VersionResult:
    def __init__(self, merge_conflicts: list[int], get_results: list[int]):
        self.merge_conflicts = merge_conflicts
        self.get_results = get_results

class Solution:
    def processVersionOperations(self, n: int, m: int, q: int, initial_matrix: list[list[int]], operations: list[str]) -> VersionResult:
        # Your code here
        return None
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct VersionResult {
    vector<int> mergeConflicts;
    vector<int> getResults;
};

class Solution {
public:
    VersionResult processVersionOperations(int n, int m, int q, vector<vector<int>>& initialMatrix, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class VersionResult {
  constructor(mergeConflicts, getResults) {
    this.mergeConflicts = mergeConflicts;
    this.getResults = getResults;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} q
   * @param {number[][]} initialMatrix
   * @param {string[]} operations
   * @returns {VersionResult}
   */
  processVersionOperations(n, m, q, initialMatrix, operations) {
    // Your code here
    return null;
  }
}
```
