---
problem_id: REC_RECURSIVE_ABSTRACTION_REFINEMENT__6058
display_id: NTB-REC-6058
slug: recursive-abstraction-refinement
title: "Recursive Abstraction Refinement"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-abstraction-refinement
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Abstraction Refinement

## Problem Statement

You are given an `N x N` grid, where `N` is a power of two. A square region is considered stable if the difference between its maximum and minimum values is at most `T`.

Define a recursive refinement:

- If a region is stable, stop.
- Otherwise, split it into four equal quadrants and refine each quadrant.

Compute the number of final regions (leaf regions) after full refinement.

## Input Format

- First line: integers `N` and `T`
- Next `N` lines: `N` integers each

## Output Format

- Single integer: number of leaf regions

## Constraints

- `1 <= N <= 512`
- `N` is a power of two
- `0 <= T <= 10^9`
- `-10^9 <= grid[i][j] <= 10^9`

## Clarifying Notes

- Refinement is recursive and must follow strict quadrants.
- A single cell is always stable.

## Example Input

```
2 0
1 2
1 2
```

## Example Output

```
4
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public int countLeafRegions(int N, long T, long[][] grid) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def countLeafRegions(self, N: int, T: int, grid: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int countLeafRegions(int N, long long T, vector<vector<long long>>& grid) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} N
   * @param {number} T
   * @param {number[][]} grid
   * @returns {number}
   */
  countLeafRegions(N, T, grid) {
    // Your code here
    return 0;
  }
}
```
