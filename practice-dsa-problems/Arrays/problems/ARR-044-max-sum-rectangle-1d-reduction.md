---
problem_id: ARR_MAX_SUM_RECTANGLE_1D_REDUCTION__4054
display_id: NTB-ARR-4054
slug: max-sum-rectangle-1d-reduction
title: "Max Sum Rectangle Reduced to 1D Arrays"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - max-sum-rectangle-1d-reduction
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Max Sum Rectangle Reduced to 1D Arrays

## Problem Statement

You are given a matrix with `n` rows and `m` columns. Find the maximum possible sum of any non-empty axis-aligned rectangular submatrix.

The intended solution reduces the 2D problem into multiple 1D maximum subarray computations by fixing row pairs.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: `m` integers each, the matrix values

## Output Format

- Single integer: maximum submatrix sum

## Constraints

- `1 <= n, m <= 400`
- `-10^9 <= value <= 10^9`

## Clarifying Notes

- The rectangle must contain at least one cell.
- The answer can be negative if all values are negative.

## Example Input

```
3 3
1 -2 3
-1 4 -2
2 -1 2
```

## Example Output

```
6
```

## Solution Stub

### Java

```java
class Solution {
    public long maxSubmatrixSum(int n, int m, int[][] matrix) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxSubmatrixSum(self, n: int, m: int, matrix: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxSubmatrixSum(int n, int m, vector<vector<int>>& matrix) {
        // Implement here
        return 0;
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number[][]} matrix
   * @return {number}
   */
  maxSubmatrixSum(n, m, matrix) {
    // Implement here
    return 0;
  }
}
```
