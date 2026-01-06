---
problem_id: REC_RECURSIVE_DEPENDENCY_TRACKING__1455
display_id: NTB-REC-1455
slug: recursive-dependency-tracking
title: "Recursive Dependency Tracking"
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
  - recursive-dependency-tracking
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Dependency Tracking

## Problem Statement

You are given a directed graph of recursive subproblems. Each node `i` has a base value `base[i]` and depends on a list of other nodes. Define:

`Solve(i) = base[i] + sum(Solve(dep))` for all dependencies `dep` of `i`.

If the dependency graph contains a cycle reachable from the start node `S`, the recursion is invalid.

Compute `Solve(S)` or report `CYCLE`.

## Input Format

- First line: integers `n`, `m`, and `S`
- Second line: `n` integers `base[1..n]`
- Next `m` lines: directed edges `u v` meaning `u` depends on `v`

## Output Format

- If a cycle is reachable from `S`, print `CYCLE`
- Otherwise print `Solve(S)`

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `1 <= S <= n`
- `-10^9 <= base[i] <= 10^9`

## Clarifying Notes

- Only cycles reachable from `S` invalidate the recursion.
- Dependencies are evaluated with memoization; each node is computed once if valid.

## Example Input

```
4 3 1
5 2 3 1
1 2
2 3
1 4
```

## Example Output

```
11
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String solveRecursionWithCycles(int n, int m, int S, long[] base, int[][] edges) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def solveRecursionWithCycles(self, n: int, m: int, S: int, base: list[int], edges: list[list[int]]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string solveRecursionWithCycles(int n, int m, int S, vector<long long>& base, vector<vector<int>>& edges) {
        // Your code here
        return "";
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} S
   * @param {number[]} base
   * @param {number[][]} edges
   * @returns {string}
   */
  solveRecursionWithCycles(n, m, S, base, edges) {
    // Your code here
    return "";
  }
}
```
