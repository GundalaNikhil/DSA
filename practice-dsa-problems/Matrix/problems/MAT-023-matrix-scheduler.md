---
problem_id: MAT_MATRIX_SCHEDULER__8257
display_id: NTB-MAT-8257
slug: matrix-scheduler
title: "Matrix Scheduler"
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
  - matrix-scheduler
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Scheduler

## Problem Statement

Each cell is a task with a duration. You are given dependency edges between tasks. A task can start only after all its prerequisites finish. You have unlimited parallelism.

Compute the minimum total completion time (makespan).

## Input Format

- First line: integers `n`, `m`, `k`
- Next `n` lines: `m` integers (durations)
- Next `k` lines: `r1 c1 r2 c2` meaning task `(r2, c2)` depends on `(r1, c1)`

## Output Format

- Single integer: minimum completion time

## Constraints

- `1 <= n, m <= 200`
- `0 <= k <= 200000`
- `1 <= duration <= 10^9`

## Clarifying Notes

- If the dependency graph has a cycle, output `-1`.
- Indices are 1-based.

## Example Input

```
2 2 2
3 1
2 4
1 1 2 2
1 2 2 1
```

## Example Output

```
7
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long calculateMakespan(int n, int m, int k, int[][] durations, int[][] dependencies) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def calculateMakespan(self, n: int, m: int, k: int, durations: list[list[int]], dependencies: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    long long calculateMakespan(int n, int m, int k, vector<vector<int>>& durations, vector<vector<int>>& dependencies) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} k
   * @param {number[][]} durations
   * @param {number[][]} dependencies
   * @returns {number}
   */
  calculateMakespan(n, m, k, durations, dependencies) {
    // Your code here
    return 0;
  }
}
```
