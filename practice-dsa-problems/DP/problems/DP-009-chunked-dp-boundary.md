---
problem_id: DP_CHUNKED_DP_BOUNDARY__6929
display_id: NTB-DP-6929
slug: chunked-dp-boundary
title: "Chunked DP with Boundary Conditions"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - chunked-dp-boundary
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Chunked DP with Boundary Conditions

## Problem Statement

You must assign integers `x_1..x_n` in range `[0, M]`. The sequence is divided into chunks of size `K` (last chunk may be smaller). Each chunk must satisfy:

- Sum of values in the chunk is between `L` and `R`.
- The absolute difference between the first and last value of the chunk is at most `D`.

The cost of the sequence is `sum cost_i[x_i]`. Find the minimum total cost.

## Input Format

- First line: integers `n`, `K`, `M`, `L`, `R`, `D`
- Next `n` lines: `M+1` integers: cost table for position `i`

## Output Format

- Single integer: minimum total cost, or `-1` if impossible

## Constraints

- `1 <= n <= 60`
- `1 <= K <= n`
- `0 <= M <= 15`
- `0 <= L <= R <= K * M`
- `0 <= D <= M`

## Clarifying Notes

- Costs are 32-bit signed integers.

## Example Input

```
4 2 2 1 3 1
1 2 3
1 1 1
2 2 2
3 1 0
```

## Example Output

```
4
```

## Solution Stub

### Java

```java
class Solution {
    public long minTotalCost(int n, int k, int m, int l, int r, int d, int[][] costTable) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def minTotalCost(self, n: int, k: int, m: int, l: int, r: int, d: int, costTable: list[list[int]]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long minTotalCost(int n, int k, int m, int l, int r, int d, vector<vector<int>>& costTable) {
        // Implement here
        return -1;
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} k
   * @param {number} m
   * @param {number} l
   * @param {number} r
   * @param {number} d
   * @param {number[][]} costTable
   * @return {number}
   */
  minTotalCost(n, k, m, l, r, d, costTable) {
    // Implement here
    return -1;
  }
}
```
