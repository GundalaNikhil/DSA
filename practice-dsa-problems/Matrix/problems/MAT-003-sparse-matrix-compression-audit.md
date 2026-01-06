---
problem_id: MAT_SPARSE_MATRIX_COMPRESSION_AUDIT__2770
display_id: NTB-MAT-2770
slug: sparse-matrix-compression-audit
title: "Sparse Matrix Compression Audit"
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
  - sparse-matrix-compression-audit
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Sparse Matrix Compression Audit

## Problem Statement

You are given an original dense matrix `A` and a sequence of `k` compression steps. Each step provides:

1. A sparse list (COO format) claiming to represent all non-zero entries of `A`.
2. A decompressed dense matrix claiming to be the result of decompressing that sparse list.

A step is valid if:

- The sparse list matches **exactly** the non-zero entries of `A` (including positions and values).
- The decompressed matrix is identical to `A`.

Report the first invalid step and the stage where it fails. If all steps are valid, output `OK`.

## Input Format

- First line: integers `n`, `m`, `k`
- Next `n` lines: `m` integers (original matrix `A`)
- For each step `i` from 1 to `k`:
  - Line: integer `s` (number of sparse entries)
  - Next `s` lines: `r c val` (1-based indices)
  - Next `n` lines: `m` integers (decompressed matrix)

## Output Format

- `OK` if all steps are valid, otherwise
- `COMPRESS i` if step `i` has an invalid sparse list
- `DECOMPRESS i` if step `i` has a valid sparse list but invalid decompressed matrix

## Constraints

- `1 <= n, m <= 200`
- `0 <= k <= 50`
- `-10^9 <= A[r][c], val <= 10^9`

## Clarifying Notes

- A value is considered non-zero if it is not equal to 0.
- Sparse entries may appear in any order but must be unique.

## Example Input

```
2 2 1
1 0
0 2
2
1 1 1
2 2 2
1 0
0 2
```

## Example Output

```
OK
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class SparseEntry {
        public int r, c, val;
        public SparseEntry(int r, int c, int val) {
            this.r = r;
            this.c = c;
            this.val = val;
        }
    }

    public static class CompressionStep {
        public List<SparseEntry> sparseList;
        public int[][] decompressedMatrix;
        public CompressionStep(List<SparseEntry> sparseList, int[][] decompressedMatrix) {
            this.sparseList = sparseList;
            this.decompressedMatrix = decompressedMatrix;
        }
    }

    public String auditCompression(int n, int m, int k, int[][] A, List<CompressionStep> steps) {
        // Your code here
        return "";
    }
}
```

```python
class SparseEntry:
    def __init__(self, r: int, c: int, val: int):
        self.r = r
        self.c = c
        self.val = val

class CompressionStep:
    def __init__(self, sparse_list: list[SparseEntry], decompressed_matrix: list[list[int]]):
        self.sparse_list = sparse_list
        self.decompressed_matrix = decompressed_matrix

class Solution:
    def auditCompression(self, n: int, m: int, k: int, A: list[list[int]], steps: list[CompressionStep]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct SparseEntry {
    int r, c, val;
};

struct CompressionStep {
    vector<SparseEntry> sparseList;
    vector<vector<int>> decompressedMatrix;
};

class Solution {
public:
    string auditCompression(int n, int m, int k, vector<vector<int>>& A, vector<CompressionStep>& steps) {
        // Your code here
        return "";
    }
};
```

```javascript
class SparseEntry {
  constructor(r, c, val) {
    this.r = r;
    this.c = c;
    this.val = val;
  }
}

class CompressionStep {
  constructor(sparseList, decompressedMatrix) {
    this.sparseList = sparseList;
    this.decompressedMatrix = decompressedMatrix;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} k
   * @param {number[][]} A
   * @param {CompressionStep[]} steps
   * @returns {string}
   */
  auditCompression(n, m, k, A, steps) {
    // Your code here
    return "";
  }
}
```
