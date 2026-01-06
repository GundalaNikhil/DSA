---
problem_id: DP_PERMUTATION_CONSTRAINTS__6396
display_id: NTB-DP-6396
slug: permutation-constraints
title: "DP on Permutation with Constraints"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - permutation-constraints
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Permutation with Constraints

## Problem Statement

You must build a permutation of `1..n` under forbidden adjacency constraints. You are given a matrix `forbid[i][j]` where `1` means `i` cannot be immediately followed by `j`.

Find the maximum total score, where score is the sum of weights `w[i][position]` for placing value `i` at that position.

## Input Format

- First line: integer `n`
- Next `n` lines: `n` integers: weights `w[i][1..n]`
- Next `n` lines: `n` integers: forbid matrix

## Output Format

- Single integer: maximum score, or `-1` if impossible

## Constraints

- `1 <= n <= 15`
- `-10^9 <= w[i][pos] <= 10^9`

## Clarifying Notes

- This is a bitmask DP over permutations.

## Example Input

```
3
3 2 1
2 3 1
1 2 3
0 1 0
0 0 1
0 0 0
```

## Example Output

```
8
```

## Solution Stub

### Java

```java
class Solution {
    public long maxScore(int n, int[][] weights, int[][] forbid) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def maxScore(self, n: int, weights: list[list[int]], forbid: list[list[int]]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long maxScore(int n, vector<vector<int>>& weights, vector<vector<int>>& forbid) {
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
   * @param {number[][]} weights
   * @param {number[][]} forbid
   * @return {number}
   */
  maxScore(n, weights, forbid) {
    // Implement here
    return -1;
  }
}
```
